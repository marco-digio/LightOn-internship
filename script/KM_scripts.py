import numpy as np
import kmeans_tools as kmt

krange = np.arange(10, 100, 10) 
n = 100 
d = 10
r = 100
n_it = 10
#kmt.run_k_kmeans(krange, n, d, r, n_it, rand_init=False)
#kmt.k_kmeans(krange, n, d, r=0, n_it=n_it, rand_init=False)
#kmt.k_kmeans(krange, n, d, r,   n_it=n_it, rand_init=False)
#kmt.run_plot('k', 'kmeans')

k = 10
nrange = np.arange(10, 1000, 50) 
d = 1000
r = 100
n_it = 10
#kmt.run_n_kmeans(k, nrange, d, r, n_it, rand_init=False)
#kmt.n_kmeans(k, nrange, d, r=0, n_it=n_it, rand_init=False)
#kmt.n_kmeans(k, nrange, d, r,   n_it=n_it, rand_init=False)
#kmt.run_plot('n', 'kmeans')

k = 10
n = 100
drange = np.arange(10, 100, 10) 
r = 10
n_it = 10 
#kmt.run_d_kmeans(k, n, drange, r, n_it, rand_init=False)
#kmt.d_kmeans(k, n, drange, r=0, n_it=n_it, rand_init=False)
#kmt.d_kmeans(k, n, drange, r,   n_it=n_it, rand_init=False)
#kmt.run_plot('d', 'kmeans')

k = 10
n = 500
d = 2
rrange = np.arange(10, 800, 50)
n_it = 10 
#kmt.run_r_kmeans(k, n, d, rrange, n_it, rand_init=False)
#kmt.r_kmeans(k, n, d, rrange, n_it=n_it, rand_init=False, random_proj=False)
kmt.r_kmeans(k, n, d, rrange, n_it=n_it, rand_init=False)
#kmt.run_plot('r', 'kmeans')


