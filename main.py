#########################################################
##                                                     ##
##      Snake by NIRISON Lalaina Solofo Njaratiana     ##
##           Date de Sortie : 18/05/2020               ##
##                                                     ##
#########################################################

#importation des modules

import pygame
import os
import sys
from time import sleep
from snake import Snake
from game import Game
from random import randrange

pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS']="300,100"
pygame.display.set_caption("Snake")
window = pygame.display.set_mode((1080,720))

def rejQ():
    for event in pygame.event.get([pygame.KEYUP,pygame.KEYDOWN,pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.KEYUP:
            continue
        return event.key
    return None

def cadres():
    #creation des cadres
    pygame.draw.rect(window,game.yellow1,(862,2,230,716),5)
    pygame.draw.rect(window,game.yellow1,(862,0,230,240),5)
    pygame.draw.rect(window,game.yellow1,(862,240,230,240),5)

    window.blit(game.imageHeart,(840,320))

    textS = game.fontSco.render("{}".format(snake.score),True,game.yellow1)
    window.blit(textS,(940,110))
    nbHealth = game.fontSco.render("x {}".format(snake.health),True,game.yellow1)
    window.blit(nbHealth,(970,350))
    textBs = game.fontSco.render("{}".format(game.bestScore),True,game.yellow1)
    window.blit(textBs,(940,600))

    textScore = game.fontt.render("Score", True, game.yellow1)
    window.blit(textScore, (910, 10))
    textHealth = game.fontt.render("Health", True, game.yellow1)
    window.blit(textHealth, (900, 260))
    textBestScore = game.fontt.render("Best Score", True, game.yellow1)
    window.blit(textBestScore, (870, 500))

snake = Snake()
game = Game()

#methode de la bestScore
game.hsc()
game.bestScore = game.listScore[-1]

pygame.display.flip()
def ecranDebut():
    window.fill(game.black)
    #ecran du debut
    while not game.play:
        window.fill(game.black)
        cadres()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game.play = True

        # ajouts d'images
        imageFond = pygame.image.load("images/ouvert.png").convert_alpha()
        imageFondG = pygame.image.load("images/ouvertG.png").convert_alpha()
        window.blit(imageFondG, (40, -35))
        window.blit(imageFond, (350, -35))

        # les textes
        textt = game.fontt.render("Press  enter  key", True, game.yellow)
        window.blit(textt, (300, 400))
        textS = game.fontS.render("Snake", False, game.greenS)
        window.blit(textS, (190, 30))
        pygame.display.flip()

ecranDebut()

def over():
    game.listScore.append(snake.score)
    game.listScore.sort()
    game.bestScore = game.listScore[-1]
    game.highScore()
    game.musicExplo.play()
    game.musicFond.stop()
    snake.health -= 1
    sleep(3)
    game.musicFond.play(500)
    snake.gameOver()

def overGame():
    window.fill(game.black)
    cadres()
    textgo = game.fontGo.render("GAME OVER",True,game.greenS)
    window.blit(textgo,(160,280))
    snake.health = snake.max_health
    game.musicFond.stop()
    game.musicGameOver.play()
    pygame.display.flip()

    while rejQ() == None:
        game.time.tick()
    principal()

def principal():
    game.listScore.sort()
    game.musicFond.play(500)
    game.musicFond.set_volume(0.6)

    while game.lanched:
        window.fill(game.black)
        game.time.tick(13)
        cadres()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake.move_right()

                elif event.key == pygame.K_LEFT:
                    snake.move_left()

                elif event.key == pygame.K_UP:
                    snake.move_up()

                elif event.key == pygame.K_DOWN:
                    snake.move_down()

        pygame.draw.rect(window, game.greenS, snake.rect)
        window.blit(game.pom, game.pomme)

        snake.rect.x += snake.moveX
        snake.rect.y += snake.moveY

        teteS = []
        teteS.append(snake.rect.x)
        teteS.append(snake.rect.y)

        # mange de pomme
        if snake.rect.x == game.pomme.x and snake.rect.y == game.pomme.y:
            game.musicEat.play()
            game.pomme.x = randrange(20, 800, 20)
            game.pomme.y = randrange(20, 600, 20)
            snake.score += 5
            snake.queu += 1

        if len(snake.serpent) > snake.queu:
            snake.serpent.pop(0)

        snake.serpent.append(teteS)
        for i in range(snake.queu):
            pygame.draw.rect(window,game.greenS,pygame.Rect(snake.serpent[i][0],snake.serpent[i][1],20,20),1)

        # detection de game over
        if snake.rect.x < -20 or snake.rect.y < -20 or snake.rect.x > 860 or snake.rect.y > 720 :
            over()

        for q in snake.serpent[:-2]:
            if teteS == q:
                over()

        if snake.health < 0:
            snake.health = 0
            overGame()

        pygame.display.flip()
principal()
