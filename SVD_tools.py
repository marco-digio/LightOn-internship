import numpy as np
import os
import matplotlib.pyplot as plt
import RQR

	
# synthetic data
def synthetic_data(m, n, k):
	return np.dot(np.random.randn(m, k), np.random.randn(k, n))


# QR for different values of m
def m_svd(mrange, n, k, n_it, er_out = False, p=10, random=False):
	n_m = np.size(mrange)
	
	error = np.zeros(n_m)
	t_tot = np.zeros(n_m)
	t_rp  = np.zeros(n_m)
	
	for i in range(n_m):
		m = mrange[i]
		print 'm = ', m
		A = synthetic_data(m, n, k)
		error[i], t_tot[i], t_rp[i] = RSVD.av_et_SVD(A, k+p, n_it, er_out, random)
		
	try:
		os.mkdir('data')
	except OSError:
		pass

	if random == False:
		np.savez('data/m_svd.npz', mrange=mrange, error=error, t_tot=t_tot)
		return error, t_tot
	else:
		np.savez('data/m_rsvd.npz', mrange=mrange, error=error, t_tot=t_tot, t_rp=t_rp)
		return error, t_tot, t_rp
	
	
# QR for different values of n
def n_svd(m, nrange, k, n_it, er_out = False, p=10, random=False):
	n_n = np.size(nrange)
	
	error = np.zeros(n_n)
	t_tot = np.zeros(n_n)
	t_rp  = np.zeros(n_n)
	
	for i in range(n_n):
		n = nrange[i]
		print 'n = ', n
		A = synthetic_data(m, n, k)
		error[i], t_tot[i], t_rp[i] = RSVD.av_et_SVD(A, k+p, n_it, er_out, random)
		
	try:
		os.mkdir('data')
	except OSError:
		pass

	if random == False:
		np.savez('data/n_svd.npz', nrange=nrange, error=error, t_tot=t_tot)
		return error, t_tot
	else:
		np.savez('data/n_rsvd.npz', nrange=nrange, error=error, t_tot=t_tot, t_rp=t_rp)
		return error, t_tot, t_rp


# QR for different values of k
def k_svd(m, n, krange, n_it, er_out = False, p=10, random = False):
	n_k = np.size(krange)
	
	error = np.zeros(n_k)
	t_tot = np.zeros(n_k)
	t_rp  = np.zeros(n_k)
	
	for i in range(n_k):
		k = krange[i]
		print 'k = ', k
		A = synthetic_data(m, n, k)
		error[i], t_tot[i], t_rp[i]  = RSVD.av_et_SVD(A, k+p, n_it, er_out, random)
			
	try:
		os.mkdir('data')
	except OSError:
		pass			

	if random == False:
		np.savez('data/k_svd.npz', krange=krange, error=error, t_tot=t_tot)
		return error, t_tot
	else:
		np.savez('data/k_rsvd.npz', krange=krange, error=error, t_tot=t_tot, t_rp=t_rp)
		return error, t_tot, t_rp


# test run changing m
def run_m_svd():
	mrange = np.arange(200, 1000, 100)
	n = 2000
	k = 100
	n_it = 10
	error1, t1 = m_svd(mrange, n, k, n_it, er_out=True, random=False)
	error2, t2, t_rp = m_svd(m, n, krange, n_it, er_out=True, random=True)


# test run changing n
def run_n_svd():
	m = 500
	nrange = np.arange(200, 1000, 100)
	k = 100
	n_it = 10
	error1, t1 = n_svd(m, nrange, k, n_it, er_out=True, random=False)
	error2, t2, t_rp = n_svd(m, nrange, k, n_it, er_out=True, random=True)


# test run changing k
def run_k_svd():
	m = 1500
	n = 2500
	krange = np.arange(110, 580, 100)
	n_it = 10
	error1, t1 = k_svd(m, n, krange, n_it, er_out=True, random=False)
	error2, t2, t_rp = k_svd(m, n, krange, n_it, er_out=True, random=True)
	
	
# make three plots
def plot_q(range1, range2, error1, t1, error2, t2, t_rp, type, type2):
	
	try:
		os.mkdir('plot')
	except OSError:
		pass
	
	# plot error
	plt.figure(1)
	plt.plot(range1, error1, 'r', label = type2, linewidth = 2)
	plt.plot(range2, error2, 'b', label = 'Randomized '+type2, linewidth = 2)
	plt.ylabel('error', fontsize = 20)
	plt.xlabel(type, fontsize = 20)
	plt.legend(loc = 'best', fontsize = 20)
	plt.xlim(min(range1[0], range2[0]), max(range1[-1], range2[-1]))
	plt.ylim(0, max([np.max(error1), np.max(error2)]) * 1.1)
	plt.savefig('plot/'+type+'_'+type2+'_error.pdf')

	# plot time
	plt.figure(2)
	plt.plot(range1, t1, 'r', label = type2, linewidth = 2)
	plt.plot(range2, t2, 'b', label = 'Randomized '+type2, linewidth = 2)
	plt.plot(range2, t_rp, 'g', label = 'RP', linewidth = 2)
	plt.ylabel('computational time', fontsize = 20)
	plt.xlabel(type, fontsize = 20)
	plt.legend(loc = 'best', fontsize = 20)
	plt.xlim(min(range1[0], range2[0]), max(range1[-1], range2[-1]))
	plt.ylim(0, max([np.max(t1), np.max(t2)]) * 1.1)
	plt.savefig('plot/'+type+'_'+type2+'_time.pdf')
	
	# plot ratio
	plt.figure(3)
	plt.plot(range2, t_rp/t2, 'b', label = 'ratio', linewidth = 2)
	plt.ylabel('ratio', fontsize = 20)
	plt.xlabel('k', fontsize = 20)
	plt.legend(loc = 'best', fontsize = 20)
	plt.xlim(range2[0], range2[-1])
	plt.ylim(0, np.max(t_rp/t2) * 1.1)
	plt.savefig('plot/'+type+'_'+type2+'_ratio.pdf')

	plt.show()
	
	
# read and plot
def run_plot(type, type2):
	# read first file
	data1 = np.load('data/'+type+'_'+type2+'.npz')
	range1 = data1[type+'range']
	error1 = data1['error']
	t1 = data1['t_tot']

	# read second file
	data2 = np.load('data/'+type+'_r'+type2+'.npz')
	range2 = data2[type+'range']
	error2 = data2['error']
	t2 = data2['t_tot']
	t_rp = data2['t_rp']

	# plot
	plot_q(range1, range2, error1, t1, error2, t2, t_rp, type, type2)

     
     
