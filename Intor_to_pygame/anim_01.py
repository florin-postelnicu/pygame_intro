
'''
The size of a sprite in this example is 64x64 pixels.
The sprite-sheet rob2.png is a 6 rows  by 9 columns.The numbers of the lines are given like in the program anim_01.py

Step1 Load the whole sprite-sheet
59   page = os.path.join('images', 'rob2.png')
60   sheet = pygame.image.load(page).convert_alpha()

Step 2 Break the sprite-sheet in 54 independent images , reading one-by-one,
and append each such independent image(frame) to the list of frames.
62   ind_images = []
63   for row in range(9):
64        for column in range(6):
65            single_image = sheet.subsurface((64*row, 64*column, 64, 64))
66            ind_images.append(single_image)

Step 3 Set up the ticking clock for displaying the frames in the list of frames
67    nextFrame = pygame.time.get_ticks()
68    frame = 0

Step 4 Inside the main loop blit in order every one of the frames in your list,
by allowing a time of 50 miliseconds between every other frame.
92     now = pygame.time.get_ticks()
93   if  now - nextFrame> 50:
94       frame = (frame +1) %len(ind_images)
95       screen.blit(ind_images[frame], ( aero_x, aero_y))
96       nextFrame = now


Note !
88    screen.fill(BLACK) , or (WHITE) should be placed before blitting the background
its purpose is to hide the previous frame when the next one is blit.
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
page = os.path.join('images', 'rob2.png')
sheet = pygame.image.load(page).convert_alpha()

ind_images = []
for row in range(9):
    for column in range(6):
        single_image = sheet.subsurface((64 * row, 64 * column, 64, 64))
        ind_images.append(single_image)
nextFrame = pygame.time.get_ticks()
frame = 0
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

    now = pygame.time.get_ticks()
    if now - nextFrame > 50:
        frame = (frame + 1) % len(ind_images)
        screen.blit(ind_images[frame], (aero_x, aero_y))
        nextFrame = now
    pygame.display.flip()

    # ------Limit 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()

