import pygame
import sys
import math
import time

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('georgia.ttf', 180)
        self.running = True
        self.dialog_show = False
        self.character_spritesheet = Spritesheet('img/character.png')
        self.terrain_spritesheet = Spritesheet('img/terrain.png')
        self.queen_spritesheet = Spritesheet('img/queen.png')
        self.wqueen_spritesheet = Spritesheet('img/wqueen.png')
        self.king_spritesheet = Spritesheet('img/king.png')
        self.cursor = pygame.image.load('img/cursor.png')
        self.dialog_background = pygame.image.load('img/dialog.png')
        self.isolani_vetor = pygame.image.load('img/isolani.png')
        self.blackqueen_vetor = pygame.image.load('img/blackqueen.png')
        self.whitequeen_vetor = pygame.image.load('img/whitequeen.png')
        self.whiteking_vetor = pygame.image.load('img/whiteking.png')
        self.intro_background = pygame.image.load('img/introbackground.png')
        self.go_background = pygame.image.load('img/go_background.png')
        self.xm_background = pygame.image.load('img/xequemate.png')
        self.dialogue_sound = pygame.mixer.Sound('sound/dialogue_sound.wav')
        self.intro_song = pygame.mixer.music.load('sound/intromusic.mp3')
        pygame.mixer.music.set_volume(0.5)
        self.titulo = self.CriarTexto('Rainha Negra', "georgia", WHITE, 45)
        self.isolani = self.CriarTexto('Isolani', "georgia", WHITE, 45)
        self.contador_falas = 0

    def createTilemap(self):
        self.prox_sala = 2
        self.dialog_show = False
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "B":
                    Block(self, j, i)
                if column == "C":
                    Block(self, j, i, [128, 0])
                if column == "D":
                    Block(self, j, i, [256, 0])
                if column == "E":
                    Block(self, j, i, [384, 0])
                if column == "F":
                    Block(self, j, i, [512, 0])
                if column == "G":
                    Block(self, j, i, [640, 0])
                if column == "U":
                    Block(self, j, i, [256, 128])

                if column == "Q":
                    self.npc = NPC(self, j, i)
                if column == "P":
                    self.player = Player(self, j, i)
    
    def createTilemapA(self):
        self.prox_sala = 2
        for i, row in enumerate(tilemapA):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "B":
                    Block(self, j, i)
                if column == "C":
                    Block(self, j, i, [128, 0])
                if column == "D":
                    Block(self, j, i, [256, 0])
                if column == "E":
                    Block(self, j, i, [384, 0])
                if column == "F":
                    Block(self, j, i, [512, 0])
                if column == "G":
                    Block(self, j, i, [640, 0])
                if column == "U":
                    Block(self, j, i, [256, 128])

                if column == "Q":
                    self.npc = NPC(self, j, i)
                if column == "P":
                    self.player = Player(self, j, i)

    def createTilemap2(self):
        self.prox_sala = 3
        self.dialog_show = False
        for i, row in enumerate(tilemap2):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "H":
                    Block(self, j, i, [0, 256])
                if column == "I":
                    Block(self, j, i, [128, 256])
                if column == "J":
                    Block(self, j, i, [256, 256])
                if column == "K":
                    Block(self, j, i, [384, 256])
                if column == "L":
                    Block(self, j, i, [512, 256])
                if column == "M":
                    Block(self, j, i, [640, 256])
                if column == "N":
                    Block(self, j, i, [0, 384])
                if column == "R":
                    Block(self, j, i, [128, 384])
                if column == "U":
                    Block(self, j, i, [256, 128])

                if column == "Q":
                    NPC(self, j, i)
                if column == "P":
                    Player(self, j, i)
    
    def createTilemap2A(self):
        self.prox_sala = 3
        for i, row in enumerate(tilemap2A):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "H":
                    Block(self, j, i, [0, 256])
                if column == "I":
                    Block(self, j, i, [128, 256])
                if column == "J":
                    Block(self, j, i, [256, 256])
                if column == "K":
                    Block(self, j, i, [384, 256])
                if column == "L":
                    Block(self, j, i, [512, 256])
                if column == "M":
                    Block(self, j, i, [640, 256])
                if column == "N":
                    Block(self, j, i, [0, 384])
                if column == "R":
                    Block(self, j, i, [128, 384])
                if column == "U":
                    Block(self, j, i, [256, 128])

                if column == "Q":
                    NPC(self, j, i)
                if column == "P":
                    Player(self, j, i)

    def createTilemap3(self):
        self.prox_sala = 0
        self.dialog_show = False
        for i, row in enumerate(tilemap3):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "B":
                    Block(self, j, i)
                if column == "C":
                    Block(self, j, i, [128, 0])
                if column == "D":
                    Block(self, j, i, [256, 0])
                if column == "E":
                    Block(self, j, i, [384, 0])
                if column == "F":
                    Block(self, j, i, [512, 0])
                if column == "G":
                    Block(self, j, i, [640, 0])
                if column == "S":
                    Block(self, j, i, [0, 128])
                if column == "T":
                    Block(self, j, i, [128, 128])

                if column == "Q":
                    NPC(self, j, i)
                if column == "P":
                    Player(self, j, i)


    def new(self):
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.npcs = pygame.sprite.LayeredUpdates()

        self.createTilemap()
    
    def CriarTexto(self, texto, fonte, cor, tamanho):
        formatar_fonte = pygame.font.SysFont(fonte, tamanho)

        mensagem = formatar_fonte.render(texto, True, cor)

        return mensagem
    
    def MostrarMensagem(self, tela, texto, tempo, titulo, textNum=0):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

        text2 = texto[:textNum]

        mensagem = self.CriarTexto(text2, "georgia", WHITE, 35)

        print(titulo)
        tela.blit(self.dialog_background, (0, 576))
        tela.blit(titulo, (30, 600))
        tela.blit(mensagem, (45, 680))
        self.dialogue_sound.play()
        pygame.display.update()

        time.sleep(tempo)

        if text2 != texto:
            textNum += 1
            pygame.event.pump()
            self.MostrarMensagem(tela, texto, tempo, titulo, textNum)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    if self.dialog_show:
                        letras = True
                        resposta = True
                        num_pergunta = 1
                        perdeu = False
                        resp = 's'
                        self.contador_falas = 0

                        if self.prox_sala == 2:
                            self.screen.blit(self.isolani_vetor, (36, 0))
                            self.screen.blit(self.blackqueen_vetor, (470, 0))
                            if self.contador_falas == 0:
                                while letras:
                                    self.MostrarMensagem(self.screen, "Isolani...", 0.08, self.titulo)
                                    self.MostrarMensagem(self.screen, "É você?", 0.05, self.titulo)
                                    letras = False
                                self.screen.blit(self.dialog_background, (0, 576))
                                self.screen.blit(self.titulo, (30, 600))
                                self.screen.blit(self.CriarTexto("É você?", "georgia", WHITE, 35), (45, 680))
                                self.screen.blit(self.CriarTexto("Sim", "georgia", WHITE, 50), (750, 650))
                                self.screen.blit(self.CriarTexto("Não", "georgia", WHITE, 50), (750, 750))
                                self.screen.blit(self.cursor, (690, 665))
                                pygame.display.update()

                                while resposta:
                                    for event in pygame.event.get():
                                        if event.type == pygame.KEYDOWN:
                                            if event.key == pygame.K_UP:
                                                self.screen.blit(self.dialog_background, (0, 576))
                                                self.screen.blit(self.titulo, (30, 600))
                                                self.screen.blit(self.CriarTexto("É você?", "georgia", WHITE, 35), (45, 680))
                                                self.screen.blit(self.CriarTexto("Sim", "georgia", WHITE, 50), (750, 650))
                                                self.screen.blit(self.CriarTexto("Não", "georgia", WHITE, 50), (750, 750))
                                                self.screen.blit(self.cursor, (690, 665))
                                                pygame.display.update()
                                                resp = 's'

                                            elif event.key == pygame.K_DOWN:
                                                self.screen.blit(self.dialog_background, (0, 576))
                                                self.screen.blit(self.titulo, (30, 600))
                                                self.screen.blit(self.CriarTexto("É você?", "georgia", WHITE, 35), (45, 680))
                                                self.screen.blit(self.CriarTexto("Sim", "georgia", WHITE, 50), (750, 650))
                                                self.screen.blit(self.CriarTexto("Não", "georgia", WHITE, 50), (750, 750))
                                                print(resp)
                                                self.screen.blit(self.cursor, (690, 765))
                                                pygame.display.update()
                                                resp = 'n'
                                            
                                            if event.key == pygame.K_z:
                                                self.contador_falas += 1
                                                letras = True
                                                resposta = False
                                    
                                        if event.type == pygame.QUIT:
                                            self.playing = False
                                            self.running = False
                            
                            if resp == 's':
                                while self.contador_falas < 14:
                                    if self.contador_falas == 1:
                                        while letras:
                                            self.MostrarMensagem(self.screen, "Ouça com atenção, Isolani.", 0.05, self.titulo)
                                            letras = False
                                        self.screen.blit(self.dialog_background, (0, 576))
                                        self.screen.blit(self.titulo, (30, 600))
                                        self.screen.blit(self.CriarTexto("Ouça com atenção, Isolani.", "georgia", WHITE, 10), (30, 650))
                                    elif self.contador_falas == 2:
                                        while letras:
                                            self.MostrarMensagem(self.screen, "pois estas serão minhas últimas palavras.", 0.05, self.titulo)
                                            letras = False
                                        self.screen.blit(self.dialog_background, (0, 576))
                                        self.screen.blit(self.titulo, (30, 600))
                                        self.screen.blit(self.CriarTexto("pois estas serão minhas últimas palavras.", "georgia", WHITE, 10), (30, 650))       
                                    elif self.contador_falas == 3:
                                        while letras:
                                            self.MostrarMensagem(self.screen, "Sacrifiquei-me a fim de criar", 0.05, self.titulo)
                                            letras = False
                                        self.screen.blit(self.dialog_background, (0, 576))
                                        self.screen.blit(self.titulo, (30, 600))
                                        self.screen.blit(self.CriarTexto("Sacrifiquei-me a fim de criar", "georgia", WHITE, 10), (30, 650))
                                    elif self.contador_falas == 4:
                                        while letras:
                                            self.MostrarMensagem(self.screen, "um ataque forçado ao Rei Branco,", 0.05, self.titulo)
                                            letras = False
                                        self.screen.blit(self.dialog_background, (0, 576))
                                        self.screen.blit(self.titulo, (30, 600))
                                        self.screen.blit(self.CriarTexto("um ataque forçado ao Rei Branco,", "georgia", WHITE, 10), (30, 650))
                                    elif self.contador_falas == 5:
                                        while letras:
                                            self.MostrarMensagem(self.screen, "contudo as habilidades de cálculo da Rainha Branca", 0.05, self.titulo)
                                            letras = False
                                        self.screen.blit(self.dialog_background, (0, 576))
                                        self.screen.blit(self.titulo, (30, 600))
                                        self.screen.blit(self.CriarTexto("contudo as habilidades de cálculo da Rainha Branca", "georgia", WHITE, 10), (30, 650))       
                                    elif self.contador_falas == 6:
                                        while letras:
                                            self.MostrarMensagem(self.screen, "vão além de tudo que nós já tenhamos enfrentado antes.", 0.05, self.titulo)
                                            letras = False
                                        self.screen.blit(self.dialog_background, (0, 576))
                                        self.screen.blit(self.titulo, (30, 600))
                                        self.screen.blit(self.CriarTexto("vão além de tudo que nós já tenhamos enfrentado antes.", "georgia", WHITE, 10), (30, 650))
                                    elif self.contador_falas == 7:
                                        while letras:
                                            self.MostrarMensagem(self.screen, "Você é nossa última esperança. Chegue até a última sala!", 0.05, self.titulo)
                                            letras = False
                                        self.screen.blit(self.dialog_background, (0, 576))
                                        self.screen.blit(self.titulo, (30, 600))
                                        self.screen.blit(self.CriarTexto("Você é nossa última esperança. Chegue até a última sala!", "georgia", WHITE, 10), (30, 650))
                                    elif self.contador_falas == 8:
                                        while letras:
                                            self.MostrarMensagem(self.screen, "Capture o Rei Branco!", 0.05, self.titulo)
                                            letras = False
                                        self.screen.blit(self.dialog_background, (0, 576))
                                        self.screen.blit(self.titulo, (30, 600))
                                        self.screen.blit(self.CriarTexto("Capture o Rei Branco!", "georgia", WHITE, 10), (30, 650))
                                    elif self.contador_falas == 9:
                                        while letras:
                                            self.MostrarMensagem(self.screen, "Coroe-se a próxima Rainha Negra, Isolani!", 0.05, self.titulo)
                                            letras = False
                                        self.screen.blit(self.dialog_background, (0, 576))
                                        self.screen.blit(self.titulo, (30, 600))
                                        self.screen.blit(self.CriarTexto("Coroe-se a próxima Rainha Negra, Isolani!", "georgia", WHITE, 10), (30, 650))                               
                                    elif self.contador_falas == 9:
                                        while letras:
                                            self.MostrarMensagem(self.screen, "Você é nossa última esperança. Chegue até a última sala!", 0.05, self.titulo)
                                            letras = False
                                        self.screen.blit(self.dialog_background, (0, 576))
                                        self.screen.blit(self.titulo, (30, 600))
                                        self.screen.blit(self.CriarTexto("Você é nossa última esperança. Chegue até a última sala!", "georgia", WHITE, 10), (30, 650))
                                    elif self.contador_falas == 10:
                                        while letras:
                                            self.MostrarMensagem(self.screen, "E não se esqueça jamais:", 0.05, self.titulo)
                                            letras = False
                                        self.screen.blit(self.dialog_background, (0, 576))
                                        self.screen.blit(self.titulo, (30, 600))
                                        self.screen.blit(self.CriarTexto("E não se esqueça jamais:", "georgia", WHITE, 10), (30, 650))
                                    elif self.contador_falas == 11:
                                        while letras:
                                            self.MostrarMensagem(self.screen, "um peão isolado...", 0.05, self.titulo)
                                            letras = False
                                        self.screen.blit(self.dialog_background, (0, 576))
                                        self.screen.blit(self.titulo, (30, 600))
                                        self.screen.blit(self.CriarTexto("um peão isolado...", "georgia", WHITE, 10), (30, 650))                                
                                    elif self.contador_falas == 12:
                                        while letras:
                                            self.MostrarMensagem(self.screen, "espalha escuridão...", 0.05, self.titulo)
                                            letras = False
                                        self.screen.blit(self.dialog_background, (0, 576))
                                        self.screen.blit(self.titulo, (30, 600))
                                        self.screen.blit(self.CriarTexto("espalha escuridão...", "georgia", WHITE, 10), (30, 650))
                                    elif self.contador_falas == 13:
                                        while letras:
                                            self.MostrarMensagem(self.screen, "por todo tabuleiro...", 0.05, self.titulo)
                                            letras = False
                                        self.screen.blit(self.dialog_background, (0, 576))
                                        self.screen.blit(self.titulo, (30, 600))
                                        self.screen.blit(self.CriarTexto("por todo tabuleiro...", "georgia", WHITE, 10), (30, 650))
                                        for sprite in self.all_sprites:
                                            sprite.kill()
                                        self.createTilemapA()

                                    for event in pygame.event.get():
                                        if event.type == pygame.KEYDOWN:
                                            if event.key == pygame.K_z:
                                                self.contador_falas += 1
                                                letras = True
                                        
                                        if event.type == pygame.QUIT:
                                            self.playing = False
                                            self.running = False
                            elif resp == 'n':
                                letras = True
                                while letras:
                                    self.MostrarMensagem(self.screen, "Ainda não é a sua hora...", 0.06, self.titulo)
                                    self.contador_falas = 0
                                    letras = False

                                self.screen.blit(self.dialog_background, (0, 143))
                                self.screen.blit(self.titulo, (10, 610))
                                self.screen.blit(self.CriarTexto("Ainda não é a sua hora...", "georgia", WHITE, 15), (15, 170))
                                
                        
                        elif self.prox_sala == 3:
                            self.contador_falas = 1
                            self.titulo = self.CriarTexto("Rainha Branca", "georgia", WHITE, 45)
                            self.screen.blit(self.isolani_vetor, (36, 0))
                            self.screen.blit(self.whitequeen_vetor, (470, 0))

                            while self.contador_falas < 23:
                                if self.contador_falas == 1:
                                    while letras:
                                        self.MostrarMensagem(self.screen, "Então é você... a última, Isolani", 0.05, self.titulo)
                                        letras = False
                                    self.screen.blit(self.dialog_background, (0, 576))
                                    self.screen.blit(self.titulo, (30, 600))
                                    self.screen.blit(self.CriarTexto("Então é você... a última, Isolani", "georgia", WHITE, 10), (30, 650))
                                if self.contador_falas == 2:
                                    while letras:
                                        self.MostrarMensagem(self.screen, "Sou Isolani, sim, e você pagará pelo que fez, Rainha Branca!", 0.05, self.isolani)
                                        letras = False
                                    self.screen.blit(self.dialog_background, (0, 576))
                                    self.screen.blit(self.isolani, (30, 600))
                                    self.screen.blit(self.CriarTexto("Sou Isolani, sim, e você pagará pelo que fez, Rainha Branca!", "georgia", WHITE, 10), (30, 650))       
                                if self.contador_falas == 3:
                                    while letras:
                                        self.MostrarMensagem(self.screen, "Oh, fala em tom de superioridade", 0.05, self.titulo)
                                        letras = False
                                    self.screen.blit(self.dialog_background, (0, 576))
                                    self.screen.blit(self.titulo, (30, 600))
                                    self.screen.blit(self.CriarTexto("Oh, fala em tom de superioridade", "georgia", WHITE, 10), (30, 650))
                                if self.contador_falas == 4:
                                    while letras:
                                        self.MostrarMensagem(self.screen, "como se não fosse apenas um peão isolado.", 0.05, self.titulo)
                                        letras = False
                                    self.screen.blit(self.dialog_background, (0, 576))
                                    self.screen.blit(self.titulo, (30, 600))
                                    self.screen.blit(self.CriarTexto("como se não fosse apenas um peão isolado.", "georgia", WHITE, 10), (30, 650))
                                if self.contador_falas == 5:
                                    while letras:
                                        self.MostrarMensagem(self.screen, "Não se esqueça: você é um peão e nada além disso.", 0.05, self.titulo)
                                        letras = False
                                    self.screen.blit(self.dialog_background, (0, 576))
                                    self.screen.blit(self.titulo, (30, 600))
                                    self.screen.blit(self.CriarTexto("Não se esqueça: você é um peão e nada além disso.", "georgia", WHITE, 10), (30, 650))
                                if self.contador_falas == 6:
                                    while letras:
                                        self.MostrarMensagem(self.screen, "Que utilidade ou desejos seriam cabíveis a um peão?", 0.05, self.titulo)
                                        letras = False
                                    self.screen.blit(self.dialog_background, (0, 576))
                                    self.screen.blit(self.titulo, (30, 600))
                                    self.screen.blit(self.CriarTexto("Que utilidade ou desejos seriam cabíveis a um peão?", "georgia", WHITE, 10), (30, 650))
                                if self.contador_falas == 7:
                                    while letras:
                                        self.MostrarMensagem(self.screen, "Eu tenho um sonho.", 0.05, self.isolani)
                                        letras = False
                                    self.screen.blit(self.dialog_background, (0, 576))
                                    self.screen.blit(self.isolani, (30, 600))
                                    self.screen.blit(self.CriarTexto("Eu tenho um sonho.", "georgia", WHITE, 10), (30, 650))
                                if self.contador_falas == 8:
                                    while letras:
                                        self.MostrarMensagem(self.screen, "Tola! Sonhos não são feitos para peões.", 0.05, self.titulo)
                                        letras = False
                                    self.screen.blit(self.dialog_background, (0, 576))
                                    self.screen.blit(self.titulo, (30, 600))
                                    self.screen.blit(self.CriarTexto("Tola! Sonhos não são feitos para peões.", "georgia", WHITE, 10), (30, 650))
                                if self.contador_falas == 9:
                                    while letras:
                                        self.MostrarMensagem(self.screen, "A você resta sacrificar-se", 0.05, self.titulo)
                                        letras = False
                                    self.screen.blit(self.dialog_background, (0, 576))
                                    self.screen.blit(self.titulo, (30, 600))
                                    self.screen.blit(self.CriarTexto("A você resta sacrificar-se", "georgia", WHITE, 10), (30, 650))
                                if self.contador_falas == 10:
                                    while letras:
                                        self.MostrarMensagem(self.screen, "pelos sonhos daqueles que possuem poder, nada mais.", 0.05, self.titulo)
                                        letras = False
                                    self.screen.blit(self.dialog_background, (0, 576))
                                    self.screen.blit(self.titulo, (30, 600))
                                    self.screen.blit(self.CriarTexto("pelos sonhos daqueles que possuem poder, nada mais.", "georgia", WHITE, 10), (30, 650))              
                                if self.contador_falas == 11:
                                    while letras:
                                        self.MostrarMensagem(self.screen, "Vivo pela minha Rainha e por seus sonhos.", 0.05, self.isolani)
                                        letras = False
                                    self.screen.blit(self.dialog_background, (0, 576))
                                    self.screen.blit(self.isolani, (30, 600))
                                    self.screen.blit(self.CriarTexto("Vivo pela minha Rainha e por seus sonhos.", "georgia", WHITE, 10), (30, 650))
                                if self.contador_falas == 12:
                                    while letras:
                                        self.MostrarMensagem(self.screen, "Passar por você é apenas o primeiro passo para alcançá-los.", 0.05, self.isolani)
                                        letras = False
                                    self.screen.blit(self.dialog_background, (0, 576))
                                    self.screen.blit(self.isolani, (30, 600))
                                    self.screen.blit(self.CriarTexto("Passar por você é apenas o primeiro passo para alcançá-los.", "georgia", WHITE, 10), (30, 650))                                
                                if self.contador_falas == 13:
                                    while letras:
                                        self.MostrarMensagem(self.screen, "Mova-se!", 0.05, self.isolani)
                                        letras = False
                                    self.screen.blit(self.dialog_background, (0, 576))
                                    self.screen.blit(self.isolani, (30, 600))
                                    self.screen.blit(self.CriarTexto("Mova-se!", "georgia", WHITE, 10), (30, 650))
                                if self.contador_falas == 14:
                                    while letras:
                                        self.MostrarMensagem(self.screen, "Não haverá trocas, aberturas ou ataques", 0.05, self.titulo)
                                        letras = False
                                    self.screen.blit(self.dialog_background, (0, 576))
                                    self.screen.blit(self.titulo, (30, 600))
                                    self.screen.blit(self.CriarTexto("Não haverá trocas, aberturas ou ataques", "georgia", WHITE, 10), (30, 650))
                                if self.contador_falas == 15:
                                    while letras:
                                        self.MostrarMensagem(self.screen, "pois além dessa sala não passará! Prepare-se!", 0.05, self.titulo)
                                        letras = False
                                    self.screen.blit(self.dialog_background, (0, 576))
                                    self.screen.blit(self.titulo, (30, 600))
                                    self.screen.blit(self.CriarTexto("pois além dessa sala não passará! Prepare-se!", "georgia", WHITE, 10), (30, 650))
                                        
                                if self.contador_falas == 16:
                                    while letras:
                                        self.MostrarMensagem(self.screen, "Você pode me quebrar, mas não pode me tocar ou pegar.", 0.08, self.titulo)
                                        self.MostrarMensagem(self.screen, "Quem sou eu?", 0.05, self.titulo)
                                        time.sleep(0.2)
                                        letras = False
                                    self.screen.blit(self.dialog_background, (0, 576))
                                    self.screen.blit(self.titulo, (30, 600))
                                    self.screen.blit(self.CriarTexto("Você pode me quebrar, mas não pode ", "georgia", WHITE, 35), (45, 680))
                                    self.screen.blit(self.CriarTexto("me tocar ou pegar. Quem sou eu?", "georgia", WHITE, 35), (47, 730))
                                    self.screen.blit(self.CriarTexto("O ego.", "georgia", WHITE, 30), (750, 610))
                                    self.screen.blit(self.CriarTexto("O Argumento.", "georgia", WHITE, 30), (750, 680))
                                    self.screen.blit(self.CriarTexto("A Promessa.", "georgia", WHITE, 30), (750, 750))
                                    self.screen.blit(self.CriarTexto("O Gelo.", "georgia", WHITE, 30), (750, 820))
                                    self.screen.blit(self.cursor, (690, 610))
                                    pygame.display.update()

                                    while resposta:
                                        for event in pygame.event.get():
                                            if event.type == pygame.KEYDOWN:
                                                if event.key == pygame.K_UP:
                                                    if num_pergunta > 1:
                                                        num_pergunta -= 1
                                                    
                                                    print(num_pergunta)
                                                    self.screen.blit(self.dialog_background, (0, 576))
                                                    self.screen.blit(self.titulo, (30, 600))
                                                    self.screen.blit(self.CriarTexto("Você pode me quebrar, mas não pode ", "georgia", WHITE, 35), (45, 680))
                                                    self.screen.blit(self.CriarTexto("me tocar ou pegar. Quem sou eu?", "georgia", WHITE, 35), (47, 730))
                                                    self.screen.blit(self.CriarTexto("O ego.", "georgia", WHITE, 30), (750, 610))
                                                    self.screen.blit(self.CriarTexto("O Argumento.", "georgia", WHITE, 30), (750, 680))
                                                    self.screen.blit(self.CriarTexto("A Promessa.", "georgia", WHITE, 30), (750, 750))
                                                    self.screen.blit(self.CriarTexto("O Gelo.", "georgia", WHITE, 30), (750, 820))

                                                    pygame.display.update()
                                                    
                                                elif event.key == pygame.K_DOWN:
                                                    if num_pergunta < 4:
                                                        num_pergunta += 1

                                                    print(num_pergunta)
                                                    self.screen.blit(self.dialog_background, (0, 576))
                                                    self.screen.blit(self.titulo, (30, 600))
                                                    self.screen.blit(self.CriarTexto("Você pode me quebrar, mas não pode ", "georgia", WHITE, 35), (45, 680))
                                                    self.screen.blit(self.CriarTexto("me tocar ou pegar. Quem sou eu?", "georgia", WHITE, 35), (47, 730))
                                                    self.screen.blit(self.CriarTexto("O ego.", "georgia", WHITE, 30), (750, 610))
                                                    self.screen.blit(self.CriarTexto("O Argumento.", "georgia", WHITE, 30), (750, 680))
                                                    self.screen.blit(self.CriarTexto("A Promessa.", "georgia", WHITE, 30), (750, 750))
                                                    self.screen.blit(self.CriarTexto("O Gelo.", "georgia", WHITE, 30), (750, 820))

                                                    pygame.display.update()

                                                if event.key == pygame.K_z:
                                                    self.contador_falas += 1
                                                    letras = True
                                                    resposta = False
                                                
                                        if num_pergunta == 1:
                                            self.screen.blit(self.cursor, (690, 610))
                                            pygame.display.update()
                                            resp = 'ego'
                                        elif num_pergunta == 2:
                                            self.screen.blit(self.cursor, (690, 680))
                                            pygame.display.update()
                                            resp = 'argumento'
                                        elif num_pergunta == 3:
                                            self.screen.blit(self.cursor, (690, 750))
                                            pygame.display.update()
                                            resp = 'promessa'
                                        else:
                                            self.screen.blit(self.cursor, (690, 820))
                                            pygame.display.update()
                                            resp = 'gelo'
                                                    
                                if resp == 'ego':
                                    if self.contador_falas == 17:
                                        while letras:
                                            self.MostrarMensagem(self.screen, "O que sabe um mero peão sobre Ego?!", 0.05, self.titulo)
                                            letras = False
                                        self.screen.blit(self.dialog_background, (0, 576))
                                        self.screen.blit(self.titulo, (30, 600))
                                        self.screen.blit(self.CriarTexto("O que sabe um mero peão sobre Ego?!", "georgia", WHITE, 10), (30, 650))
                                    if self.contador_falas == 18:
                                        while letras:
                                            self.MostrarMensagem(self.screen, "Nascem para morrer pela vontade de outros", 0.05, self.titulo)
                                            letras = False
                                        self.screen.blit(self.dialog_background, (0, 576))
                                        self.screen.blit(self.titulo, (30, 600))
                                        self.screen.blit(self.CriarTexto("Nascem para morrer pela vontade de outros", "georgia", WHITE, 10), (30, 650))
                                    if self.contador_falas == 19:
                                        while letras:
                                            self.MostrarMensagem(self.screen, "e a ti concederei esta honra!", 0.05, self.titulo)
                                            letras = False
                                        self.screen.blit(self.dialog_background, (0, 576))
                                        self.screen.blit(self.titulo, (30, 600))
                                        self.screen.blit(self.CriarTexto("e a ti concederei esta honra!", "georgia", WHITE, 10), (30, 650))
                                    if self.contador_falas == 20:
                                        while letras:
                                            self.MostrarMensagem(self.screen, "Adeus, Isolani.", 0.05, self.titulo)
                                            letras = False
                                        self.screen.blit(self.dialog_background, (0, 576))
                                        self.screen.blit(self.titulo, (30, 600))
                                        self.screen.blit(self.CriarTexto("Adeus, Isolani.", "georgia", WHITE, 10), (30, 650))
                                        perdeu = True
                                        break             

                                elif resp == 'argumento':
                                    if self.contador_falas == 17:
                                        while letras:
                                            self.MostrarMensagem(self.screen, "Tente quebrar este Argumento, Isolani:", 0.05, self.titulo)
                                            letras = False
                                        self.screen.blit(self.dialog_background, (0, 576))
                                        self.screen.blit(self.titulo, (30, 600))
                                        self.screen.blit(self.CriarTexto("Tente quebrar este Argumento, Isolani:", "georgia", WHITE, 10), (30, 650))
                                    if self.contador_falas == 18:
                                        while letras:
                                            self.MostrarMensagem(self.screen, "um peão existe para nunca questionar", 0.05, self.titulo)
                                            letras = False
                                        self.screen.blit(self.dialog_background, (0, 576))
                                        self.screen.blit(self.titulo, (30, 600))
                                        self.screen.blit(self.CriarTexto("um peão existe para nunca questionar", "georgia", WHITE, 10), (30, 650))
                                    if self.contador_falas == 19:
                                        while letras:
                                            self.MostrarMensagem(self.screen, "e sempre seguir ordens!", 0.05, self.titulo)
                                            letras = False
                                        self.screen.blit(self.dialog_background, (0, 576))
                                        self.screen.blit(self.titulo, (30, 600))
                                        self.screen.blit(self.CriarTexto("e sempre seguir ordens!", "georgia", WHITE, 10), (30, 650))
                                    if self.contador_falas == 20:
                                        while letras:
                                            self.MostrarMensagem(self.screen, "Desapareça!", 0.05, self.titulo)
                                            letras = False
                                        self.screen.blit(self.dialog_background, (0, 576))
                                        self.screen.blit(self.titulo, (30, 600))
                                        self.screen.blit(self.CriarTexto("Desapareça!", "georgia", WHITE, 10), (30, 650))
                                        perdeu = True
                                        break   
                                        
                                elif resp == 'promessa':
                                    if self.contador_falas == 17:
                                        while letras:
                                            self.MostrarMensagem(self.screen, "Sua vontade é maior do que eu imaginava...", 0.05, self.titulo)
                                            letras = False
                                        self.screen.blit(self.dialog_background, (0, 576))
                                        self.screen.blit(self.titulo, (30, 600))
                                        self.screen.blit(self.CriarTexto("Sua vontade é maior do que eu imaginava...", "georgia", WHITE, 10), (30, 650))
                                    if self.contador_falas == 18:
                                        while letras:
                                            self.MostrarMensagem(self.screen, "Você é um peão de valor, prestes a coroar,", 0.05, self.titulo)
                                            letras = False
                                        self.screen.blit(self.dialog_background, (0, 576))
                                        self.screen.blit(self.titulo, (30, 600))
                                        self.screen.blit(self.CriarTexto("Você é um peão de valor, prestes a coroar,", "georgia", WHITE, 10), (30, 650))
                                    if self.contador_falas == 19:
                                        while letras:
                                            self.MostrarMensagem(self.screen, "de valor muito superior ao meu.", 0.05, self.titulo)
                                            letras = False
                                        self.screen.blit(self.dialog_background, (0, 576))
                                        self.screen.blit(self.titulo, (30, 600))
                                        self.screen.blit(self.CriarTexto("de valor muito superior ao meu.", "georgia", WHITE, 10), (30, 650))   
                                    if self.contador_falas == 20:
                                        while letras:
                                            self.MostrarMensagem(self.screen, "De onde tira tanta determinação, Isolani?", 0.05, self.titulo)
                                            letras = False
                                        self.screen.blit(self.dialog_background, (0, 576))
                                        self.screen.blit(self.titulo, (30, 600))
                                        self.screen.blit(self.CriarTexto("De onde tira tanta determinação, Isolani?", "georgia", WHITE, 10), (30, 650))
                                    if self.contador_falas == 21:
                                        while letras:
                                            self.MostrarMensagem(self.screen, "É melhor que cumpra a sua promessa, Isolani", 0.05, self.titulo)
                                            letras = False
                                        self.screen.blit(self.dialog_background, (0, 576))
                                        self.screen.blit(self.titulo, (30, 600))
                                        self.screen.blit(self.CriarTexto("É melhor que cumpra a sua promessa, Isolani", "georgia", WHITE, 10), (30, 650))
                                    if self.contador_falas == 22:
                                        while letras:
                                            self.MostrarMensagem(self.screen, "e mostre que peões são a alma de tudo que existe!", 0.05, self.titulo)
                                            letras = False
                                        self.screen.blit(self.dialog_background, (0, 576))
                                        self.screen.blit(self.titulo, (30, 600))
                                        self.screen.blit(self.CriarTexto("e mostre que peões são a alma de tudo que existe!", "georgia", WHITE, 10), (30, 650))
                                        for sprite in self.all_sprites:
                                            sprite.kill()
                                        self.createTilemap2A()

                                elif resp == 'gelo':
                                    if self.contador_falas == 17:
                                        while letras:
                                            self.MostrarMensagem(self.screen, "Aqui não existe calor ou frio; dia ou noite.", 0.05, self.titulo)
                                            letras = False
                                        self.screen.blit(self.dialog_background, (0, 576))
                                        self.screen.blit(self.titulo, (30, 600))
                                        self.screen.blit(self.CriarTexto("Aqui não existe calor ou frio; dia ou noite.", "georgia", WHITE, 10), (30, 650))
                                    if self.contador_falas == 18:
                                        while letras:
                                            self.MostrarMensagem(self.screen, "Existe apenas o branco e o preto; o sim e o não;", 0.05, self.titulo)
                                            letras = False
                                        self.screen.blit(self.dialog_background, (0, 576))
                                        self.screen.blit(self.titulo, (30, 600))
                                        self.screen.blit(self.CriarTexto("Existe apenas o branco e o preto; o sim e o não;", "georgia", WHITE, 10), (30, 650))
                                    if self.contador_falas == 19:
                                        while letras:
                                            self.MostrarMensagem(self.screen, "criação e destruição. Você escolheu destruição.", 0.05, self.titulo)
                                            letras = False
                                        self.screen.blit(self.dialog_background, (0, 576))
                                        self.screen.blit(self.titulo, (30, 600))
                                        self.screen.blit(self.CriarTexto("criação e destruição. Você escolheu destruição.", "georgia", WHITE, 10), (30, 650))
                                    if self.contador_falas == 20:
                                        while letras:
                                            self.MostrarMensagem(self.screen, "Sucumba, Isolani.", 0.05, self.titulo)
                                            letras = False
                                        self.screen.blit(self.dialog_background, (0, 576))
                                        self.screen.blit(self.titulo, (30, 600))
                                        self.screen.blit(self.CriarTexto("Sucumba, Isolani.", "georgia", WHITE, 10), (30, 650))
                                        perdeu = True
                                        break

                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_z:
                                            self.contador_falas += 1
                                            letras = True

                            if perdeu == True:
                                g.game_over()
                        
                        else:
                            self.contador_falas = 1
                            self.titulo = self.CriarTexto("Rei Branco", "georgia", WHITE, 45)
                            self.screen.blit(self.isolani_vetor, (36, 0))
                            self.screen.blit(self.whiteking_vetor, (470, 0))

                            while self.contador_falas < 13:
                                if self.contador_falas == 1:
                                    while letras:
                                        self.MostrarMensagem(self.screen, "!!!...", 0.05, self.titulo)
                                        letras = False
                                    self.screen.blit(self.dialog_background, (0, 576))
                                    self.screen.blit(self.titulo, (30, 600))
                                    self.screen.blit(self.CriarTexto("!!!...", "georgia", WHITE, 10), (30, 650))
                                elif self.contador_falas == 2:
                                    while letras:
                                        self.MostrarMensagem(self.screen, "Como… como chegou até aqui?!", 0.05, self.titulo)
                                        letras = False
                                    self.screen.blit(self.dialog_background, (0, 576))
                                    self.screen.blit(self.titulo, (30, 600))
                                    self.screen.blit(self.CriarTexto("Como… como chegou até aqui?!", "georgia", WHITE, 10), (30, 650))       
                                if self.contador_falas == 3:
                                    while letras:
                                        self.MostrarMensagem(self.screen, "Onde está minha Rainha?!", 0.05, self.titulo)
                                        letras = False
                                    self.screen.blit(self.dialog_background, (0, 576))
                                    self.screen.blit(self.titulo, (30, 600))
                                    self.screen.blit(self.CriarTexto("Onde está minha Rainha?!", "georgia", WHITE, 10), (30, 650))  
                                if self.contador_falas == 4:
                                    while letras:
                                        self.MostrarMensagem(self.screen, "Não há luz sem a escuridão…", 0.05, self.isolani)
                                        letras = False
                                    self.screen.blit(self.dialog_background, (0, 576))
                                    self.screen.blit(self.isolani, (30, 600))
                                    self.screen.blit(self.CriarTexto("Não há luz sem a escuridão…", "georgia", WHITE, 10), (30, 650))
                                if self.contador_falas == 5:
                                    while letras:
                                        self.MostrarMensagem(self.screen, "Não há o branco sem o preto…", 0.05, self.isolani)
                                        letras = False
                                    self.screen.blit(self.dialog_background, (0, 576))
                                    self.screen.blit(self.isolani, (30, 600))
                                    self.screen.blit(self.CriarTexto("Não há o branco sem o preto…", "georgia", WHITE, 10), (30, 650))
                                if self.contador_falas == 6:
                                    while letras:
                                        self.MostrarMensagem(self.screen, "Não há reinado sem queda…", 0.05, self.isolani)
                                        letras = False
                                    self.screen.blit(self.dialog_background, (0, 576))
                                    self.screen.blit(self.isolani, (30, 600))
                                    self.screen.blit(self.CriarTexto("Não há reinado sem queda…", "georgia", WHITE, 10), (30, 650))
                                if self.contador_falas == 7:
                                    while letras:
                                        self.MostrarMensagem(self.screen, "Você é apenas um peão Isolado, sua Rainha está morta!", 0.05, self.titulo)
                                        letras = False
                                    self.screen.blit(self.dialog_background, (0, 576))
                                    self.screen.blit(self.titulo, (30, 600))
                                    self.screen.blit(self.CriarTexto("Você é apenas um peão Isolado, sua Rainha está morta!", "georgia", WHITE, 10), (30, 650))
                                if self.contador_falas == 8:
                                    while letras:
                                        self.MostrarMensagem(self.screen, "Tudo que te resta é ajoelhar-se a mim", 0.05, self.titulo)
                                        letras = False
                                    self.screen.blit(self.dialog_background, (0, 576))
                                    self.screen.blit(self.titulo, (30, 600))
                                    self.screen.blit(self.CriarTexto("Tudo que te resta é ajoelhar-se a mim", "georgia", WHITE, 10), (30, 650))
                                if self.contador_falas == 9:
                                    while letras:
                                        self.MostrarMensagem(self.screen, "e tornar-se minha prisioneira!", 0.05, self.titulo)
                                        letras = False
                                    self.screen.blit(self.dialog_background, (0, 576))
                                    self.screen.blit(self.titulo, (30, 600))
                                    self.screen.blit(self.CriarTexto("e tornar-se minha prisioneira!", "georgia", WHITE, 10), (30, 650))                           
                                if self.contador_falas == 10:
                                    while letras:
                                        self.MostrarMensagem(self.screen, "Ajoelhe-se perante ao vitorioso!", 0.05, self.titulo)
                                        letras = False
                                    self.screen.blit(self.dialog_background, (0, 576))
                                    self.screen.blit(self.titulo, (30, 600))
                                    self.screen.blit(self.CriarTexto("Ajoelhe-se perante ao vitorioso!", "georgia", WHITE, 10), (30, 650))
                                if self.contador_falas == 11:
                                    while letras:
                                        self.MostrarMensagem(self.screen, "Uma rainha não se ajoelha, reina.", 0.05, self.isolani)
                                        letras = False
                                    self.screen.blit(self.dialog_background, (0, 576))
                                    self.screen.blit(self.isolani, (30, 600))
                                    self.screen.blit(self.CriarTexto("Uma rainha não se ajoelha, reina.", "georgia", WHITE, 10), (30, 650))
                                if self.contador_falas == 12:
                                    while letras:
                                        self.MostrarMensagem(self.screen, "Xeque-mate.", 0.05, self.isolani)
                                        letras = False
                                    self.screen.blit(self.dialog_background, (0, 576))
                                    self.screen.blit(self.isolani, (30, 600))
                                    self.screen.blit(self.CriarTexto("Xeque-mate.", "georgia", WHITE, 10), (30, 650))
                                    
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_z:
                                            self.contador_falas += 1
                                            letras = True
                            g.xeque_mate()
                    else:
                        pass

    def update(self):
        self.all_sprites.update()
        print(self.dialog_show)

    def draw(self):
        self.all_sprites.draw(self.screen)
        self.clock.tick(fps)
        pygame.display.update()

    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def game_over(self):
        text = self.font.render('Game Over', True, WHITE)
        text_rect = text.get_rect(center=(screen_width/2, screen_height-810))

        restart_button = Button(screen_width-560, screen_height-210, 100, 50, WHITE, BLUE, 'jogar', 40)

        for sprite in self.all_sprites:
            sprite.kill()
        
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            
            if restart_button.is_pressed(mouse_pos, mouse_pressed):
                self.new()
                self.main()
                self.createTilemap()

            self.screen.blit(self.go_background, (0,0))
            self.screen.blit(text, text_rect)
            self.screen.blit(restart_button.image, restart_button.rect)
            self.clock.tick(fps)
            pygame.display.update()
    
    def xeque_mate(self):
        text = self.font.render('Xeque-mate', True, WHITE)
        text_rect = text.get_rect(center=(screen_width/2, screen_height-810))

        restart_button = Button(screen_width-1024, screen_height-110, 200, 50, WHITE, BLUE, 'jogar', 40)

        for sprite in self.all_sprites:
            sprite.kill()
        
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            
            if restart_button.is_pressed(mouse_pos, mouse_pressed):
                self.new()
                self.main()
                self.createTilemap()

            self.screen.blit(self.xm_background, (0,0))
            self.screen.blit(text, text_rect)
            self.screen.blit(restart_button.image, restart_button.rect)
            self.clock.tick(fps)
            pygame.display.update()

    def intro_screen(self):
        intro = True

        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)

        title = self.font.render('ISOLANI', True, WHITE)
        title_rect = title.get_rect(center=(screen_width/2, screen_height-810))

        play_button = Button(screen_width-560, screen_height-210, 100, 50, WHITE, BLUE, 'jogar', 40)

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
        self.rect = self.image.get_rect(center = (x, y))
        self.rect.x = self.x
        self.rect.y = self.y

        self.down_animations = [self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(64, 0, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(128, 0, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(192, 0, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(256, 0, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(320, 0, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(384, 0, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(448, 0, self.width, self.height)]

        self.left_animations = [self.game.character_spritesheet.get_sprite(0, 144, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(64, 144, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(128, 144, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(192, 144, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(256, 144, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(320, 144, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(384, 144, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(448, 144, self.width, self.height)]

        self.up_animations = [self.game.character_spritesheet.get_sprite(0, 288, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(64, 288, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(128, 288, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(192, 288, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(256, 288, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(320, 288, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(384, 288, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(448, 288, self.width, self.height)]

        self.right_animations = [self.game.character_spritesheet.get_sprite(0, 432, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(64, 432, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(128, 432, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(192, 432, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(256, 432, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(320, 432, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(384, 432, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(448, 432, self.width, self.height)]

    def update(self):
        self.movement()
        self.animate()
        self.transition()

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
                self.game.dialog_show = True
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                    for sprite in self.game.npcs:
                        if self.game.prox_sala == 2:
                            sprite.image = self.game.queen_spritesheet.get_sprite(64, 0, self.width, self.height)
                        elif self.game.prox_sala == 3:
                            sprite.image = self.game.wqueen_spritesheet.get_sprite(64, 0, self.width, self.height)
                        elif self.game.prox_sala == 0:
                            sprite.image = self.game.king_spritesheet.get_sprite(64, 0, self.width, self.height)

                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
                    for sprite in self.game.npcs:
                        if self.game.prox_sala == 2:
                            sprite.image = self.game.queen_spritesheet.get_sprite(192, 0, self.width, self.height)
                        elif self.game.prox_sala == 3:
                            sprite.image = self.game.wqueen_spritesheet.get_sprite(192, 0, self.width, self.height)
                        elif self.game.prox_sala == 0:
                            sprite.image = self.game.king_spritesheet.get_sprite(192, 0, self.width, self.height)
            
                        
        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.npcs, False)
            if hits:
                self.game.dialog_show = True
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                    for sprite in self.game.npcs:
                        if self.game.prox_sala == 2:
                            sprite.image = self.game.queen_spritesheet.get_sprite(128, 0, self.width, self.height)
                        elif self.game.prox_sala == 3:
                            sprite.image = self.game.wqueen_spritesheet.get_sprite(128, 0, self.width, self.height)
                        elif self.game.prox_sala == 0:
                            sprite.image = self.game.king_spritesheet.get_sprite(128, 0, self.width, self.height)


                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
                    for sprite in self.game.npcs:
                        if self.game.prox_sala == 2:
                            sprite.image = self.game.queen_spritesheet.get_sprite(0, 0, self.width, self.height)
                        elif self.game.prox_sala == 3:
                            sprite.image = self.game.wqueen_spritesheet.get_sprite(0, 0, self.width, self.height)
                        elif self.game.prox_sala == 0:
                            sprite.image = self.game.king_spritesheet.get_sprite(0, 0, self.width, self.height)                  

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
                self.image = self.game.character_spritesheet.get_sprite(0, 144, self.width, self.height)
            else:
                self.image = self.left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 8:
                        self.animation_loop = 0

        if self.facing == "up":
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(0, 288, self.width, self.height)
            else:
                self.image = self.up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 8:
                        self.animation_loop = 0

        if self.facing == "right":
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(0, 432, self.width, self.height)
            else:
                self.image = self.right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 8:
                        self.animation_loop = 0

    def transition(self):
        if self.rect.x >= 96 and self.rect.y <= -39:
           if self.game.prox_sala == 2:
                for sprite in self.game.all_sprites:
                    sprite.kill()
                self.game.createTilemap2()
           elif self.game.prox_sala == 3:
                for sprite in self.game.all_sprites:
                    sprite.kill()
                self.game.createTilemap3()

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

        if self.game.prox_sala == 2:
           self.image = self.game.queen_spritesheet.get_sprite(0, 0, self.width, self.height)
        elif self.game.prox_sala == 3:
            self.image = self.game.wqueen_spritesheet.get_sprite(0, 0, self.width, self.height)
        elif self.game.prox_sala == 0:
            self.image = self.game.king_spritesheet.get_sprite(0, 0, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    
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

        self.image = self.game.terrain_spritesheet.get_sprite(768, 0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

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

screen_width = 1024
screen_height = 896
TILESIZE = 128
PLAYERSIZE1 = 144
PLAYERSIZE2 = 64
TEXTBOXSIZE = 1024
TEXTBOXSIZE2 = 320

fps = 60

PLAYER_LAYER = 3
NPC_LAYER = 4
BLOCK_LAYER = 2
GROUND_LAYER = 1
DIALOG_LAYER = 5

PLAYER_SPEED = 4

RED = (255, 0, 0)
BLACK = (128, 128, 128)
BLUE = (0, 0, 0)
WHITE = (255, 255, 255)

tilemap = [
    'BEEUUEED',
    'B......D',
    'B......DQ',
    'B...P..D',
    'B......D',
    'B......D',
    'FCCCCCCG',]

tilemapA = [
    'BEE..EED',
    'B......D',
    'B......DP',
    'B......D',
    'B......D',
    'B......D',
    'FCCCCCCG',]

tilemap2 = [
    'HKKUUKKJ',
    'H......J',
    'H......JQ',
    'H......J',
    'H......J',
    'H.....PJ',
    'LIR..NIM',
    'LIIIIIIM']

tilemap2A = [
    'HKK..KKJ',
    'H......J',
    'H......JP',
    'H......J',
    'H......J',
    'H......J',
    'LIR..NIM',
    'LIIIIIIM']

tilemap3 = [
    'BEEEEEED',
    'B......D',
    'B......DQ',
    'B......D',
    'B......D',
    'B.....PD',
    'FCT..SCG',
    'FCCCCCCG']

g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()