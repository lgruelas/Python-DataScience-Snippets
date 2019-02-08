import aux_funcs as aux
import classes as cl
import numpy as np
import scipy

def test_layers():
    nn = cl.MLPerceptron(4, [3,4,3], 3)
    assert nn._layers == [4,3,4,3,3] and nn._C == 5

def test_net_input():
    nn = cl.MLPerceptron(4, [3,4,3], 3)
    nn.net_input(np.array([1,2,3,4]))
    assert np.array_equal(nn._activations[0], np.array([1,2,3,4]))

def test_layers_sizes():
    errors = []
    nn = cl.MLPerceptron(4, [3,4,3], 3)
    if not nn._layers == [4,3,4,3,3]:
        errors.append("error")
    if not nn._C == 5:
        errors.append("error")
    assert not errors

def test_weights_size():
    errors = []
    nn = cl.MLPerceptron(4, [3,4,3], 3)
    if not len(nn._weights) == 4:
        errors.append("error")
    for i in xrange(1,5):
        if nn._weights[i-1].shape != (nn._layers[i-1], nn._layers[i]):
            errors.append("error")
    assert not errors

def test_activations_size():
    errors = []
    desired_layers = [4,3,4,3,3]
    nn = cl.MLPerceptron(4, [3,4,3], 3)
    for i in xrange(len(desired_layers)):
        if not nn._activations[i].size == desired_layers[i]:
            errors.append("error")
    assert not errors

def test_thetas_size():
    errors = []
    desired_layers = [4,3,4,3,3]
    nn = cl.MLPerceptron(4, [3,4,3], 3)
    for i in xrange(len(desired_layers)-1):
        if not nn._theta[i].size == desired_layers[i+1]:
            errors.append("error")
    assert not errors