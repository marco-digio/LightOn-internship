import numpy as np
import sys
sys.path.insert(0, '../core/')
import SVD_tools as svdt

er_out = True


# generate data changing m
mrange  = np.arange(120, 400, 100)
n       = 150
k       = 100
n_it    = 3
svdt.m_svd(mrange, n, k, n_it, er_out, random=False)
svdt.m_svd(mrange, n, k, n_it, er_out, random=True)


# generate data changing n
m       = 150
nrange  = np.arange(120, 400, 100)
k       = 100
n_it    = 3
svdt.n_svd(m, nrange, k, n_it, er_out, random=False)
svdt.n_svd(m, nrange, k, n_it, er_out, random=True)

#generate data changing k
m       = 150
n       = 150
krange  = np.arange(10, 70, 10)
n_it    = 3
svdt.k_svd(m, n, krange, n_it, er_out, random=False)
svdt.k_svd(m, n, krange, n_it, er_out, random=True)

# plot data
svdt.run_plot('m', 'svd')
svdt.run_plot('n', 'svd')
svdt.run_plot('k', 'svd')

