import pygame
import sys
import player as p
import tiles as level


def main():
    pygame.init()
    pygame.display.set_caption("Platformer")
    screen = pygame.display.set_mode((1024, 576))
    clock = pygame.time.Clock()

    player = p.Player(100, 100, 32, 32)

    tile = level.Tile(0,screen)
    tiles = [tile]*17 + [0]*14 + [tile]*2 + [0]*14 + [tile]*4 + [0]*12 + [tile]*2 + [0]*15 + [tile] + [0]*4 + [tile]*3+ [0]*8 + [tile] + [0]*15 + [tile] + [0]*15 + [tile] * 17
    room = level.Room(tiles)
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

        p.handle_move(player, room.rect_tiles)
        player.draw(screen)
        room.draw()
        pygame.display.update()


        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()


main()