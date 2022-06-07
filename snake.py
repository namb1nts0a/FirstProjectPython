import pygame
from random import randrange

#cree un class snake
class Snake:

    def __init__(self):
        self.health = 3
        self.max_health = 3
        self.rect = pygame.Rect(200,200,20,20)
        self.moveX = 0
        self.moveY = 0
        self.queu = 1
        self.score = 0
        self.serpent = []

    #methodes
    def move_right(self):
        self.moveX = 20
        self.moveY = 0

    def move_left(self):
        self.moveX = -20
        self.moveY = 0

    def move_up(self):
        self.moveX = 0
        self.moveY = -20

    def move_down(self):
        self.moveX = 0
        self.moveY = 20

    def gameOver(self):
        self.moveX = 0
        self.moveY = 0
        self.queu = 1
        self.score = 0
        self.serpent.clear()
        self.rect.x = randrange(0,860,20)
        self.rect.y = randrange(0,720,20)

