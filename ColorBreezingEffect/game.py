import pygame
import random 
import sys

pygame.init()
screen = pygame.display.set_mode((600,600))

c1 = random.randint(0,255)
c2 = random.randint(0,255)
c3 = random.randint(0,255)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    if 0 < c1 < 255: 
        c1 += 1
    elif c1 >= 255:
        c1 -= 255
    elif c1 <= 0:
        c1 += 3

    if 0 < c2 < 255: 
        c2 += 1
    elif c2 >= 255:
        c2 -= 255
    elif c2 <= 0:
        c2 += 3
    
    if 0 < c3 < 255: 
        c3 += 1
    elif c3 >= 255:
        c3 -= 255
    elif c3 <= 0:
        c3 += 3
    
    clock.tick(60)
    screen.fill((c1,c2,c3))
    pygame.display.update()