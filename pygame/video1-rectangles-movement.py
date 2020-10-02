import pygame, time, random
from pygame.locals import *

def main2():
    #********** Game variables **********
    quit = False
    x = 0
    y = 0
    #********** Start game loop **********
    while not quit:
        window.fill((0,0,0))                            # Reset screen to black
        #********** Process events **********
        keyspressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            print(event)    # Useful debugging tip
            if event.type == QUIT:
                quit = True
        if keyspressed[ord("a")]:
            x = x - 50
        if keyspressed[ord("d")]:
            x = x + 50
        if keyspressed[ord("w")]:
            y = y - 50
        if keyspressed[ord("s")]:
            y = y + 50
        if y < 0: 
            y = 0
        if y >= window.get_height()-50: 
            y = window.get_height()-50
        if x < 0: 
            x = 0
        if x >= window.get_width()-50: 
            x = window.get_width()-50

        #********** Your game logic here **********
        player = Rect(x, y, 50, 50)
        pygame.draw.rect(window, (204,0,255), player)

        #********** Update screen **********
        pygame.display.update()                         # Actually does the screen update
        clock.tick(25)                                  # Run the game at 25 frames per second

#********** Initialise & run the game **********
if __name__ == "__main__":
    width, height = 800, 600                            # Set screen width,height
    pygame.init()                                       # Start graphics system
    pygame.mixer.init()                                 # Start audio system
    pygame.display.set_caption("Mr B's awesome game")   # Title bar
    window = pygame.display.set_mode((width, height))   # Create window
    clock = pygame.time.Clock()                         # Create game clock
    main2()
    pygame.quit()
