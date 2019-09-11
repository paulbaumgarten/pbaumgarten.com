###
### DEMO TO TEST OUR NEURAL NETWORK
###

import random
import neuralnetwork
import logging

### Seed the random number generator
random.seed()

### Define training data
# The network is a lot more reliable if we give it two output nodes. 
# So, instead of just one target to indicate 1=TRUE, 0=FALSE, 
# we we will use two output nodes, 
# one to indicate the network is predicting TRUE, 
# the other to indicate the network is predicting FALSE 
training_data_inputs = [ [0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0] ]
training_data_target = [ [0.0, 1.0], [1.0, 0.0], [1.0, 0.0], [0.0, 1.0] ]

### Setup the network
nn = neuralnetwork.NeuralNetwork(2,6,2)
nn.set_activation_functions(neuralnetwork.sigmoid, neuralnetwork.sigmoid_derivative)
nn.set_learning_rate(0.1)

### Train the network
for i in range(200000):
    r = random.randint(0, 3)
    if (i % 1000 == 0):
        print("Training run {}".format(i))
    nn.train(training_data_inputs[r], training_data_target[r])

### Make some predictions
result = nn.predict( [0.0, 0.0] )
print(result.data)
result = nn.predict( [0.0, 1.0] )
print(result.data)
result = nn.predict( [1.0, 0.0] )
print(result.data)
result = nn.predict( [1.0, 1.0] )
print(result.data)
