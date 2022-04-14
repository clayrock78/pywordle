import pygame as pg
import pywordle.load_words as words

WIDTH = 360
HEIGHT = 480
FPS = 30

# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (200, 200, 200)

# initialize pygame and create window
pg.init()
#pg.mixer.init()  # For sound
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("PyWordle")

# create font
pg.font.init()
FONT = pg.font.SysFont('Comic Sans MS', 30)

clock = pg.time.Clock()     # For syncing the FPS

words_guessed = 0
previous_guesses = list()
current_guess = ""
word_to_guess = words.get_random_word()

def get_color(char:str, index:int) -> tuple[int, int, int]:
    if char not in word_to_guess: return GRAY
    if word_to_guess[index] == char: return GREEN
    return YELLOW

def draw_letter(x: int, y: int, letter:str) -> None:
    # get and draw the letter to the screen
    text_surface = FONT.render(letter, True, BLACK)
    xpos = x*68 + (44 - text_surface.get_width() / 2)
    ypos = y*68 + (44 - text_surface.get_height() / 2)
    screen.blit(text_surface, (xpos, ypos))

# Game loop
running = True
while running:
    for event in pg.event.get():        
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:

            if event.key == pg.K_BACKSPACE:
                if len(current_guess) >= 1:
                    current_guess = current_guess[:-1]
            elif event.key == pg.K_RETURN:
                if len(current_guess) == 5 and words.is_valid_word(current_guess):
                    previous_guesses.append(current_guess)
                    current_guess = ""
                    words_guessed += 1
            else:               
                try:
                    char = chr(event.key).upper()
                except ValueError: continue # character is not valid
                
                if len(current_guess) < 5:
                    current_guess += char

    #3 Draw/render
    screen.fill(BLACK)

    for y in range(6):
        for x in range(5):
            pg.draw.rect(screen, WHITE, (20+68*x, 20+y*68, 48, 48))

            if y == words_guessed:
                # center of box (x,y) is (x*48+44, y*48+44)
                if x >= len(current_guess): continue 
                letter = current_guess[x]
                draw_letter(x, y, letter)
            elif y < words_guessed:
                letter = previous_guesses[y][x]
                color = get_color(letter, x)
                pg.draw.rect(screen, color, (20+68*x, 20+y*68, 48, 48))               
                draw_letter(x, y, letter)


    # Done after drawing everything to the screen
    pg.display.flip()       

pg.quit()