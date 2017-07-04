import numpy as np
import sys
sys.path.insert(0, '../core/')
import SVD_tools as svdt

er_out = True


# generate data changing m
#mrange  = np.arange(120, 400, 100)
mrange  = np.asarray([200, 500, 1000, 2000, 5000, 10000, 15000, 20000, 30000]) 

n       = 2000
k       = 500
n_it    = 5
svdt.m_svd(mrange, n, k, n_it, er_out, random=False)
svdt.m_svd(mrange, n, k, n_it, er_out, random=True)


# generate data changing n
m       = 2000
#nrange  = np.arange(120, 400, 100)
nrange  = np.asarray([200, 500, 1000, 2000, 5000, 10000, 15000, 20000, 30000]) 

k       = 500
n_it    = 5
svdt.n_svd(m, nrange, k, n_it, er_out, random=False)
svdt.n_svd(m, nrange, k, n_it, er_out, random=True)

#generate data changing k
m       = 2000
n       = 2000
#krange  = np.arange(10, 70, 15)
krange  = np.asarray([20, 50, 100, 200, 500, 700, 1000, 1400, 1800]) 

n_it    = 5
svdt.k_svd(m, n, krange, n_it, er_out, random=False)
svdt.k_svd(m, n, krange, n_it, er_out, random=True)

# plot data
svdt.run_plot('m', 'svd')
svdt.run_plot('n', 'svd')
svdt.run_plot('k', 'svd')

