import numpy as np
import sys
sys.path.insert(0, '../core/')
import SK_tools as skt


typed = 'l2'
N = 500
n = 100

drange = np.arange(2, 20, 2)
m = 10
n_it = 3
skt.d_sk(drange, N, n, m, typed, n_it) 


d = 5
mrange = np.arange(1, 100, 6)
n_it = 3
skt.m_sk(d, N, n, mrange, typed, n_it)


skt.run_plot('d', 'sk')
skt.run_plot('m', 'sk')

