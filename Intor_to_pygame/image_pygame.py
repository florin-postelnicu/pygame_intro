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


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # Call Sprite Initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Gallows(pygame.sprite.Sprite):
    def __init__(self, image_file,  location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file).convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

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

BckG = Background('bkg.jpg', [0,0])
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
    screen.blit(BckG.image, BckG.rect )

    #--------Drawing code should go here
    # blit the gallows here

    #---------Update thje screen with what we have drawn
    pygame.display.flip()

    #------Limit 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()


