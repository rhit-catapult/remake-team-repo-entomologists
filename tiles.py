import pygame
pygame.init()
class Solid(pygame.sprite.Sprite):
    def __init__ (self, image, x, y, spritesheet):
        pygame.sprite.Sprite.__init__(self)
        self.image = spritesheet.parse_sprite(image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.spritesheet = spritesheet
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
class Tilemap():
    def __init__ (self, filename, spritesheet):
        self.spritesheet = spritesheet
        self.tile_size = 25
        self.start_x, self.start_y = 0, 0
        

