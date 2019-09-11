import random
import neuralnetwork
import logging
import pygame, time, random
from pygame.locals import *
import json

# Seed the random number generator
random.seed()

pygame.init()
window = pygame.display.set_mode((600,300))
fps = pygame.time.Clock()

# Declare colors, images, sounds, fonts, variables
BLACK = (0,0,0)
R = (255,0,0)
G = (0,255,0)
ARIAL12 = pygame.font.SysFont("Arial", 12)
ARIAL24 = pygame.font.SysFont("Arial", 24)
ARIAL36 = pygame.font.SysFont("Arial", 36)
quit = False

# Setup neural network
training_data_inputs = [
    [0.0, 0.0],
    [0.0, 1.0],
    [1.0, 0.0],
    [1.0, 1.0]
]
training_data_target = [
    [0.0, 1.0],
    [1.0, 0.0],
    [1.0, 0.0],
    [0.0, 1.0]
]
nn = neuralnetwork.NeuralNetwork(2,6,2, True)
nn.set_activation_functions(neuralnetwork.sigmoid, neuralnetwork.sigmoid_derivative)
nn.set_learning_rate(0.1)

def style(num):
    return str("{:+6.4f}".format(num))

prediction_count = len(training_data_target)
predictions = {}
for prediction in range(prediction_count):
    predictions[prediction] = []
loop = 0
paused = False

# Main game loop
while not quit:
    # Process events
    for event in pygame.event.get():
        if event.type == QUIT:
            quit = True
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                quit = True
            if event.key == K_RETURN:
                data = nn.serialise()
                print(data)
            if event.key == K_SPACE:
                print("[current predictions] =")
                for i in range(len(training_data_inputs)):
                    print(f"Input data = {training_data_inputs[i]}")
                    guess = nn.predict(training_data_inputs[i]).data
                    print(f"Prediction = {guess}")
            if event.key == K_p:
                paused = not paused

    if not paused:
        # Train the network
        r = random.randint(0, len(training_data_inputs)-1)
        nn.train(training_data_inputs[r], training_data_target[r])
        data = json.loads(nn.serialise())
        loop += 1


    if (loop % 1000 == 0):
        window.fill((0,0,0))

        for prediction in range(prediction_count):
            predictions[prediction].append( nn.predict( training_data_inputs[prediction] ).data )
        # Only 100 values per prediction history
        for prediction in range(prediction_count):
            while len(predictions[prediction]) > 100:
                predictions[prediction].pop(0)

        for p in range(prediction_count):
            COL = R
            if training_data_target[p][0] == 1.0:
                COL = G
            for i in range(len(predictions[p])):
                pygame.draw.line(window, COL, (100 + i * 2, 50+p*50), (100 + i * 2, p*50 + 50 - (predictions[p][i][0][0] * 50)), 2)
            window.blit(ARIAL12.render(style(predictions[p][-1][0][0]), 1, (255,255,255)), (300, 35+p*50))
            if len(training_data_target[p]) > 1:
                COL = R
                if training_data_target[p][1] == 1.0:
                    COL = G
                for i in range(len(predictions[p])):
                    pygame.draw.line(window, COL, (350 + i * 2, 50+p*50), (350 + i * 2, p*50 + 50 - (predictions[p][i][1][0] * 50)), 2)
                window.blit(ARIAL12.render(style(predictions[p][-1][1][0]), 1, (255,255,255)), (550, 35 + p * 50))

        window.blit(ARIAL36.render("TRUE", 1, (255,255,255)), (100, 210))
        window.blit(ARIAL36.render("FALSE", 1, (255,255,255)), (350, 210))
        window.blit(ARIAL36.render("1", 1, (255,255,255)), (600, 210))
        window.blit(ARIAL36.render("XOR", 1, (255,255,255)), (10, 260))
        window.blit(ARIAL12.render("Iteration: "+str(loop), 1, (255,255,255)), (480, 270))

        window.blit(ARIAL24.render("0, 0", 1, (255,255,255)), (10, 25))
        window.blit(ARIAL24.render("0, 1", 1, (255,255,255)), (10, 75))
        window.blit(ARIAL24.render("1, 0", 1, (255,255,255)), (10, 125))
        window.blit(ARIAL24.render("1, 1", 1, (255,255,255)), (10, 175))

        pygame.display.update() # Actually does the screen update
        fps.tick(50) # Run the game at 25 frames per second

# Loop over, game over
pygame.quit()

