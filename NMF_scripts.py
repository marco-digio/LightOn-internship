import numpy as np
import NMF_tools as nmft

mrange  = np.arange(200, 600, 100)
n       = 500
r       = 10
k       = 100
n_it    = 3
nmft.run_m_nmf(mrange, n, r, k, n_it)
nmft.run_plot('m', 'nmf')

m       = 500
nrange  = np.arange(200, 600, 100)
r       = 10
k       = 100
n_it    = 3
nmft.run_n_nmf(m, nrange, r, k, n_it)
nmft.run_plot('n', 'nmf')

m       = 500
n       = 500
rrange  = np.arange(10, 50, 10)
k       = 100
n_it    = 3
nmft.run_r_nmf(m, n, rrange, k, n_it)
nmft.run_plot('r', 'nmf')

m       = 500
n       = 500
r       = 10
krange  = np.arange(90, 490, 100)
n_it    = 3
nmft.run_k_nmf(m, n, r, krange, n_it)
nmft.run_plot('k', 'nmf')


