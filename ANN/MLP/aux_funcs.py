import numpy as np
import copy

def sigmoid(activation_value):
    return np.float64(1) / (1 + np.exp( -activation_value ))

def shuffle(attrs, y, generator, in_situ=False):
    '''
        INPUT:
            attrs: ndarray.
            y: array.
    '''
    move = np.arange(y.shape[0])
    generator.shuffle(move)
    if in_situ:
        for i in xrange(y.shape[0]):
            attrs[[i, move[i]]] = attrs[[move[i], i]]
            y[i], y[move[i]] = y[move[i]], y[i]
    else:
        dn = copy.deepcopy(attrs)
        d1 = copy.deepcopy(y)
        for i in xrange(d1.shape[0]):
            dn[[i, move[i]]] = dn[[move[i], i]]
            d1[i], d1[move[i]] = d1[move[i]], d1[i]
        return dn, d1


def loadfile(fname):
    attrs, classes = [], []
    with open(fname) as f:
        for line in f:
            line = line.strip().split()
            attrs.append(np.array(line[:-1], np.float64))
            classes.append(line[-1])
    return np.array(attrs), np.array(classes, np.float64)

def loadfile2(fname):
    attrs, classes = [], []
    with open(fname) as f:
        for line in f:
            line = line.strip().split(',')
            attrs.append(np.array(line[:-1], np.float64))
            classes.append(line[-1])
    return np.array(attrs), np.array(classes)

def normalize(array):
    if len(array.shape) == 1:
        lowest = np.min(array)
        highest = np.max(array)
        return np.array(map(lambda x: (x-lowest)/(highest-lowest), array))
    elif len(array.shape) == 2:
        normalized_data = copy.deepcopy(array)
        lowest = np.min(array, axis=0)
        highest = np.max(array, axis=0)
        for i in xrange(array.shape[1]):
            normalized_data[:,i] = map(lambda x: (x-lowest[i])/(highest[i]-lowest[i]), array[:,i])
        return normalized_data

def standarize(array):
    if len(array.shape) == 1:
        mean = np.mean(array)
        sd = np.std(array)
        return np.array(map(lambda x: (x-mean)/sd, array), np.float64)
    elif len(array.shape) == 2:
        standarized_data = copy.deepcopy(array)
        mean = np.mean(array, axis=0)
        sd = np.std(array, axis=0)
        for i in xrange(array.shape[1]):
            standarized_data[:,i] = map(lambda x: (x-mean[i])/sd[i], array[:,i])
        return standarized_data