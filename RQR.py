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
def rQR(A, k, abs_val = False):
	l = k + 10 # oversampling 
	
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
	Q, Rt = LA.qr(np.dot(X.T, Q1))
	R = np.dot(Rt[:l, :], R1)
	return Q[:, :l], R, t_RP
	

# Error and time of (R)QR decomposition.
# er_out = True calculate the error (it could take some time)
# random = True will use the randomize algorithm
# abs_val = True will do the RP with absolute value (only for randomized QR)
def et_QR(A, k, er_out = False, random = False, abs_val = False):

	t_in = time.clock()
	if random == False:
		Q, R = LA.qr(A)
		Q = Q[:, 0:k]
		R = R[0:k, :]
		t_RP = 0
	else:
		Q, R, t_RP = rQR(A, k, abs_val)
	t = time.clock() - t_in
	
	if (er_out == False):
		error = 0
	else:
		error = LA.norm(A - np.dot(Q, R))
		
	return Q, R, error, t, t_RP
		
