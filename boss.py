import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1024, 576))
class Boss:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 800
        self.screen = screen
        self.screen.blit(pygame.image.load('pixil-frame-0.png'), (0, 0))
    def draw(self):
        self.screen.blit( self.screen, (self.x, self.y))
    #def move(self):


    #def shoot(self):

