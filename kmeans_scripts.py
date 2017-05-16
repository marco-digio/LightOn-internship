import numpy as np
import kmeans_tools as kmt

krange = np.arange(10, 100, 10) 
n = 100 
d = 10
r = 100
n_it = 10
kmt.run_k_kmeans(krange, n, d, r, n_it, rand_init=False)
kmt.run_plot('k', 'kmeans')

k = 10
nrange = np.arange(10, 100, 10) 
d = 10
r = 100
n_it = 10
kmt.run_k_kmeans(k, nrange, d, r, n_it, rand_init=False)
kmt.run_plot('k', 'kmeans')

k = 10
n = 100
drange = np.arange(10, 100, 10) 
r = 10
n_it = 10 
kmt.run_k_kmeans(k, n, drange, r, n_it, rand_init=False)
kmt.run_plot('k', 'kmeans')

k = 10
n = 100
d = 10
rrange = np.arange(10, 100, 10)
n_it = 10 
kmt.run_k_kmeans(k, n, d, rrange, n_it, rand_init=False)
kmt.run_plot('k', 'kmeans')


