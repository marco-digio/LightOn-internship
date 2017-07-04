import numpy as np
import sys
sys.path.insert(0, '../core/')
import SVD_tools as svdt

er_out = True


# generate data changing m
mrange  = np.arange(1000, 1400, 100)
n       = 1500
k       = 500
n_it    = 2
#svdt.m_svd(mrange, n, k, n_it, er_out, random=False)
#svdt.m_svd(mrange, n, k, n_it, er_out, random=True)


# generate data changing n
m       = 1500
nrange  = np.arange(1000, 1400, 100)
k       = 500
n_it    = 2
#svdt.n_svd(m, nrange, k, n_it, er_out, random=False)
#svdt.n_svd(m, nrange, k, n_it, er_out, random=True)

#generate data changing k
m       = 1500
n       = 1500
krange  = np.arange(110, 600, 70)
n_it    = 2
#svdt.k_svd(m, n, krange, n_it, er_out, random=False)
#svdt.k_svd(m, n, krange, n_it, er_out, random=True)

# plot data
svdt.run_plot('m', 'svd')
svdt.run_plot('n', 'svd')
svdt.run_plot('k', 'svd')

