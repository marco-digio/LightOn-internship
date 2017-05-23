import numpy as np
import matplotlib.pyplot as plt



# draw mu and sigma for a mixture of gaussians (equal weights)
def gmm_par(dimension, n_gaussian, show_img = False):
	mu = np.random.randn(dimension, n_gaussian) * n_gaussian ** (1.0 / dimension) #* 2
	sigma = np.sqrt(np.random.rand(1, n_gaussian) * 1.5 + 0.25)
	
	# plot
	if (show_img == True):
		plt.figure(1)
		ax = plt.axes(aspect = 'equal')
		plt.scatter(mu[0, :], mu[1, :], c = 'k', s = 10)
	
		for i in range(n_gaussian):
			circle = plt.Circle((mu[0][i], mu[1][i]), sigma[0][i], fill = False)
			ax.add_artist(circle)
		plt.show()
		
	return mu, sigma
	

# draw points from a mixture of gaussians
def synthetic_mixture_gaussians(mu, sigma, n_points, show_img = False):
	dimension = np.shape(mu)[0]
	n_gaussian = np.shape(mu)[1]
	data = np.zeros((dimension, n_gaussian * n_points))
	label = np.zeros((n_gaussian * n_points))

	for i in range(n_gaussian):
		data[:, i * n_points:(i+1) * n_points] = np.random.randn(dimension, n_points) * sigma[:, i] + mu[:, i:i+1]
		label[i * n_points:(i+1) * n_points] = i

	# plot
	if (show_img == True):
		plt.figure(1)
		plt.scatter(data[0, :], data[1, :], c = label, s = 10)
		plt.show()
		
	return data, label 
# change the size of the sketch
def change_m(X, X_s, X_d, mrange, type):
	n_s = np.shape(X_s)[1]
	n_d = np.shape(X_d)[1]
	ds = np.zeros((np.size(mrange), 1))
	dd = np.zeros((np.size(mrange), 1))
	d_same = np.zeros((n_s, 1))
	d_diff = np.zeros((n_d, 1))
	
	for it in range(np.size(mrange)):
		m = mrange[it]
		print m
		#t_start = time.clock()
		W = freq(X, m)
		z = emp_sketch(W, X)
		#print time.clock() - t_start
		for i in range(n_s):
			d_same[i] = dist(z, emp_sketch(W, X_s[:, i:i+1]), type)
		for i in range(n_d):
			d_diff[i] = dist(z, emp_sketch(W, X_d[:, i:i+1]), type)

		ds[it] = np.mean(d_same)
		dd[it] = np.mean(d_diff)
		
	plt.figure(2)
	plt.plot(mrange, ds, 'b', label = 'same distribution', linewidth = 2)
	plt.plot(mrange, dd, 'g', label = 'different distribution', linewidth = 2)
	plt.ylabel('distance', fontsize = 15)
	plt.xlabel('m', fontsize = 15)
	plt.legend(loc = 'best', fontsize = 15)
	plt.show()
	
	
# exemple function
def exemple():
	# data parameters
	dim = 70
	n_gaussian = 10
	N = 600
	n_try = 100
	
	# data creation
	#X 	= np.random.normal(0, 1, (dim, N))
	#X_s = np.random.normal(0, 1, (dim, n_try))
	mu, sigma = gmm.gmm_par(dim, n_gaussian)
	X = gmm.synthetic_mixture_gaussians(mu, sigma, N)[0]
	X_s = gmm.synthetic_mixture_gaussians(mu, sigma, n_try)[0]
	X_d = np.random.normal(6, 1, (dim, n_try))
	
	
	mrange = np.arange(1, 100, 6)
	type = 'l2'
	change_m(X, X_s, X_d, mrange, type)
	
	



