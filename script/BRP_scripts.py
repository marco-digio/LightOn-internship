import numpy as np
import sys
sys.path.insert(0, '../core/')
import BRP_tools as brpt


# generate data changing m
mrange  = np.arange(120, 400, 100)
n       = 150
k       = 100
n_it    = 3
qrt.m_qr(mrange, n, k, n_it, random=False)
qrt.m_qr(mrange, n, k, n_it, random=True)


# generate data changing n
m       = 150
nrange  = np.arange(120, 400, 100)
k       = 100
n_it    = 3
qrt.n_qr(m, nrange, k, n_it, random=False)
qrt.n_qr(m, nrange, k, n_it, random=True)

#generate data changing k
m       = 150
n       = 150
krange  = np.arange(10, 70, 10)
n_it    = 3
qrt.k_qr(m, n, krange, n_it, random=False)
qrt.k_qr(m, n, krange, n_it, random=True)

# plot data
qrt.run_plot('m', 'brp')
qrt.run_plot('n', 'brp')
qrt.run_plot('k', 'brp')

