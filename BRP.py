import numpy as np
import numpy.linalg as LA

# Bilateral Random Projection
def BilateralRP(X, r, corr=False, abs_val=False):
    m, n = np.shape(X)
    t_in1 = time.clock()
    A1 = np.random.randn(n, r)
    if corr==False:
        A2 = np.random.randn(m, r)
        Y1 = np.dot(X,   A1)
        Y2 = np.dot(X.T, A2)
        if abs_val==True:
            Y1 = np.abs(Y1)
            Y2 = np.abs(Y2)
        t_rp = time.clock() - t_in1
    else:
        Y1 = np.dot(X,   A1)
        if abs_val==True:
            Y1 = np.abs(Y1)
        t_rp = time.clock() - t_in1
        A2 = Y1
        Y2 = np.dot(X.T, A2)
        Y1 = np.dot(X, Y2)

    L = np.dot(Y1, LA.lstsq(np.dot(A2.T, Y1), Y2.T))
    return L, t_rp


# error and computational time of bilateral random projection
def et_BRP(X, r, corr=False, abs_val=False):
    t_in = time.clock()
    L, t_rp = BilateralRP(X, r, corr, abs_val)
    t_tot = time.clock() - t_in
    error = LA.norm(X - L) / LA.norm(X)

    return error, t_tot, t_rp


