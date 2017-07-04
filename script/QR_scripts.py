import numpy as np
import sys
sys.path.insert(0, '../core/')
import QR_tools as qrt

er_out = True


# generate data changing m
mrange  = np.arange(1000, 3000, 100)
n       = 1500
k       = 500
n_it    = 5
qrt.m_qr(mrange, n, k, n_it, er_out, random=False)
qrt.m_qr(mrange, n, k, n_it, er_out, random=True, abs_val=True)


# generate data changing n
m       = 1500
nrange  = np.arange(1000, 3000, 100)
k       = 500
n_it    = 5
qrt.n_qr(m, nrange, k, n_it, er_out, random=False)
qrt.n_qr(m, nrange, k, n_it, er_out, random=True, abs_val=True)

#generate data changing k
m       = 1500
n       = 1500
krange  = np.arange(100, 700, 100)
n_it    = 5
qrt.k_qr(m, n, krange, n_it, er_out, random=False)
qrt.k_qr(m, n, krange, n_it, er_out, random=True, abs_val=True)

# plot data
qrt.run_plot('m', 'qr')
qrt.run_plot('n', 'qr')
qrt.run_plot('k', 'qr')

