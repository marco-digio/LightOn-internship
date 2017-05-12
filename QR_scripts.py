import numpy as np
import QR_tools as qrt

mrange  = np.arange(200, 600, 100)
n       = 500
k       = 100
n_it    = 3
qrt.run_m_qr(mrange, n, k, n_it)
qrt.run_plot('m', 'qr')

m       = 500
nrange  = np.arange(200, 600, 100)
k       = 100
n_it    = 3
qrt.run_n_qr(m, nrange, k, n_it)
qrt.run_plot('n', 'qr')

m       = 500
n       = 500
krange  = np.arange(90, 490, 100)
n_it    = 3
qrt.run_k_qr(m, n, krange, n_it)
qrt.run_plot('k', 'qr')


