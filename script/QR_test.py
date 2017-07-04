import numpy as np
import sys
sys.path.insert(0, '../core/')
import QR_tools as qrt

er_out = True


# generate data changing m
mrange  = np.arange(1000, 1300, 110)
n       = 1000
k       = 500
n_it    = 2
qrt.m_qr(mrange, n, k, n_it, er_out, random=False)
qrt.m_qr(mrange, n, k, n_it, er_out, random=True, abs_val=False)


# generate data changing n
m       = 1000
nrange  = np.arange(1000, 1400, 110)
k       = 500
n_it    = 2
qrt.n_qr(m, nrange, k, n_it, er_out, random=False)
qrt.n_qr(m, nrange, k, n_it, er_out, random=True, abs_val=False)

#generate data changing k
m       = 1000
n       = 1000
krange  = np.arange(100, 700, 130)
n_it    = 2
qrt.k_qr(m, n, krange, n_it, er_out, random=False)
qrt.k_qr(m, n, krange, n_it, er_out, random=True, abs_val=False)

# plot data
qrt.run_plot('m', 'qr')
qrt.run_plot('n', 'qr')
qrt.run_plot('k', 'qr')
