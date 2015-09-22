def activation_prob(x, model):
    """Return the probability from the activation function

    Parameters:
    ----------
    x:

    model: Model object
        Current parameters of neural network


    Output:
    ------
    probs: float
        Probability of activation function
    """

    W1 = model.W1
    b1 = model.b1
    W2 = model.W2
    b2 = model.b2

    z1 = x.dot(W1) + b1
    a1 = activation_function_input_layer(z1)
    z2 = a1.dot(W2) + b2
    exp_scores = np.exp(z2)
    probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
    return probs

    

def predict(x, model):
    # Helper function to predict an output (0 or 1)

    probs = activation_prob(x, model)
    return np.argmax(probs, axis=1)


def regularization(model, reg_lambda=0.01):
    """Compute regularization term"""
    
    W1 = model.W1
    W2 = model.W2
    return reg_lambda/2 * (np.sum(np.square(W1)) + np.sum(np.square(W2)))



def calculate_loss(X, model):
    # Helper function to evaluate the total loss on the dataset    

    probs = activation_prob(X, model)
    
    # Calculating the loss
    corect_logprobs = -np.log(probs[range(num_examples), y])
    data_loss = np.sum(corect_logprobs)
    
    # Add regulatization term to loss (optional)
    data_loss += regularization(model)
    return 1./num_examples * data_loss








#num_examples = len(X) # training set size
 
# Gradient descent parameters (I picked these by hand)
epsilon = 0.01 # learning rate for gradient descent
