import pygame
pygame.init()
class Solid(pygame.sprite.Sprite):
    def __init__ (self, image, x, y, spritesheet):
        pygame.sprite.Sprite.__init__(self)
        self.image = spritesheet.parse_sprite(image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.spritesheet = spritesheet
    def collide(self, player):
        if player.rect.colliderect(self.rect):
            print("yay")
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
class Tilemap():
    def __init__ (self, filename, spritesheet):
        self.spritesheet = spritesheet
        self.tile_size = 32
        self.start_x, self.start_y = 0, 0
        self.tiles = self.load_tiles(filename)
        self.map_surface = pygame.Surface(self.map_w, self.map_h)
        self.map_surface.set_colorkey((0, 0, 0))
        self.load_map()
    def draw_map(self, surface):
        surface.blit(self.map_surface, (0, 0))
    def load_map(self, filename):
        for tile in self.tiles:
            tile.draw(self.map_surface)
    def read_cvs (self, filename):
        map = []
        with open(os.path.join(filename)) as data:
            data = cvs.reader(data, delimiter=',')
            for row in data:
                map.append(list(row))
        return map
    def load_tiles(self, filename):
        tiles = []
        map = self.read_cvs(filename)
        x, y = 0, 0
        for row in map:
            x = 0
            for tile in row:
                if tile == 0:
                    self.start_x, self.start_y = x*self.tile_size, y*self.tile_size
                elif tile == 131:
                    tiles.append('Placeholder.svg', x * self.tile_size, y * self.tile_size, self.spritesheet)
                elif tile == 736:
                    tiles.append('Grass.png', x * self.tile_size, y * self.tile_size, self.spritesheet)

                x += 1
            y += 1
        self.map_w, self.map_h = x * self.tile_size,y * self.tile_size
        return tiles



