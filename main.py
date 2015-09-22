from parameters import *
import model
import make_data as mk
import initialization
import neural_network as nn
from visualize import plot_decision_boundary
import matplotlib.pyplot as plt


## INITIALISATION
training_data = mk.generate_data(n_points)
neural_network = initialization.setup_network()
epoch = 0
plt.figure()



## TRAINING NEURAL NETWORK
loss = 2 * stop_criterion #initialize so as loss > stop_criterion
loss = stop_criterion/2. #debug
while loss > stop_criterion:
    print "Training neural network at epoch=", epoch

    neural_network = nn.train(neural_network)

    if epoch % evaluate_loss_frequency == 0:
        loss = evaluate_loss(neural_network)

    if epoch % visualize_classifier_frequency == 0:
    	plt.clf()
        plot_decision_boundary(training_data)
        plt.show()

    epoch += 1


## SUMMARY
print "Final epoch / loss = ", epoch, loss
plot_decision_boundary(training_data)
plt.show()










