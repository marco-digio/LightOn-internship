import numpy as np
import numpy.linalg as LA
import time


# synthetic data (n observations of dimension d
def synthetic_data(n, d):
    return np.random.randn(n, d)


# randomly create the frequencies
def find_omega(dim, k):
    return np.random.randn(dim, k)


# create the random features 
def rand_features(A, m):
    t_in = time.clock()
    Y = np.dot(A, find_omega(np.shape(A)[1], m))
    #Y = np.dot(find_omega(m, np.shape(A)[0]), A)
    t_rp = time.clock() - t_in
    b = np.random.rand(m)*2*np.pi
    res =  np.cos(Y+b)
    return res, t_rp


# create linear random features (not useful)
def linear_rand_features(X, k):
    return np.dot(X, find_omega(np.shape(X)[1], k))


# original kernel matrix
def KernelMatrix(X):
    n = np.shape(X)[0]
    K = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            K[i][j] = np.exp(-LA.norm(X[i:i+1,:]-X[j:j+1,:])**2 * 0.5)
    return K


# approximated kernel matrix with random (nonlinear) features
def RandKernel(data, m):
    z, t_rp = rand_features(data, m)
    return np.dot(z, z.T) / m, t_rp


# error and time for randomized nonlinear pca with respect to the original
def et_rnpca(A, m):
    t_in1 = time.clock()
    K1 = KernelMatrix(A)
    t1 = time.clock() - t_in1

    t_in2 = time.clock()
    K2, t_rp = RandKernel(A, m)
    t2 = time.clock() - t_in2
    
    error = LA.norm(K1 - K2) #FIXME
    return error, t1, t2, t_rp


# average error and time
def av_et_rnpca(n, d, m, n_it):
    er   = np.zeros(n_it)
    t1   = np.zeros(n_it)
    t2   = np.zeros(n_it)
    t_rp = np.zeros(n_it)

    for it in range(n_it):
        A = synthetic_data(n, d)
        er[it], t1[it], t2[it], t_rp[it] = et_rnpca(A, m)

    return np.mean(er), np.mean(t1), np.mean(t2), np.mean(t_rp)

