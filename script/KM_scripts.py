import numpy as np
import sys
sys.path.insert(0, '../core/')
import KM_tools as kmt


rand_init=False

krange = np.arange(2, 12, 1) 
n = 100 
d = 10
r = 100
n_it = 3
kmt.k_kmeans(krange, n, d, r=0, n_it=n_it, rand_init=rand_init)
kmt.k_kmeans(krange, n, d, r,   n_it=n_it, rand_init=rand_init)

k = 5
nrange = np.arange(10, 400, 20) 
d = 10
r = 100
n_it = 3
kmt.n_kmeans(k, nrange, d, r=0, n_it=n_it, rand_init=rand_init)
kmt.n_kmeans(k, nrange, d, r,   n_it=n_it, rand_init=rand_init)

k = 5
n = 100
drange = np.arange(10, 100, 10) 
r = 100
n_it = 3 
kmt.d_kmeans(k, n, drange, r=0, n_it=n_it, rand_init=rand_init)
kmt.d_kmeans(k, n, drange, r,   n_it=n_it, rand_init=rand_init)

k = 5
n = 100
d = 10
rrange = np.arange(10, 800, 50)
n_it = 3 
kmt.r_kmeans(k, n, d, rrange, n_it=n_it, rand_init=rand_init, random_proj=False)
kmt.r_kmeans(k, n, d, rrange, n_it=n_it, rand_init=rand_init)



kmt.run_plot('k', 'kmeans')
kmt.run_plot('n', 'kmeans')
kmt.run_plot('d', 'kmeans')
kmt.run_plot('r', 'kmeans')

