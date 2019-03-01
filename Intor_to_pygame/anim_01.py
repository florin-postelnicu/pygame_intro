
'''
The size of a sprite in this example is 64x64 pixels.
The sprite-sheet rob2.png is a 6 rows  by 9 columns.

Step1 Load the whole sprite-sheet
   page = os.path.join('images', 'rob2.png')
   sheet = pygame.image.load(page).convert_alpha()

Step 2 Break the sprite-sheet in 54 independent images , reading one-by-one,
and append each such independent image(frame) to the list of frames(ind_images).
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


Note !
      screen.fill(BLACK) 
or (WHITE) should be placed before blitting the background.
Its purpose is to hide the previous frame when the next one is blit.
'''


import pygame
import os
import sys

# Define some colors

BLACK = (0 ,0 ,0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0 , 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()

os.environ['SDL_VIDEO_WINDOW_POS'] = '20,50'
WIDTH = 1200
HEIGHT = 700
size = ( WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Template for Pygame Programs')

done = False

clock = pygame.time.Clock()


bg = os.path.join('images', 'bkg.jpg')
BckG = pygame.image.load(bg)
# The next two lines are to load the sprite sheet
# Step 1 
page = os.path.join('images', 'rob2.png')
sheet = pygame.image.load(page).convert_alpha()
# End of Step1
# Step 2
ind_images = []
for row in range(9):
    for column in range(6):
        single_image = sheet.subsurface((64 * row, 64 * column, 64, 64))
        ind_images.append(single_image)
# End of Step 3
# Step 3
nextFrame = pygame.time.get_ticks()
frame = 0
# End of Step 3
aero_x = 200
aero_y = 200

# --------------Main Program Loop -------------
while not done:
    # ---Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True



    screen.fill(BLACK)
    screen.blit(BckG, (0, 0))




    # ---------Update thje screen with what we have drawn
    # Step 4
    now = pygame.time.get_ticks()
    if now - nextFrame > 50:
        frame = (frame + 1) % len(ind_images)
        screen.blit(ind_images[frame], (aero_x, aero_y))
        nextFrame = now
    # End of Step 4
    pygame.display.flip()

    # ------Limit 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()

