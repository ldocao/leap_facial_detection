import numpy as np
from layer import Layer
from model import Linear
import copy
import ipdb

def activation_prob(x, neural_network):
    """Return the probability from the activation function

    Parameters:
    ----------
    x: np.array
        coordinates of points
    neural_network: neural_network object
        Current parameters of neural network


    Output:
    ------
    probs: float
        Probability of activation function
    """

    a1 = neural_network.hidden_layer.output(x)
    probs = neural_network.output_layer.output(a1)
    return probs


def regularization(neural_network):
    """Compute regularization term"""
    from parameters import reg_lambda

    W1 = neural_network.hidden_layer.model.a
    W2 = neural_network.output_layer.model.b
    return reg_lambda/2 * (np.sum(np.square(W1)) + np.sum(np.square(W2)))



def evaluate_loss(points, neural_network):
    """Return the loss value of the prediction

    Parameters:
    ----------
    training_coord: np.array
        coordinates of the training data points

    neural_network: neural_network object
        current state of neural network
    """
    probs = activation_prob(points.coordinates, neural_network)
    
    # Calculating the loss
    num_examples = len(points.coordinates) #number of points
    correct_logprobs = -np.log(probs[range(num_examples), points.label])
    data_loss = np.sum(correct_logprobs)
    
    # Add regulatization term to loss (optional)
    data_loss += regularization(neural_network)
    return 1./num_examples * data_loss






    




# This function learns parameters for the neural network and returns the model.
# - nn_hdim: Number of nodes in the hidden layer
# - num_passes: Number of passes through the training data for gradient descent
# - print_loss: If True, print the loss every 1000 iterations
def train(training_data, neural_network):

    from parameters import reg_lambda, epsilon
    y = training_data.label
    X = training_data.coordinates
    a1 = neural_network.hidden_layer.model.result(X)
    W1 = neural_network.hidden_layer.model.a
    b1 = neural_network.hidden_layer.model.b
    W2 = neural_network.output_layer.model.a
    b2 = neural_network.output_layer.model.b
    num_examples = len(X)
    probs = activation_prob(training_data.coordinates, neural_network)

    # Backpropagation
    delta3 = probs
    delta3[range(num_examples), y] -= 1
    dW2 = (a1.T).dot(delta3)
    db2 = np.sum(delta3, axis=0, keepdims=True)
    delta2 = delta3.dot(W2.T) * (1 - np.power(a1, 2))
    dW1 = np.dot(X.T, delta2)
    db1 = np.sum(delta2, axis=0)


    # Add regularization terms (b1 and b2 don't have regularization terms)
    dW2 += reg_lambda * W2
    dW1 += reg_lambda * W1

    # Gradient descent parameter update
    W1 += -epsilon * dW1
    b1 += -epsilon * db1
    W2 += -epsilon * dW2
    b2 += -epsilon * db2
    
    new_network = copy.deepcopy(neural_network)
    new_network.hidden_layer.model = Linear(W1,b1)
    new_network.output_layer.model = Linear(W2,b2)

    return new_network



def predict(x, neural_network):
    """

    Parameters:
    ----------
    x: np.array
        coordinates of points
    """
    # Helper function to predict an output (0 or 1)

    probs = activation_prob(x, neural_network)
    return np.argmax(probs, axis=1)



