import pygame
import sys

if __name__ == "__main__":
    pygame.init()

pygame.init()

class Scoreboard:
    def __init__(self,screen):
        self.screen = screen
        self.score = 1
        self.font = pygame.font.SysFont('Times New Roman', 12)

    def draw(self):
        text = pygame.font.Font.render(self.font, f'{self.score}', True, (200,255,200))
        self.screen.blit(text, (100,50))

    def update(self,value):
        self.score += value
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    def debug():
        pygame.display.init()
        screen = pygame.display.set_mode((800,600))
        scoreboard = Scoreboard(screen)
        while True:
            screen.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            scoreboard.draw()
            scoreboard.update(1)
            pygame.display.update()

    debug()
