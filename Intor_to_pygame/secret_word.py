'''
The text in draw_text(text) should be string or bites.
If a message has numerical characters,
than it should be converted to a string
 str(message)
 For pygame.draw check :
 https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect
'''
import pygame
import os
from hangman_list import text_w
import random




def draw_text(text, font_size):
    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Times New Roman', font_size, True, False)
    # Render the text. "True" means anti-aliased text.
    # Black is the color. This creates an image of the
    # letters, but does not put it on the screen
    text_new = font.render(text, True, RED)
    return text_new
# Classes



class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # Call Sprite Initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Gallows(pygame.sprite.Sprite):
    def __init__(self, image_file,  location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file).convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class Grid(pygame.sprite.Sprite):
    global LETTER_BOX, WIDTH_LETTER_BOX, HEIGHT_LETTER_BOX, LETTERS
    LETTER_BOX = (50, 550)
    WIDTH_LETTER_BOX = 50
    HEIGHT_LETTER_BOX = 50
    LETTERS = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'],
               ['N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']]
    def __init__(self, ):
        pygame.sprite.Sprite.__init__(self)
        self.table = []
        for row in range(2):
            # Add an empty array that will hold each cell
            # in this row
            self.table.append([])
            for column in range(13):
                self.table[row].append(LETTERS[row][column])  # Append a cell
    # @staticmethod
    def blinking (self):
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            if pos[0] >= 50 and pos[0] <= 700 and pos[1] >= 550 and pos[1] <= 650:
                columny = (pos[0] - LETTER_BOX[0]) // WIDTH_LETTER_BOX
                rowx = (pos[1] - LETTER_BOX[1]) // HEIGHT_LETTER_BOX
                pygame.draw.rect(screen, (255,25,255, 70), [50 + 50 * columny, 550 + 50 * rowx, 50,50], 8)


    def drawgrid(self):
        for row in range(2):
            for column in range(13):
                screen.blit(draw_text(self.table[row][column], 50), [50 + 50 * column, 550 + 50 * row])

    def update(self):
        self.blinking()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            if pos[0] >= 50 and pos[0] <= 700 and pos[1] >= 550 and pos[1] <= 650:
                # Change the x/y screen coordinates to grid coordinates
                column = (pos[0] - LETTER_BOX[0]) // WIDTH_LETTER_BOX
                row = (pos[1] - LETTER_BOX[1]) // HEIGHT_LETTER_BOX
                # # Set that location to one
                # grid[row][column] = 1
                print("Click ", pos, "Grid coordinates: ", row, column, 'letter is ', self.table[row][column])


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


index = random.randint(0, len(text_w)-1)
word = text_w[index]
pygame.init()

# Set the WIDTH and the HEIGHT for the screen
os.environ['SDL_VIDEO_WINDOW_POS'] = '20,50'
WIDTH = 1200
HEIGHT = 700
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Secret Word')

done = False
# Use how fast the screen updates
clock = pygame.time.Clock()
allsprites = pygame.sprite.Group()
grid1 = Grid()
allsprites.add(grid1)

BckG = Background('bkg.jpg', [0,0])
# --------------Main Program Loop -------------
while not done:

    # ---Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        else :
             Grid.update(grid1)


    # Game Logic should go here


    # Screen clearing goes here

    # Here we clear the screen to white. Don't put other drawing commands
    #  above this , or they will be erased with this command

    # If you want a background image, replace this clear with
    
    screen.blit(BckG.image, BckG.rect)

    # --------Drawing code should go here
    # rect1 is for the secret word

    rect1 = pygame.draw.rect(screen, YELLOW, [50, 400, 50*(len(word)-1), 100], 3)
    # rect 2 is LETTER_BOX
    rect2 = pygame.draw.rect(screen, YELLOW, [LETTER_BOX[0],LETTER_BOX[1], 13*WIDTH_LETTER_BOX, 2*HEIGHT_LETTER_BOX], 3)

    # ---------Update the screen with what we have drawn
    # ---------Put the image of the text on the screen at 220 x220

    screen.blit(draw_text(str(word.upper()), 50), [60, 420])

    # Draw each letter of the alphabet on the corresponding location
    Grid.blinking(grid1)
    Grid.drawgrid(grid1)
    # for row in range(2):
    #     for column in range(13):
    #         # blinking()
    #         screen.blit(draw_text(grid[row][column], 50), [50 + 50 * column, 550 + 50 * row])

    allsprites.update()
    # screen.fill(BLACK)
    # ------Limit 60 frames per second
    clock.tick(60)
    pygame.event.pump()
    # Go ahead and update the screen with what we've drawn.
    # if the classes have attributes images , then allsprites.draw()
    # allsprites.draw(screen)



    pygame.display.flip()



    # Close the window and quit.
pygame.quit()