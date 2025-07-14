import pygame
import sys
import math
class Tile:
    def __init__(self, type, screen):
        self.type = type
        self.width = 64
        self.height = 64
        self.surface = pygame.Surface((self.width,self.height))
        self.screen = screen

        if type == 0:
            self.surface.fill((70,70,95))

    def draw(self, x, y):
        if self.type != -1:
            self.screen.blit(self.surface,(x, y))


class Room:
    def __init__(self,tiles):
        self.tiles = tiles
    def draw(self):
        for i in range(len(self.tiles)):
            self.tiles[i].draw(64 * (i % 16), 64 * math.floor(i / 16))


def test_level():
    pygame.init()
    pygame.display.set_caption('platformer test')
    screen = pygame.display.set_mode((1024, 576))
    clock = pygame.time.Clock()
    tile = Tile(0,screen)
    tile2 = Tile(-1,screen)
    tiles = [tile]*17 + [tile2]*14 + [tile]*2 + [tile2]*14 + [tile]*2 + [tile2]*14 + [tile]*2 + [tile2]*15 + [tile] + [tile2]*15 + [tile] + [tile2]*15 + [tile] + [tile2]*15 + [tile] * 17
    room = Room(tiles)
    screen.fill((40, 40, 50))
    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        room.draw()

        pygame.display.update()

if __name__ == "__main__":
    test_level()