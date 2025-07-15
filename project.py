import pygame
import sys
import player as p
import tiles as level

SCREENWIDTH = 1024
SCREENHEIGHT = 576

def apply_offset(screen, player, l, x_offset, y_offset):
    x_setpoint = 0
    y_setpoint = 0

    if player.rect.x + player.rect.width / 2 > SCREENWIDTH + x_offset:
        x_offset += SCREENWIDTH
    elif player.rect.x + player.rect.width / 2 < 0 + x_offset:
        x_offset -= SCREENWIDTH

    player.draw(screen, x_offset, y_offset)
    l.draw(x_offset, y_offset)

    return x_offset, y_offset


def main():
    pygame.init()
    pygame.display.set_caption("Platformer")
    screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    clock = pygame.time.Clock()

    player = p.Player(100, 100, 32, 32)

    tile = level.Tile(0,screen)
    tiles1 = [tile]*17 + [0]*14 + [tile]*2 + [0]*14 + [tile]*4 + [0]*12 + [tile]*2 + [0]*15 + [tile] + [0]*4 + [tile]*3+ [0]*8 + [tile] + [0]*15 + [tile] + [0]*15 + [tile] * 17
    tiles2 = [tile]*17 + [0]*14 + [tile]*2 + [0]*14 + [tile]*2 + [0]*14 + [tile]*1 + [0]*16 + [0]*16 + [0]*16+ [0]*16 + [tile]*16
    room = [level.Room(tiles1, 0, 0), level.Room(tiles2, 1, 0)]
    l = level.Level(room)

    x_offset = 0
    y_offset = 0

    while True:
        clock.tick(60)

        screen.fill((40, 40, 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and player.jump_count < 2:
                    player.jump()

        player.loop(60)
        x_offset, y_offset = apply_offset(screen, player, l, x_offset, y_offset)
        p.handle_move(player, l.rect_tiles)
        pygame.display.update()


        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()

main()