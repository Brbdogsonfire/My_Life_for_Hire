from settings import *
import pygame as pg
import math
from main import *
from settings import *
from map import *



class Player:
    def __init__(self,game):
               
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.delta_time = 1
 

    #math for movement
    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx = 0 
        dy = 0
        speed = PLAYER_SPEED * self.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a


        # player controls
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos

        #collision with walls, A B
        self.check_wall_collision(dx,dy)

        if keys[pg.K_q]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pg.K_e]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau

    #collision with wall detection
    def check_wall(self,x,y):
        return (x,y) not in self.game.map.world_map
    
    def check_wall_collision(self,dx,dy):
        scale = PLAYER_SIZE_SCALE / self.game.delta_time
        if self.check_wall(int(self.x + dx * scale), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * scale)):
            self.y += dy

#mouse controls, rel is angle of mouse from center and adjusts based on that angel
    def mouse_control(self):
        mx, my = pg.mouse.get_pos()
        if mx < MOUSE_BORDER_LEFT or mx > MOUSE_BORDER_RIGHT:
            pg.mouse.set_pos([HALF_WIDTH, HALF_HEIGHT])
        self.rel = pg.mouse.get_rel()[0]
        self.rel = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, self.rel))
        self.angle += self.rel * MOUSE_SENSITIVITY * self.game.delta_time


    #draw
    def draw(self):
        # pg.draw.line(self.game.screen, 'yellow', (self.x * 100, self.y *100), (self.x * 100 + WIDTH * math.cos(self.angle), self.y * 100 + WIDTH * math.sin(self.angle)), 2)
        pg.draw.circle(self.game.screen, 'green', (self.x * 100, self.y *100), 15)
 
    #movement updating
    def update(self):
        self.movement()
        self.mouse_control()

    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def map_pos(self):
        return int(self.x), int(self.y)
    