import numpy as np
import RNPCA_tools as RNPCAt

nrange = np.arange(100, 4000, 100)
d = 10
m = 1000
n_it = 1
RNPCAt.run_n(nrange, d, m, n_it)
RNPCAt.run_plot('n')

n = 1000
drange = np.arange(1, 30, 2)
m = 1000
n_it = 1
RNPCAt.run_d(n, drange, m, n_it)
RNPCAt.run_plot('d')

n = 1000
d = 10
mrange = np.arange(100, 4000, 100)
n_it = 1
RNPCAt.run_m(n, d, mrange, n_it)
RNPCAt.run_plot('m')

