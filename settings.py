# settings for the final project
import pygame as pg
vec = pg.math.Vector2

TITLE = "Bunny Hops"
# screen dims
WIDTH = 960
HEIGHT = 700
# frames per second
FPS = 60
# colors
WHITE = (255, 255, 255)
BLACK = (0,0,0)
REDDISH = (240,55,66)
SKY_BLUE = (143, 185, 252)
FONT_NAME = 'arial'
SPRITESHEET = "spritesheet_jumper.png"
SPRITESHEET2 = "spritesheet.png"
# data files
HS_FILE = "highscore.txt"
# player settings
PLAYER_ACC = 0.3
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 20
# game settings
BOOST_POWER = 60
POW_SPAWN_PCT = 3
SPEED_SPAWN_PCT = 3
MOB_FREQ = 3
# layers - uses numerical value in layered sprites
PLAYER_LAYER = 2
PLATFORM_LAYER = 1
POW_LAYER = 1
MOB_LAYER = 2
CLOUD_LAYER = 0

BARREL_OFFSET = vec(30, 10)
# gun settings
BULLET_IMG = 'cloud1.png'
BULLET_SPEED = 500
BULLET_LIFETIME = 1000
BULLET_RATE = 150
KICKBACK = 200
GUN_SPREAD = 5
BULLET_DAMAGE = 10

# platform settings
''' old platforms from drawing rectangles'''
'''
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40),
                 (65, HEIGHT - 300, WIDTH-400, 40),
                 (20, HEIGHT - 350, WIDTH-300, 40),
                 (200, HEIGHT - 150, WIDTH-350, 40),
                 (200, HEIGHT - 450, WIDTH-350, 40)]
'''
PLATFORM_LIST = [(0, HEIGHT - 450),
                 (50, HEIGHT - 800),
                 (100, HEIGHT - 700),
                 (150, HEIGHT - 600),
                 (200, HEIGHT - 500),
                 (250, HEIGHT - 400),
                 (300, HEIGHT - 300),
                 (350, HEIGHT - 200),
                 (400, HEIGHT - 100),
                 (450, HEIGHT - 50),
                 (500, HEIGHT - 800),
                 (550, HEIGHT - 700),
                 (600, HEIGHT - 600),
                 (650, HEIGHT - 500),
                 (700, HEIGHT - 400),
                 (750, HEIGHT - 300),
                 (800, HEIGHT - 200),
                 (900, HEIGHT - 100),
                 (900, HEIGHT - 500),
                 (900, HEIGHT - 450)]
