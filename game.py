import core
import pyglet
from pyglet.window import key
from core import GameElement
import sys

#### DO NOT TOUCH ####
GAME_BOARD = None
DEBUG = False
KEYBOARD = None
PLAYER = None
######################

GAME_WIDTH = 12
GAME_HEIGHT = 10

#### Put class definitions here ####
class Hedge(GameElement):
    IMAGE = "GrassBlock"
    SOLID = True

class Goblet(GameElement):
    IMAGE = "Goblet"
    SOLID = False

class Cauldron(GameElement):
    IMAGE = "Cauldron"
    SOLID = False    

class Broom(GameElement):
    IMAGE = "Broom"
    SOLID = False

class Snitch(GameElement):
    IMAGE = "Snitch"
    SOLID = False

class SortingHat(GameElement):
    IMAGE = "SortingHat"
    SOLID = False

class Glasses(GameElement):
    IMAGE = "Glasses"
    SOLID = False        

class Books(GameElement):
    IMAGE = "Books"
    SOLID = False        

class Gem(GameElement):
    IMAGE = "BlueGem"
    SOLID = False

    def interact(self, player):
        player.inventory.append(self)
        
        GAME_BOARD.draw_msg("You just acquired a gem! You have %d items!" % (len(player.inventory)))

class Character(GameElement):
    IMAGE = "Harry"

    def __init__(self):
        GameElement.__init__(self)
        self.inventory = []
        self.points = []

    def next_pos(self, direction):
        if direction == "up":
            return (self.x, self.y-1)
        elif direction == "down":
            return (self.x, self.y+1)
        elif direction == "left":
            return (self.x-1, self.y)
        elif direction == "right":
            return (self.x+1, self.y)
        return None

####   End class definitions    ####

def initialize():
    """Put game initialization code here"""

    hedge_positions = [
        (2, 2),
        (2, 3),
        (2, 5),
        (2, 6),
        (2, 7),
        (2, 8),
        (3, 5),
        (4, 2),
        (4, 4),
        (4, 5),
        (4, 6),
        (4, 7),
        (5, 2),
        (5, 7),
        (6, 2),
        (6, 4),
        (7, 2),
        (7, 4),
        (7, 5), 
        (7, 6),
        (7, 7),
        (7, 8),
        (9, 1),
        (9, 2),
        (9, 3),
        (9, 4),
        (9, 5),
        (9, 6),
        (9, 7)
    ]

    hedges = []

    for pos in hedge_positions:
        hedge = Hedge()
        GAME_BOARD.register(hedge)
        GAME_BOARD.set_el(pos[0], pos[1], hedge)
        hedges.append(hedge)

    #hedges[-1].SOLID = True

    for hedge in hedges:
        print hedge

    global PLAYER
    PLAYER = Character()
    GAME_BOARD.register(PLAYER)
    GAME_BOARD.set_el(10, 1, PLAYER)
    print PLAYER

    GAME_BOARD.draw_msg("This game is wicked awesome.")
    # GAME_BOARD.erase_msg()

    books = Books()
    GAME_BOARD.register(books)
    GAME_BOARD.set_el(3, 2, books)

    cauldron = Cauldron()
    GAME_BOARD.register(cauldron)
    GAME_BOARD.set_el(6, 6, cauldron)

    broom = Broom()
    GAME_BOARD.register(broom)
    GAME_BOARD.set_el(6, 1, broom)

    snitch = Snitch()
    GAME_BOARD.register(snitch)
    GAME_BOARD.set_el(3, 6, snitch)

    sortinghat = SortingHat()
    GAME_BOARD.register(sortinghat)
    GAME_BOARD.set_el(6, 3, sortinghat)

    glasses = Glasses()
    GAME_BOARD.register(glasses)
    GAME_BOARD.set_el(8, 8, glasses)

    goblet = Goblet()
    GAME_BOARD.register(goblet)
    GAME_BOARD.set_el(1, 8, goblet)


def keyboard_handler():
    direction = None

    if KEYBOARD[key.UP]:
        direction = "up"
    if KEYBOARD[key.DOWN]:
        direction = "down"
    if KEYBOARD[key.LEFT]:
        direction = "left"
    if KEYBOARD[key.RIGHT]:
        direction = "right"

    if direction:
        next_location = PLAYER.next_pos(direction)
        next_x = next_location[0]
        next_y = next_location[1]

        existing_el = GAME_BOARD.get_el(next_x, next_y)

        if existing_el:
            existing_el.interact(PLAYER)

        if existing_el is None or not existing_el.SOLID:
        #If there's nothing there _or_ if the existing element isnt solid, then walk through        
            GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
            GAME_BOARD.set_el(next_x, next_y, PLAYER)