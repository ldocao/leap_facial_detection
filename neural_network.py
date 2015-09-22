import numpy as np

def activation_prob(x, neural_network):
    """Return the probability from the activation function

    Parameters:
    ----------
    x: Points object

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


def regularization(neural_network, reg_lambda=0.01):
    """Compute regularization term"""
    
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






    

def predict(x, neural_network):
    # Helper function to predict an output (0 or 1)

    probs = activation_prob(x, neural_network)
    return np.argmax(probs, axis=1)

