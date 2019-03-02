'''
The lists of sprites are reorganized, such that the order of rendering 
them on the screen is the same as the order in which they are displayed
on the sprite sheet.
This way the animation is smooth enough.


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
miau = pygame.transform.rotozoom(miau, 36, .50)

bg = os.path.join('images', 'bkg.jpg')
BckG = pygame.image.load(bg)
girl = os.path.join('images', 'girl_dancing.png')
sheet_g = pygame.image.load(girl).convert_alpha()
girl_list = []
for row in range(7):
    for col in range(3):
        girl_frame = sheet_g.subsurface((95*row, 130*col,  95, 130))
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
girl_x = 400
girl_y = 400


page = os.path.join('images', 'rob2.png')
sheet = pygame.image.load(page).convert_alpha()
ind_images = []
for row in range(9):
    for column in range(6):

        single_image = sheet.subsurface((64*row, 64*column, 64, 64))
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

    # screen.fill(BLACK)
    screen.blit(BckG , (0, 0))

    #--------Drawing code should go here
    # blit the gallows here


    #---------Update thje screen with what we have drawn

    now = pygame.time.get_ticks()
    if  now - nextFrame> 60:
        frame = (frame +1) %len(ind_images)
        screen.blit(ind_images[frame], ( aero_x, aero_y))
        item = (item + 1) % len(girl_list)
        screen.blit(girl_list[item], (girl_x, girl_y))
        nextFrame = now
    screen.blit(miau, (450, 250))

    # nowg = pygame.time.get_ticks()
    # if nowg - newGirl > 60:
    #     item = (item + 1)%len(girl_list)
    #     screen.blit(girl_list[item], (girl_x, girl_y))
    #     newGirl = nowg
    pygame.display.flip()


    #------Limit 60 frames per second
    clock.tick(60)


# Close the window and quit.
pygame.quit()



