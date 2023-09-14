from sprite_objects import *

class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.static_sprite_path = 'textures/static_sprites/'
        self.animated_sprites_path = 'textures/animated_sprites/'
        add_sprite = self.add_sprite

        #sprite map
        add_sprite(SpriteObject(game, pos=(3,3)))
        add_sprite(AnimatedSprite(game, pos=(5,4)))

    def update(self):
        [sprite.update() for sprite in self.sprite_list]

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)