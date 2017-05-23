import numpy as np
import sys
sys.path.insert(0, '../core/')
import QR_tools as qrt

er_out = True


# generate data changing m
mrange  = np.arange(120, 400, 100)
n       = 150
k       = 100
n_it    = 3
qrt.m_qr(mrange, n, k, n_it, er_out, random=False)
qrt.m_qr(mrange, n, k, n_it, er_out, random=True)


# generate data changing n
m       = 150
nrange  = np.arange(120, 400, 100)
k       = 100
n_it    = 3
qrt.n_qr(m, nrange, k, n_it, er_out, random=False)
qrt.n_qr(m, nrange, k, n_it, er_out, random=True)

#generate data changing k
m       = 150
n       = 150
krange  = np.arange(10, 70, 10)
n_it    = 3
qrt.k_qr(m, n, krange, n_it, er_out, random=False)
qrt.k_qr(m, n, krange, n_it, er_out, random=True)

# plot data
qrt.run_plot('m', 'qr')
qrt.run_plot('n', 'qr')
qrt.run_plot('k', 'qr')

