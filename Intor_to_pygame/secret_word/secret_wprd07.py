'''
Version 7
Try to work with game class fully
'''
import pygame
import os
import pickle
from hangman_list import text_w
import random


#
# history = {'Anonymous': (0,0)}
# f1 = open('historydict,p', 'wb')
# pickle.dump(history, f1)
# f1.close()
def generate_random_word(text_w):
    index = random.randint(0, len(text_w)-1)
    word = text_w[index]
    return word
    # word = text_w[index]

def gallows(penal):
    if penal == 0:
        gal = "---------I \n" \
              "         I \n" \
              "         I \n" \
              "         I \n" \
              "         I \n" \
              "         I \n" \
              "        / \  \n" \
              "       /   \  \n" \
              "      ====  \n"
    if penal == 1:
        gal = "---------I \n" \
              "  I      I \n" \
              " O      I \n" \
              "         I \n" \
              "         I \n" \
              "         I \n" \
              "        / \  \n" \
              "       /   \  \n" \
              "      ====  \n"
    if penal == 2:
        gal = "---------I \n" \
              "         I \n" \
              "         I \n" \
              "         I \n" \
              "   2    I \n" \
              "         I \n" \
              "        / \  \n" \
              "       /   \  \n" \
              "      ====  \n"

    if penal == 3:
        gal = "---------I \n" \
              "         I \n" \
              "         I \n" \
              "         I \n" \
              "   3    I \n" \
              "         I \n" \
              "        / \  \n" \
              "       /   \  \n" \
              "      ====  \n"
    if penal == 4:
        gal = "---------I \n" \
              "         I \n" \
              "         I \n" \
              "         I \n" \
              "   4    I \n" \
              "         I \n" \
              "        / \  \n" \
              "       /   \  \n" \
              "      ====  \n"
    if penal == 5:
        gal = "---------I \n" \
              "         I \n" \
              "         I \n" \
              "         I \n" \
              "   5    I \n" \
              "         I \n" \
              "        / \  \n" \
              "       /   \  \n" \
              "      ====  \n"
    if penal == 6:
        gal = "---------I \n" \
              "         I \n" \
              "         I \n" \
              "         I \n" \
              "   6    I \n" \
              "         I \n" \
              "        / \  \n" \
              "       /   \  \n" \
              "      ====  \n"
    if penal == 7:
        gal = "---------I \n" \
              "         I \n" \
              "         I \n" \
              "         I \n" \
              "   7    I \n" \
              "         I \n" \
              "        / \  \n" \
              "       /   \  \n" \
              "      ====  \n"
    return gal


def draw_text(text, font_size):
    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Times New Roman', font_size, True, False)
    # Render the text. "True" means anti-aliased text.
    # Black is the color. This creates an image of the
    # letters, but does not put it on the screen
    text_new = font.render(text, True, RED)
    return text_new


# Classes


class InputBox(object):

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)

        self.color = COLOR_ACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.player = Player()
                    self.player.name = self.text
                    self.player.greetings()
                    self.player.play_the_game()
                    return self.text
                    # game1 = Game(self.player.name, self.player.battles, self.player.victories)
                    # self.player.update_warrior( True)


                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # Call Sprite Initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class Gallows(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file).convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class Grid(pygame.sprite.Sprite):
    # pygame.init()
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

    def blinking(self):

        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            if pos[0] >= 50 and pos[0] <= 700 and pos[1] >= 550 and pos[1] <= 650:
                columny = (pos[0] - LETTER_BOX[0]) // WIDTH_LETTER_BOX
                rowx = (pos[1] - LETTER_BOX[1]) // HEIGHT_LETTER_BOX
                pygame.draw.rect(screen, (255, 25, 255, 70), [50 + 50 * columny, 550 + 50 * rowx, 50, 50], 8)

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


class Player(object):

    def __init__(self, name=None, battles=0, victories=0 ):
        self.name = name
        self.battles = battles
        self.victories = victories




    def word_on_display(self):
        self.word = generate_random_word(text_w)
        print(self.word)
        return self.word


    def play_the_game(self):
        again = 'y'
        while again == 'y':

            # Chose a random word from the text_w
            # generate_word()
            #
            # index = random.randint(0, len(text_w))
            # word = text_w[index]

            self.secret_word = list(Player.word_on_display())
            print(self.secret_word)
            # self.s_w = ''.join(secret_word)
            # screen.blit(draw_text(str(self.s_w.upper()), 50), [60, 420])

            new_word = ['*' for i in range(len(self.secret_word))]
            print(new_word)
            penalty = 0
            letters_used = []
            while '*' in new_word and penalty < 7:

                guess = input('Enter a letter  \n')
                if guess not in self.secret_word or guess in letters_used:
                    penalty += 1
                else:
                    for i in range(len(self.secret_word)):
                        if guess == self.secret_word[i]:
                            new_word[i] = self.secret_word[i]
                letters_used.append(guess)
                print(letters_used)
                print('penalty ', penalty)  # Here will be placed the gallows call
                print(gallows(penalty))
                print(new_word)
                # return secret_word, new_word, penalty

            print('The End')
            if penalty < 7:
                wiky = True
            else:
                wiky = False
            Player.update_warrior(self, wiky)
            again = input('Enter y if you want to play another game, else enter n \n')


        print("Good by, See you again!")
        Game.game_over(self)

    def greetings(self):
        Player.get_warrior_infos(self)
        print('from the class Player', self.name)
        history = Player.get_warrior_infos(self)

        if self.name in history.keys():
            self.battles = history[self.name][0]
            self.victories = history[self.name][1]

        else:

            # No, call the Setters
            Player.set_warrior_infos(self)
            history[self.name] = (0, 0)
            f1 = open('historydict,p', 'wb')
            pickle.dump(history, f1)
            f1.close()
            Player.update_warrior(self, vic=None)

        print("History book : \n", history)

    # Define Getters

    def get_warrior_infos(self):
        f1 = open('historydict,p', 'rb')
        history = pickle.load(f1)
        f1.close()
        return history

    def set_warrior_infos(self):
        self.battles = 0
        self.victories = 0

    def print_stats(self):
        print("Warrior ", self.name)
        print("Lots of battles ", self.battles)
        print("Lots of winning scars ", self.victories)

    def update_warrior(self, vic):
        history = Player.get_warrior_infos(self)
        if self.name in history.keys() and vic is not None:

            # Update victories
            if vic:
                self.victories += 1
                # Update battles
                self.battles += 1
            else:
                self.victories += 0
                # Update battles
                self.battles += 1

        print('before dumping', history)
        history[self.name] = (self.battles, self.victories)
        f1 = open('historydict,p', 'wb')
        pickle.dump(history, f1)
        f1.close()
        Player.print_stats(self)
        Player.print_all_warriors(self)



    def print_all_warriors(self):
        history = Player.get_warrior_infos(self)
        print(history)



class Game(object):
    def __init__(self, name, battles, victories):
        self.name = name
        self.battles = battles
        self.victories = victories

        print('From Game class name is  ', self.name)

    def game_over(self):
        print('This is after game_over \n the game is over')




# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')

index = random.randint(0, len(text_w) - 1)
word = text_w[index]
pygame.init()
FONT = pygame.font.Font(None, 32)
# Set the WIDTH and the HEIGHT for the screen
os.environ['SDL_VIDEO_WINDOW_POS'] = '20,50'
WIDTH = 1200
HEIGHT = 700
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Secret Word 02')
# word_on_display = generate_random_word(text_w)
done = False
# Use how fast the screen updates
clock = pygame.time.Clock()
# player1 = Player()

input_box1 = InputBox(50, 100, 140, 32)
input_box2 = InputBox(100, 300, 140, 32)
input_boxes = [input_box1, input_box2]
allsprites = pygame.sprite.Group()
grid1 = Grid()

bg = os.path.join('images', 'bkg.jpg')
BckG = Background( bg , [0, 0])
# --------------Main Program Loop -------------
while not done:

    # ---Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:

            # Player.greetings(player1)
            Grid.update(grid1)
            pos = pygame.mouse.get_pos()
            if pos[0] > 600 and pos[0] < 800 and pos[1] >200 and pos[1] < 300:
                player = Player()




        # Game Logic should go here
        input_box1.handle_event(event)

    input_box1.update()
    # Screen clearing goes here

    # Here we clear the screen to white. Don't put other drawing commands
    #  above this , or they will be erased with this command

    screen.blit(BckG.image, BckG.rect)

    # --------Drawing code should go here
    input_box1.draw(screen)

    # rect0 is for mouse control over the game Y/N
    rect0 = pygame.draw.rect(screen, GREEN, (600, 200, 200,100), 1)

    # rect1 is for the secret word

    rect1 = pygame.draw.rect(screen, YELLOW, [50, 400, 50 * (len(word) - 1), 100], 3)
    # rect 2 is LETTER_BOX
    rect2 = pygame.draw.rect(screen, YELLOW,
                             [LETTER_BOX[0], LETTER_BOX[1], 13 * WIDTH_LETTER_BOX, 2 * HEIGHT_LETTER_BOX], 3)

    # ---------Update the screen with what we have drawn
    # ---------Put the image of the text on the screen at 220 x220

    screen.blit(draw_text(str(Player.word_on_display(Player).upper()), 50), [60, 420])

    # Draw each letter of the alphabet on the corresponding location

    Grid.drawgrid(grid1)
    Grid.blinking(grid1)

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
