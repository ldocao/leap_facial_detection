import matplotlib.pyplot as plt
import numpy as np
import sklearn.datasets
import sklearn.linear_model
import plotting



class Points():
	def __init__(self, coordinates, label):
		self.coordinates = coordinates 
		self.label = label



def generate_data(n_points, noise=0.2):
    """Generate a dataset for training

    Parameters:
    ----------
    n_points: integer
        number of points for training

    noise: float
        noise in data
    """
    np.random.seed(0)
    X, y = sklearn.datasets.make_moons(n_points, noise=noise)
    return Points(X,y)






# plt.figure()
# plt.scatter(X[:,0], X[:,1], s=40, c=y, cmap=plt.cm.Spectral)


# # Train the logistic regression classifier
# clf = sklearn.linear_model.LogisticRegressionCV()
# clf.fit(X, y)

# # Plot the decision boundary
# plotting.plot_decision_boundary(X, y, lambda x: clf.predict(x))
# plt.title("Logistic Regression")
# plt.show()


