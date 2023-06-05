import pygame
import sys
import math

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height), pygame.SCALED)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('georgia.ttf', 32)
        self.running = True
        self.dialog_show = False
        self.character_spritesheet = Spritesheet('img/character.png')
        self.terrain_spritesheet = Spritesheet('img/terrain.png')
        self.queen_spritesheet = Spritesheet('img/queen.png')
        self.tutorial_spritesheet = Spritesheet('img/tutorial.png')
        self.dialog_background = pygame.image.load('img/dialog.png')
        self.isolani_vetor = pygame.image.load('img/isolani.png')
        self.blackqueen_vetor = pygame.image.load('img/blackqueen.png')
        self.intro_background = pygame.image.load('img/introbackground.png')
        self.intro_song = pygame.mixer.music.load('sound/intromusic.mp3')
        pygame.mixer.music.set_volume(0.5)


    def createTilemap(self):
        self.prox_sala = 2
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "B":
                    Block(self, j, i)
                if column == "C":
                    Block(self, j, i, [32, 0])
                if column == "D":
                    Block(self, j, i, [64, 0])
                if column == "E":
                    Block(self, j, i, [96, 0])
                if column == "F":
                    Block(self, j, i, [128, 0])
                if column == "G":
                    Block(self, j, i, [160, 0])

                if column == "Q":
                    self.npc = NPC(self, j, i)
                if column == "P":
                    self.player = Player(self, j, i)

    def createTilemap2(self):
        self.prox_sala = 3
        for i, row in enumerate(tilemap2):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "H":
                    Block(self, j, i, [0, 64])
                if column == "I":
                    Block(self, j, i, [32, 64])
                if column == "J":
                    Block(self, j, i, [64, 64])
                if column == "K":
                    Block(self, j, i, [96, 64])
                if column == "L":
                    Block(self, j, i, [128, 64])
                if column == "M":
                    Block(self, j, i, [160, 64])
                if column == "N":
                    Block(self, j, i, [0, 96])
                if column == "R":
                    Block(self, j, i, [32, 96])

                if column == "Q":
                    NPC(self, j, i)
                if column == "P":
                    Player(self, j, i)

    def createTilemap3(self):
        self.prox_sala = 0
        for i, row in enumerate(tilemap3):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "B":
                    Block(self, j, i)
                if column == "C":
                    Block(self, j, i, [32, 0])
                if column == "D":
                    Block(self, j, i, [64, 0])
                if column == "E":
                    Block(self, j, i, [96, 0])
                if column == "F":
                    Block(self, j, i, [128, 0])
                if column == "G":
                    Block(self, j, i, [160, 0])
                if column == "S":
                    Block(self, j, i, [0, 32])
                if column == "T":
                    Block(self, j, i, [32, 32])

                if column == "Q":
                    npcs = NPC(self, j, i)
                if column == "P":
                    player = Player(self, j, i)


    def new(self):
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.npcs = pygame.sprite.LayeredUpdates()
        self.dialog = pygame.sprite.LayeredUpdates()
        self.tutorial = pygame.sprite.LayeredUpdates()
        #self.attacks = pygame.sprite.LayeredUpdates()

        self.createTilemap()

    def events(self):
        #game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    for sprite in self.all_sprites:
                        sprite.kill()
                    self.createTilemap()

                if event.key == pygame.K_x:
                    for sprite in self.all_sprites:
                        sprite.kill()
                    self.createTilemap2()

                if event.key == pygame.K_c:
                    for sprite in self.all_sprites:
                        sprite.kill()
                    self.createTilemap3()
                
                if event.key == pygame.K_a:
                    if self.player.y_change == 0 and self.player.x_change == 0:
                        Tutorial(self, self.player.rect.x - 8, self.player.rect.y - TILESIZE)
                        if self.player.y_change > 0:
                            for sprite in self.tutorial:
                                sprite.kill()
                        if self.player.y_change < 0:
                            for sprite in self.tutorial:
                                sprite.kill()
                        if self.player.x_change > 0:
                            for sprite in self.tutorial:
                                sprite.kill()
                        if self.player.x_change < 0:
                            for sprite in self.tutorial:
                                sprite.kill()

                if event.key == pygame.K_SPACE:
                    self.dialog_show = True

                    while self.dialog_show:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    self.dialog_show = False

                        #Dialog(0,144, WHITE, 'Isolani... é você?', 16)
                        self.screen.blit(self.isolani_vetor, (-90, -65))
                        self.screen.blit(self.blackqueen_vetor, (50, -65))
                        self.screen.blit(self.dialog_background, (0, 144))
                        self.clock.tick(fps)
                        pygame.display.update()


    def update(self):
        # game loop updates
        self.all_sprites.update()

    def draw(self):
        # game loop draw
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
        intro = True

        pygame.mixer.music.play(-1)

        title = self.font.render('ISOLANI', True, WHITE)
        title_rect = title.get_rect(center=(screen_width-128, screen_height-200))

        play_button = Button(10, 50, 100, 50, WHITE, BLUE, 'jogar', 32)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False
                pygame.mixer.music.load('sound/gamemusic.mp3')
                pygame.mixer.music.set_volume(0.5)
                pygame.mixer.music.play(-1)


            self.screen.blit(self.intro_background, (0,0))
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.clock.tick(fps)
            pygame.display.update()

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

        self.animation_loop = 0

        self.image = self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)

        #image_to_load = pygame.image.load("img/single.png").convert_alpha()
        #self.image = pygame.Surface([self.width, self.height], pygame.SRCALPHA)
        #self.image.set_colorkey(BLUE)
        #self.image.blit(image_to_load, (0,0))
        #self.image.fill(RED)

        #self.rect = pygame.Rect(self.y + 15,self.x + 15, 30, 40)
        self.rect = self.image.get_rect()
        #self.hitbox = (self.x + 15, self.y + 15, 30, 40)
        #pygame.draw.rect(self.game.screen, WHITE, self.rect, 3)
        self.rect.x = self.x
        self.rect.y = self.y

        self.down_animations = [self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(16, 0, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(32, 0, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(48, 0, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(64, 0, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(80, 0, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(96, 0, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(112, 0, self.width, self.height)]

        self.left_animations = [self.game.character_spritesheet.get_sprite(0, 36, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(16, 36, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(32, 36, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(48, 36, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(64, 36, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(80, 36, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(96, 36, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(112, 36, self.width, self.height)]

        self.up_animations = [self.game.character_spritesheet.get_sprite(0, 72, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(16, 72, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(32, 72, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(48, 72, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(64, 72, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(80, 72, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(96, 72, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(112, 72, self.width, self.height)]

        self.right_animations = [self.game.character_spritesheet.get_sprite(0, 108, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(16, 108, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(32, 108, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(48, 108, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(64, 108, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(80, 108, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(96, 108, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(112, 108, self.width, self.height)]

        self.wakeup_animations = [self.game.character_spritesheet.get_sprite(0, 144, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(16, 144, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(32, 144, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(48, 144, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(64, 144, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(80, 144, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(96, 144, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(112, 144, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(0, 180, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(16, 180, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(32, 180, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(48, 180, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(64, 180, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(80, 180, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(96, 180, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(112, 180, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(0, 216, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(16, 216, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(32, 216, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(48, 216, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(64, 216, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(80, 216, self.width, self.height),]

    def update(self):
        self.movement()
        self.animate()
        self.transition()
        #self.waking_up()

        self.rect.x += self.x_change
        self.collide_blocks('x'), self.collide_npcs('x')
        self.rect.y += self.y_change
        self.collide_blocks('y'), self.collide_npcs('y')

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

    def collide_blocks(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right

        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom

    def collide_npcs(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.npcs, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                    for sprite in self.game.npcs:
                        sprite.image = self.game.queen_spritesheet.get_sprite(16, 0, self.width, self.height)
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
                    for sprite in self.game.npcs:
                        sprite.image = self.game.queen_spritesheet.get_sprite(48, 0, self.width, self.height)

        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.npcs, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                    for sprite in self.game.npcs:
                        sprite.image = self.game.queen_spritesheet.get_sprite(32, 0, self.width, self.height)
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
                    for sprite in self.game.npcs:
                        sprite.image = self.game.queen_spritesheet.get_sprite(0, 0, self.width, self.height)

    def animate(self):
        if self.facing == "down":
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)
            else:
                self.image = self.down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 8:
                        self.animation_loop = 0

        if self.facing == "left":
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(0, 36, self.width, self.height)
            else:
                self.image = self.left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 8:
                        self.animation_loop = 0

        if self.facing == "up":
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(0, 72, self.width, self.height)
            else:
                self.image = self.up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 8:
                        self.animation_loop = 0

        if self.facing == "right":
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(0, 108, self.width, self.height)
            else:
                self.image = self.right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 8:
                        self.animation_loop = 0

    def transition(self):
        if self.rect.x >= 119 and self.rect.y <= -39:
           if self.game.prox_sala == 2:
                for sprite in self.game.all_sprites:
                    sprite.kill()
                self.game.createTilemap2()
           elif self.game.prox_sala == 3:
                for sprite in self.game.all_sprites:
                    sprite.kill()
                self.game.createTilemap3()

    #def waking_up(self):

        #sleeping = True

        #while sleeping:
         #   keys = pygame.key.get_pressed()
          #  movement = keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]
           # self.x_change = 0
            #self.y_change = 0
            #self.image = self.game.character_spritesheet.get_sprite(0, 144, self.width, self.height)

            #if movement:

             #   self.image = wakeup_animations[math.floor(self.animation_loop)]
              #  self.animation_loop += 0.1
               # if self.animation_loop >= 22:
                #        self.animation_loop = 1
                #sleeping = False




        #if wake[K]
            #if pressed_keys[K_a]:
             #       self.image = self.game.character_spritesheet.get_sprite(0, 144, self.width, self.height)
            #else:
             #   self.image = wakeup_animations[math.floor(self.animation_loop)]
              #  self.animation_loop += 0.1
               # if self.animation_loop >= 22:
                #        self.animation_loop = 1

class NPC(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = NPC_LAYER
        self.groups = self.game.all_sprites, self.game.npcs
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * PLAYERSIZE2
        self.y = y * PLAYERSIZE1
        self.width = PLAYERSIZE2
        self.height = PLAYERSIZE1

        self.x_change = 0
        self.y_change = 0

        self.facing = 'down'

        self.image = self.game.queen_spritesheet.get_sprite(0, 0, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    
    def movement(self):
        pass

    
    def update(self):

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y, pos = [0,0]):

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

        self.image = self.game.terrain_spritesheet.get_sprite(192, 0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Dialog(pygame.sprite.Sprite):
    def __init__(self, x, y, fg, content, fontsize):
        super().__init__()
        self.font = pygame.font.Font('georgia.ttf', fontsize)
        self.content = content

        self.x = x
        self.y = y
        self. width = TEXTBOXSIZE
        self.height = TEXTBOXSIZE2
        self.fg = fg
        self.image = pygame.image.load('img/dialog.png')

        self.text = self.font.render(self.content, True, self.fg)
        self.text_rect = self.text.get_rect(center=(self.width/2, self.height/2))

    def update(self):
        pass

class Tutorial(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = DIALOG_LAYER
        self.groups = self.game.all_sprites, self.game.tutorial
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x
        self.y = y
        self.width = TILESIZE
        self.height = TILESIZE

        self.animation_loop = 0

        self.image = self.game.tutorial_spritesheet.get_sprite(0, 0, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.tutorial1_animations = [self.game.tutorial_spritesheet.get_sprite(0, 32, self.width, self.height),
                           self.game.tutorial_spritesheet.get_sprite(32, 32, self.width, self.height),
                           self.game.tutorial_spritesheet.get_sprite(64, 32, self.width, self.height),
                           ]

        self.tutorial2_animations = [self.game.tutorial_spritesheet.get_sprite(0, 0, self.width, self.height),
                           self.game.tutorial_spritesheet.get_sprite(32, 0, self.width, self.height),
                           self.game.tutorial_spritesheet.get_sprite(64, 0, self.width, self.height),
                           ]

    def update(self):
        self.animate()
    
    def animate(self):
        direction = self.game.player.facing
        direction2 = self.game.npc.facing

        if direction == 'down':
            self.image = self.tutorial1_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 3:
                self.animation_loop = 0
        
        if direction2 == 'down':
            self.image = self.tutorial2_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 3:
                self.animation_loop = 0
        


class Button:
    def __init__(self, x, y, width, height, fg, bg, content, fontsize):
        self.font = pygame.font.Font('georgia.ttf', fontsize)
        self.content = content

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.fg = fg
        self.bg = bg

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.bg)
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

        self.text = self.font.render(self.content, True, self.fg)
        self.text_rect = self.text.get_rect(center=(self.width/2, self.height/2))
        self.image.blit(self.text, self.text_rect)

    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False

screen_width = 256
screen_height = 224
#screen_width = 640
#screen_height = 480
TILESIZE = 32
PLAYERSIZE1 = 36
PLAYERSIZE2 = 16
TEXTBOXSIZE = 256
TEXTBOXSIZE2 = 80

fps = 60

PLAYER_LAYER = 3
NPC_LAYER = 4
BLOCK_LAYER = 2
GROUND_LAYER = 1
DIALOG_LAYER = 5

PLAYER_SPEED = 1

RED = (255, 0, 0)
BLACK = (128, 128, 128)
BLUE = (0, 0, 0)
WHITE = (255, 255, 255)

tilemap = [
    'BEE..EED',
    'B......D',
    'B......DQ',
    'B...P..D',
    'B......D',
    'B......D',
    'FCCCCCCG',
]

tilemap2 = [
    'HKK..KKJ',
    'H......J',
    'H......JQ',
    'H......J',
    'H......J',
    'H.....PJ',
    'LIR..NIM',
    'LIIIIIIM'
]

tilemap3 = [
    'BEEEEEED',
    'B......D',
    'B......DQ',
    'B......D',
    'B......D',
    'B.....PD',
    'FCT..SCG',
    'FCCCCCCG'
]

g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()