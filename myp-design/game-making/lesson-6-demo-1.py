import pygame, time, random
from pygame.locals import *
from pygamemadeeasy import *

### START GAME CODE ###
pygame.init()
window = pygame.display.set_mode((300,300))
fps = pygame.time.Clock()

folder = "/users/pbaumgarten/repos/paulbaumgarten/myp-design/game-making/img/"
# Declare colors, fonts, images
mario_right_animation   = SpriteAnimation(folder+"mario-right-animation.png", 90, 133)

# Variables
player_x = 100                                      # x-value of player
player_y = 100                                      # y-value of player
quit = False                                        # game still playing while this is True

# Main game loop
while not quit:

    # Process events
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                quit = True

    # Draw graphics
    window.fill( colors.black )

    # Draw the animated sprite    
    window.blit( mario_right_animation.next_frame(), ( player_x, player_y ) )

    # Update the window
    pygame.display.update()
    fps.tick(10)
pygame.quit()
