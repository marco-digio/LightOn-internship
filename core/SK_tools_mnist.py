from keras.datasets import mnist
import numpy as np
import SK
import matplotlib.pyplot as plt
import time
import os

def load_mnist():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    dim = np.shape(x_train)[1] * np.shape(x_train)[2]
    x_train = x_train.reshape(x_train.shape[0], dim)
    x_test = x_test.reshape(x_test.shape[0], dim)
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    x_train = x_train.T / 255
    x_test = x_test.T / 255
    return x_train, x_test, y_train, y_test




def multiple_sk(x_train, x_test, y_train, y_test, dig_in, type1, m):
    print "digits = ", dig_in
    print "distance = ", type1
    print "m = ", m

    ind_in = []
    ind_tot = []
    for i in dig_in:
        ind = np.where(y_train==i)[0]
        ind_in.append(ind)
        ind_tot = np.hstack((ind_tot, ind)).astype(int)

    W = SK.freq(x_train[:,ind_tot], m)
    z = []
    for i in dig_in:
        z.append(SK.emp_sketch(W, x_train[:,ind_in[i]])[0])

    cont = 0
    tot  = 0
    
    for j in range(np.shape(y_test)[0]):
        if y_test[j] in dig_in:
            z_test = SK.emp_sketch(W, x_test[:, j:j+1])[0]
            D = []
            for i in range(np.shape(dig_in)[0]):
                D.append(SK.dist(z[i], z_test, type1))
            y_pred = dig_in[np.argmin(D)]
            if y_test[j] == y_pred:
                cont += 1
            tot +=1
    error = float(tot - cont)/cont
    print "error = ", error
    
    try:
        os.mkdir('../data')
    except OSError:
        pass

    np.savez('../data/sk_'+str(np.size(dig_in))+'_'+type1+'_'+str(m)+'.npz',
            dig_in=dig_in, type1=type1, m=m, error=error)

def anomalies_det(x_train, x_test, y_train, y_test, dig_in, dig_out, m, type1):
    dig_tot = np.hstack((dig_in, dig_out))
    ind_in = []
    for i in dig_in:
        ind_in = np.hstack((ind_in, np.where(y_train == i)[0])).astype(int)
    ind_out = []
    for i in dig_out:
        ind_out = np.hstack((ind_out, np.where(y_train == i)[0])).astype(int)
    
    W = SK.freq(x_train[:, ind_in], m)
    z = SK.emp_sketch(W, x_train[:, ind_in])[0]

    ds    = 0.
    dd    = 0.
    nsame = 0.
    ndiff = 0.

    H  = []
    Hs = []
    Hd = []

    for j in range(np.shape(y_test)[0]):
        if y_test[j] in dig_tot:
            z_test = SK.emp_sketch(W, x_test[:, j:j+1])[0]
            D = SK.dist(z, z_test, type1)
            H.append(D)
        if y_test[j] in dig_in:
            Hs.append(D)
            ds = ds + D
            nsame += 1
        elif y_test[j] in dig_out:
            Hd.append(D)
            dd = dd + D
            ndiff += 1
    
    print ds/nsame, dd/ndiff
    
    try:
        os.mkdir('../data')
    except OSError:
        pass

    np.savez('../data/sk_'+str(np.size(dig_in))+'_'+str(np.size(dig_out))+'_'+type1+'_'+str(m)+'.npz',
            dig_in=dig_in, dig_out=dig_out, m=m, type1=type1, H=H, Hd=Hd, Hs=Hs)




def plot(Hd, Hs, name):
    
    plt.figure(1)
    plt.hist(Hs, 50, alpha=0.5, label='same', color='b', normed=True)
    plt.hist(Hd, 50, alpha=0.5, label='diff', color='r', normed=True)
    plt.xlabel('distance')
    plt.ylabel('occurrence normalized')
    plt.legend(loc='best')
    plt.savefig('../plot/'+name+'.pdf')
    plt.close('all')


def run_plot(l1, l2, type1, m):
    name = 'sk_'+str(l1)+'_'+str(l2)+'_'+type1+'_'+str(m)
    data = np.load('../data/'+name+'.npz')
    Hd = data['Hd']
    Hs = data['Hs']

    plot(Hd, Hs, name)







