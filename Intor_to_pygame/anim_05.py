'''
For each object animated a special class has been created.
class AnimGirl
class AeroCam
The animation sequencing is done in update method corresponding to each class,
thaus the animation is controlled only by the
allsprites.update() function.
girl_dancing is an instance for class AnimGirl, while
aero is an instance of AeroCam class.
Each one of these objects have been added to allsprites group.
The motion of aero camera is done in the AeroCam method
move_aero()
'''

import pygame
import os
from pygame.math import  Vector2 as vec


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
        now = pygame.time.get_ticks()
        screen.blit(girl_list[self.frame], self.pos)
        if now - self.last_update > 100:
            self.frame = (self.frame + 1) % len(girl_list)
            self.last_update = now


    def update(self):
        self.anim_girl()


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
        self.vel = vec(0,0 )
        self.acc = vec(0.05,0)
        self.fric = vec(-0.06, 0)
        self.last_update = pygame.time.get_ticks()

    def anim_aero(self):

        now = pygame.time.get_ticks()
        screen.blit(ind_images[self.frame], self.pos)
        if now - self.last_update > 100:
            self.frame = (self.frame + 1) % (len(ind_images))
            self.last_update = now

    def move_aero(self):
        self.aero_change_y = 0
        self.aero_change_x = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.aero_change_x -= 10
        if keys[pygame.K_RIGHT]:
            self.aero_change_x += 10
        if keys[pygame.K_DOWN]:
            self.aero_change_y += 10
        if keys[pygame.K_UP]:
            self.aero_change_y -= 10
        if self.aero_change_x != 0 and self.aero_change_x != 0:
            self.aero_change_x *= 0.7071
            self.aero_change_y *= 0.7071
        if self.x < 0 or self.x > WIDTH:
            self.aero_change_x *= -1
        if self.y < 0 or self.y > HEIGHT:
            self.aero_change_y *= -1

        self.x += self.aero_change_x
        self.y += self.aero_change_y
        self.rect.center = (self.x, self.y)
        self.vel = (self.aero_change_x, self.aero_change_y)
        # self.vel += self.acc - self.fric
        self.pos += self.vel

    def update(self):
        self.anim_aero()
        self.move_aero()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self, bullets)
        self.x = x
        self.y = y
        self.image = bullet_image
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.pos = vec(self.x, self.y)
        self.acc = vec(0, 0.5)
        self.vel = (0, 0)
        self.last_update = pygame.time.get_ticks()


# Define some colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()

# Set the WIDTH and the HEIGHT for the screen
os.environ['SDL_VIDEO_WINDOW_POS'] = '20,50'
WIDTH = 1200
HEIGHT = 700
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size, pygame.HWSURFACE | pygame.DOUBLEBUF)
pygame.display.set_caption('Template for Pygame Programs')

# Loop until the user clicks the close button
done = False

# Use how fast the screen updates
clock = pygame.time.Clock()

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
        girl_frame = sheet_g.subsurface((95 * column, 130 * row, 95, 130))
        # pos_girl = girl_frame.get_rect()
        # pos_girl.center = girl_x, girl_y
        girl_list.append(girl_frame)
list_0 = []
list_1 = []
list_2 = []
for i in range(len(girl_list)):
    if i % 3 == 0:
        list_0.append(girl_list[i])
    elif i % 3 == 1:
        list_1.append(girl_list[i])
    else:
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
        single_image = sheet.subsurface((64 * column, 64 * row, 64, 64))
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
    if j % 6 == 0:
        blist_0.append(ind_images[j])
    elif j % 6 == 1:
        blist_1.append(ind_images[j])
    elif j % 6 == 2:
        blist_2.append(ind_images[j])
    elif j % 6 == 3:
        blist_3.append(ind_images[j])
    elif j % 6 == 4:
        blist_4.append(ind_images[j])
    else:
        blist_5.append(ind_images[j])
ind_images = blist_0 + blist_1 + blist_2 + blist_3 + blist_4 + blist_5

# Create allsprites group for rendering each sprite through only one command allsprites.update()
allsprites = pygame.sprite.Group()

# Generate instances for each class , and add them to the allsprites
girl_dancing = AnimGirl(400, 400, girl_list)
allsprites.add(girl_dancing)
aero = Aerocam(200, 200, ind_images)
allsprites.add(aero)

# --------------Main Program Loop -------------
while not done:
    # ---Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(BckG, (0, 0))

    # --------Drawing code should go here
    # blit the gallows here

    # ---------Update thje screen with what we have drawn

    allsprites.update()
    pygame.display.flip()

    # ------Limit 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()