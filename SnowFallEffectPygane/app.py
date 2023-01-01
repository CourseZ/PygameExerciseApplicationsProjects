import pygame
import sys
import random

pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
SIZE = (400,400)

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Snow Fall Effect")

snowFall = []
for i in range(50):
    x = random.randrange(0,400)
    y = random.randrange(0,400)
    snowFall.append([x,y])

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(BLACK)
    for i in range(len(snowFall)):
        pygame.draw.circle(screen,WHITE,snowFall[i],5)
        snowFall[i][1] += 1
        if snowFall[i][1] > 400:
            y = random.randrange(-50,-10)
            snowFall[i][1] = y
            x = random.randrange(0,400)
            snowFall[i][0] = x
    pygame.display.update()
    clock.tick(40)