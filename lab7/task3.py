from pygame.locals import *

import sys,pygame

pygame.init()

screen = pygame.display.set_mode((700, 700))
clock = pygame.time.Clock()

a = 200
b = 200
h = pygame.draw.circle(screen, (255, 0, 0), (200, 200), 25, 0)
while True:
    clock.tick(60)
    for i in pygame.event.get():
        if i.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('white')
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        if(a<695 and a>25):
            a-=20
    elif key[pygame.K_RIGHT]:
        if(a<675 and a>0):
            a+=20
    elif key[pygame.K_UP]:
        if(b<690 and b>25):
            b-=20
    elif key[pygame.K_DOWN]:
        if(b<670 and b>0):
            b+=20
    pygame.draw.circle(screen, (255, 0, 0), (a, b), 25, 0)
    pygame.display.update()