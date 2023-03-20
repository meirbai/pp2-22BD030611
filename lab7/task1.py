import time
import datetime as dt
import math
from pygame.locals import *

import sys,pygame


pygame.init()
x = (dt.datetime.now().second)%60


def rot_center(image, angle, x, y):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=(x, y)).center)

    return rotated_image, new_rect

k = pygame.display.set_mode((600, 450))
pygame.display.set_caption("Task 1")

clock = pygame.image.load("clock.png")

min = pygame.transform.scale(pygame.image.load("liney.png"), (200, 200))
minmin = pygame.transform.scale(pygame.image.load("liney.png"), (150, 300))
k.blit(clock, (0, 0))
a = 1
while True:
    for i in pygame.event.get():
        if i.type== QUIT:
            pygame.quit()
            sys.exit()
    y = -90 - ((dt.datetime.now().minute)%60)*6
    x = -90 - ((dt.datetime.now().second) % 60)*6
    img, bound = rot_center(min, x, *k.get_rect().center)
    imgimg, boundt = rot_center(minmin,y , 299.5, 225)
    k.blit(clock, (0, 0))
    k.blit(img, bound)
    k.blit(imgimg, boundt)
    pygame.display.flip()


