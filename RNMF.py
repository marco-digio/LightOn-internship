import numpy as np
import scipy.linalg as LA
import time
import scipy.linalg.interpolative as sli


# Randomized NMF decomposition. A = WH
def rNMF(A, r, k):	
	# random projection
	t_in = time.clock()
	Y = np.abs(np.dot(A, np.random.randn(np.shape(A)[1], k)))
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
		
		
# Average of error and time for (R)NMF decomposition
def av_et_NMF(A, r, n_it, k=0, er_out=False):

	er = np.zeros(n_it)
	t_tot = np.zeros(n_it)
	t_rp = np.zeros(n_it)

	for it in range(n_it):
		#print 'it = ', it
		_, _, er[it], t_tot[it], t_rp[it] = et_NMF(A, r, k, er_out)
	
	return np.mean(er), np.mean(t_tot), np.mean(t_rp)
		
		
