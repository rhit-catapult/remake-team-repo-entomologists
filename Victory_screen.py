import pygame
pygame.init()

class Victory:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont('Arial', 20)
    def draw(self):
        self.screen.fill((40, 40, 50))
        self.screen.blit(self.font.render('Victor', True, (255, 255, 255)), (100, -200))
        self.screen.blit(self.font.render('Score: '). True, (255, 255, 255), (100, -200))