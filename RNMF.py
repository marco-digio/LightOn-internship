import numpy as np
import scipy.linalg as LA
import time
from sklearn.decomposition import nmf

# Randomized NMF decomposition. A = WH
def rNMF(A, r, k):	
	# random projection
	t_in = time.clock()
	Y = np.abs(np.dot(np.random.randn(k, np.shape(A)[0]), A))
	t_RP = time.clock() - t_in

	# algorithm
	W1, H1, _ = nmf.non_negative_factorization(Y, n_components=r)	
	W2, _, _  = nmf.non_negative_factorization(A, H = H1, update_H = False, n_components=r)
	return W2, H1, t_RP
	

# Error and time of (R)NMF decomposition.
# er_out = True calculate the error (it could take some time)
def et_NMF(A, r, k=0, er_out=False):

	t_in = time.clock()
	if k == 0:
		W, H, _ = nmf.non_negative_factorization(A, n_components=r)
		t_RP = 0
	else:
		W, H, t_RP = rNMF(A, r, k)
	t = time.clock() - t_in
	
	if (er_out == False):
		error = 0
	else:
		error = nmf._safe_compute_error(A, W, H)/LA.norm(A, 'fro')
		
	return W, H, error, t, t_RP
		
