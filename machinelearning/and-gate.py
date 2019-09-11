import random
import neuralnetwork
import logging
import pygame, time, random
from pygame.locals import *
import json

# Seed the random number generator
random.seed()

pygame.init()
window = pygame.display.set_mode((1000,500))
fps = pygame.time.Clock()

# Declare colors, images, sounds, fonts, variables
BLACK = (0,0,0)
ARIAL12 = pygame.font.SysFont("Arial", 12)
ARIAL24 = pygame.font.SysFont("Arial", 24)
ARIAL36 = pygame.font.SysFont("Arial", 36)
quit = False

# Setup neural network
training_data_inputs = [ [0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0] ]
training_data_target = [ [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [1.0, 0.0] ] # 1st value = 1st column on pygame grid
nn = neuralnetwork.NeuralNetwork(2,6,2)
nn.set_activation_functions(neuralnetwork.sigmoid, neuralnetwork.sigmoid_derivative)
nn.set_learning_rate(0.1)


def style(num):
    return str("{:+6.4f}".format(num))

prediction0 = []
prediction1 = []
prediction2 = []
prediction3 = []
loop = 0

# Main game loop
while not quit:
    loop+= 1
    # Process events
    for event in pygame.event.get():
        print(event)
        if event.type == QUIT:
            quit = True
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                quit = True

    # Train the network
    r = random.randint(0, 3)
    nn.train(training_data_inputs[r], training_data_target[r])
    data = json.loads(nn.serialise())

    prediction0.append(nn.predict( [0,0] ).data)
    prediction1.append(nn.predict( [1,0] ).data)
    prediction2.append(nn.predict( [0,1] ).data)
    prediction3.append(nn.predict( [1,1] ).data)

    if (loop % 10 == 0) and (len(prediction0) > 100):
        window.fill((255,255,255))

        while len(prediction0) > 100:
            prediction0.pop(0)
            prediction1.pop(0)
            prediction2.pop(0)
            prediction3.pop(0)
        for i in range(100):
            #print(prediction0)
            pygame.draw.line(window, BLACK, (i * 4, 100), (i * 4, 100 - (prediction0[i][0][0] * 100)), 4)
            pygame.draw.line(window, BLACK, (i * 4, 200), (i * 4, 200 - (prediction1[i][0][0] * 100)), 4)
            pygame.draw.line(window, BLACK, (i * 4, 300), (i * 4, 300 - (prediction2[i][0][0] * 100)), 4)
            pygame.draw.line(window, BLACK, (i * 4, 400), (i * 4, 400 - (prediction3[i][0][0] * 100)), 4)

            pygame.draw.line(window, BLACK, (500+i * 4, 100), (500+i * 4, 100 - (prediction0[i][1][0] * 100)), 4)
            pygame.draw.line(window, BLACK, (500+i * 4, 200), (500+i * 4, 200 - (prediction1[i][1][0] * 100)), 4)
            pygame.draw.line(window, BLACK, (500+i * 4, 300), (500+i * 4, 300 - (prediction2[i][1][0] * 100)), 4)
            pygame.draw.line(window, BLACK, (500+i * 4, 400), (500+i * 4, 400 - (prediction3[i][1][0] * 100)), 4)

        window.blit(ARIAL36.render("AND GATE", 1, (0,0,0)), (20, 420))
        window.blit(ARIAL36.render("= TRUE", 1, (0,0,0)), (350, 420))
        window.blit(ARIAL36.render("= FALSE", 1, (0,0,0)), (850, 420))
        window.blit(ARIAL12.render("Iteration: "+str(loop), 1, (0,0,0)), (20, 470))

        window.blit(ARIAL12.render("[0,0] = "+style(prediction0[99][0][0]), 1, (0,0,0)), (410, 100))
        window.blit(ARIAL12.render("[0,1] = "+style(prediction1[99][0][0]), 1, (0,0,0)), (410, 200))
        window.blit(ARIAL12.render("[1,0] = "+style(prediction2[99][0][0]), 1, (0,0,0)), (410, 300))
        window.blit(ARIAL12.render("[1,1] = "+style(prediction3[99][0][0]), 1, (0,0,0)), (410, 400))

        window.blit(ARIAL12.render("[0,0] = "+style(prediction0[99][1][0]), 1, (0,0,0)), (910, 100))
        window.blit(ARIAL12.render("[0,1] = "+style(prediction1[99][1][0]), 1, (0,0,0)), (910, 200))
        window.blit(ARIAL12.render("[1,0] = "+style(prediction2[99][1][0]), 1, (0,0,0)), (910, 300))
        window.blit(ARIAL12.render("[1,1] = "+style(prediction3[99][1][0]), 1, (0,0,0)), (910, 400))

        pygame.display.update() # Actually does the screen update
        fps.tick(50) # Run the game at 25 frames per second

# Loop over, game over
pygame.quit()

