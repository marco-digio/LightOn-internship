import numpy as np
import sys
sys.path.insert(0, '../core/')
import SK_tools_mnist as sktm

x_train, x_test, y_train, y_test = sktm.load_mnist()
'''
m = 500
type = 'l1'
dig_in 	= np.asarray([0, 1])
sktm.multiple_sk(x_train, x_test, y_train, y_test, dig_in, type, m)
dig_in 	= np.asarray([0, 1, 2, 3])
sktm.multiple_sk(x_train, x_test, y_train, y_test, dig_in, type, m)
dig_in 	= np.asarray([0, 1, 2, 3, 4, 5])
sktm.multiple_sk(x_train, x_test, y_train, y_test, dig_in, type, m)
dig_in 	= np.asarray([0, 1, 2, 3, 4, 5, 6, 7])
sktm.multiple_sk(x_train, x_test, y_train, y_test, dig_in, type, m)
dig_in 	= np.asarray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
sktm.multiple_sk(x_train, x_test, y_train, y_test, dig_in, type, m)
type = 'l2'
dig_in 	= np.asarray([0, 1])
sktm.multiple_sk(x_train, x_test, y_train, y_test, dig_in, type, m)
dig_in 	= np.asarray([0, 1, 2, 3])
sktm.multiple_sk(x_train, x_test, y_train, y_test, dig_in, type, m)
dig_in 	= np.asarray([0, 1, 2, 3, 4, 5])
sktm.multiple_sk(x_train, x_test, y_train, y_test, dig_in, type, m)
dig_in 	= np.asarray([0, 1, 2, 3, 4, 5, 6, 7])
sktm.multiple_sk(x_train, x_test, y_train, y_test, dig_in, type, m)
dig_in 	= np.asarray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
sktm.multiple_sk(x_train, x_test, y_train, y_test, dig_in, type, m)
type = 'cos'
dig_in 	= np.asarray([0, 1])
sktm.multiple_sk(x_train, x_test, y_train, y_test, dig_in, type, m)
dig_in 	= np.asarray([0, 1, 2, 3])
sktm.multiple_sk(x_train, x_test, y_train, y_test, dig_in, type, m)
dig_in 	= np.asarray([0, 1, 2, 3, 4, 5])
sktm.multiple_sk(x_train, x_test, y_train, y_test, dig_in, type, m)
dig_in 	= np.asarray([0, 1, 2, 3, 4, 5, 6, 7])
sktm.multiple_sk(x_train, x_test, y_train, y_test, dig_in, type, m)
dig_in 	= np.asarray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
sktm.multiple_sk(x_train, x_test, y_train, y_test, dig_in, type, m)
'''


type1 = 'l1'
m = 100
dig_in 	= np.asarray([0])
dig_out	= np.asarray([1, 2, 3, 4, 5, 6, 7, 8, 9])
sktm.anomalies_det(x_train, x_test, y_train, y_test, dig_in, dig_out, m, type1)
sktm.run_plot(np.size(dig_in), np.size(dig_out), type1, m)
type1 = 'l2'
m = 100
dig_in 	= np.asarray([0])
dig_out	= np.asarray([1, 2, 3, 4, 5, 6, 7, 8, 9])
sktm.anomalies_det(x_train, x_test, y_train, y_test, dig_in, dig_out, m, type1)
sktm.run_plot(np.size(dig_in), np.size(dig_out), type1, m)
type1 = 'cos'
m = 100
dig_in 	= np.asarray([0])
dig_out	= np.asarray([1, 2, 3, 4, 5, 6, 7, 8, 9])
sktm.anomalies_det(x_train, x_test, y_train, y_test, dig_in, dig_out, m, type1)
sktm.run_plot(np.size(dig_in), np.size(dig_out), type1, m)
type1 = 'l1'
m = 1000
dig_in 	= np.asarray([0])
dig_out	= np.asarray([1, 2, 3, 4, 5, 6, 7, 8, 9])
sktm.anomalies_det(x_train, x_test, y_train, y_test, dig_in, dig_out, m, type1)
sktm.run_plot(np.size(dig_in), np.size(dig_out), type1, m)
type1 = 'l2'
m = 1000
dig_in 	= np.asarray([0])
dig_out	= np.asarray([1, 2, 3, 4, 5, 6, 7, 8, 9])
sktm.anomalies_det(x_train, x_test, y_train, y_test, dig_in, dig_out, m, type1)
sktm.run_plot(np.size(dig_in), np.size(dig_out), type1, m)
type1 = 'cos'
m = 1000
dig_in 	= np.asarray([0])
dig_out	= np.asarray([1, 2, 3, 4, 5, 6, 7, 8, 9])
sktm.anomalies_det(x_train, x_test, y_train, y_test, dig_in, dig_out, m, type1)
sktm.run_plot(np.size(dig_in), np.size(dig_out), type1, m)

type1 = 'l2'
m = 1000
dig_in 	= np.asarray([0])
dig_out	= np.asarray([1])
sktm.anomalies_det(x_train, x_test, y_train, y_test, dig_in, dig_out, m, type1)
sktm.run_plot(np.size(dig_in), np.size(dig_out), type1, m)
type1 = 'l1'
m = 1000
dig_in 	= np.asarray([0, 2])
dig_out	= np.asarray([1])
sktm.anomalies_det(x_train, x_test, y_train, y_test, dig_in, dig_out, m, type1)
sktm.run_plot(np.size(dig_in), np.size(dig_out), type1, m)
type1 = 'l2'
m = 1000
dig_in 	= np.asarray([0, 2])
dig_out	= np.asarray([1])
sktm.anomalies_det(x_train, x_test, y_train, y_test, dig_in, dig_out, m, type1)
sktm.run_plot(np.size(dig_in), np.size(dig_out), type1, m)
type1 = 'cos'
m = 1000
dig_in 	= np.asarray([0, 2])
dig_out	= np.asarray([1])
sktm.anomalies_det(x_train, x_test, y_train, y_test, dig_in, dig_out, m, type1)
sktm.run_plot(np.size(dig_in), np.size(dig_out), type1, m)








