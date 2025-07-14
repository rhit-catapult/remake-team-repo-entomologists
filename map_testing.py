import pygame
from pygame.examples.scrap_clipboard import screen

import player
import tiles
#import spritesheet
pygame.init()
#spritesheet = Spritesheet(SPRITESHEET FILE)
#player_img = spritesheet.parse_sprite(CHARACTER IMAGE FILE)
player_rect = player_img.get_rect()
DISPLAY_W, DISPLAY_H = 1000, 800
canvas = pygame.Surface((DISPLAY_W, DISPLAY_H))
window = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
running = True
clock = pygame.time.Clock()
map = tiles.Tilemap("Placeholder.svg", spritesheet)
player_rect.x, player_rect.y = map.start_x, map.start_y


while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            pass

canvas.fill((0, 180, 240))
canvas.blit(player_image, player_rect)
window.blit(canvas, (0, 0))
pygame.display.update()