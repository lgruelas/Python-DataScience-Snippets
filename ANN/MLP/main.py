#! /usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import aux_funcs as aux
import numpy as np
import classes as g_c
    
if __name__ == '__main__':
    my_seed = 42 #SEED
    max_iter = 300 #Max iterations for training
    learning_rate = 0.02 #learning rate (alfa)
    
    print "Start dummy test with XORG problem..."

    nn = g_c.MLPerceptron(2, [2], 1)

    print "MLPerceptron created with layers ", nn._layers

    classes = np.array([0,0,1,1])
    data = np.array([np.array([0, 0]), np.array([1, 1]), np.array([1, 0]), np.array([0, 1])])

    print "Classes and data ready"

    print "Starting training by hand..."
    test = range(4)
    for i in xrange(5000):
        to_train = np.random.choice(test)
        nn.train(classes[to_train], data[to_train], learning_rate)
    print "trained"

    print "Results: "
    for i in data:
        print i
        print nn.forward(i)

    print "Starting training for IRIS Data..."
    nn = g_c.MLPerceptron(4, [3,4,3], 3)

    print "MLPerceptron created with layers ", nn._layers

    # Loading the data
    a, b = aux.loadfile2('iris.data')

    print "Data loaded from file"

    # Standarizing the data (mean = 0 and std = 1)
    dataset_normalized = aux.normalize(a)
    print "Data normalized"

    classes = []
    other = []
    for i in b:
        if i == "Iris-setosa":
            classes.append(np.array([1,0,0]))
            other.append(0)
        elif i == "Iris-versicolor":
            classes.append(np.array([0,1,0]))
            other.append(1)
        elif i == "Iris-virginica":
            classes.append(np.array([0,0,1]))
            other.append(2)
        else:
            raise ValueError("Class not in the list.")   

    print "OHE classes vectors created"

    print "Training..."
    etrain, etest = nn.fit(dataset_normalized, np.array(classes), max_iter, learning_rate)
    print "Tranied"
    print "plotting..."

    x_label = np.arange(max_iter)
    plt.plot(x_label, etrain, label="Training")
    plt.plot(x_label, etest, label="Validation")
    plt.xlabel(u'Época')
    plt.ylabel(u'Training MSE')
    plt.legend(loc = 0)
    plt.show()

    error = 0
    for i in xrange(len(dataset_normalized)):
        output = nn.predict(dataset_normalized[i])
        if output == other[i]:
            error+=1
        
    print "porcentaje de correctas: ", (error/150.) * 100, "%"
    

    print "Starting Housing data test."

    nn = g_c.MLPerceptron(13, [6,4,3], 1)

    print "MLPerceptron created with layers ", nn._layers

    print "Loading data..."
    a, b = aux.loadfile('housing.data')
    # Preprocessing
    print "Normalizing data..."
    dataset = aux.normalize(a)
    desired = aux.normalize(b)

    desired = map(lambda x: np.array([x]), desired)
    
    print "Training..."
    etrain, etest = nn.fit(dataset, np.array(desired), max_iter, learning_rate)
    print "Plotting..."
    x_label = np.arange(max_iter)
    plt.plot(x_label, etrain, label="Training")
    plt.plot(x_label, etest, label="Validation")
    plt.xlabel(u'Época')
    plt.ylabel(u'Training MSE')
    plt.legend(loc = 0)
    plt.show()

    print "Sorry :("