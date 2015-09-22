from parameters import *
import model
import make_data as mk
import initialization
import neural_network as nn
from visualize import plot_decision_boundary
import matplotlib.pyplot as plt
import ipdb


## INITIALISATION
training_data = mk.generate_data(n_points)
neural_network = initialization.setup_network()
plt.figure()



## TRAINING NEURAL NETWORK
epoch = 0
loss = 2 * stop_criterion #initialize so as loss > stop_criterion
print "Start learning [epoch/loss]=", epoch, loss


while loss > stop_criterion:
    print "Training neural network at epoch=", epoch

    #neural_network = nn.train(neural_network)

    if epoch % evaluate_loss_frequency == 0:
        loss = nn.evaluate_loss(training_data, neural_network)
        print "    loss=", loss

    if epoch % visualize_classifier_frequency == 0:
        plot_decision_boundary(training_data)


    if epoch >= max_epochs:
    	break
    	
    epoch += 1


## SUMMARY
print "Final epoch / loss = ", epoch, loss
plot_decision_boundary(training_data)











