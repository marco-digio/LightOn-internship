import numpy as np
import matplotlib.pyplot as plt
import os
import SK

# draw mu and sigma for a mixture of gaussians (equal weights)
def gmm_par(dimension, n_gaussian):
    mu = np.random.randn(dimension, n_gaussian) * n_gaussian ** (1.0 / dimension) #* 2
    sigma = np.sqrt(np.random.rand(1, n_gaussian) * 1.5 + 0.25)		
    return mu, sigma
	

# draw points from a mixture of gaussians
def synt_gmm(mu, sigma, n_points, show_img = False):
	dimension = np.shape(mu)[0]
	n_gaussian = np.shape(mu)[1]
	data = np.zeros((dimension, n_gaussian * n_points))
	label = np.zeros((n_gaussian * n_points))

	for i in range(n_gaussian):
		data[:,i*n_points:(i+1)*n_points] = np.random.randn(dimension,n_points)*sigma[:,i] + mu[:,i:i+1]
		label[i*n_points:(i+1)*n_points] = i		
	return data, label 


def synthetic_data(d, n, mu, sigma=1):
    return np.random.normal(mu, sigma, (d, n))

def distances(X, X_s, X_d, m, typed):
    n_s = np.shape(X_s)[1]
    n_d = np.shape(X_d)[1]

    d_same = np.zeros((n_s, 1))
    d_diff = np.zeros((n_d, 1))

    W = SK.freq(X, m)
    z, _ = SK.emp_sketch(W, X)
    for i in range(n_s):
        z_test, _ = SK.emp_sketch(W, X_s[:,i:i+1])
        d_same[i] = SK.dist(z, z_test, typed)
    for i in range(n_d):
        z_test, _ = SK.emp_sketch(W, X_d[:,i:i+1])
        d_diff[i] = SK.dist(z, z_test, typed)
    return np.mean(d_same), np.mean(d_diff)


def av_dist(d, N, n, m, typed, n_it):
    d_same = np.zeros(n_it)
    d_diff = np.zeros(n_it)

    for it in range(n_it):
        X   = synthetic_data(d, N, 0)
        X_s = synthetic_data(d, n, 0)
        X_d = synthetic_data(d, n, 6)
        d_same[it], d_diff[it] = distances(X, X_s, X_d, m, typed)
    return np.mean(d_same), np.mean(d_diff)




def m_sk(d, N, n, mrange, typed, n_it):
    n_m = np.size(mrange)

    ds = np.zeros(n_m)
    dd = np.zeros(n_m)

    for i in range(n_m):
        m = mrange[i]
        print "m = ", m
        ds[i], dd[i] = av_dist(d, N, n, m, typed, n_it)

    try:
        os.mkdir('../data')
    except OSError:
        pass

    np.savez('../data/sk_m.npz', mrange=mrange, ds=ds, dd=dd)
    return ds, dd


def d_sk(drange, N, n, m, typed, n_it):
    n_d = np.size(drange)

    ds = np.zeros(n_d)
    dd = np.zeros(n_d)

    for i in range(n_d):
        d = drange[i]
        print "d = ", d
        ds[i], dd[i] = av_dist(d, N, n, m, typed, n_it)

    try:
        os.mkdir('../data')
    except OSError:
        pass

    np.savez('../data/sk_d.npz', drange=drange, ds=ds, dd=dd)
    return ds, dd


def plot(range1, ds, dd, type1, type2):
    try:
        os.mkdir('../plot')
    except OSError:
        pass

    plt.figure(1)
    plt.plot(range1, ds, 'b', label='same distribution', linewidth=2)
    plt.plot(range1, dd, 'b', label='different distribution', linewidth=2)
    plt.ylabel('distance', fontsize=15)
    plt.xlabel(type1, fontsize=15)
    plt.legend(loc='best', fontsize=15)
    plt.savefig('../plot/'+type2+'_'+type1+'_distance.pdf')
    #plt.show()
    plt.close('all')


def run_plot(type1, type2):
    data = np.load('../data/'+type2+'_'+type1+'.npz')
    range1 = data[type1+'range']
    ds = data['ds']
    dd = data['dd']
    plot(range1, ds, dd, type1, type2)
	
	
# exemple function
def exemple():
	# data parameters
	dim = 70
	n_gaussian = 10
	N = 600
	n_try = 100
	
	# data creation
	#X 	= np.random.normal(0, 1, (dim, N))
	#X_s = np.random.normal(0, 1, (dim, n_try))
	mu, sigma = gmm.gmm_par(dim, n_gaussian)
	X = gmm.synthetic_mixture_gaussians(mu, sigma, N)[0]
	X_s = gmm.synthetic_mixture_gaussians(mu, sigma, n_try)[0]
	X_d = np.random.normal(6, 1, (dim, n_try))
	
	
	mrange = np.arange(1, 100, 6)
	type = 'l2'
	change_m(X, X_s, X_d, mrange, type)
	

