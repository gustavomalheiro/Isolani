import pygame
import sys
import math
import random

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height), pygame.SCALED)
        self.clock = pygame.time.Clock()
        #self.font = pygame.font.Font()
        self.running = True
        self.character_spritesheet = Spritesheet('img/character.png')
        self.terrain_spritesheet = Spritesheet('img/terrain.png')

    def createTilemap(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "B":
                    Block(self, j, i)
                if column == "T":
                    Block(self, j, i, [126, 160])
                if column == "P":
                    Player(self, j, i)


    def new(self):
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        #self.enemies = pygame.sprite.LayeredUpdates()
        #self.attacks = pygame.sprite.LayeredUpdates()

        self.createTilemap()
           
    def events(self):
        #game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        # game loop updates
        self.all_sprites.update()

    
    def draw(self):
        # game loop draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(fps)
        pygame.display.update()


    def main(self):
        #game loop
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False
    
    def game_over(self):
        pass
    
    def intro_screen(self):
        pass

class Spritesheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert_alpha()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height], pygame.SRCALPHA)
        sprite.blit(self.sheet, (0,0), (x, y, width, height))
        return sprite

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * PLAYERSIZE2
        self.y = y * PLAYERSIZE1
        self.width = PLAYERSIZE2
        self.height = PLAYERSIZE1

        self.x_change = 0
        self.y_change = 0

        self.facing = 'down'
        self.animation_loop = 1

        self.image = self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)

        #image_to_load = pygame.image.load("img/single.png").convert_alpha()
        #self.image = pygame.Surface([self.width, self.height], pygame.SRCALPHA)
        #self.image.set_colorkey(BLUE)
        #self.image.blit(image_to_load, (0,0))
        #self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.movement()
        self.animate()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pygame.K_RIGHT]:
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
        if keys[pygame.K_UP]:
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
        if keys[pygame.K_DOWN]:
            self.y_change += PLAYER_SPEED
            self.facing = 'down'
    

    def animate(self):
        down_animations = [self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(16, 0, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(32, 0, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(48, 0, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(64, 0, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(80, 0, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(96, 0, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(112, 0, self.width, self.height)]

        left_animations = [self.game.character_spritesheet.get_sprite(0, 36, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(16, 36, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(32, 36, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(48, 36, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(64, 36, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(80, 36, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(96, 36, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(112, 36, self.width, self.height)]

        up_animations = [self.game.character_spritesheet.get_sprite(0, 72, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(16, 72, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(32, 72, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(48, 72, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(64, 72, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(80, 72, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(96, 72, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(112, 72, self.width, self.height)]

        right_animations = [self.game.character_spritesheet.get_sprite(0, 108, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(16, 108, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(32, 108, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(48, 108, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(64, 108, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(80, 108, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(96, 108, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(112, 108, self.width, self.height)]

        if self.facing == "down":
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)
            else:
                self.image = down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 8:
                        self.animation_loop = 1

        if self.facing == "left":
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(0, 36, self.width, self.height)
            else:
                self.image = left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 8:
                        self.animation_loop = 1
        
        if self.facing == "up":
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(0, 72, self.width, self.height)
            else:
                self.image = up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 8:
                        self.animation_loop = 1

        if self.facing == "right":
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(0, 108, self.width, self.height)
            else:
                self.image = right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 8:
                        self.animation_loop = 1

class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y, pos = [126, 160]):

        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(pos[0], pos[1], self.width, self.height)
        #self.image = pygame.Surface([self.width, self.height])
        #self.image.fill(BLUE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(126, 160, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

screen_width = 256
screen_height = 224
#screen_width = 640
#screen_height = 480
TILESIZE = 32
PLAYERSIZE1 = 36
PLAYERSIZE2 = 16

fps = 60

PLAYER_LAYER = 3
BLOCK_LAYER = 2
GROUND_LAYER = 1

PLAYER_SPEED = 3

RED = (255, 0, 0)
BLACK = (128, 128, 128)
BLUE = (0, 0, 0)

tilemap = [
    'T'*20,
    'TTTTTTPTTTTTTTTTTTTTTT'*20,
    'T'*20,
    'T'*20,
    'T'*20,
    'T'*20,
    'T'*20,
]

g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()
