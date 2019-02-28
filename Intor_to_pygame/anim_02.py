


 
'''
The size of a sprite in this example is 64x64 pixels.
The sprite-sheet rob2.png is a 6 rows  by 9 columns.
Step1 Load the whole sprite-sheet
    page = os.path.join('images', 'rob2.png')
    sheet = pygame.image.load(page).convert_alpha()
    
Step 2 Break the sprite-sheet in 54 independent images , reading one-by-one,
and append each such independent image(frame) to the list of frames.

   ind_images = []
   for row in range(9):
        for column in range(6):

            single_image = sheet.subsurface((64*row, 64*column, 64, 64))
            ind_images.append(single_image)

Step 3 Set up the ticking clock for displaying the frames in the list of frames

    nextFrame = pygame.time.get_ticks()
    frame = 0

Step 4 Inside the main loop blit in order every one of the frames in your list,
by allowing a time of 50 miliseconds between every other frame.


     now = pygame.time.get_ticks()
     if  now - nextFrame> 50:
         frame = (frame +1) %len(ind_images)
         screen.blit(ind_images[frame], ( aero_x, aero_y))
         nextFrame = now


'''


import pygame
import os
import sys
import itertools
# Define some colors

BLACK = (0,0,0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0 , 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()

def cycle(ind_images):
    saved = []
    for element in ind_images:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
            yield element
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
ktn = os.path.join('images', 'kitten2.png')
# Make the background of the kitten sprite transparent using .convert_alpha()
miau = pygame.image.load(ktn).convert_alpha()
# use transformations to flip the kitten on the x_axis, by making True
# the corresponding field, and False the other
# pygame.transform.flip( image, flip_x, flip_y)
miau = pygame.transform.flip( miau, True, False )
miau = pygame.transform.rotozoom(miau, 45, .50)

bg = os.path.join('images', 'bkg.jpg')
BckG = pygame.image.load(bg)
page = os.path.join('images', 'rob2.png')
sheet = pygame.image.load(page).convert_alpha()
ind_images = []
for row in range(9):
    for column in range(6):

        single_image = sheet.subsurface((64*row, 64*column, 64, 64))
        ind_images.append(single_image)
nextFrame = pygame.time.get_ticks()
frame = 0
aero_x = 200
aero_y = 200
aero_change_x = 0
aero_change_y = 0
#--------------Main Program Loop -------------
while not done:
    #---Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                aero_change_x -= 10
            elif event.key == pygame.K_RIGHT:
                aero_change_x +=10
            elif event.key == pygame.K_UP:
                aero_change_y -=10
            elif event.key == pygame.K_DOWN:
                aero_change_y +=10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                aero_change_x = 0
            elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                aero_change_y = 0


    # Game Logic should go here
    if aero_x < 0 or aero_x> (WIDTH -64) or aero_y < 0 or aero_y > (HEIGHT - 64):
        aero_x += -1* aero_change_x
        aero_y += -1*aero_change_y
    else :
        aero_x = aero_x + aero_change_x
        aero_y = aero_y + aero_change_y

    # Screen clearing goes here

    #Here we clear the screen to white. Don't put other drawing commands
    #  above this , or they will be erased with this command

    #If you want a background image, replace this clear with
    # blit' ing the background image.

    screen.fill(BLACK)
    screen.blit(BckG , (0, 0))

    #--------Drawing code should go here
    # blit the gallows here
    screen.blit(miau, (450, 250))


    #---------Update thje screen with what we have drawn

    now = pygame.time.get_ticks()
    if  now - nextFrame> 50:
        frame = (frame +1) %len(ind_images)
        screen.blit(ind_images[frame], ( aero_x, aero_y))
        nextFrame = now
    pygame.display.flip()




    #------Limit 60 frames per second
    clock.tick(60)


# Close the window and quit.
pygame.quit()



