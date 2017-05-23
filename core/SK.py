import numpy as np
from scipy.optimize import minimize
from scipy import spatial
import numpy.linalg as LA
from scipy.interpolate import interp1d
import time

# function to minimize in estimate_mean_var
def cost_fit_exp(sigma, y, R):
    e1   = np.exp(- 0.5 * sigma * R)
    d    = e1 - y
    val  = np.sum(d ** 2)
    grad = -np.sum(R * np.dot(e1.T, d))
    return val, grad


# estimation of the variance of the data 
def estimate_mean_var(X, smallN = 5000, nb_iter = 4, m0 = 500, c = 30):
    # small random subset of the data
    x=X[:, np.random.permutation(np.shape(X)[1])[:min(np.shape(X)[1],smallN)] ];	
    mean_var = np.asarray([1.]) # initial value

    for it in range(nb_iter):
    	w = draw_freq(mean_var, m0, np.shape(X)[0], 'adapted')
    	R = np.sum(w ** 2, axis = 0)
    	R = R[np.newaxis, :]
    	sk_ri, _ = emp_sketch(w, x)
        sk_ri *= np.sqrt(m0)
    	sk_dim = np.shape(sk_ri)[0] / 2
    	sk = np.abs(sk_ri[:sk_dim] + sk_ri[sk_dim:] *1j)
		
    	fr = int(np.floor(sk_dim / c))
    	val = np.zeros((1, c))
    	RR  = np.zeros((1, c))

    	for k in range(c):
    	    i = np.argmax(sk[k*fr:(k+1)*fr])
	    val[0, k] = sk[k*fr + i]
	    RR[0, k] = R[0, k*fr + i]
	    mean_var = minimize(cost_fit_exp, mean_var, args = (val, RR), method='TNC', bounds = [(0, None)], jac = True ).x
    return mean_var
	

# Lookup table
def cdf_lookup(ax, pdf, N):
    pdf = pdf / np.sum(pdf)
    cdf = np.cumsum(pdf)
    np.append(cdf, 0)
    ind = np.where(cdf[0:-2] - cdf[1:-1] >=0)[0][0]
    cdf = cdf[0:ind]
    ax = ax[0:ind]
    y = np.random.rand(1, N)
    Y = interp1d(cdf,ax)(y)
    Y[np.isnan(Y)] = 0 
    return Y
	

# draw radius with adapted distribution
def adapted(m):
    ax = np.arange(0., 10, 0.001)
    radius_density = np.sqrt((ax ** 2 + ax ** 4 / 4) * np.exp(-ax ** 2))
    Wnorm = cdf_lookup(ax, radius_density, m)
    return Wnorm


# draw direction uniform in a hypershpere
def angles(m, n, sigma):
    Wdir = np.random.randn(m, n)
    Wdir = Wdir / (np.sqrt(np.sum(Wdir **2, axis = 0)))
    return Wdir


# draw frequencies
def draw_freq(sigma, n_freq, dim, type = 'gaussian'):
    W = np.zeros((dim, n_freq))
    if type == 'gaussian':
	W = np.random.normal(0, 1./sigma, (dim, n_freq))
    elif type == 'gaussian2':
    	print 'not implemented yet'
    	W = 0
    elif type == 'adapted':
    	Wnorm = adapted(n_freq)
    	Wdir = angles(dim, n_freq, sigma)
    	W = Wnorm * Wdir
    else:
    	print 'type not defined'
		
    ind = np.argsort(np.sum(W ** 2, axis = 0))[::-1]
    W = W[:, ind]
    return W
	
	
# return mean and variance of the data X	
def mean_var(X):
    return np.mean(X, axis = 1), np.var(X, axis = 1)
	
	
# normalize the data X
def normalize(X, X_mean = None, Xvar = None):
    if X_mean == None or X_var == None:
    	X_mean, X_var = mean_var(X)
    if (np.shape(X)[1] == 1):
    	X_var = np.ones(np.shape(X)[0])
    X = X - X_mean[:, np.newaxis]
    X /= np.sqrt(X_var[:, np.newaxis])
    return X
	
	
# compute the sketch of the data
def emp_sketch(W, X):
    sk_dim = np.shape(W)[1]	
    N = np.shape(X)[1]
    z = np.zeros((sk_dim * 2, 1))

    t_s = time.clock()
    Y = np.dot(W.T, X)
    t_RP = time.clock() - t_s
	
    z[:sk_dim, 0] = np.mean( np.cos(Y), axis = 1)
    z[sk_dim:, 0] = np.mean(-np.sin(Y), axis = 1)
    #z = np.vstack[np.mean( np.cos(Y), axis = 1), np.mean(-np.sin(Y), axis = 1)]
    return z / np.sqrt(sk_dim), t_RP
	
# compute the sketch of the data with a phase factor
def emp_sketch2(W, b, X):
    sk_dim = np.shape(W)[1]	
    N = np.shape(X)[1]
    z = np.zeros((sk_dim * 2, 1))

    #t_s = time.clock()
    Y = np.dot(W.T, X) + b
    #print 't_RP = ', time.clock() - t_s
	
    z[:sk_dim, 0] = np.mean( np.cos(Y), axis = 1)
    z[sk_dim:, 0] = np.mean(-np.sin(Y), axis = 1)
    #z = np.vstack[np.mean( np.cos(Y), axis = 1), np.mean(-np.sin(Y), axis = 1)]
    return z / np.sqrt(sk_dim)

# from data gives frequencies adapted
def freq(X, n_freq):
    sigma = estimate_mean_var(X)
    W = draw_freq(sigma, n_freq, np.shape(X)[0], 'adapted')
    return W


# calculate distance between sketches
def dist(z1, z2, type = 'l2'):
    s = 0.
    if (type == 'l1'):
    	s = LA.norm(z1 - z2, 1)
    elif (type == 'l2'):
    	s = LA.norm(z1 - z2, 'fro')
    elif (type == 'cos'):
    	s = spatial.distance.cosine(z1, z2)
    else:
    	print "unknown distance"
    return s
	
	
# given a sketch, return the data that would create the sketch
def from_sketch_to_data(z, W):
    sk_dim = np.shape(W)[1]
		
    z *= np.sqrt(sk_dim)
    sk = z[:sk_dim] + z[sk_dim:] *1j
    Y = np.angle(sk)
    X = LA.lstsq(W.T, Y)[0]
    return X

