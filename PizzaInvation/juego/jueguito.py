import pygame
import random
#se inicializa pygame
pygame.init()

# inicializamos la pantalla
screen = pygame.display.set_mode((800,600))
#titulo de pantalla e incono
pygame.display.set_caption("Pizza Invasion")
incono = pygame.image.load("transbordador-espacial (1).png")
pygame.display.set_icon(incono)
fondo = pygame.image.load("14658088_5509862.jpg")


# imagen del jugador y sus varibales
playerImg = pygame.image.load("cohete.png")
playerX = 368
playerY = 500
playerXchange =0

#funcion para inicilizar jugardor en la patalla
def player(x,y):
    screen.blit(playerImg,(playerX,playerY))


#variables para enemigos
enemyImg = pygame.image.load("porcion-de-pizza.png")
enemyX = random.randint(0,736)
enemyY = random.randint(50,200)
enemyXchange = 0.3
enemyYchange = 50

#funcion de enemigos

def enemy(x,y):
    screen.blit(enemyImg,(enemyX,enemyY))

# loop para que se ejecute el juego
itexcutes = True
while itexcutes:
    screen.blit(fondo, (0,0))
    #iterar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            itexcutes = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                playerXchange = -0.1
            if event.key == pygame.K_RIGHT:
                playerXchange = 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXchange = 0
    playerX += playerXchange
    #mantener en borders
    if playerX <=0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    #ubicar enemigos
    enemyX += enemyXchange
    # actualizar ubicacion del enemigo
    if enemyX <= 0:
        enemyXchange = 0.3
        enemyY += enemyYchange
    elif enemyX >= 736:
        enemyXchange = -0.3
        enemyY += enemyYchange

    player(playerX,playerY)
    enemy(enemyX,enemyY)
    #actualizamos pantalla
    pygame.display.update()