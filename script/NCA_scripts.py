import numpy as np
import sys
sys.path.insert(0, '../core/')
import NPCA_tools as npcat


nrange  = np.asarray([600, 800, 1000, 1200, 1600, 2000, 3000, 4000]) 
d 		= 2000
m       = 500
n_it    = 3
npcat.run_n(nrange, d, m, n_it)


n       = 2000
drange  = np.asarray([600, 800, 1000, 1200, 1600, 2000, 3000, 4000]) 
m       = 500
n_it    = 3
npcat.run_d(n, drange, m, n_it)


n       = 2000
d       = 2000
mrange  = np.asarray([20, 50, 100, 200, 500, 700, 1000, 1400, 1800]) 
n_it    = 3
npcat.run_m(n, d, mrange, n_it)


npcat.run_plot('n')
npcat.run_plot('d')
npcat.run_plot('m')

