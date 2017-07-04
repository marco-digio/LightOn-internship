import numpy as np
import os
import matplotlib.pyplot as plt
import QR

	
# synthetic data
def synthetic_data(m, n, k):
    return np.dot(np.random.randn(m, k), np.random.randn(k, n))


# Average of error and time for (R)QR decomposition
def av_et_QR(m, n, k, n_it, er_out=True, random=False, abs_val=False):

    er = np.zeros(n_it)
    t_tot = np.zeros(n_it)
    t_rp = np.zeros(n_it)

    for it in range(n_it):
	#print 'it = ', it
		A = synthetic_data(m, n, k)
		_, _, er[it], t_tot[it], t_rp[it] = QR.et_QR(A, int(k * 1.1), er_out, random, abs_val)
	
    return np.mean(er), np.mean(t_tot), np.mean(t_rp)


# QR for different values of m
def m_qr(mrange, n, k, n_it, er_out=True, random=False, abs_val=False):
    n_m = np.size(mrange)
	
    error = np.zeros(n_m)
    t_tot = np.zeros(n_m)
    t_rp  = np.zeros(n_m)
	
    for i in range(n_m):
	m = mrange[i]
	print 'm = ', m
	error[i], t_tot[i], t_rp[i] = av_et_QR(m, n, k, n_it, er_out, random, abs_val)
		
    try:
	os.mkdir('../data')
    except OSError:
	pass

    if random == False:
	np.savez('../data/qr_m.npz', mrange=mrange, error=error, t_tot=t_tot)
	return error, t_tot
    else:
	np.savez('../data/rqr_m.npz', mrange=mrange, error=error, t_tot=t_tot, t_rp=t_rp)
	return error, t_tot, t_rp
	
	
# QR for different values of n
def n_qr(m, nrange, k, n_it, er_out=True, random=False, abs_val=False):
    n_n = np.size(nrange)
	
    error = np.zeros(n_n)
    t_tot = np.zeros(n_n)
    t_rp  = np.zeros(n_n)
	
    for i in range(n_n):
	n = nrange[i]
	print 'n = ', n
	error[i], t_tot[i], t_rp[i] = av_et_QR(m, n, k, n_it, er_out, random,
                abs_val)
		
    try:
    	os.mkdir('../data')
    except OSError:
    	pass

    if random == False:
	np.savez('../data/qr_n.npz', nrange=nrange, error=error, t_tot=t_tot)
	return error, t_tot
    else:
	np.savez('../data/rqr_n.npz', nrange=nrange, error=error, t_tot=t_tot, t_rp=t_rp)
	return error, t_tot, t_rp


# QR for different values of k
def k_qr(m, n, krange, n_it, er_out=True, random=False, abs_val=False):
    n_k = np.size(krange)
	
    error = np.zeros(n_k)
    t_tot = np.zeros(n_k)
    t_rp  = np.zeros(n_k)
	
    for i in range(n_k):
	k = krange[i]
	print 'k = ', k
	error[i], t_tot[i], t_rp[i]  = av_et_QR(m, n, k, n_it, er_out, random,
                abs_val)
			
    try:
	os.mkdir('../data')
    except OSError:
	pass			

    if random == False:
	np.savez('../data/qr_k.npz', krange=krange, error=error, t_tot=t_tot)
        return error, t_tot
    else:
	np.savez('../data/rqr_k.npz', krange=krange, error=error, t_tot=t_tot, t_rp=t_rp)
	return error, t_tot, t_rp


# make three plots
def plot(range1, range2, error1, t1, error2, t2, t_rp, type1, type2):
	
    try:
	os.mkdir('../plot')
    except OSError:
	pass
    
    # plot error
    plt.figure(1)
    plt.plot(range1, error1, 'r', label=type2, linewidth=2,
             marker='o', linestyle='-')
    plt.plot(range2, error2, 'b', label = 'Randomized '+type2, linewidth=2,
             marker='o', linestyle='-')
    plt.ylabel('error', fontsize = 20)
    plt.xlabel(type1, fontsize = 20)
    plt.legend(loc='best', fontsize=20)
    plt.xlim(min(range1[0], range2[0]), max(range1[-1], range2[-1]))
    plt.ylim(0, max([np.max(error1), np.max(error2)]) * 1.1)
    plt.savefig('../plot/'+type2+'_'+type1+'_error.pdf')

    # plot time
    plt.figure(2)
    plt.plot(range1, t1, 'r', label=type2, linewidth=2,
             marker='o', linestyle='-')
    plt.plot(range2, t2, 'b', label='Randomized '+type2, linewidth=2,
             marker='o', linestyle='-')
    plt.plot(range2, t_rp, 'g', label='RP', linewidth=2,
             marker='o', linestyle='-')
    plt.ylabel('computational time', fontsize=20)
    plt.xlabel(type1, fontsize=20)
    plt.legend(loc='best', fontsize=20)
    plt.xlim(min(range1[0], range2[0]), max(range1[-1], range2[-1]))
    plt.ylim(0, max([np.max(t1), np.max(t2)]) * 1.1)
    plt.savefig('../plot/'+type2+'_'+type1+'_time.pdf')
	
    # plot ratio
    plt.figure(3)
    plt.plot(range2, t_rp/t2, 'b', label = 'ratio', linewidth=2,
             marker='o', linestyle='-')
    plt.ylabel('ratio', fontsize=20)
    plt.xlabel(type1, fontsize=20)
    plt.legend(loc='best', fontsize=20)
    plt.xlim(range2[0], range2[-1])
    plt.ylim(0, np.max(t_rp/t2) * 1.1)
    plt.savefig('../plot/'+type2+'_'+type1+'_ratio.pdf')

    #plt.show()
    plt.close('all')
	
	
# read and plot
def run_plot(type1, type2):
    # read first file
    data1 = np.load('../data/'+type2+'_'+type1+'.npz')
    range1 = data1[type1+'range']
    error1 = data1['error']
    t1 = data1['t_tot']

    # read second file
    data2 = np.load('../data/r'+type2+'_'+type1+'.npz')
    range2 = data2[type1+'range']
    error2 = data2['error']
    t2 = data2['t_tot']
    t_rp = data2['t_rp']

    # plot
    plot(range1, range2, error1, t1, error2, t2, t_rp, type1, type2)

     
     
