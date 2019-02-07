'''
The text in draw_text(text) should be string or bites.
If a message has numerical characters,
than it should be converted to a string
 str(message)

 For pygame.draw check :
 https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect
 
pygame.draw.rect()
draw a rectangle shape

rect(Surface, color, Rect, width=0) -> Rect

Draws a rectangular shape on the Surface. The given Rect is the area of the rectangle. 
The width argument is the thickness to draw the outer edge. If width is zero then the rectangle will be filled.

Keep in mind the Surface.fill() method works just as well for drawing filled rectangles. 
In fact the Surface.fill() can be hardware accelerated on some platforms with both software and hardware display modes.
'''
import pygame
import os
import datetime

# Define some colors


def draw_text(text):
    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 25, True, False)
    # Render the text. "True" means anti-aliased text.
    # Black is the color. This creates an image of the
    # letters, but does not put it on the screen
    text_new = font.render(text, True, RED)
    return text_new

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

#--------------Main Program Loop -------------
while not done:
    #---Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Game Logic should go here
    something = datetime.datetime.now()
    something.strftime("%Y-%m-%d  %H:%M:%S")



    # Screen clearing goes here

    #Here we clear the screen to white. Don't put other drawing commands
    #  above this , or they will be erased with this command

    #If you want a background image, replace this clear with
    # blit' ing the background image.
    screen.fill(WHITE)

    #--------Drawing code should go here
    pygame.draw.rect(screen, YELLOW, [200,200, 400, 100],0)

    #---------Update thje screen with what we have drawn
    # ---------Put the image of the text on the screen at 250 x250

    screen.blit(draw_text(str(something)), [250, 250])
    pygame.display.flip()

    #------Limit 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()


