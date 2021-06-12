from tunnel import *
from classlib import *

import pygame, math, os, sys
pygame.init()
pygame.font.init()

class Counter(Script):
    def start(self):
        self.i = 0
    def update(self):
        self.i += 1

class Printme(Script):
    def update(self):
        print(self.counter.i)

class Transform(Script):
    def start(self):
        self.position = Vector2(0, 0)

class Map(Script):
    def start(self):
        self.background = (255, 255, 255)
        self.objects = []

class CameraView(Script):
    def start(self):
        self.width = 640
        self.height = 360
    def setup(self):
        self.window = pygame.display.set_mode((self.width, self.height))
        os.system('cls')
    def update(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        bkgcolour = self.parent.parent['Map'].background
        self.window.fill(bkgcolour)

        pygame.draw.rect(self.window, (0, 0, 0), pygame.Rect(0, 0, 100, 200))

        pygame.display.flip()
