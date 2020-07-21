import pygame
import random
#initializing pygame window
pygame.init()
#creating a screan
screen = pygame.display.set_mode((800, 600))

#title and icon
pygame.display.set_caption("Space Invaders.")
icon = pygame.image.load("download.jpg")
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load('player3.png')
playerX = 300
playerY = 480
playerX_change = 0

#enemy
enemyImg = pygame.image.load('enemy1.png')
enemyX = random.randint(0,650)
enemyY = random.randint(50,150)
enemyX_change = 0
enemyY_change = 0


def player(x,y):
	screen.blit(playerImg, (x,y))


def enemy(x,y):
	screen.blit(enemyImg, (x,y))	

#game loop
running = True
while running:

	#screen color
	screen.fill((0, 0, 0))
	# playerX += 0.1

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		# if keypress
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				playerX_change = -0.5
			if event.key == pygame.K_RIGHT:
				playerX_change = 0.5

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				playerX_change = 0
			

	playerX += playerX_change

	if playerX <= 0:
		playerX = 0
	elif playerX >= 650:
		playerX = 650

	enemyX += enemyX_change

	if enemyX <= 0:
		enemyX = 0
	elif enemyX >= 650:
		enemyX = 650

	player(playerX,playerY)
	enemy(enemyX,enemyY)
	pygame.display.update()
		