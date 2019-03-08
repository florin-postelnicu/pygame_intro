'''
The areo shoots in the direction of displacement.
If still, the aero shoots vertically.
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
        self.last_update = pygame.time.get_ticks()

    def anim_aero(self):

        now = pygame.time.get_ticks()
        screen.blit(ind_images[self.frame], self.pos)
        if now - self.last_update > 100:
            self.frame = (self.frame + 1) % (len(ind_images))
            self.last_update = now

    def move_aero(self ):
        self.aero_change_y = 0
        self.aero_change_x = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.aero_change_x -= 20
        if keys[pygame.K_RIGHT]:
            self.aero_change_x += 20
        if keys[pygame.K_DOWN]:
            self.aero_change_y += 20
        if keys[pygame.K_UP]:
            self.aero_change_y -= 20

        if keys[pygame.K_SPACE]:
            self.aero_change_y *= 2
             self.aero_change_x *= 2
            self.shoot()
        if self.x < 0 or self.x > WIDTH:
            self.aero_change_x *= -1
        if self.y < 0 or self.y > HEIGHT:
            self.aero_change_y *= -1

        self.x += self.aero_change_x
        self.y += self.aero_change_y
        self.rect.center = (self.x, self.y)
        self.velo = (self.aero_change_x, self.aero_change_y)
        self.pos += self.velo

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top, self.velo)
        allsprites.add(bullet)
        bullets.add(bullet)
        print(self.velo)

    def update(self):
        self.anim_aero()
        self.move_aero()



class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, vel):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.top = y + 32
        self.rect.centerx = x + 32
        self.pos = vec(self.rect.x, self.rect.y)
        self.bullet_clock = pygame.time.get_ticks()
        self.vel = vel

    def update(self):

        now = pygame.time.get_ticks()
        if now - self.bullet_clock > 50:
            if self.vel == vec(0, 0):
                self.vel = vec(0, -30)
            self.pos += vec(self.vel )
            screen.blit(self.image, self.pos)
            self.bullet_clock = now
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0: # out of the screen's frame
            self.kill()
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
pygame.display.set_caption('Firing Aero')

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

for column in range(7):
    for row in range(3):
        girl_frame = sheet_g.subsurface((95 * column, 130 * row, 95, 130))
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
for column in range(9):
    for row in range(6):
        single_image = sheet.subsurface((64 * column, 64 * row, 64, 64))
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
bullets = pygame.sprite.Group()
allsprites.add(aero)

# --------------Main Program Loop -------------
while not done:
    # ---Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(BckG, (0, 0))

    # --------Drawing code should go here


    # ---------Update the screen with what we have drawn

    allsprites.update()
    pygame.display.flip()

    # ------Limit 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
