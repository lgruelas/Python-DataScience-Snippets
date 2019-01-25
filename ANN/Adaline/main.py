#! /usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import copy
import matplotlib.pyplot as plt
import aux_funcs as aux

class Adaline:
    def __init__(self):
        '''
            CLASS ATTRIBUTES: weights - np.array with Ws of the network.
            theta - threshold 
        '''
        self.weights = np.array([])
        self.theta = 0

    def __str__(self):
        '''
            RETURN: a human readable representation of the adaline: weights and umbral.
                this method is called with "print adaline"
        '''
        return "weights: [" + " ".join(map(str, self.weights)) + "] Umbral: %.2f" % self.theta

    def fit(self, X, y, seed, max_iter, alfa, random=True, print_mse=True):
        '''
            Learning process for the Adaline."
        '''
        rand_generator = np.random.RandomState(seed)
        self.theta = rand_generator.uniform(-0.01, 0.01)
        self.weights = rand_generator.uniform(-0.01, 0.01, X[0].shape[0])
        mse_list = []
        for _iter in xrange(max_iter):
            mse = 0.
            if random:
                attrs, d = aux.shuffle(X, y, rand_generator)
            else:
                attrs, d = X, y
            for i in xrange(attrs.shape[0]):
                diff = (d[i] - self.net_input(attrs[i]))
                self.theta += (diff * alfa)
                self.weights += (attrs[i] * diff * alfa)
                mse += (diff*diff) # faster that pow, math.pow, np.power and diff**2 in my tests
                
            if print_mse:
                if max_iter < 10 or _iter % 100 == 0 or _iter==max_iter-1:
                    print "Iteration: %i, MSE: %.4f" % (_iter, mse/attrs.shape[0])
            mse_list.append(mse/attrs.shape[0])
        print "######################################################################################"
        return mse_list

    def net_input(self, ind):
        '''
            INPUT: ind - numpy array with the attributes of an individual
                    best - when True we use the best weights found until know to get the response
            RETURN: dot product between weights of the net and the attributes of the individual plus the umbral theta
        '''
        return ind.dot(self.weights) + self.theta

    activation = net_input # activation function (identity)
    predict = net_input
    
if __name__ == '__main__':
    my_seed = 42 #SEED
    max_iter = 1000 #Max iterations for training
    learning_rates = [0.1,0.01,0.001,0.0001] #learning rates (alfa)
    

    # Loading the data
    a, b = aux.loadfile('housing.data')
    # Preprocessing
    dataset = aux.normalize(a)
    desired = aux.normalize(b)

    adaline = Adaline()

    #First Graph
    folds = 5
    mse_validations_folds = []
    print "Traning adaline using cross validation %i-folds..." % folds 
    for i, errors_validations in enumerate(aux.cross_validation(folds, dataset, desired, adaline, my_seed, max_iter, 0.001)):
        plt.plot(np.linspace(1, len(errors_validations[0]), len(errors_validations[0])), errors_validations[0], label="fold %i" % (i+1))
        mse_validations_folds.append(errors_validations[1])
    plt.xlabel(u'Época')
    plt.ylabel(u'Training MSE')
    plt.legend(loc = 0)
    print mse_validations_folds
    print "%i-folds CV = %.3f" % (folds, np.mean(mse_validations_folds))
    print "Plotting..."
    plt.show()

    #Second Graph
    print "Training adaline with full dataset in different learning rates..."
    for i in learning_rates:
        print "alpha = %f" % i
        mse_rate = adaline.fit(dataset, desired, my_seed, max_iter, i)
        plt.plot(np.linspace(1, max_iter, max_iter), mse_rate, label="rate = %s" % str(i)) 
    plt.xlabel(u'Época')
    plt.ylabel(u'MSE')
    plt.legend(loc = 0)
    print "Plotting..."
    plt.show()