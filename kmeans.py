# greedy algorithm to compute the misclassification
def misclassification(predicted, real):
	n = max(max(predicted), max(real))
	l = np.shape(predicted)[0]
	
	# create the table 
	table = -np.ones((n, n))
	for j in np.arange(l):
		table[predicted[j]][real[j]] +=1.
		
	# search the indeces 
	index = np.zeros((n, 1))
	for i in np.arange(n):
		max1 = np.max(table)
		id1 = 
		id2 = np.argmax(max1)
		index[id1[id2]] = id2
		for k in np.arange(n):
			table[id1[id2]][k] = 0
			table[k][id2] = 0
	
	# compute the misclassification
	miss = 0.
	for j in np.arange(l):
		if predicted[j] != index[real[j]]:
			miss += 1.
	return miss /= l
	
		
# objective function
def objective_function(X, predicted, k):
	N = np.shape(X)[0]
	l = np.shape(predicted)[0]
	# compute z
	z = np.zeros((n, 1))
	for i in np.arange(N):
		z[predicted[i]] += 1
	
	# compute T
	T = np.zeros((N, k))
	for j in np.arange(l):
		T[j][predicted[j]] = 1./np.sqrt(z[predicted[j]])
	
	# return F
	return (LA.norm(np.dot((np.eye(N) - np.dot(T, T.T), X))) / LA.norm(X, 'fro'))**2
			

# Randomized k-means
def rkmeans(X, k, r, init=None):
	t_s = time.clock()
	Xr = np.dot(X, np.random.rand((np.shape(X)[1], r)))
	t_RP = time.clock() - t_s
	if start == None:
		predicted = kmeans(Xr, k)
	else:
		predicted = kmeans(Xr, k, init)
	t = time.clock() - t_s
	return predicted, t_RP
			

# Error, objective function and time for k-means
def eFt_kmeans(X, k, real, r=0, init=None):
	t_s = time.clock()
	if r==0:
		if init == None:
			predicted, t_RP = rkmeans(X, k, r) #FIXME
		else:
			predicted, t_RP = rkmeans(X, k, r, data[init]) #FIXME
	else:
		if init == None:
			predicted, t_RP = rkmeans(X, k, r) #FIXME
		else:
			predicted, t_RP = rkmeans(X, k, r, data[init]) #FIXME
	t = time.clock() - t_s
	
	error = misclassification(predicted, real)
	F = objective_function(X, predicted, k)
	return error, F, t, t_RP, predicted
	
# Average of error and time for (R)k-means
def av_eTt_kmeans(X, k, real, n_it, r=0, init=None):

	er = np.zeros(n_it)
	F = np.zeros(n_it)
	t_tot = np.zeros(n_it)
	t_rp = np.zeros(n_it)

	for it in range(n_it):
		#print 'it = ', it
		er[it], F[it], t_tot[it], t_rp[it] = eFt_kmeans(X, k, real, r, init)
	
	return np.mean(er), np.mean(F), np.mean(t_tot), np.mean(t_rp)