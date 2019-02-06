'''
Pygame base template for opening  a window
Colors Chart (RGB)
https://www.rapidtables.com/web/color/RGB_Color.html

'''

import pygame
import os
# Define some colors

BLACK = (0,0,0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0 , 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()

# this sets the upper left corner of the window at (x =20, y = 50). The point (x =0, y = 0) is
# the Upper Left corner of the screen
os.environ['SDL_VIDEO_WINDOW_POS'] = '20,50'
# Set the WIDTH and the HEIGHT for the screen
WIDTH = 1200
HEIGHT = 700
size = ( WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Template for Pygame Programs')

# Loop until the user clicks the close button
done = False
# Use how fast the screen updates
clock = pygame.time.Clock()

#--------------Main Program Loop -------------
while not done:
    #---Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Game Logic should go here

    # Screen clearing goes here

    #Here we clear the screen to white. Don't put other drawing commands
    #  above this , or they will be erased with this command

    #If you want a background image, replace this clear with
    # blit' ing the background image.
    screen.fill(WHITE)

    #--------Drawing code should go here

    #---------Update thje screen with what we have drawn
    pygame.display.flip()

    #------Limit 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()


