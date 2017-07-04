import numpy as np
import scipy.linalg as LA
import time
import scipy.linalg.interpolative as sli

	
# Interpolative decomposition. A = A[:, idx] * X
def id(A, k):
    idx, proj = sli.interp_decomp(A, k)
    X = np.hstack([np.eye(k), proj])[:,np.argsort(idx)]
    return idx[:k], X


# Randomized QR decomposition. A = QR
def RQR(A, l, abs_val=False):
	
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
    #Q, Rt, P2 = LA.qr(np.dot(X.T, Q1), pivoting=True)
    Q, Rt = LA.qr(np.dot(X.T, Q1))
    R = np.dot(Rt, R1)
    return Q, R, np.arange(np.shape(A)[1]), t_RP

    
def RQR2(A, k, abs_val=False):
	t_in = time.clock()
	if (abs_val == False):
		Y = np.dot(A, np.random.randn(np.shape(A)[1], k))
	else:
		Y = np.abs(np.dot(A, np.random.randn(np.shape(A)[1], k)))
	t_RP = time.clock() - t_in

	#Q1, R1 = LA.qr(Y, pivoting=False)
	Q1, R1, P1 = LA.qr(Y, pivoting=True)
	Q2, R2, P2 = LA.qr(np.dot(Q1.T, A), pivoting=True)
	return np.dot(Q1, Q2)[:, :k], R2[:k, :], P2, t_RP

# Error and time of (R)QR decomposition.
# er_out = True calculate the error (it could take some time)
# random = True will use the randomize algorithm
# abs_val = True will do the RP with absolute value (only for randomized QR)
def et_QR(A, k, er_out=True, random=False, abs_val=False):

	t_in = time.clock()
	if random == False:
		Q, R, P = LA.qr(A, pivoting=True)
		Q = Q[:, 0:k]
		R = R[0:k, :]
		t_RP = 0
	else:
		Q, R, P, t_RP = RQR(A, k, abs_val)
	t = time.clock() - t_in
	
	if (er_out == False):
		error = 0
	else:
		error = LA.norm(A[:, P] - np.dot(Q, R))
		#error = LA.norm(A - np.dot(Q, R))
	
	print error, t
	return Q, R, error, t, t_RP
		
