import numpy as np
import sys
sys.path.insert(0, '../core/')
import BRP_tools as brpt

corr = True
abs_val = False


# generate data changing m
mrange  = np.asarray([200, 500, 1000, 2000, 5000, 10000, 15000, 20000]) 
n       = 2000
k       = 500
n_it    = 3
brpt.m_brp(mrange, n, k, n_it, corr, abs_val)


# generate data changing n
m       = 2000
nrange  = np.asarray([200, 500, 1000, 2000, 5000, 10000, 15000, 20000]) 
k       = 500
n_it    = 3
brpt.n_brp(m, nrange, k, n_it, corr, abs_val)

#generate data changing k
m       = 2000
n       = 2000
krange  = np.asarray([20, 50, 100, 200, 500, 700, 1000, 1400, 1800]) 
n_it    = 3
brpt.k_brp(m, n, krange, n_it, corr, abs_val)

# plot data
#brpt.run_plot('m', 'brp')
#brpt.run_plot('n', 'brp')
#brpt.run_plot('k', 'brp')

