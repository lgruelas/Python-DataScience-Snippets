import numpy as np
import copy

def classifierOvA(dataset, classes, *args):
    '''
        INPUT: dataset - numpy ndArray with instances to clasify
                classes - dictionary with the order of given classifiers and associated items
                *args - the n number of classifiers
        RETURN: to_return - a list with the assigned classes
    '''
    for i in xrange(dataset.shape[0]):
        scores = []
        for j in args:
            scores.append(j.net_input(dataset[i], best=True))
        yield classes[max(xrange(len(scores)), key=scores.__getitem__)]

def shuffle(attrs, y, generator, in_situ=False):
    move = np.arange(y.size)
    generator.shuffle(move)
    if in_situ:
        for i in xrange(y.size):
            attrs[[i, move[i]]] = attrs[[move[i], i]]
            y[i], y[move[i]] = y[move[i]], y[i]
    else:
        dn = copy.deepcopy(attrs)
        d1 = copy.deepcopy(y)
        for i in xrange(d1.size):
            dn[[i, move[i]]] = dn[[move[i], i]]
            d1[i], d1[move[i]] = d1[move[i]], d1[i]
        return dn, d1


def loadfile(fname):
    attrs, classes = [], []
    with open(fname) as f:
        for line in f:
            line = line.strip().split(',')
            attrs.append(np.array(line[:-1], np.float64))
            classes.append(line[-1])
    return np.array(attrs), np.array(classes)

def normalize(array):
    normalized_data = copy.deepcopy(array)
    lowest = np.min(array, axis=0)
    highest = np.max(array, axis=0)
    for i in xrange(array.shape[1]):
        normalized_data[:,i] = map(lambda x: (x-lowest[i])/(highest[i]-lowest[i]), array[:,i])
    return normalized_data

def standarize(array):
    standarized_data = copy.deepcopy(array)
    mean = np.mean(array, axis=0)
    sd = np.std(array, axis=0)
    for i in xrange(array.shape[1]):
        standarized_data[:,i] = map(lambda x: (x-mean[i])/sd[i], array[:,i])
    return standarized_data