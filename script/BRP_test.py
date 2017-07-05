import numpy as np
import sys
sys.path.insert(0, '../core/')
import BRP_tools as brpt

corr = False
abs_val = False


# generate data changing m
mrange  = np.arange(120, 400, 100)
n       = 150
k       = 100
n_it    = 3
#brpt.m_brp(mrange, n, k, n_it, corr, abs_val)


# generate data changing n
m       = 150
nrange  = np.arange(120, 400, 100)
k       = 100
n_it    = 3
#brpt.n_brp(m, nrange, k, n_it, corr, abs_val)

#generate data changing k
m       = 150
n       = 150
krange  = np.arange(10, 70, 10)
n_it    = 3
#brpt.k_brp(m, n, krange, n_it, corr, abs_val)

# plot data
brpt.run_plot('m', 'brp')
brpt.run_plot('n', 'brp')
brpt.run_plot('k', 'brp')

