import numpy as np
import QR_tools as qrt

mrange  = np.arange(120, 2000, 100)
n       = 1500
k       = 100
n_it    = 10
qrt.run_m_qr(mrange, n, k, n_it)
qrt.run_plot('m', 'qr')

m       = 1500
nrange  = np.arange(120, 2000, 100)
k       = 100
n_it    = 10
qrt.run_n_qr(m, nrange, k, n_it)
qrt.run_plot('n', 'qr')

m       = 1500
n       = 1500
krange  = np.arange(10, 710, 50)
n_it    = 10
qrt.run_k_qr(m, n, krange, n_it)
qrt.run_plot('k', 'qr')


