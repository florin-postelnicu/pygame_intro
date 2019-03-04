'''
The lists of sprites are reorganized, such that the order of rendering
them on the screen is the same as the order in which they are displayed
on the sprite sheet.
This way the animation is smooth enough.


'''


import pygame
import os

vec = pygame.math.Vector2
# classes


class AnimGirl(pygame.sprite.Sprite):


    def __init__(self, x, y, girl_list):
        pygame.sprite.Sprite.__init__(self, allsprites)

        self.x = x
        self.y = y
        self.frame = 0
        self.image = girl_list[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.pos = vec(self.x, self.y)
        self.last_update = pygame.time.get_ticks()


    def anim_girl(self):

            screen.blit(girl_list[self.frame], self.pos)


    def update(self):
        self.anim_girl()
        now = pygame.time.get_ticks()

        if now - self.last_update > 100:
            self.frame = (self.frame + 1) % len(girl_list)
            self.last_update = now

#


class Aerocam(pygame.sprite.Sprite):

    def __init__(self, x, y, ind_images):
        pygame.sprite.Sprite.__init__(self, allsprites)
        self.x = x
        self.y = y
        self.frame = 0
        self.image = ind_images[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.pos = vec(self.x, self.y)
        self.aero_change_x = 0
        self.aero_change_y = 0
        self.vel = (self.aero_change_x, self.aero_change_y)
        self.last_update = pygame.time.get_ticks()

    def anim_aero(self):

        screen.blit(ind_images[self.frame], self.pos)

    def update(self):
        self.anim_aero()
        now = pygame.time.get_ticks()

        if now - self.last_update > 100:
            self.frame = (self.frame + 1) % (len(ind_images))
            self.last_update = now


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
screen = pygame.display.set_mode(size, pygame.HWSURFACE | pygame.DOUBLEBUF)
pygame.display.set_caption('Template for Pygame Programs')

# Loop until the user clicks the close button
done = False

# Use how fast the screen updates
clock = pygame.time.Clock()
# create a path to join the folder 'images' with the file 'kitten.png
ktn = os.path.join('images', 'kitten2.png')

# Load background image
bg = os.path.join('images', 'bkg.jpg')
BckG = pygame.image.load(bg)
# load the girl frames for animation, and create the list for these frames
girl = os.path.join('images', 'girl_dancing.png')
sheet_g = pygame.image.load(girl).convert_alpha()
girl_list = []
# girl_x = 400
# girl_y = 400
for column in range(7):
    for row in range(3):
        girl_frame = sheet_g.subsurface((95*column, 130*row,  95, 130))
        # pos_girl = girl_frame.get_rect()
        # pos_girl.center = girl_x, girl_y
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


# load the aero camera frames for animation, and create the list ind_images
page = os.path.join('images', 'rob2.png')
sheet = pygame.image.load(page).convert_alpha()

ind_images = []
# aero_x = 200
# aero_y = 200
for column in range(9):
    for row in range(6):

        single_image = sheet.subsurface((64*column, 64*row, 64, 64))
        # pos_aero = single_image.get_rect()
        # pos_aero.center = aero_x, aero_y
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
item = 0

# aero_change_x = 0
# aero_change_y = 0

allsprites = pygame.sprite.Group()
anim_girls =pygame.sprite.Group()
girl_dancing = AnimGirl(400,400, girl_list)
allsprites.add(girl_dancing)
anim_girls.add(girl_dancing)

aero = Aerocam(200, 200, ind_images)
aero_cams = pygame.sprite.Group()
aero_cams.add(aero)
allsprites.add(aero)

#--------------Main Program Loop -------------
while not done:
    #---Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #     if event.type == pygame.KEYDOWN:
    #
    #         if event.key == pygame.K_LEFT:
    #             aero_change_x -= 10
    #         elif event.key == pygame.K_RIGHT:
    #             aero_change_x += 10
    #         elif event.key == pygame.K_UP:
    #             aero_change_y -= 10
    #         elif event.key == pygame.K_DOWN:
    #             aero_change_y += 10
    #     if event.type == pygame.KEYUP:
    #         if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
    #             aero_change_x = 0
    #         elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
    #             aero_change_y = 0
    #
    #
    # # Game Logic should go here
    # if aero_x < 0 or aero_x> (WIDTH -64) or aero_y < 0 or aero_y > (HEIGHT - 64):
    #     aero_x += -1* aero_change_x
    #     aero_y += -1*aero_change_y
    # else :
    #     aero_x = aero_x + aero_change_x
    #     aero_y = aero_y + aero_change_y

    # Screen clearing goes here

    #Here we clear the screen to white. Don't put other drawing commands
    #  above this , or they will be erased with this command

    #If you want a background image, replace this clear with
    # blit' ing the background image.

    screen.fill(BLACK)
    screen.blit(BckG , (0, 0))


    #--------Drawing code should go here
    # blit the gallows here


    #---------Update thje screen with what we have drawn

    allsprites.update()
    pygame.display.flip()




    #------Limit 60 frames per second
    clock.tick(60)



# Close the window and quit.
pygame.quit()


