import numpy as np
import os
import matplotlib.pyplot as plt
import KM

	
# synthetic data
def synthetic_data(k, n, d):
    centers = np.random.normal(0, k**(1./d), (d, k))
    sigma = np.sqrt(np.random.uniform(0.25, 1.75, k))
    A = np.random.normal(np.tile(centers, (1, n)), np.tile(sigma, (d, n)))
    label = np.tile(np.arange(0, k, 1), (1, n))
    #print np.shape(A), "A"
    return A.T, label


# Average of error and time for (R)k-means
def av_eFt_kmeans(k, n, d, n_it, r=0, rand_init=True):

    er = np.zeros(n_it)
    F = np.zeros(n_it)
    t_tot = np.zeros(n_it)
    t_rp = np.zeros(n_it)

    for it in range(n_it):
	#print 'it = ', it
        A, real = synthetic_data(k, n, d)
        if rand_init==True:
            init=None
        else:
            init=np.arange(0, k, 1)

        er[it], F[it], t_tot[it], t_rp[it], _ = KM.eFt_kmeans(A, k, real, r, init)
	
    return np.mean(er), np.mean(F), np.mean(t_tot), np.mean(t_rp)


def k_kmeans(krange, n, d, r, n_it, rand_init=True):
    n_k = np.size(krange)
	
    error = np.zeros(n_k)
    F     = np.zeros(n_k)
    t_tot = np.zeros(n_k)
    t_rp  = np.zeros(n_k)
    
    for i in range(n_k):
        k = krange[i]
        print 'k = ', k
        error[i], F[i], t_tot[i], t_rp[i] = av_eFt_kmeans(k, n, d, n_it, 
                                                          r, rand_init)
    
    try:
        os.mkdir('data')
    except OSError:
        pass

    if r==0:
        np.savez('data/kmeans_k.npz', krange=krange, error=error, F=F,
                t_tot=t_tot)
        return error, F, t_tot
    else:
        np.savez('data/rkmeans_k.npz', krange=krange, error=error, F=F,
                t_tot=t_tot, t_rp=t_rp)
        return error, F, t_tot, t_rp

def n_kmeans(k, nrange, d, r, n_it, rand_init=True):
    n_n = np.size(nrange)
	
    error = np.zeros(n_n)
    F     = np.zeros(n_n)
    t_tot = np.zeros(n_n)
    t_rp  = np.zeros(n_n)
    
    for i in range(n_n):
        n = nrange[i]
        print 'n = ', n
        error[i], F[i], t_tot[i], t_rp[i] = av_eFt_kmeans(k, n, d, n_it, 
                                                          r, rand_init)
    
    try:
        os.mkdir('data')
    except OSError:
        pass

    if r==0:
        np.savez('data/kmeans_n.npz', nrange=nrange, error=error, F=F,
                t_tot=t_tot)
        return error, F, t_tot
    else:
        np.savez('data/rkmeans_n.npz', nrange=nrange, error=error, F=F,
                t_tot=t_tot, t_rp=t_rp)
        return error, F, t_tot, t_rp


def d_kmeans(k, n, drange, r, n_it, rand_init=True):
    n_d = np.size(drange)
	
    error = np.zeros(n_d)
    F     = np.zeros(n_d)
    t_tot = np.zeros(n_d)
    t_rp  = np.zeros(n_d)
    
    for i in range(n_d):
        d = drange[i]
        print 'd = ', d
        error[i], F[i], t_tot[i], t_rp[i] = av_eFt_kmeans(k, n, d, n_it, 
                                                          r, rand_init)
    
    try:
        os.mkdir('data')
    except OSError:
        pass

    if r==0:
        np.savez('data/kmeans_d.npz', drange=drange, error=error, F=F,
                t_tot=t_tot)
        return error, F, t_tot
    else:
        np.savez('data/rkmeans_d.npz', drange=drange, error=error, F=F,
                t_tot=t_tot, t_rp=t_rp)
        return error, F, t_tot, t_rp



def r_kmeans(k, n, d, rrange, n_it, rand_init=True, random_proj=True):
    if random_proj==False:
        error, F, t_tot, _ = av_eFt_kmeans(k, n, d, n_it, r=0,
                rand_init=rand_init)
    else:
        n_r = np.size(rrange)
	
        error = np.zeros(n_r)
        F     = np.zeros(n_r)
        t_tot = np.zeros(n_r)
        t_rp  = np.zeros(n_r)
    
        for i in range(n_r):
            r = rrange[i]
            print 'r = ', r
            error[i], F[i], t_tot[i], t_rp[i] = av_eFt_kmeans(k, n, d, n_it, 
                                                          r, rand_init)
    
    try:
        os.mkdir('data')
    except OSError:
        pass

    if random_proj==False:
        np.savez('data/kmeans_r.npz', rrange=rrange, 
                error=np.ones(np.size(rrange))*error, 
                F=np.ones(np.size(rrange))*F,
                t_tot=np.ones(np.size(rrange))*t_tot)
        return error, F, t_tot
    else:
        np.savez('data/rkmeans_r.npz', rrange=rrange, error=error, F=F,
                t_tot=t_tot, t_rp=t_rp)
        return error, F, t_tot, t_rp


# make three plots
def plot_kmeans(range1, range2, error1, F1, t1, error2, F2, t2, t_rp, type1, type2):
	
    try:
        os.mkdir('plot')
    except OSError:
	pass
	
    # plot error
    plt.figure(1)
    plt.plot(range1, error1, 'r', label=type2, linewidth=2, marker='o',
            linestyle='-')
    plt.plot(range2, error2, 'b', label='Randomized '+type2, linewidth=2,
            marker='o', linestyle='-')
    plt.ylabel('error', fontsize=20)
    plt.xlabel(type1, fontsize=20)
    plt.legend(loc='best', fontsize=20)
    plt.xlim(min(range1[0], range2[0]), max(range1[-1], range2[-1]))
    plt.ylim(0, max([np.max(error1), np.max(error2)]) * 1.1)
    plt.savefig('plot/'+type2+'_'+type1+'_error.pdf')

    # plot objective function
    plt.figure(2)
    plt.plot(range1, F1, 'r', label=type2, linewidth=2, marker='o',
            linestyle='-')
    plt.plot(range2, F2, 'b', label='Randomized '+type2, linewidth=2,
            marker='o', linestyle='-')
    plt.ylabel('objective function', fontsize=20)
    plt.xlabel(type1, fontsize=20)
    plt.legend(loc='best', fontsize=20)
    plt.xlim(min(range1[0], range2[0]), max(range1[-1], range2[-1]))
    plt.ylim(0, max([np.max(F1), np.max(F2)]) * 1.1)
    plt.savefig('plot/'+type2+'_'+type1+'_F.pdf')

    # plot time
    plt.figure(3)
    plt.plot(range1, t1, 'r', label=type2, linewidth=2, marker='o',
            linestyle='-')
    plt.plot(range2, t2, 'b', label='Randomized '+type2, linewidth=2,
            marker='o', linestyle='-')
    plt.plot(range2, t_rp, 'g', label='RP', linewidth=2, marker='o',
            linestyle='-')
    plt.ylabel('computational time', fontsize=20)
    plt.xlabel(type1, fontsize=20)
    plt.legend(loc='best', fontsize=20)
    plt.xlim(min(range1[0], range2[0]), max(range1[-1], range2[-1]))
    plt.ylim(0, max([np.max(t1), np.max(t2)]) * 1.1)
    plt.savefig('plot/'+type2+'_'+type1+'_time.pdf')
	
    # plot ratio
    plt.figure(4)
    plt.plot(range2, t_rp/t2, 'b', label='ratio', linewidth=2, marker='o',
            linestyle='-')
    plt.ylabel('ratio', fontsize=20)
    plt.xlabel(type1, fontsize=20)
    plt.legend(loc='best', fontsize=20)
    plt.xlim(range2[0], range2[-1])
    plt.ylim(0, np.max(t_rp/t2) * 1.1)
    plt.savefig('plot/'+type2+'_'+type1+'_ratio.pdf')

    #plt.show()
    plt.close('all')
	
# read and plot
def run_plot(type1, type2):
    # read first file
    data1 = np.load('data/'+type2+'_'+type1+'.npz')
    range1 = data1[type1+'range']
    error1 = data1['error']
    F1 = data1['F']
    t1 = data1['t_tot']

    # read second file
    data2 = np.load('data/r'+type2+'_'+type1+'.npz')
    range2 = data2[type1+'range']
    error2 = data2['error']
    F2 = data2['F']
    t2 = data2['t_tot']
    t_rp = data2['t_rp']

    # plot
    plot_kmeans(range1, range2, error1, F1,t1, error2, F2, t2, t_rp, type1, type2)

     
     
