import pygame, time, random
from pygame.locals import *

def main():
    #********** Game variables **********
    quit = False
    #********** Start game loop **********
    while not quit:
        window.fill((0,0,0))                            # Reset screen to black
        #********** Process events **********
        keyspressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                quit = True

        #********** Your game logic here **********

        #********** Update screen **********
        pygame.display.update()                         # Actually does the screen update
        clock.tick(25)                                  # Run the game at 25 frames per second

#********** Initialise & run the game **********
if __name__ == "__main__":
    width, height = 800, 600                            # Set screen width,height
    pygame.init()                                       # Start graphics system
    pygame.mixer.init()                                 # Start audio system
    window = pygame.display.set_mode((width, height))   # Create window
    clock = pygame.time.Clock()                         # Create game clock
    main()
    pygame.quit()
