import pygame
from random import randrange

class Game:

    def __init__(self):
        self.play = False
        self.lanched = True
        self.listScore = [0]
        self.bestScore = 0
        self.time = pygame.time.Clock()
        #les couleur
        self.white = (255, 255, 255)
        self.yellow1 = (150, 149, 65)
        self.fondColor = (165, 173, 159)
        self.black = (0, 0, 0)
        self.greenS = (30, 140, 20)
        self.yellow  = (200,230,14)
        #les fonts
        self.fontS = pygame.font.Font("fonts/fonts.ttf", 140)
        self.fontt = pygame.font.Font("fonts/fontt.ttf", 50)
        self.fontSco = pygame.font.Font("fonts/fontsco.TTF", 80)
        self.fontGo = pygame.font.Font('fonts/fontg.ttf',120)
        #les music
        self.musicFond = pygame.mixer.Sound('sounds/fondsong.ogg')
        self.musicEat = pygame.mixer.Sound('sounds/eat.ogg')
        self.musicExplo = pygame.mixer.Sound('sounds/explo.ogg')
        self.musicGameOver = pygame.mixer.Sound('sounds/gameOver.ogg')

        #pomme
        self.pom = pygame.image.load('images/pomme.png')
        self.pomme = self.pom.get_rect()
        self.pomme.x = randrange(0,860,20)
        self.pomme.y = randrange(0,720,20)

        self.imageC = pygame.image.load('images/heart.png')
        self.imageHeart = pygame.transform.scale(self.imageC, (150, 150))

    def highScore(self):
        with open(".score.txt", "w+") as fileScore:
            fileScore.write(str(self.bestScore))
            fileScore.close()

    def hsc(self):
        with open(".score.txt","r") as fileS:
            hs = int(fileS.read())
            self.listScore.append(hs)
            fileS.close()


