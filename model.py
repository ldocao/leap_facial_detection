class Model():
    def __init__(self, input_layer, hidden_layer, output_layer):
        self.input_layer = input_layer
        self.hidden_layer = hidden_layer
        self.output_layer = output_layer



class Linear():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def result(self, x):
        return x.dot(self.a) + self.b


def softmax(x):
    """Return a probability [0,1] which is the activation function of the output layer

    Parameters:
    ----------
    x: np.array
    """
    exp_scores = np.exp(x)  
    return exp_scores / np.sum(exp_scores, axis=1, keepdims=True)


def identity(x):
    return x
