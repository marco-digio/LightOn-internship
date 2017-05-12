import numpy as np
import os
import matplotlib.pyplot as plt
import RNMF

	
# synthetic data
def synthetic_data(m, n, j = 100, sigma = 0.1):
	X = np.random.random((m, j));
	Y = np.random.random((j, n));
	N = np.random.normal(0, sigma, (m, n));
	A = np.abs(np.dot(X, Y) + N);
	return A
	

# another kind of synthetic data
def synthetic_data2(m, n, k):
	A = np.abs(np.dot(np.random.random((m, k)), np.random.random((k, n))))
	return A


# NMF for different values of m
def m_nmf(mrange, n, r, n_it, k=0, er_out = False):
	n_m = np.size(mrange)
	
	error = np.zeros(n_m)
	t_tot = np.zeros(n_m)
	t_rp  = np.zeros(n_m)
	
	for i in range(n_m):
		m = mrange[i]
		print 'm = ', m
		A = synthetic_data(m, n)
		error[i], t_tot[i], t_rp[i] = RNMF.av_et_NMF(A, r, n_it, k, er_out)
		
	try:
		os.mkdir('data')
	except OSError:
		pass

	if k==0:
		np.savez('data/m_nmf.npz', mrange=mrange, error=error, t_tot=t_tot)
		return error, t_tot
	else:
		np.savez('data/m_rnmf.npz', mrange=mrange, error=error, t_tot=t_tot, t_rp=t_rp)
		return error, t_tot, t_rp
	
	
# NMF for different values of n
def n_nmf(m, nrange, r, n_it, k=0, er_out = False):
	n_n = np.size(nrange)
	
	error = np.zeros(n_n)
	t_tot = np.zeros(n_n)
	t_rp  = np.zeros(n_n)
	
	for i in range(n_n):
		n = nrange[i]
		print 'n = ', n
		A = synthetic_data(m, n)
		error[i], t_tot[i], t_rp[i] = RNMF.av_et_NMF(A, r, n_it, k, er_out)
		
	try:
		os.mkdir('data')
	except OSError:
		pass

	if k==0:
		np.savez('data/n_nmf.npz', nrange=nrange, error=error, t_tot=t_tot)
		return error, t_tot
	else:
		np.savez('data/n_rnmf.npz', nrange=nrange, error=error, t_tot=t_tot, t_rp=t_rp)
		return error, t_tot, t_rp

# NMF for different values of r
def r_nmf(m, n, rrange, n_it, k=0, er_out = False):
	n_r = np.size(rrange)
	
	error = np.zeros(n_r)
	t_tot = np.zeros(n_r)
	t_rp  = np.zeros(n_r)
	
	for i in range(n_r):
		r = rrange[i]
		print 'r = ', r
		A = synthetic_data(m, n)
		error[i], t_tot[i], t_rp[i] = RNMF.av_et_NMF(A, r, n_it, k, er_out)
		
	try:
		os.mkdir('data')
	except OSError:
		pass

	if k==0:
		np.savez('data/r_nmf.npz', rrange=rrange, error=error, t_tot=t_tot)
		return error, t_tot
	else:
		np.savez('data/r_rnmf.npz', rrange=rrange, error=error, t_tot=t_tot, t_rp=t_rp)
		return error, t_tot, t_rp

# NMF for different values of k
def k_nmf(m, n, r, n_it, krange, er_out = False, random=True):
        if random==False:
            error, t_tot, _ = RNMF.av_et_NMF(synthetic_data(m, n), r, n_it, k=0, er_out=True)
        else:
	    n_k = np.size(krange)
	
            error = np.zeros(n_k)
	    t_tot = np.zeros(n_k)
	    t_rp  = np.zeros(n_k)
	
	    for i in range(n_k):
	        k = krange[i]
		print 'k = ', k
		A = synthetic_data(m, n)
		error[i], t_tot[i], t_rp[i]  = RNMF.av_et_NMF(A, r, n_it, k, er_out)
			
        try:
	    	os.mkdir('data')
	except OSError:
		pass	

        if random==False:
            np.savez('data/k_nmf.npz', krange=krange,
                    error=np.ones(np.size(krange))*error,
                    t_tot=np.ones(np.size(krange))*t_tot)
            return error, t_tot
        else:
            np.savez('data/k_rnmf.npz', krange=krange, error=error, t_tot=t_tot, t_rp=t_rp)
	    return error, t_tot, t_rp


# test run changing m
def run_m_nmf(mrange, n, r, k, n_it):
        error1, t1 = m_nmf(mrange, n, r, n_it, k=0, er_out=True)
	error2, t2, t_rp = m_nmf(mrange, n, r, n_it, k, er_out=True)
        

# test run changing n
def run_n_nmf(m, nrange, r, k, n_it):
	error1, t1 = n_nmf(m, nrange, r, n_it, k=0, er_out=True)
	error2, t2, t_rp = n_nmf(m, nrange, r, n_it, k, er_out=True)

# test run changing k
def run_r_nmf(m, n, rrange, k, n_it):
	error1, t1 = r_nmf(m, n, rrange, n_it, k=0, er_out=True)
	error2, t2, t_rp = r_nmf(m, n, rrange, n_it, k, er_out=True)

# test run changing k
def run_k_nmf(m, n, r, krange, n_it):
        error1, t1, _ = k_nmf(m, n, r, n_it, krange, er_out=True, random=True)
	error2, t2, t_rp = k_nmf(m, n, r, n_it, krange, er_out=True)
	
	
# make three plots
def plot_nmf(range1, range2, error1, t1, error2, t2, t_rp, type, type2):
	
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

	#plt.show()
	plt.close('all')
	
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
	plot_nmf(range1, range2, error1, t1, error2, t2, t_rp, type, type2)

     
     
