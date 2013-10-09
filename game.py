import core
import pyglet
from pyglet.window import key
from core import GameElement
import sys
from random import *

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

class Acquireable(GameElement):
    def interact(self, player):
        player.inventory.append(self)
        player.points += 10
        GAME_BOARD.draw_msg("You just acquired an object! You have %d items and %d points!" % (len(player.inventory), player.points))

class Goblet(Acquireable):
    IMAGE = "Goblet"
    SOLID = False
    def interact(self, player):
        player.inventory.append(self)
        player.points += 100
        GAME_BOARD.draw_msg("Congratulations, Harry!!! You have won the Tri-Wizard Tournament with %d items and %d points!" % (len(player.inventory), player.points))

class Cauldron(Acquireable):
    IMAGE = "Cauldron"
    SOLID = False    

class Broom(Acquireable):
    IMAGE = "Broom"
    SOLID = False

class Snitch(Acquireable):
    IMAGE = "Snitch"
    SOLID = False

class SortingHat(Acquireable):
    IMAGE = "SortingHat"
    SOLID = False

class Glasses(Acquireable):
    IMAGE = "Glasses"
    SOLID = False        

class Books(Acquireable):
    IMAGE = "Books"
    SOLID = False

class Hedwig(Acquireable):
    IMAGE = "Hedwig"
    SOLID = False 


class Character(GameElement):
    IMAGE = "Harry"
    
    def __init__(self):
        GameElement.__init__(self)
        self.inventory = []
        self.points = 0
        self.reversed = 0

    def next_pos(self, direction):
        if self.reversed > 0:
            self.reversed -= 1
            if direction == "up":
                if self.y + 1 == 0:
                    return (self.x, self.y)
                else: 
                    return (self.x, self.y + 1)
            elif direction == "down":
                if self.y - 2 == GAME_HEIGHT:
                    return (self.x, self.y)
                else:
                    return (self.x, self.y - 1)
            elif direction == "left":
                if self.x + 1 == 0:
                    return (self.x, self.y)
                else:
                    return (self.x + 1, self.y)
            elif direction == "right":
                if self.x - 2 == GAME_WIDTH:
                    return (self.x, self.y)
                else:
                    return (self.x - 1, self.y)
        else:
            if direction == "up":
                if self.y - 1 == 0:
                    return (self.x, self.y)
                else: 
                    return (self.x, self.y - 1)
            elif direction == "down":
                if self.y + 2 == GAME_HEIGHT:
                    return (self.x, self.y)
                else:
                    return (self.x, self.y + 1)
            elif direction == "left":
                if self.x - 1 == 0:
                    return (self.x, self.y)
                else:
                    return (self.x - 1, self.y)
            elif direction == "right":
                if self.x + 2 == GAME_WIDTH:
                    return (self.x, self.y)
                else:
                    return (self.x + 1, self.y)
        return None

class Mist(GameElement):
    IMAGE = "Mist"
    def interact(self, player):
        player.reversed = 5
        GAME_BOARD.draw_msg("You have entered a magical mist!")

class Dementor(GameElement):
    IMAGE = "Dementor"

    def __init__(self):
        GameElement.__init__(self)
        self.x = 5
        self.y = 5
        self.elapsed_time = 0

    def update(self, dt):
        self.elapsed_time += dt
        #print self.elapsed_time

        if self.elapsed_time > 0.5:
            GAME_BOARD.del_el(self.x, self.y)

            direction_options = ["up", "down", "left", "right"]
            direction = choice(direction_options)
            
            next_x = self.x
            next_y = self.y

            if direction == "up":
                next_x = self.x
                if self.y - 1 == 0:
                    next_y = self.y
                else:
                    next_y = self.y - 1
            elif direction == "down":
                next_x = self.x 
                if self.y + 2 == GAME_HEIGHT:
                    next_y = self.y
                else:
                    next_y = self.y + 1                
            elif direction == "left":
                if self.x - 1 == 0:
                    next_x = self.x
                else:
                    next_x = self.x - 1      
                next_y = self.y
            elif direction == "right":
                if self.x + 2 == GAME_WIDTH:
                    next_x = self.x
                else:
                    next_x = self.x + 1              
                next_y = self.y        
            
            existing_el = GAME_BOARD.get_el(next_x, next_y)

            if existing_el:
                next_x = self.x
                next_y = self.y
                GAME_BOARD.set_el(next_x, next_y, self)
            else:
                GAME_BOARD.set_el(next_x, next_y, self)

            self.elapsed_time = 0

    def interact(self,player):
        player.points -= 50
        GAME_BOARD.draw_msg("You have been attacked by a dementor! You now have %d points!" % (player.points))

#####   End class definitions    ####

def initialize():
    """Put game initialization code here"""
    dementor_position = [
        (1, 1),
        (5, 5)
    ]

    dementors = []

    for pos in dementor_position:
        dementor = Dementor()
        GAME_BOARD.register(dementor)
        GAME_BOARD.set_el(pos[0], pos[1], dementor)
        dementors.append(dementor)

    #hedges[-1].SOLID = False

    #for hedge in hedges:
    #    print hedge

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

    #hedges[-1].SOLID = False

    for hedge in hedges:
        print hedge

    global PLAYER
    PLAYER = Character()
    GAME_BOARD.register(PLAYER)
    GAME_BOARD.set_el(10, 1, PLAYER)
    print PLAYER

    # global DEMENTOR
    # DEMENTOR = Dementor()
    # GAME_BOARD.register(DEMENTOR)
    # GAME_BOARD.set_el(5, 5, DEMENTOR)
    # print DEMENTOR

    GAME_BOARD.draw_msg("Harry, get the Tri-Wizard Cup!")
    # GAME_BOARD.erase_msg()

    books = Books()
    GAME_BOARD.register(books)
    GAME_BOARD.set_el(3, 2, books)

    cauldron = Cauldron()
    GAME_BOARD.register(cauldron)
    GAME_BOARD.set_el(6, 6, cauldron)

    broom = Broom()
    GAME_BOARD.register(broom)
    GAME_BOARD.set_el(8, 2, broom)

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

    hedwig = Hedwig()
    GAME_BOARD.register(hedwig)
    GAME_BOARD.set_el(10, 4, hedwig)

    mist = Mist()
    GAME_BOARD.register(mist)
    GAME_BOARD.set_el(4, 3 , mist)


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
