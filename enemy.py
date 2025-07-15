import pygame
import sys
import tiles
pygame.init()
bullet_damage = 100
enemy_damage = 50

class Walker:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speedx = 100
        self.health = 500
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, 32, 32))
    def move(self, x, y):
        self.x = self.x + self.speedx
    def collide(self, tile):
        self.speedx = -self.speedx
    def hurt(self, player):
        player.health = player.health - enemy_damage
    def get_hurt(self):
        self.health = self.health - bullet_damage