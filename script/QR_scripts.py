import numpy as np
import sys
sys.path.insert(0, '../core/')
import QR_tools as qrt

er_out = True


# generate data changing m
#mrange  = np.arange(1000, 3000, 100)
mrange  = np.asarray([1000, 2000, 5000, 10000, 15000]) 
n       = 2000
k       = 500
n_it    = 3
qrt.m_qr(mrange, n, k, n_it, er_out, random=False)
qrt.m_qr(mrange, n, k, n_it, er_out, random=True, abs_val=True)


# generate data changing n
m       = 2000
#nrange  = np.arange(1000, 3000, 100)
nrange  = np.asarray([1000, 2000, 5000, 10000, 15000]) 
k       = 500
n_it    = 3
qrt.n_qr(m, nrange, k, n_it, er_out, random=False)
qrt.n_qr(m, nrange, k, n_it, er_out, random=True, abs_val=True)

#generate data changing k
m       = 2000
n       = 2000
#krange  = np.arange(100, 700, 100)
krange  = np.asarray([20, 50, 100, 200, 500, 700, 1000, 1400, 1800]) 
n_it    = 3
qrt.k_qr(m, n, krange, n_it, er_out, random=False)
qrt.k_qr(m, n, krange, n_it, er_out, random=True, abs_val=True)

# plot data
#qrt.run_plot('m', 'qr')
#qrt.run_plot('n', 'qr')
#qrt.run_plot('k', 'qr')

