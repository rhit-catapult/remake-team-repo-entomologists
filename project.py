import pygame
import sys
import player as p
import tiles as level
import math
import Weapons as weapons

SCREENWIDTH = 1024
SCREENHEIGHT = 576

def apply_offset(screen, player, l, x_offset, y_offset, target_x, target_y):

    if player.rect.x + player.rect.width / 2 > SCREENWIDTH + x_offset:
        x_offset += SCREENWIDTH
    elif player.rect.x + player.rect.width / 2 < 0 + x_offset:
        x_offset -= SCREENWIDTH

    if player.rect.y + player.rect.height / 2 > SCREENHEIGHT + y_offset:
        y_offset += SCREENHEIGHT
    elif player.rect.y + player.rect.height / 2 < 0 + y_offset:
        y_offset -= SCREENHEIGHT

    error_x = x_offset - target_x
    target_x += error_x * 0.2

    error_y = y_offset - target_y
    target_y += error_y * 0.2

    if math.isclose(target_x, x_offset, abs_tol=2):
        target_x = x_offset

    if math.isclose(target_y, y_offset, abs_tol=2):
        target_y = y_offset

    player.draw(screen, target_x, target_y)
    l.draw(target_x, target_y)

    return x_offset, y_offset, target_x, target_y


def main():
    pygame.init()
    pygame.display.set_caption("Platformer")
    screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    clock = pygame.time.Clock()

    player = p.Player(100, 100, 32, 32)
    gun = weapons.Gun(screen, 0, 0, "Pistol.png", 20, 100)

    tile = level.Tile(0,screen)
    tiles1 = [tile]*17 + [0]*14 + [tile]*2 + [0]*14 + [tile]*4 + [0]*12 + [tile]*2 + [0]*15 + [tile] + [0]*4 + [tile]*3+ [0]*8 + [tile] + [0]*15 + [tile] + [0]*15 + [tile] * 17
    tiles2 = [tile]*17 + [0]*14 + [tile]*2 + [0]*14 + [tile]*2 + [0]*14 + [tile] + [0]*15 + [tile] + [0]*16 + [0]*16 + [0]*16 + [tile]*16
    tiles3 = [tile]*13 + [0]*2 + [tile]*2 + [0]*14 + [tile]*2 + [0]*12 + [tile]*4 + [0]*14 + [tile]*2 + [0]*14 + [tile]*1 + [0]*7 + [tile]*2 + [0]*6 + [tile]*1 + [0]*15 + [tile]*1 + [0]*15 + [tile]*17
    room = [level.Room(tiles1, 0, 0), level.Room(tiles2, 1, 0), level.Room(tiles3, 2, 0)]
    l = level.Level(room)

    x_offset = 0
    y_offset = 0
    target_x = 0
    target_y = 0

    while True:
        clock.tick(60)

        screen.fill((40, 40, 50))

        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and player.jump_count < 2:
                    player.jump()

            if event.type == pygame.MOUSEBUTTONDOWN:
                gun.shoot(mouse_pos[0], mouse_pos[1])

        player.loop(60)
        x_offset, y_offset, target_x, target_y = apply_offset(screen, player, l, x_offset, y_offset, target_x, target_y)
        p.handle_move(player, l.rect_tiles)

        gun.update_offset(target_x, target_y)

        gun.x = player.rect.x - target_x + player.rect.width / 2
        gun.y = player.rect.y - target_y + player.rect.height / 2

        gun.bullet_run(l.rect_tiles)

        gun.draw(mouse_pos[0], mouse_pos[1])

        pygame.display.update()

main()