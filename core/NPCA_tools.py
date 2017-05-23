import NPCA
import numpy as np
import os 
import matplotlib.pyplot as plt


# synthetic data (n observations of dimension d
def synthetic_data(n, d):
    return np.random.randn(n, d)


# average error and time
def av_et_rnpca(n, d, m, n_it):
    er   = np.zeros(n_it)
    t1   = np.zeros(n_it)
    t2   = np.zeros(n_it)
    t_rp = np.zeros(n_it)

    for it in range(n_it):
        A = synthetic_data(n, d)
        er[it], t1[it], t2[it], t_rp[it] = NPCA.et_rnpca(A, m)

    return np.mean(er), np.mean(t1), np.mean(t2), np.mean(t_rp)


# change n and perform RNPCA
def run_n(nrange, d, m, n_it):
    n_n = np.size(nrange)

    error = np.zeros(n_n)
    t1    = np.zeros(n_n)
    t2    = np.zeros(n_n)
    t_rp  = np.zeros(n_n)

    for i in range(n_n):
        n = nrange[i]
        print 'n = ', n
        error[i], t1[i], t2[i], t_rp[i] = av_et_rnpca(n, d, m, n_it)
    
    try:
        os.mkdir('../data')
    except OSError:
        pass

    np.savez('../data/rnpca_n.npz', nrange=nrange, error=error, t1=t1, t2=t2,
            t_rp=t_rp)


# change d and perform RNPCA
def run_d(n, drange, m, n_it):
    n_d = np.size(drange)

    error = np.zeros(n_d)
    t1    = np.zeros(n_d)
    t2    = np.zeros(n_d)
    t_rp  = np.zeros(n_d)

    for i in range(n_d):
        d = drange[i]
        print 'd = ', d
        error[i], t1[i], t2[i], t_rp[i] = av_et_rnpca(n, d, m, n_it)
    
    try:
        os.mkdir('../data')
    except OSError:
        pass

    np.savez('../data/rnpca_d.npz', drange=drange, error=error, t1=t1, t2=t2,
            t_rp=t_rp)


# change m and perform RNPCA
def run_m(n, d, mrange, n_it):
    n_m = np.size(mrange)

    error = np.zeros(n_m)
    t1    = np.zeros(n_m)
    t2    = np.zeros(n_m)
    t_rp  = np.zeros(n_m)

    for i in range(n_m):
        m = mrange[i]
        print 'm = ', m
        error[i], t1[i], t2[i], t_rp[i] = av_et_rnpca(n, d, m, n_it)
    
    try:
        os.mkdir('../data')
    except OSError:
        pass

    np.savez('../data/rnpca_m.npz', mrange=mrange, error=error, t1=t1, t2=t2,
            t_rp=t_rp)


# plot error, computational time and ratio
def plot(range1, error, t1, t2, t_rp, type1):
    
    try:
        os.mkdir('plot')
    except OSError:
        pass

    plt.figure(1)
    plt.plot(range1, error, 'b', label='error', linewidth=2)
    plt.ylabel('error = $|| \hat{K} - K||$', fontsize=20)
    plt.xlabel(type1, fontsize=20)
    plt.legend(loc='best', fontsize=20)
    plt.savefig('../plot/rnpca_'+type1+'_error.pdf')

    plt.figure(2)
    plt.plot(range1, t1, 'r', label='Kernel', linewidth=2)
    plt.plot(range1, t2, 'b', label='RNPCA', linewidth=2)
    plt.plot(range1, t_rp, 'g', label='RP', linewidth=2)
    plt.ylabel('computational time', fontsize=20)
    plt.xlabel(type1, fontsize=20)
    plt.legend(loc='best', fontsize=20)
    plt.ylim(0, max([np.max(t1), np.max(t2)]) * 1.1)
    plt.savefig('../plot/rnpca_'+type1+'_time.pdf')

    plt.figure(3)
    plt.plot(range1, t_rp/t2, 'b', label='ratio', linewidth=2)
    plt.ylabel('ratio', fontsize=20)
    plt.xlabel(type1, fontsize=20)
    plt.legend(loc='best', fontsize=20)
    plt.savefig('../plot/rnpca_'+type1+'_ratio.pdf')
    
    plt.close('all')


# read file and plot data
def run_plot(type1):
    data = np.load('../data/rnpca_'+type1+'.npz')
    range1 = data[type1+'range']
    error = data['error']
    t1 = data['t1']
    t2 = data['t2']
    t_rp = data['t_rp']
    plot(range1, error, t1, t2, t_rp, type1)
    


