import numpy as np
import sys
sys.path.insert(0, '../core/')
import NPCA_tools as npcat


nrange = np.arange(10, 100, 10)
d = 10
m = 100
n_it = 3
npcat.run_n(nrange, d, m, n_it)


n = 50
drange = np.arange(1, 20, 2)
m = 100
n_it = 3
npcat.run_d(n, drange, m, n_it)


n = 50
d = 10
mrange = np.arange(10, 100, 10)
n_it = 3
npcat.run_m(n, d, mrange, n_it)


npcat.run_plot('n')
npcat.run_plot('d')
npcat.run_plot('m')

