import numpy as np
import copy

def cross_validation(folds, X, y, adaline, seed, max_iter, rate, random=True):
    for train, test in cv_fold(folds, X, y):
        errors = adaline.fit(train[0], train[1], seed, max_iter, rate, random)
        mse_validation = validation_accuracy(adaline, test[0], test[1])
        yield errors, mse_validation

def cv_fold(k, X, y):
    partition = (X.shape[0]//k)+1
    biggers = (X.shape[0]%k)+1
    for i in (j*partition for j in xrange(1,biggers)):
        yield (np.concatenate((X[:i-partition], X[i:])), np.concatenate((y[:i-partition], y[i:]))), (X[i-partition: i], y[i-partition: i])
    partition -= 1
    for i in xrange((biggers-1)*(partition+1), X.shape[0], partition):
        yield (np.concatenate((X[:i], X[i+partition:])), np.concatenate((y[:i], y[i+partition:]))), (X[i:i+partition], y[i:i+partition])

def cross_validation_accuracy(folds, X, y, adaline, seed, max_iter, rates, random):
    cv_folds = []
    for i in rates:
        counter = 0
        for __, mse_validation in cross_validation(folds, X, y, adaline, seed, max_iter, i, random):
            counter += mse_validation
        cv_folds.append(counter/folds)
    return cv_folds

def validation_accuracy(classifier, validation, desired):
    mse = 0.
    for i in xrange(validation.shape[0]):
        diff = desired[i] - classifier.net_input(validation[i])
        mse += (diff*diff)
    return mse / validation.shape[0]

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
            line = line.strip().split()
            attrs.append(np.array(line[:-1], np.float64))
            classes.append(line[-1])
    return np.array(attrs), np.array(classes, np.float64)

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