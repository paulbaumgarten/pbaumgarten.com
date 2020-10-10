import pygame, time, random
from pygame.locals import *
from pytmx.util_pygame import load_pygame

def blit_all_tiles(window, tmxdata, world_offset):
    for layer in tmxdata:
        for tile in layer.tiles():
            # tile[0] .... x grid location
            # tile[1] .... y grid location
            # tile[2] .... image data for blitting
            img = pygame.transform.scale( tile[2], (35,35))
            x_pixel = tile[0] * 35 + world_offset[0]
            y_pixel = tile[1] * 35 + world_offset[1]
            window.blit( img, (x_pixel, y_pixel))

def get_tile_properties(tmxdata, x, y, world_offset):
    world_x = x - world_offset[0]
    world_y = y - world_offset[1]
    tile_x = world_x // 35
    tile_y = world_y // 35
    layer = tmxdata.layers[0]
    try:
        properties = tmxdata.get_tile_properties(tile_x, tile_y, 0)
    except ValueError:
        properties = {"id": -1, "climbable": 0, "ground":0, "health":-10000, "points": 0, "provides":"", "requires":"", "solid":0}
    if properties is None:
        properties = {"id": -1, "climbable": 0, "ground":0, "health":0, "points": 0, "provides":"", "requires":"", "solid":0}
    properties['x'] = tile_x
    properties['y'] = tile_y
    return properties

def main5():   # Lesson 2... multiple animations, maintaining direction
    #********** Game variables **********
    tmxdata = load_pygame("my whole new world.tmx")
    y_ground = window.get_height()-170 # DRY - Don't repeat yourself
    arial = pygame.font.SysFont("Arial", 18)
    quit = False
    x = 400
    health = 100
    points = 0
    y = y_ground
    # Load a single image for standing still
    player_stand = pygame.image.load("assets/p3_stand.png").convert_alpha()
    player_stand = pygame.transform.scale(player_stand, (25, 35))   # Resize to 50 wide 70 high
    # Jumping
    player_jump = pygame.image.load("assets/p3_jump.png").convert_alpha()
    player_jump = pygame.transform.scale(player_jump, (25, 35))   # Resize to 50 wide 70 high
    player_jump_frame = 0
    # Landing
    player_land = pygame.image.load("assets/p3_duck.png").convert_alpha()
    player_land = pygame.transform.scale(player_land, (25, 35))   # Resize to 50 wide 70 high
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
    player_right = [ pygame.transform.scale(image, (25, 35)) for image in player_right ]
    # Variable to remember which frame from the list we last displayed
    player_right_frame = 0
    # Create moving left images by flipping the right facing ones on the horizontal axis
    player_left = [ pygame.transform.flip(image, True, False) for image in player_right ]
    player_left_frame = 0
    # Maintain our direction
    direction = "stand"
    world_offset = [0,0]

    #********** Start game loop **********
    while not quit:
        window.fill((64,64,64))                            # Reset screen to black
        blit_all_tiles(window, tmxdata, world_offset)
        points_image = arial.render(f"Points: {points}", 1, (255,255,255))
        health_image = arial.render("Health: "+str(health), 1, (255,255,255) )
        window.blit(points_image, (50, 10))
        window.blit(health_image, (50, 30))
        #********** Process events **********
        keyspressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            #print(event)    # Useful debugging tip
            if event.type == QUIT:
                quit = True
        if keyspressed[ord("a")]:
            left_tile = get_tile_properties(tmxdata, x-10, y+17, world_offset)
            if left_tile['solid'] == 0:
                x = x - 10
                direction = "left"
        if keyspressed[ord("d")]:
            right_tile = get_tile_properties(tmxdata, x+25+10, y+17, world_offset)
            print(right_tile)
            if right_tile['solid'] == 0:
                x = x + 10
                direction = "right"
        standing_on = get_tile_properties(tmxdata, x+12, y+35, world_offset)
        if keyspressed[ord("w")]:
            if standing_on['ground'] == 1:
                player_jump_frame = 20
        if keyspressed[ord("s")]:
            pass # Do nothing
        if sum(keyspressed) == 0:   # No key is pressed
            direction = "stand"
        #********** Your game logic here **********
        touching = get_tile_properties(tmxdata, x+12, y+17, world_offset)
        health += touching['health']
        points += touching['points']
        if health < 0:
            quit = True
        if touching['id'] == 408: # Gold coin
            tile_x = touching['x']
            tile_y = touching['y']
            tmxdata.layers[0].data[tile_y][tile_x] = 0

        if player_jump_frame > 0: # Jumping in progress
            above_tile = get_tile_properties(tmxdata, x+12, y-10, world_offset)
            if above_tile['solid'] == 0:
                y = y - 10
                direction = "jump"
                player_jump_frame -= 1
            else: # We hit our head, start falling immediately
                player_jump_frame = 0
        elif standing_on['ground'] == 0: # Stopped movinng up, now falling
            y = y + 10
            direction = "land"

        # Keep player within screen limits
        if y < 140: 
            y = 140
            world_offset[1] += 10
        if y > y_ground: 
            y = y_ground
            world_offset[1] -= 10
        if x < 140: 
            x = 140
            world_offset[0] += 10
        if x > window.get_width()-140-15: 
            x = window.get_width()-140-15
            world_offset[0] -= 10

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
    main5()
    pygame.quit()
