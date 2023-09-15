import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import *
from object_handler import *
from weapon import *
from sound import *
from pathfinding import *


# ideas for how to integrat gamestates - use video on game stats to produce a minimum of 4 states. 1 main, 2 level 1, 3 shop, 4 level 2. This will
# allow for in game store, level select, and a variety of enemies and help flush out the program. Pray that the job is still open and you have this week
# end to finish. job is at least 50% done and its all polish now. Get this job. Follow your dreams even if you thought they were dead.
class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)
        pg.event.set_grab(True)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 40)  
        self.current_gold = 0
        self.gamestate = 'main'
        self.map = Map(self)

        self.new_game()
     
    def new_game(self):
        self.map.get_map()
       
        
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self)
        self.weapon = Double_Barreled_Shotun(self)  
        self.sound = Sound(self)
        self.pathfinding = PathFinding(self)
        pg.mixer.music.play(-1)
        self.object_handler.spawn_npc()
        

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()
        self.draw_player_gold()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')




        

        

        
     
     
        
       #  Map.map_change(self)

    def draw_player_gold(self):
        font = pg.font.SysFont("arial", 80)
        gold_print = font.render(('Gold =' + str(self.current_gold)), True, (255, 215, 0))
        self.screen.blit(gold_print, (750, 0))


    def draw(self):
        # self.screen.fill('black')
        
        self.object_renderer.draw()
        self.draw_player_gold()
        self.weapon.draw()

        
        # self.map.draw()
        # self.player.draw()

    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True
            self.player.single_fire_event(event)

    def run(self):
        while True:

            self.check_events()
            self.update()
            self.draw()




if __name__ == '__main__':
    game = Game()
    game.run()
