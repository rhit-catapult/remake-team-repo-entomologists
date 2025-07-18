import pygame









import enemy as e
import sys
import player as p
import tiles as level
import math

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




    player = p.Player(3500, -800, 32, 32)

    tile = level.Tile(0,screen)
    tile2 = level.Tile(1,screen)
    tiles1 = [tile]*17 + [0]*14 + [tile]*2 + [0]*14 + [tile]*4 + [0]*12 + [tile]*2 + [0]*15 + [tile] + [0]*4 + [tile]*3+ [0]*8 + [tile] + [0]*15 + [tile] + [0]*15 + [tile] * 17
    tiles2 = [tile]*17 + [0]*14 + [tile]*2 + [0]*14 + [tile]*2 + [0]*14 + [tile] + [0]*15 + [tile] + [0]*16 + [0]*16 + [0]*16 + [tile]*16
    tiles3 = [tile]*13 + [0]*2 + [tile]*2 + [0]*14 + [tile]*2 + [0]*12 + [tile]*4 + [0]*14 + [tile]*2 + [0]*14 + [tile]*1 + [0]*7 + [tile]*2 + [0]*6 + [tile]*1 + [0]*15 + [tile]*1 + [0]*15 + [tile]*17
    tiles4 = [tile]*17 + [0]*15 + [tile] + [0]*15 + [tile]*1 + [0]*15 + [tile] + [0]*5 + [tile]*11 + [0]*14 + [tile]*5 + [0]*11 + [tile]*5 + [0]*11 + [tile]*14 + [0]*2+[tile]
    tiles5 = [tile]*16 + [0]*15 + [tile] + [0]*15 + [tile] + [0]*15 + [tile]*12 + [0]*4 + [tile]*2 + [0]*13 + [tile]*3 + [0]*12 + [tile]*3 + [tile] + [0]*11 + [tile]*6 + [0]*2 + [tile]*12
    tiles6 = [tile]*2 + [0]*2 + [tile]*13 + [0]*14 + [tile]*2 + [0]*14 + [tile]*2 + [0] + [tile]*2 + [0]*11 + [tile]*2 + [0]*5 + [tile]*2 +[0]*7 +[tile]*2 + [0]*14 + [tile]*2 + [0]*9 +[tile]*2 +[0]*4 +[tile] + [0]*15 + [tile] + [tile2]*12 + [tile]*3
    tiles7 = [tile]*13 + [0]*2 + [tile]*2 + [0]*14 + [tile]*2 + [0]*12 + [tile]*4 + [0]*14 + [tile]*2 + [0]*6+[tile]*3 + [tile]*2 +[0]*3 + [tile]*2 + [0]*14+ [tile] + [0]*4 + [tile]*2 +[0]*9+ [tile] + [0]*15 + [tile]*4 + [tile2]*12 + [tile]
    tiles8 = [tile]*13 + [0]*2 + [tile]*2 + [0]*14 + [tile]*2 + [0]*13 + [tile]*3 + [0]*6 +[tile] + [0]*2 +[tile] + [0]*2 +[tile]*2 + [tile]*2 + [0]*3 + [tile] + [tile2]*8 + [tile]*5 + [0]*2 + [tile]*13 + [0]*14 + [tile]*2 + [0]*14 + [tile]*14 + [0]*2 + [tile]
    tiles9 = [tile]*17 + [0]*14 + [tile]*2 + [0]*14 + [tile]*2 + [0]*4 + [tile]*6 + [0]*4 + [tile]*2 + [0]*6 + [tile]*2 + [0]*6 + [tile]*5 + [0]*3 + [tile]*2 + [0]*3 + [tile]*4 + [0]*7 + [tile]*2 + [0]*6 + [tile] + [0]*7 + [tile]*2 + [0]*6 + [tile]*14 + [0]*2 +[tile]
    tiles10 = [tile]*16 + [tile]*5 + [0]*6 + [tile]*5 + [tile]*3 + [0]*10 +[tile]*3 + [tile]*2 + [0]*12 + [tile]*2 +[tile]+[0]*14 +[tile] +[tile] +[0]*14 +[tile]*2+ [0]*15 +[tile] +[0]*15 + [tile]*16
    #tiles11 = [tile]*17 + [0]*14 + [tile]*2+ [0]*14 + [tile]*2+ [0]*14 + [tile]*2+ [0]*14 + [tile]*2+ [0]*14 + [tile]*2+ [0]*15 + [tile]+ [0]*15 + [tile]*16

    room = [level.Room(tiles1, 0, 0), level.Room(tiles2, 1, 0), level.Room(tiles3, 2, 0), level.Room(tiles4, 2, -1), level.Room(tiles5, 3, -1), level.Room(tiles6, 3, 0), level.Room(tiles7, 4, 0), level.Room(tiles8, 4, -1), level.Room(tiles9, 4, -2), level.Room(tiles10, 3, -2)]
    l = level.Level(room)

    x_offset = 0
    y_offset = 0
    target_x = 0
    target_y = 0



    pygame.mixer_music.load("Cave Music _) (1).wav")
    pygame.mixer_music.play(-1)
    while True:
        clock.tick(60)

        screen.fill((40, 40, 50))

        Ethan_Faust = e.Boss(3500, -1000, 3300, 3700, 35, size=200, shoot=False)
        Ethan_Faust.draw(screen, x_offset, y_offset)
        Ethan_Faust.move()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and player.jump_count < 2:
                    player.jump()

        player.loop(60)
        x_offset, y_offset, target_x, target_y = apply_offset(screen, player, l, x_offset, y_offset, target_x, target_y)
        p.handle_move(player, l.rect_tiles)
        pygame.display.update()


        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()

main()