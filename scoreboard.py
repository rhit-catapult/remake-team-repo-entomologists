import pygame
import sys

if __name__ == "__main__":
    pygame.init()

pygame.init()

class Scoreboard:
    def __init__(self,screen):
        self.screen = screen
        self.score = 0
        self.time = 0
        self.font = pygame.font.SysFont('Times New Roman', 16)

    def draw(self):
        text1 = pygame.font.Font.render(self.font, f"Score: {self.score}", True, (200,255,200))
        text2 = pygame.font.Font.render(self.font, f"Time: {self.time}", True, (200,255,200))
        self.screen.blit(text1, (10,10))
        self.screen.blit(text2, (10,10 + text2.get_height()))

    def update(self,s,t):
        self.score = s
        self.time = t

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
            scoreboard.update(1, 1)
            pygame.display.update()

    debug()
