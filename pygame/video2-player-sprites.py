import pygame, time, random
from pygame.locals import *
import os

def main2c():   # Lesson 2... multiple animations, maintaining direction
    #********** Game variables **********
    quit = False
    x = 400
    y = 300
    # Load a single image for standing still
    player_stand = pygame.image.load("assets/p3_stand.png").convert_alpha()
    player_stand = pygame.transform.scale(player_stand, (50, 70))   # Resize to 50 wide 70 high
    # Jumping
    player_jump = pygame.image.load("assets/p3_jump.png").convert_alpha()
    player_jump = pygame.transform.scale(player_jump, (50, 70))   # Resize to 50 wide 70 high
    # Landing
    player_land = pygame.image.load("assets/p3_duck.png").convert_alpha()
    player_land = pygame.transform.scale(player_land, (50, 70))   # Resize to 50 wide 70 high
    # Create a list of images for walking left
    player_right = [
        pygame.image.load("assets/p3_walk01.png").convert_alpha(),
        pygame.image.load("assets/p3_walk02.png").convert_alpha(),
        pygame.image.load("assets/p3_walk03.png").convert_alpha(),
        pygame.image.load("assets/p3_walk04.png").convert_alpha(),
        pygame.image.load("assets/p3_walk05.png").convert_alpha(),
        pygame.image.load("assets/p3_walk06.png").convert_alpha(),
        pygame.image.load("assets/p3_walk07.png").convert_alpha(),
        pygame.image.load("assets/p3_walk08.png").convert_alpha(),
        pygame.image.load("assets/p3_walk09.png").convert_alpha(),
        pygame.image.load("assets/p3_walk10.png").convert_alpha(),
        pygame.image.load("assets/p3_walk11.png").convert_alpha(),
    ]
    # Resize all images in the list to 50x70
    player_right = [ pygame.transform.scale(image, (50, 70)) for image in player_right ]
    # Variable to remember which frame from the list we last displayed
    player_right_frame = 0
    # Create moving left images by flipping the right facing ones on the horizontal axis
    player_left = [ pygame.transform.flip(image, True, False) for image in player_right ]
    player_left_frame = 0
    # Maintain our direction
    direction = "stand"

    #********** Start game loop **********
    while not quit:
        window.fill((0,0,0))                            # Reset screen to black
        #********** Process events **********
        keyspressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            #print(event)    # Useful debugging tip
            if event.type == QUIT:
                quit = True
        if keyspressed[ord("a")]:
            x = x - 10
            direction = "left"
        if keyspressed[ord("d")]:
            x = x + 10
            direction = "right"
        if keyspressed[ord("w")]:
            y = y - 10
            direction = "jump"
        if keyspressed[ord("s")]:
            y = y + 10
            direction = "land"
        if sum(keyspressed) == 0:   # No key is pressed
            direction = "stand"
        #********** Your game logic here **********
        # Keep player within screen limits
        if y < 0: 
            y = 0
        if y >= window.get_height()-70: 
            y = window.get_height()-70
        if x < 0: 
            x = 0
        if x >= window.get_width()-50: 
            x = window.get_width()-50

        # Draw the player
        if direction == "left":
            window.blit(player_left[ player_left_frame ], (x,y))               
            player_left_frame = (player_left_frame + 1) % len(player_left)                  
        elif direction == "right":
            window.blit(player_right[ player_right_frame ], (x,y))                
            player_right_frame = (player_right_frame + 1) % len(player_right)                 
        elif direction == "jump":
            window.blit(player_jump, (x,y))
        elif direction == "land":
            window.blit(player_land, (x,y))
        else:
            window.blit(player_stand, (x,y))

        #********** Update screen **********
        pygame.display.update()                         # Actually does the screen update
        clock.tick(25)                                  # Run at 25 frames per second

#********** Initialise & run the game **********
if __name__ == "__main__":
    width, height = 800, 600                            # Set screen width,height
    pygame.init()                                       # Start graphics system
    pygame.mixer.init()                                 # Start audio system
    pygame.display.set_caption("Mr B's awesome game")   # Title bar
    window = pygame.display.set_mode((width, height))   # Create window
    clock = pygame.time.Clock()                         # Create game clock
    main2c()
    pygame.quit()
