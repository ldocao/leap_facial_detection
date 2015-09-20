import matplotlib.pyplot as plt
import numpy as np
import sklearn.datasets
import sklearn.linear_model
import ipdb
import plotting



    
# Generate a dataset and plot it
np.random.seed(0)
X, y = sklearn.datasets.make_moons(200, noise=0.20)
plt.figure()
plt.scatter(X[:,0], X[:,1], s=40, c=y, cmap=plt.cm.Spectral)


# Train the logistic rgeression classifier
clf = sklearn.linear_model.LogisticRegressionCV()
clf.fit(X, y)
 
# Plot the decision boundary
plotting.plot_decision_boundary(X, y, lambda x: clf.predict(x))
plt.title("Logistic Regression")
plt.show()

