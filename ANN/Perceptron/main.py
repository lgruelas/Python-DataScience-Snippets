#! /usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import aux_funcs as aux
from perceptron import Perceptron

if __name__ == '__main__':
    my_seed = 42 #SEED
    max_iter = 30 #Max iterations for training
    learning_rate = 0.02 #learning rate (alpha)

    # Creating the perceptrons
    perceptron_setosa = Perceptron()
    perceptron_versicolor = Perceptron()
    perceptron_virginica = Perceptron()

    # Loading the data
    a, b = aux.loadfile('iris.data')

    # Standarizing the data (mean = 0 and std = 1)
    dataset_standarized = aux.standarize(a)

    # Creating the arrays for OvA classification
    setosa = np.array([1 if i == "Iris-setosa" else -1 for i in b], np.int8)
    versicolor = np.array([1 if i == "Iris-versicolor" else -1 for i in b], np.int8)
    virginica = np.array([1 if i == "Iris-virginica" else -1 for i in b], np.int8)
    
    # Training the perceptrons
    graph_setosa = perceptron_setosa.fit(dataset_standarized, setosa, my_seed, max_iter, learning_rate)
    graph_versicolor = perceptron_versicolor.fit(dataset_standarized, versicolor, my_seed, max_iter, learning_rate)
    graph_virginica = perceptron_virginica.fit(dataset_standarized, virginica, my_seed, max_iter, learning_rate)

    # Plot with the error changes
    plt.plot(np.linspace(1, max_iter, max_iter), graph_setosa, marker='o', label='Iris-setosa')
    plt.plot(np.linspace(1, max_iter, max_iter), graph_versicolor, marker='o', label='Iris-versicolor')
    plt.plot(np.linspace(1, max_iter, max_iter), graph_virginica, marker='o', label='Iris-virginica')
    plt.xlabel(u'Época')
    plt.ylabel(u'Porcentaje de acierto')
    plt.legend(loc=0)
    plt.show()

    # OvA Classifier
    print "Starting OvA\n"
    classes = {0: "Iris-setosa", 1:"Iris-versicolor", 2:"Iris-virginica"}
    correct = 0
    for i, j in enumerate(aux.classifierOvA(dataset_standarized, classes, perceptron_setosa, perceptron_versicolor, perceptron_virginica)):
        if j == b[i]:
            correct+=1
    print "Classifiers success rate: %.2f%%" % (100. * correct / b.size)
