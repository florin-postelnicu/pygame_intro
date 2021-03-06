'''
The lists of sprites are reorganized, such that the order of rendering 
them on the screen is the same as the order in which they are displayed
on the sprite sheet.
The next technique is very common in animation; the point (coordinates) referencing the image it is 
associated to its center (like in physics, center of gravity).
For each image_frame in animation the reference point is the center of the rectangale circumscribing it.
   pos_image_frame = image_frame.get_rect()
   pos_image_frame.center = image_frame_x, image_frame_y
This way the animation is smooth enough, and the jittering of the image is eliminaated.
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


# Set the WIDTH and the HEIGHT for the screen
os.environ['SDL_VIDEO_WINDOW_POS'] = '20,50'
WIDTH = 1200
HEIGHT = 700
size = ( WIDTH, HEIGHT)
screen = pygame.display.set_mode(size, pygame.HWSURFACE|pygame.DOUBLEBUF)
pygame.display.set_caption('Animation 3 , Position = Center, Correct Order of Frames')

# Loop until the user clicks the close button
done = False

# Use how fast the screen updates
clock = pygame.time.Clock()


bg = os.path.join('images', 'bkg.jpg')
BckG = pygame.image.load(bg)
girl = os.path.join('images', 'girl_dancing.png')
sheet_g = pygame.image.load(girl).convert_alpha()
girl_list = []
girl_x = 400
girl_y = 400
for column in range(7):
    for row in range(3):
        girl_frame = sheet_g.subsurface((95*column, 130*row,  95, 130))
        pos_gril_frame = gril_frame.get_rect()
        pos_girl_frame.center = girl_x, girl_y
        girl_list.append(girl_frame)
list_0 =[]
list_1 =[]
list_2 = []
for i in range(len(girl_list)):
    if i %3 == 0:
        list_0.append(girl_list[i])
    elif i%3 == 1:
        list_1.append(girl_list[i])
    else :
        list_2.append(girl_list[i])
girl_list = list_0 + list_1 + list_2
# newGirl = pygame.time.get_ticks()
item = 0



page = os.path.join('images', 'rob2.png')
sheet = pygame.image.load(page).convert_alpha()
ind_images = []
aero_x = 200
aero_y = 200
aero_change_x = 0
aero_change_y = 0
for column in range(9):
    for row in range(6):

        single_image = sheet.subsurface((64*column, 64*row, 64, 64))
        pos_single_image = single_image.get_rect()
        pos_single_image.center = aero_x, aero_y
        ind_images.append(single_image)
blist_0 = []
blist_1 = []
blist_2 = []
blist_3 = []
blist_4 = []
blist_5 = []
for j in range(len(ind_images)):
    if j%6 == 0:
        blist_0.append(ind_images[j])
    elif j%6 == 1:
        blist_1.append(ind_images[j])
    elif j%6 == 2:
        blist_2.append(ind_images[j])
    elif j%6 == 3:
        blist_3.append(ind_images[j])
    elif j%6 == 4:
        blist_4.append(ind_images[j])
    else :
        blist_5.append(ind_images[j])

ind_images = blist_0 + blist_1 + blist_2 + blist_3 + blist_4+ blist_5

nextFrame = pygame.time.get_ticks()
frame = 0

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

    screen.blit(BckG , (0, 0))
    screen.blit(miau, (450, 250))
    #--------Drawing code should go here
 
    #---------Update thje screen with what we have drawn

    now = pygame.time.get_ticks()
    if  now - nextFrame> 60:
        frame = (frame +1) %len(ind_images)
        screen.blit(ind_images[frame], ( aero_x, aero_y))
        item = (item + 1) % len(girl_list)
        screen.blit(girl_list[item], (girl_x, girl_y))
        nextFrame = now
        pygame.display.flip()
    
    #------Limit 60 frames per second
    clock.tick(60)


# Close the window and quit.
pygame.quit()

