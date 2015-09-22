import numpy as np
import random
import model
from layer import Layer
from constants import *

def setup_network():
    """Return the initialized neural network"""
    input_layer = setup_input_layer()
    hidden_layer = setup_hidden_layer()
    output_layer = setup_output_layer()

    return model.Model(input_layer, hidden_layer, output_layer)



def setup_input_layer():
	"""Return the input layer as identity"""
	return Layer(model.identity, activation_function=model.identity)	



def setup_hidden_layer():
	"""Return the hidden layer initialized"""
	W1 = np.random.randn(INPUT_DIMENSION, N_HIDDEN_NODES) / np.sqrt(INPUT_DIMENSION)
	b1 = np.zeros((1, N_HIDDEN_NODES))
	return Layer(model.Linear(W1, b1), activation_function=np.tanh)


def setup_output_layer():
    """Return the output layer initialized"""
    W2 = np.random.randn(N_HIDDEN_NODES, OUTPUT_DIMENSION) / np.sqrt(N_HIDDEN_NODES)
    b2 = np.zeros((1, OUTPUT_DIMENSION))
    return Layer(model.Linear(W2, b2), activation_function=model.softmax)




