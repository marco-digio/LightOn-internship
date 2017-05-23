import numpy as np
import NMF_tools as nmft

name = 'synth'

mrange  = np.arange(350, 1500, 50)
n       = 1000
r       = 10
k       = 300
n_it    = 10
nmft.n_nmf(name=name, mrange=mrange, n=n, r=r, n_it=n_it, k=0, er_out=True)
nmft.n_nmf(name=name, mrange=mrange, n=n, r=r, n_it=n_it, k=k, er_out=True)
nmft.run_plot('m', 'nmf_'+name)

m       = 1000
nrange  = np.arange(350, 1500, 50)
r       = 10
k       = 300
n_it    = 10
nmft.n_nmf(name=name, m=m, nrange=nrange, r=r, n_it=n_it, k=0, er_out=True)
nmft.n_nmf(name=name, m=m, nrange=nrange, r=r, n_it=n_it, k=k, er_out=True)
nmft.run_plot('n', 'nmf_'+name)

m       = 1000
n       = 1000
rrange  = np.arange(10, 50, 4)
k       = 300
n_it    = 10
nmft.r_nmf(name=name, rrange=rrange, n_it=n_it, k=0, m=m, n=n, er_out=True)
nmft.r_nmf(name=name, rrange=rrange, n_it=n_it, k=k, m=m, n=n, er_out=True)
nmft.run_plot('r', 'nmf_'+name)

m       = 1000
n       = 1000
r       = 10
krange  = np.arange(10, 900, 25)
n_it    = 10
nmft.r_nmf(name=name, r=r, n_it=n_it, k=krange, m=m, n=n, er_out=True,
        random_proj=False)
nmft.r_nmf(name=name, r=r, n_it=n_it, k=krange, m=m, n=n, er_out=True)
nmft.run_plot('k', 'nmf_'+name)

