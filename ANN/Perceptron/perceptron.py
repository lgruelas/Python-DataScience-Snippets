import numpy as np
import aux_funcs as aux
import copy

class Perceptron:
    def __init__(self):
        '''
            CLASS ATTRIBUTES: 
                weights - np.array with Ws of the network.
                theta - threshold
                highest_score - best validation score
                best_weights - np.array with Ws that get the highest score
                best_theta - int with theta that producted the highest score
        '''
        self.weights = np.array([])
        self.theta = 0
        self.highest_score = 0
        self.best_weights = np.array([])
        self.best_theta = 0

    def __str__(self):
        '''
            RETURN: a human readable representation of the perceptron: weights and umbral.
                this method is called with "print perceptron"
        '''
        return "weights: [" + " ".join(map(str, self.weights)) + "] Umbral: %.2f" % self.theta

    def fit(self, X, y, seed, max_iter, alfa, proportion = 0.7):
        '''
            Learning process for the perceptron
        '''
        rand_generator = np.random.RandomState(seed)
        self.weights = rand_generator.uniform(-0.1, 0.1, X[0].shape[0])
        self.theta = rand_generator.uniform(-0.1, 0.1)
        training = int(np.floor(X.shape[0]*proportion))

        for_graphing = [] # this is only used for graphing

        for counter in xrange(max_iter):
            attrs, d = aux.shuffle(X, y, rand_generator)
            #TRAINING
            for i in xrange(training):
                output = self.predict(attrs[i])
                if output != d[i]:
                    self.theta += (d[i] * alfa)
                    self.weights += (attrs[i] * (d[i] * alfa))
            iter_score = self.score(attrs[:training], d[:training])

            for_graphing.append(iter_score)

            #VALIDATION
            validation_score = self.score(attrs[training:], d[training:])

            if (counter+1) % 10 == 0:
                print "Iteration: %i score: %.2f%% validation: %.2f%%" % (counter+1, iter_score, validation_score)

            if validation_score > self.highest_score:
                self.highest_score = validation_score
                self.best_theta = self.theta
                self.best_weights = copy.deepcopy(self.weights)
                # The follow if is commented only for graphing
                #if validation_score == 100:
                #    print "Iteration: %i score: %.2f%% validation: %.2f%%" % (counter+1, iter_score, validation_score)
                #    break
        print ""
        return for_graphing
    
    def predict(self, ind, best=False):
        '''
            INPUT: ind - numpy array with the attributes of an individual
                    best - when True we use the best weights found until know to get the response
            RETURN: 1 if the activation function > 0, -1 otherwise
        '''
        return 1 if self.net_input(ind, best) > 0 else -1
        
    
    def net_input(self, ind, best):
        '''
            INPUT: ind - numpy array with the attributes of an individual
                    best - when True we use the best weights found until know to get the response
            RETURN: dot product between weights of the net and the attributes of the individual plus the umbral theta
        '''
        if best:
            return ind.dot(self.best_weights) + self.best_theta
        return ind.dot(self.weights) + self.theta

    def score(self, X, y, best=False):
        '''
            INPUT: X - Entire dataset of attributes that we want to test.
                    y - Entire set of classes for each X i.e. X[i] corresponds to y[i]
                best - when True we use the best weights found until know to get the response
            RETURN: A float representing the percentage of success of the perceptron.
        '''
        total = X.shape[0]
        wrong_classifieds = 0
        for i, j in ((self.predict(X[i], best), y[i]) for i in xrange(total)):
            if i != j:
                wrong_classifieds += 1
        return 100. * (total - wrong_classifieds) / total