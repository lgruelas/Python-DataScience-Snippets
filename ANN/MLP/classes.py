#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import aux_funcs as aux

class MLPerceptron:
    def __init__(self, input_variables, hidden_layers, output_variables, seed=42):
        '''
            INPUT:
                hidden_layers - list, his len is the number of hidden layers in the network and his value is the number of neurons for the i layer.
                output_variables - int, number of variables in the output layer.
                input_variables - int, number of neurons in the entry layer.
                seed - seed for the random number generator, default 42.
            CLASS ATTRIBUTES: 
                _weights - list with a weights matrix for each hidden layer + 1.
                _theta - list containing the thresholds vector for each layer.
                _activations - list containing the activation values for each neuron of each layer.
                rand_generator - random generator.
            NOTES: 
                all class methods are 0 index based.
        '''
        #Random initialization of the weights and threshods
        self.rand_generator = np.random.RandomState(seed)
        self._weights = [np.matrix([self.rand_generator.uniform(-0.01, 0.01, hidden_layers[0]) for i in xrange(input_variables)])] + [np.matrix([self.rand_generator.uniform(-0.01, 0.01, hidden_layers[i]) for j in xrange(hidden_layers[i-1])]) for i in xrange(1, len(hidden_layers))] + [np.matrix([self.rand_generator.uniform(-0.01, 0.01, output_variables) for i in xrange(hidden_layers[-1])])]
        self._theta = [self.rand_generator.uniform(-0.01, 0.01, i) for i in hidden_layers] + [self.rand_generator.uniform(-0.01, 0.01, output_variables)]
        #self._weights = [np.matrix([[0.02,0.23],[0.005,0.178]]), np.matrix([[0.012], [0.810]])]
        #self._theta = [np.array([0.25, 0.123]), np.array([0.08])]

        #Activation values start at 0
        self._activations = [np.zeros(input_variables)] + [np.zeros(i) for i in hidden_layers] + [np.zeros(output_variables)]
        self.deltas =  [np.zeros(i) for i in hidden_layers] + [np.zeros(output_variables)]
        # Usefull information
        self._layers = [input_variables] + hidden_layers + [output_variables]
        self._C = len(hidden_layers) + 2 # C, total number of layers in the network.

    def __str__(self):
        pass

    def fit(self, X, y, max_iter, alpha, proportion = 0.7):
        '''
            Learning process for the Multi layer perceptron as described in "material-de-clase.-tema-3.pdf"
        '''
        training = int(np.floor(y.shape[0]*proportion))
        errors_training = []
        errors_test = []
        errors_training_global = []
        errors_test_global = []
        for counter in xrange(max_iter):
            attrs, d = aux.shuffle(X, y, self.rand_generator)
            for i in xrange(training):
                net_output = self.train(d[i], attrs[i], alpha)
                errors_training.append(self.cost(net_output, d[i]))
            for i in xrange(training, y.shape[0]):
                net_output = self.forward(attrs[i])
                errors_test.append(self.cost(net_output, d[i]))
            errors_training_global.append(np.mean(errors_training))
            errors_test_global.append(np.mean(errors_test))
        return errors_training_global, errors_test_global

    def backpropagation(self, desired, alpha):
        '''
            Modify weights with backpropagation method.
            INPUT:
                desired: np.array(not matrix or list) with the desired output vector.
                alpha: float or np.float64 with the learning rate.  
            OUTPUT:
                void
        '''
        # setting deltas from last layer.
        # delta_C = (S - Y)·Y·(1 - Y)
        self.deltas[-1] = (np.array(desired) - self._activations[-1])*self._activations[-1]*(np.ones(self._layers[-1])-self._activations[-1])
        for i in xrange(self._C-2, 0, -1):
            self.deltas[i-1] = self._activations[i]*(np.ones(self._layers[i])-self._activations[i]) * (self._weights[i] * self.deltas[i].reshape(self._layers[i+1], 1)).A1

        # thetas_C(n) = thetas_C(n-1) + alpha * delta_C
        self._theta[-1] = self._theta[-1] + (alpha * self.deltas[-1])
        # weights_C(n) = weights_C(n-1) + alpha * a_C-1 * delta_C
        self._weights[-1] = self._weights[-1] + (alpha * (self._activations[-2].reshape(self._layers[-2], 1) * self.deltas[-1]))

        # for the rest of layers.
        for i in xrange(self._C-3, -1, -1):
            self._theta[i] = self._theta[i] + (alpha * self.deltas[i])
            self._weights[i] = self._weights[i] + (alpha * (self._activations[i].reshape(self._layers[i], 1) * self.deltas[i]))

    def predict(self, ind):
        '''
            In classification problems, this method is used to assign a class to the output value.
            INPUT:
                ind: element to be classified
            OUTPUT:
                class: assigned class
        '''
        output = self.forward(ind)
        if self._layers[-1] > 1:
            return max(xrange(self._layers[-1]), key=output.__getitem__) #return the index of the output variable with more aptitude.
        return 1 if output[0,0] >= 0.5 else 0

    def train(self, expected, ind, alpha):
        to_return = self.forward(ind)
        self.backpropagation(expected, alpha)
        return to_return

    def forward(self, data):
        '''
            INPUT: 
                data: list with the variables to predict.
            OUTPUT:
                np.matrix (1,y) with the output vector from the network.
        '''
        self.net_input(data)
        for i in xrange(1, self._C):
            self._activations[i] = self.activation((self._activations[i-1]*self._weights[i-1]).A1+self._theta[i-1])
        return self._activations[-1]

    def net_input(self, ind):
        '''
            Sets the activations values for the first layer.
            INPUT: 
                ind - list with the attributes of an individual.
            RETURN:
                void
        '''
        if ind.shape[0] != self._layers[0]:
            raise ValueError("Data atributes are inconsistent.")
        self._activations[0] = ind

    def activation(self, activation_value):
        '''
            INPUT:  value to be activated with the activation function.
            RETURN: value after being passed with the activation function.
        '''
        return aux.sigmoid(activation_value)

    def cost(self, output, y_test):
        '''
        Evaluate the performance, returns the error op a pattern.
        INPUT:
            output: previous net output
            y_test: array with the expected values.
        OUTPUT:
            number representing the e(n), error.
        '''
        if not hasattr(y_test, '__iter__'):
            raise ValueError("Test class must be a vector, not int.")
        desired_classes = np.matrix(y_test)
        return np.square(desired_classes - output).sum()/self._layers[-1]