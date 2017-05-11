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
def rSVD(A, k, abs_val = False):
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
	U, s, Vt = LA.svd(np.dot(X.T, Q1))
	V = np.dot(Vt[:l, :], R1)
	S = np.diag(s)[:l, :l]
	return U[:, :l], S, V, t_RP
	

# Error and time of (R)SVD decomposition.
# er_out = True calculate the error (it could take some time)
# random = True will use the randomize algorithm
# abs_val = True will do the RP with absolute value (only for randomized QR)
def et_SVD(A, k, er_out = False, random = False, abs_val = False):

	t_in = time.clock()
	if random == False:
		U, s, V = LA.qr(A)
		S = np.diag(s)
		U = U[:, 0:k]
		S = S[0:k, 0:k]
		V = V[0:k, :]
		t_RP = 0
	else:
		U, S, V, t_RP = rQR(A, k, abs_val)
	t = time.clock() - t_in
	
	if (er_out == False):
		error = 0
	else:
		error = LA.norm(A - np.dot(U, np.dot(S, V)))
		
	return U, S, V, error, t, t_RP
		
		
# Average of error and time for (R)SVD decomposition
def av_et_SVD(A, k, n_it, er_out = False, random = False, abs_val = False):

	er = np.zeros(n_it)
	t_tot = np.zeros(n_it)
	t_rp = np.zeros(n_it)

	for it in range(n_it):
		#print 'it = ', it
		_, _, er[it], t_tot[it], t_rp[it] = et_SVD(A, k, er_out, random, abs_val)
	
	return np.mean(er), np.mean(t_tot), np.mean(t_rp)
		
		
