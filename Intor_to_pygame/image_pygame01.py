'''
1) Loading images for your program should br donr after
pygame.init()

but before the main loop
while not done:

2) Organize all your images in a folder named images, or what you want.
Before downloading an image from this folder, for example img1.png  from
folder images, you need to import os.
Make a variable var1

var1 = os.path.join("images , 'img1.png)

 such that, you create a path from img1.png and your program.

 Then you need to load that image:

  iamge1 = pygame.image.load(var1)

  If your image is a background , than you need to remove
  screen.fill(COLOR)
  with
  screen.blit(image1)

  If the image needs to be blit to another place( it might be a sprite representing
  a player, or an enemy, etc) , you have to do it in the drawing area of your main loop


'''

import pygame
import os
import sys
# Define some colors

BLACK = (0,0,0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0 , 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()


# Set the WIDTH and the HEIGHT for the screen
os.environ['SDL_VIDEO_WINDOW_POS'] = '20,50'
WIDTH = 1200
HEIGHT = 700
size = ( WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Template for Pygame Programs')

# Loop until the user clicks the close button
done = False
# Use how fast the screen updates
clock = pygame.time.Clock()
# create a path to join the folder 'images' with the file 'kitten.png
ktn = os.path.join('images', 'kitten.png')
# Make the background of the kitten sprite transparent using .convert_alpha()
miau = pygame.image.load(ktn).convert_alpha()
# use transformations to flip the kitten on the x_axis, by making True
# the corresponding field, and False the other
# pygame.transform.flip( image, flip_x, flip_y)
miau = pygame.transform.flip( miau, True, False )

bg = os.path.join('images', 'bkg.jpg')
BckG = pygame.image.load(bg)
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

    screen.blit(BckG , (0, 0))

    #--------Drawing code should go here
    # blit the gallows here
    screen.blit(miau, (450, 340))

    #---------Update thje screen with what we have drawn
    pygame.display.flip()

    #------Limit 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()


