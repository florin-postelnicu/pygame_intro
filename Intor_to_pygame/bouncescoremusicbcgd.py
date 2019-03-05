"""
 Bounces a rectangle around the screen.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/-GmKoaX2iMs
"""

import pygame

import time

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()

pygame.mixer.init()

hit_sound = pygame.mixer.Sound("Music for Ping\\boom.wav")
song = pygame.mixer.music.load("Music for Ping\\red alert.wav")

# Play the music throughout the game

pygame.mixer.music.play(-1)
#Load background image


# define the sound function for the collision
def boom():
    pygame.mixer.music.pause()# This stops the music when boom() activated
    time.sleep(0.05)
    pygame.mixer.Sound.play(hit_sound)# the sound at the collision
    pygame.mixer.music.unpause()# restart the music



# Draw the table score
# Choose the type of font, or alike
font_name = pygame.font.match_font('arial')

# define a function to draw the score
''' where:
 surf = the surface on which the text would be drawn (screen in our program)
 text = is the text displayed
 color = is the color of the font
 size = is the size of the font
 x, y are the coordinates of the midtop of the rectangle wrapped around the text
 text_rect = the rectangle wrapped around the text
'''

def draw_text(surf, text,color,  size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


#all_sprites = pygame.sprite.group



# Set the height and width of the screen
size = [700, 500]
screen = pygame.display.set_mode(size)
background = pygame.image.load("Imagesp\\bcgd.jpg").convert()

pygame.display.set_caption("Bouncing Rectangle")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Starting position of the rectangle
rect_x = 50
rect_y = 50
pallet1_y = 200
pallet1_y_change = 0

score = 0
score_change = 0
# Speed and direction of rectangle
rect_change_x = 2
rect_change_y = 2

# background var initialized
x_bkg = 0
# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            # if the event.type is KEYDOWN check which keys
            # are used for moving the paddle
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pallet1_y_change = -2
            if event.key == pygame.K_DOWN:
                pallet1_y_change = 2
            if event.key == pygame.K_SPACE:
                score = 0
            # if event.type is KEYUP put the conditions for
            # the corresponding keys which are not pressed any longer
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_SPACE:
                pallet1_y_change = 0

    # --- Logic
    # Move the rectangle starting point
    rect_x += rect_change_x
    rect_y += rect_change_y


    # Move the paddle

    pallet1_y += pallet1_y_change



    # Update
   # all_sprites.update()

    pallet1_y += pallet1_y_change

    score += score_change


    # --- Drawing
    # Set the screen background
    # screen.fill(BLACK)
    rel_x = x_bkg % background.get_rect().w
    screen.blit(background, (rel_x - background.get_rect().w , 0))
    x_bkg -= 1
    if rel_x < 700:
        screen.blit(background, (rel_x, 0))




    # Draw the rectangle

    #all_sprites.draw(screen)
    ball = pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])
    pygame.draw.rect(screen, RED, [rect_x + 10, rect_y + 10, 30, 30])

    pallet1 = pygame.draw.rect(screen, GREEN, (0, pallet1_y, 20, 100))

    # Draw the Table score
    pygame.draw.rect(screen, WHITE, (500, 0, 200, 500))

    draw_text(screen, "Scoring Board ", RED, 30, 600, 100)

    draw_text(screen, "Player1 Score = " + str(score), BLUE, 24, 600, 400)

    # Bounce the ball if needed

    # Establish how the score for Player1 is set
    # it is necessary to have nested if's ,
    # otherwise not all the conditions are resulting in
    # the result you wish
    if rect_x < 0:
        score_change = -1

    elif pallet1.colliderect(ball):
        score_change = 1
        boom()


    else:
        score_change = 0



    # the condition for the ball to bounce
    if rect_y > 450 or rect_y < 0:
        rect_change_y = rect_change_y * -1
    if rect_x > 450 or rect_x < 0 or ball.colliderect(pallet1):
        rect_change_x = rect_change_x * -1





    # --- Wrap-up
    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Close everything down
pygame.quit()