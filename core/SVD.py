import numpy as np
import scipy.linalg as LA
import time
import scipy.linalg.interpolative as sli

	
# Interpolative decomposition. A = A[:, idx] * X
def id(A, k):
    idx, proj = sli.interp_decomp(A, k)
    X = np.hstack([np.eye(k), proj])[:,np.argsort(idx)]
    return idx[:k], X


# Randomized singular value decomposition	
def rSVD(A, l, abs_val=False):
	
    # random projection
    t_in = time.clock()
    if (abs_val == False):
	Y = np.dot(A, np.random.randn(np.shape(A)[1], l))
    else:
    	Y = np.abs(np.dot(A, np.random.randn(np.shape(A)[1], l)))
    t_RP = time.clock() - t_in

    # algorithm
    J, X = id(Y.T, l)
    Q1, R1 = LA.qr(A[J, :])
    U, s, Vt = LA.svd(np.dot(X.T, Q1))
    V = np.dot(Vt[:l, :], R1)
    S = np.diag(s)[:l, :l]
    return U[:, :l], S, V, t_RP

	
def rSVD2(A, k, abs_val=False):
	t_in = time.clock()
	if (abs_val == False):
		Y = np.dot(A, np.random.randn(np.shape(A)[1], k))
	else:
		Y = np.abs(np.dot(A, np.random.randn(np.shape(A)[1], k)))
	t_RP = time.clock() - t_in

	Q1, R1 = LA.qr(Y, pivoting=False)
	#Q1, R1, P1 = LA.qr(Y, pivoting=True)
	Ut, s, V = LA.svd(np.dot(Q1.T, A))
	return np.dot(Q1, Ut)[:, :k], np.diag(s)[:k, :k], V[:k, :],t_RP

# Error and time of (R)SVD decomposition.
# er_out = True calculate the error (it could take some time)
# random = True will use the randomize algorithm
# abs_val = True will do the RP with absolute value (only for randomized QR)
def et_SVD(A, k, er_out=True, random=False, abs_val=False):

    t_in = time.clock()
    if random == False:
    	U, s, V = LA.svd(A)
    	S = np.diag(s)
    	U = U[:, 0:k]
    	S = S[0:k, 0:k]
    	V = V[0:k, :]
    	t_RP = 0
    else:
    	U, S, V, t_RP = rSVD(A, k, abs_val)
    t = time.clock() - t_in
	
    if (er_out == False):
    	error = 0
    else:
    	error = LA.norm(A - np.dot(U, np.dot(S, V)))
		
    return U, S, V, error, t, t_RP
		
