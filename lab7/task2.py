import os
import time

from pygame.locals import *

import sys,pygame

class mixerWrapper():

    def __init__(self):
        self.IsPaused = False

    def toggleMusic(self):
        if self.IsPaused:
            pygame.mixer.music.unpause()
            self.IsPaused = False
        else:
            pygame.mixer.music.pause()
            self.IsPaused = True

mus = os.listdir('musicc')
pygame.mixer.init()
print(mus)
display = pygame.display.set_mode((640, 480), pygame.RESIZABLE)
pygame.display.set_caption('Music Player')
j = 0
PAUSE = mixerWrapper()
play = 1
take = 'musicc/{}'
while True:
    for i in pygame.event.get():
        if i.type == QUIT:
            pygame.quit()
            sys.exit()

    key = pygame.key.get_pressed()
    paused = pygame.mixer.music.get_busy()
    if key[pygame.K_SPACE]:
        if PAUSE:
            PAUSE.toggleMusic()
        else:
            pygame.mixer.music.load(take.format(mus[j]))
            PAUSE.toggleMusic()

    if key[pygame.K_n]:
        j += 1
        if j >= len(mus):
            j = 0
        pygame.mixer.music.load(take.format(mus[j]))
        pygame.mixer.music.play()

    if key[pygame.K_p]:
        j -= 1

        if j < 0:
            j = len(mus) - 1
        pygame.mixer.music.load(take.format(mus[j]))
        pygame.mixer.music.play()
    time.sleep(0.05)




