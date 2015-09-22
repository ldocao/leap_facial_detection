import numpy as np
import matplotlib.pyplot as plt
import sklearn



def plot_decision_boundary(training):
    """Plot the points with classifier overlay

    Parameters:
    ----------
    training: Points object
        training data points
    """

    X = training.coordinates
    y = training.label


    #define here predfunc
    clf = sklearn.linear_model.LogisticRegressionCV()
    clf.fit(X, y)
    pred_func = lambda x: clf.predict(x)

    # Set min and max values and give it some padding
    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
    h = 0.01
    # Generate a grid of points with distance h between them
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    # Predict the function value for the whole gid
    Z = pred_func(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    # Plot the contour and training examples
    plt.clf()
    plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Spectral)
    plt.show()
