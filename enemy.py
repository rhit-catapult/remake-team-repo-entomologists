import pygame
import sys

import player
import tiles
pygame.init()
bullet_damage = 100
enemy_damage = 50

class Walker:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speedx = 15
        self.health = 500
    def draw(self, screen):
        if self.health <= 0:
            return False
        if True:
            pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, 32, 32))
        if False:
            pass
    def move(self):
        self.x = self.x + self.speedx
    def collide(self, tile):
        if pygame.Rect.colliderect(tile, self):
            self.speedx = -self.speedx
    def hurt(self, player):
        if pygame.Rect.colliderect(player, self):
            player.health = player.health - enemy_damage
    def get_hurt(self):
        if pygame.Rect.colliderect(self, bullet):
            self.health = self.health - bullet_damage
