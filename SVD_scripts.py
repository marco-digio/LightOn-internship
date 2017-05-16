import numpy as np
import SVD_tools as svdt

mrange  = np.arange(200, 2000, 100)
n       = 1500
k       = 100
n_it    = 10
svdt.run_m_svd(mrange, n, k, n_it)
svdt.run_plot('m', 'svd')

m       = 1500
nrange  = np.arange(200, 2000, 100)
k       = 100
n_it    = 10
svdt.run_n_svd(m, nrange, k, n_it)
svdt.run_plot('n', 'svd')

m       = 1500
n       = 1500
krange  = np.arange(90, 690, 100)
n_it    = 10
svdt.run_k_svd(m, n, krange, n_it)
svdt.run_plot('k', 'svd')


