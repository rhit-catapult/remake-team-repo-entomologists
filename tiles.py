import pygame
import sys
import math
import player

from pygame import K_SPACE


class Tile:
    def __init__(self, type, screen):
        self.type = type
        self.width = 64
        self.height = 64
        self.y_offset = 0
        self.surface = pygame.Surface((self.width,self.height))
        self.screen = screen
        if type == 0:
            self.surface.blit(pygame.image.load('Back_Ground_Bricks.png'), (0, 0))
        if type == 1:
            self.height = 50
            self.y_offset = 14
            self.surface = pygame.Surface((self.width, self.height))
            self.surface.fill((40,200,40))

    def draw(self, x, y):
        if self.type != -1:
            self.screen.blit(self.surface,(x, y + self.y_offset))
   # def burn(self):
   #     if self.type == 1 and pygame.Rect.colliderect(self.re):
   #         player_health = 0
   #         print("GAME OVER")


class Room:
    def __init__(self,tiles, x, y):
        self.tiles = tiles
        self.x = x
        self.y = y
        self.rect_tiles = []

        for i in range(len(self.tiles)):
            if self.tiles[i] != 0:
                rect = pygame.Rect(64 * (i % 16) + self.x * 1024, 64 * math.floor(i / 16) + self.y * 576 + self.tiles[i].y_offset, self.tiles[i].width, self.tiles[i].height)
                self.rect_tiles.append(rect)

    def draw(self, x_offset, y_offset):
        for i in range(len(self.tiles)):
            if self.tiles[i] != 0:
                rect = pygame.Rect(64 * (i % 16) + self.x * 1024 - x_offset, 64 * math.floor(i / 16) + self.y * 576 + y_offset, self.tiles[i].width, self.tiles[i].height)
                self.tiles[i].draw(rect.x, rect.y)

class Level:
    def __init__(self, rooms):
        self.rooms = rooms
        self.rect_tiles = []

        for room in rooms:
            for tile in room.rect_tiles:
                self.rect_tiles.append(tile)

    def draw(self, x_offset, y_offset):
        for room in self.rooms:
            room.draw(x_offset, -y_offset)



def test_level():
    pygame.init()
    pygame.display.set_caption('platformer test')
    screen = pygame.display.set_mode((1024, 576))
    clock = pygame.time.Clock()
    tile = Tile(0,screen)
    tile2 = Tile(1,screen)
    tiles = [tile]*17 + [0]*14 + [tile]*2 + [0]*14 + [tile]*2 + [0]*14 + [tile2]*2 + [0]*15 + [tile] + [0]*15 + [tile] + [0]*15 + [tile] + [0]*15 + [tile] * 17
    room = [Room(tiles, 0, 0)]

    level = Level(room)


    screen.fill((40, 40, 50))
    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        level.draw(200, 40)

        pygame.display.update()






        (pygame.display.update())

if __name__ == "__main__":
    test_level()