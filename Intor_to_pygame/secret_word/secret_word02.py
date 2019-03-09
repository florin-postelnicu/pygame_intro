
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
import pickle
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

# import pygame as pg


# pg.init()
# screen = pg.display.set_mode((640, 480))
# COLOR_INACTIVE = pg.Color('lightskyblue3')
# COLOR_ACTIVE = pg.Color('dodgerblue2')
# FONT = pg.font.Font(None, 32)


# class InputBox:

#     def __init__(self, x, y, w, h, text=''):
#         self.rect = pg.Rect(x, y, w, h)
#         self.color = COLOR_INACTIVE
#         self.text = text
#         self.txt_surface = FONT.render(text, True, self.color)
#         self.active = False

#     def handle_event(self, event):
#         if event.type == pg.MOUSEBUTTONDOWN:
#             # If the user clicked on the input_box rect.
#             if self.rect.collidepoint(event.pos):
#                 # Toggle the active variable.
#                 self.active = not self.active
#             else:
#                 self.active = False
#             # Change the current color of the input box.
#             self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
#         if event.type == pg.KEYDOWN:
#             if self.active:
#                 if event.key == pg.K_RETURN:
#                     print(self.text)
#                     self.text = ''
#                 elif event.key == pg.K_BACKSPACE:
#                     self.text = self.text[:-1]
#                 else:
#                     self.text += event.unicode
#                 # Re-render the text.
#                 self.txt_surface = FONT.render(self.text, True, self.color)

#     def update(self):
#         # Resize the box if the text is too long.
#         width = max(200, self.txt_surface.get_width()+10)
#         self.rect.w = width

#     def draw(self, screen):
#         # Blit the text.
#         screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
#         # Blit the rect.
#         pg.draw.rect(screen, self.color, self.rect, 2)



# def main():
#     clock = pg.time.Clock()
#     input_box1 = InputBox(100, 100, 140, 32)
#     input_box2 = InputBox(100, 300, 140, 32)
#     input_boxes = [input_box1, input_box2]
#     done = False

#     while not done:
#         for event in pg.event.get():
#             if event.type == pg.QUIT:
#                 done = True
#             for box in input_boxes:
#                 box.handle_event(event)

#         for box in input_boxes:
#             box.update()

#         screen.fill((30, 30, 30))
#         for box in input_boxes:
#             box.draw(screen)

#         pg.display.flip()
#         clock.tick(30)


# if __name__ == '__main__':
#     main()
#     pg.quit()



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


    def blinking (self):
        for event in pygame.event.get():
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

    def guess(self):



            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            if pos[0] >= 50 and pos[0] <= 700 and pos[1] >= 550 and pos[1] <= 650:
                # Change the x/y screen coordinates to grid coordinates
                column = (pos[0] - LETTER_BOX[0]) // WIDTH_LETTER_BOX
                row = (pos[1] - LETTER_BOX[1]) // HEIGHT_LETTER_BOX
                # self.table[row][column] is the data needed for  guess
                # self.guess = self.table[row][column]
                print((self.table[row][column]))

                return self.table[row][column]




    def update(self):
        self.blinking()
        self.guess()


class Player(object) :
    def __init__(self, name = None, battles= 0, victories = 0, game = None):
        self.game = game
        self.name = name
        self.battles = battles
        self.victories = victories

    def greetings(self):
        # self.get_warrior_infos()
        self.name = name_me()
        print(self.name)
        history = Player.get_warrior_infos(self)

        #  Check if the name is in the history.names
        # Use get_warrior_infos()

        if  self.name != None :
            print("YOUUUUU")
        elif self.name in history.keys():
            self.battles = history[self.name][0]
            self.victories = history[self.name][1]

        else:

            # No, call the Setters
            Player.set_warrior_infos(self)
            history[self.name] = (0,0)
            f1 = open('historydict,p', 'wb')
            pickle.dump(history, f1)
            f1.close()

            print("Sorry valiant warrior, but we don't believe in Fairy Tales, \n"
                  " however,  \n we want you to prove yourself and get into"
                  " our history book. Good Luck!")
            Player.update_warrior(self, vic=None)
        Player.print_stats(self)

        print("History book : \n", history)

    # Define Getters

    def get_warrior_infos(self):
        # Read the file "historydict", and return the dictionary history
        f1 = open('historydict,p', 'rb')
        history = pickle.load(f1)
        f1.close()
        return history

    # Define Setters For newbies
    def set_warrior_infos(self):
        print("What's your story {}  warrior? \n".format(self.name))
        self.battles =0
        int(input("Enter your skirmishes big warrior \n"))
        self.victories =0
        int(input("Enter the number of annihilated enemies \n"))

    def print_stats(self):
        print("Warrior ", self.name)
        print("Lots of battles ", self.battles)
        print("Lots of winning scars ", self.victories)

    def update_warrior(self, vic):
        history = Player.get_warrior_infos(self)
        if self.name in history.keys() and vic is not None:

            # Update victories
            if vic :
                self.victories += 1
                # Update battles
                self.battles += 1
            else:
                self.victories += 0
                # Update battles
                self.battles += 1

        history[self.name] = (self.battles, self.victories)
        f1 = open('historydict,p', 'wb')
        pickle.dump(history, f1)
        f1.close()
        Player.print_stats(self)

    def print_all_warriors(self):
        history = Player.get_warrior_infos(self)
        print(history)


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




BckG = Background('bkg.jpg', [0,0])
# --------------Main Program Loop -------------
while not done:

    # ---Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
             Grid.update(grid1)


    # Game Logic should go here


    # Screen clearing goes here

    # Here we clear the screen to white. Don't put other drawing commands
    #  above this , or they will be erased with this command

    # If you want a background image, replace this clear with

    screen.blit(BckG.image, BckG.rect)

    # --------Drawing code should go here
    # rect 0 is for practice
    rect0 = pygame.draw.rect(screen, YELLOW, [50, 100, 300, 100], 1)
    screen.blit(draw_text(Grid.guess(grid1), 30), [60, 120])
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

    # allsprites.update()
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
