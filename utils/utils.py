import numpy as np

def load_data():
    data = np.loadtxt("/Users/karanramdas/Documents/01-2026/coursera_supervised_machine_learning/utils/data/ex1data1.txt", delimiter=',')
    X = data[:,0]
    y = data[:,1]
    return X, y

def load_data_multi():
    data = np.loadtxt("/Users/karanramdas/Documents/01-2026/coursera_supervised_machine_learning/utils/data/ex1data2.txt", delimiter=',')
    X = data[:,:2]
    y = data[:,2]
    return X, y
