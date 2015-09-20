import plotting

# Generate a dataset
np.random.seed(0)
X, y = sklearn.datasets.make_moons(200, noise=0.20)



num_examples = len(X) # training set size
nn_input_dim = 2 # input layer dimensionality
nn_output_dim = 2 # output layer dimensionality
 
# Gradient descent parameters (I picked these by hand)
epsilon = 0.01 # learning rate for gradient descent
reg_lambda = 0.01 # regularization strength
