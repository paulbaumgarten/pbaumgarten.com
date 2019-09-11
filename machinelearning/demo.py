import random
import neuralnetwork
import logging

# Seed the random number generator
random.seed()

loop = 0
predict = False

if __name__ == "__main__":
    training_data_inputs = [ [0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0] ]
    training_data_target = [      [0.0],      [1.0],     [1.0],      [0.0] ]

    nn = neuralnetwork.NeuralNetwork(2,4,1)
    nn.set_activation_functions(neuralnetwork.sigmoid, neuralnetwork.sigmoid_derivative)
    nn.set_learning_rate(0.05)

    while True:
        for i in range(500):
            r = random.randint(0, 3)
            if (loop % 100 == 0):
                print(f"Training run {loop} with inputs {training_data_inputs[r]} and target {training_data_target[r]}")
            nn.train(training_data_inputs[r], training_data_target[r])
            loop += 1

        if predict:
            for j in range(100):
                attempt = [0.0,0.0]
                prediction = nn.predict( attempt, True ).data
                print(f"For input {attempt}, prediction is {prediction}")

            attempt = [1.0,0.0]
            prediction = nn.predict( attempt, True ).data
            print(f"For input {attempt}, prediction is {prediction}")

            attempt = [0.0,1.0]
            prediction = nn.predict( attempt, True ).data
            print(f"For input {attempt}, prediction is {prediction}")

            attempt = [1.0,1.0]
            prediction = nn.predict( attempt, True ).data
            print(f"For input {attempt}, prediction is {prediction}")

            attempt = [0.0,0.0]
            prediction = nn.predict( attempt, True ).data
            print(f"For input {attempt}, prediction is {prediction}")

            attempt = [1.0,0.0]
            prediction = nn.predict( attempt, True ).data
            print(f"For input {attempt}, prediction is {prediction}")

            attempt = [0.0,1.0]
            prediction = nn.predict( attempt, True ).data
            print(f"For input {attempt}, prediction is {prediction}")

            attempt = [1.0,1.0]
            prediction = nn.predict( attempt, True ).data
            print(f"For input {attempt}, prediction is {prediction}")

        input("Enter to keep going")
