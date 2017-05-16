import numpy as np
import SVD_tools as svdt

mrange  = np.arange(200, 600, 100)
n       = 500
k       = 100
n_it    = 3
svdt.run_m_svd(mrange, n, k, n_it)
svdt.run_plot('m', 'svd')

m       = 500
nrange  = np.arange(200, 600, 100)
k       = 100
n_it    = 3
svdt.run_n_svd(m, nrange, k, n_it)
svdt.run_plot('n', 'svd')

m       = 500
n       = 500
krange  = np.arange(90, 490, 100)
n_it    = 3
svdt.run_k_svd(m, n, krange, n_it)
svdt.run_plot('k', 'svd')


