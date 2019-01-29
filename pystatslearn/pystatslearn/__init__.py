import numpy as np

def sigmoid(activation_value):
    return np.float64(1) / (1 + np.exp( -activation_value ))