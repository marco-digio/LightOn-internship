import numpy as np
import os
import RQR
	
# synthetic data
def synthetic_data(m, n, k):
	return np.dot(np.random.randn(m, k), np.random.randn(k, n))

# QR for different values of m
def m_qr(mrange, n, k, n_it, er_out = False, p=10, random=False):
	n_m = np.size(mrange)
	
	error = np.zeros(n_m)
	t_tot = np.zeros(n_m)
	t_rp  = np.zeros(n_m)
	
	for i in range(n_m):
		m = mrange[i]
		print 'm = ', m
		A = synthetic_data(m, n, k)
		_, _, error[i], t_tot[i], t_rp[i] = RQR.av_et_qr(A, k+p, n_it, er_out, random)
		
	try:
		os.mkdir('data')
	except OSError:
		pass

	if random == False:
		np.savez('data/m_qr.npz', mrange=mrange, error=error, t_tot=t_tot)
		return error, t_tot
	else:
		np.savez('data/m_rqr.npz', mrange=mrange, error=error, t_tot=t_tot, t_rp=t_rp)
		return error, t_tot, t_rp
	
	
# QR for different values of n
def n_qr(m, nrange, k, n_it, er_out = False, p=10, random=False):
	n_n = np.size(nrange)
	
	error = np.zeros(n_n)
	t_tot = np.zeros(n_n)
	t_rp  = np.zeros(n_n)
	
	for i in range(n_n):
		n = nrange[i]
		print 'n = ', n
		A = synthetic_data(m, n, k)
		_, _, error[i], t_tot[i], t_rp[i] = RQR.av_et_qr(A, k+p, n_it, er_out, random)
		
	try:
		os.mkdir('data')
	except OSError:
		pass

	if random == False:
		np.savez('data/n_qr.npz', nrange=nrange, error=error, t_tot=t_tot)
		return error, t_tot
	else:
		np.savez('data/n_rqr.npz', nrange=nrange, error=error, t_tot=t_tot, t_rp=t_rp)
		return error, t_tot, t_rp


# QR for different values of k
def k_qr(m, n, krange, n_it, er_out = False, p=10, random = False):
	n_k = np.size(krange)
	
	error = np.zeros(n_k)
	t_tot = np.zeros(n_k)
	t_rp  = np.zeros(n_k)
	
	for i in range(n_k):
		k = krange[i]
		print 'k = ', k
		A = synthetic_data(m, n, k)
		_, _, error[i], t_tot[i], t_rp[i]  = RQR.av_et_qr(A, k+p, n_it, er_out, random)
			
	try:
		os.mkdir('data')
	except OSError:
		pass			

	if random == False:
		np.savez('data/k_qr.npz', krange=krange, error=error, t_tot=t_tot)
		return error, t_tot
	else:
		np.savez('data/k_rqr.npz', krange=krange, error=error, t_tot=t_tot, t_rp=t_rp)
		return error, t_tot, t_rp


# test run changing m
def run_m_qr():
	mrange = np.arange(200, 1000, 100)
	n = 2000
	k = 100
	n_it = 10
	error1, t1 = m_qr(mrange, n, k, n_it, er_out=True, random=False)
	error2, t2, t_rp = m_qr(m, n, krange, n_it, er_out=True, random=True)


# test run changing n
def run_n_qr():
	m = 500
	nrange = np.arange(200, 1000, 100)
	k = 100
	n_it = 10
	error1, t1 = n_qr(m, nrange, k, n_it, er_out=True, random=False)
	error2, t2, t_rp = n_qr(m, nrange, k, n_it, er_out=True, random=True)


# test run changing k
def run_k_qr():
	m = 1500
	n = 2500
	krange = np.arange(110, 580, 100)
	n_it = 10
	error1, t1 = k_qr(m, n, krange, n_it, er_out=True, random=False)
	error2, t2, t_rp = k_qr(m, n, krange, n_it, er_out=True, random=True)
	