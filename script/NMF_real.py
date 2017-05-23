import numpy as np
import NMF_tools as nmft
import scipy.io

def real_dataset(name):
    mat = scipy.io.loadmat('dataset/'+name+'/'+name+'.mat')
    data = np.asarray(mat[name+'_corrected'])
    data_matrix = np.abs(data.reshape(np.shape(data)[0] * np.shape(data)[1],
                                      np.shape(data)[2]))
    return data_matrix


name = 'salinasA'
A = real_dataset(name)

rrange = np.arange(1, 30, 2)
k = 300
n_it = 10
nmft.r_nmf(name=name, rrange=rrange, n_it=n_it, k=0, A=A, er_out=True)
nmft.r_nmf(name=name, rrange=rrange, n_it=n_it, k=k, A=A, er_out=True)
nmft.run_plot('r', 'nmf_'+name)

r = 15
krange = np.arange(10, 700, 30)
n_it = 10
nmft.k_nmf(name=name, r=r, n_it=n_it, krange=krange, A=A, er_out=True,
        random_proj=False)
nmft.k_nmf(name=name, r=r, n_it=n_it, krange=krange, A=A, er_out=True)
nmft.run_plot('k', 'nmf_'+name)


name = 'indian_pines'
A = real_dataset(name)

rrange = np.arange(1, 30, 2)
k = 300
n_it = 10
nmft.r_nmf(name=name, rrange=rrange, n_it=n_it, k=0, A=A, er_out=True)
nmft.r_nmf(name=name, rrange=rrange, n_it=n_it, k=k, A=A, er_out=True)
nmft.run_plot('r', 'nmf_'+name)

r = 15
krange = np.arange(10, 700, 30)
n_it = 10
nmft.k_nmf(name=name, r=r, n_it=n_it, krange=krange, A=A, er_out=True,
        random_proj=False)
nmft.k_nmf(name=name, r=r, n_it=n_it, krange=krange, A=A, er_out=True)
nmft.run_plot('k', 'nmf_'+name)

