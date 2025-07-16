import pygame
import sys
import player as p
import scoreboard
import tiles as level
import math
import Weapons as weapons
import enemy

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

    score = scoreboard.Scoreboard(screen)

    player = p.Player(100, 100, 32, 32)
    gun = weapons.Gun(screen, 0, 0, "Pistol.png", 20, 100)

    enemies = [enemy.Walker(600,480,200,800,2, 32, False),
               enemy.Walker(512 + SCREENWIDTH,480,412 + SCREENWIDTH,612 + SCREENWIDTH,1, 32, True),
               enemy.Walker(64 + SCREENWIDTH, 200, 0, 0, 0, 32, True),
               enemy.Walker(SCREENWIDTH - 96 + SCREENWIDTH, 200, 0, 0, 0, 32, True),
               enemy.Walker(2496, 288, 2496, 2592, 1, 32, False),
               enemy.Walker(64 + SCREENWIDTH * 2, 64, 0, 0, 0, 32, True),
               enemy.Walker(2306, -96, 2306, 2850, 3, 32, False),
               enemy.Walker(4000, -288, 0, 0, 0, 32, True),
               enemy.Walker(3936, -224, 0, 0, 0, 32, True),
               enemy.Walker(3870, -160, 0, 0, 0, 32, True),
               enemy.Walker(3806, -96, 3326, 3806, -2, 32, False),
               enemy.Walker(3456, 224, 3456, 3552, 2, 32, True),
               enemy.Walker(3808, 352, 3712, 3808, -2, 32, True),
               enemy.Walker(4160, 64, 0, 0, 0, 32, True),
               enemy.Walker(4832, 224, 4544, 4832, 4, 32, False),
               enemy.Walker(4160, -96, 0, 0, 0, 32, True),
               enemy.Walker(4160, -192, 0, 0, 0, 32, True),
               enemy.Walker(4928, -416, 0, 0, 0, 32, True),
               enemy.Walker(4992, -480, 0, 0, 0, 32, True),
               enemy.Walker(4864, -864, 4864, 5024, 4, 32, False),
               enemy.Walker(4160, -1088, 4160, 5024, 2, 32, True),
               enemy.Walker(5024, -1088, 4160, 5024, -3, 32, True),
               enemy.Walker(4160, -864, 4160, 4320, 4, 32, False),
               enemy.Boss(3140, -704, 3140, 3972, 2, 64, True)]
    enemy_handler = enemy.Enemies(screen, enemies)

    tile = level.Tile(0, screen)
    tile2 = level.Tile(1, screen)
    tiles1 = [tile] * 17 + [0] * 14 + [tile] * 2 + [0] * 14 + [tile] * 4 + [0] * 12 + [tile] * 2 + [0] * 15 + [tile] + [
        0] * 4 + [tile] * 3 + [0] * 8 + [tile] + [0] * 15 + [tile] + [0] * 15 + [tile] * 17
    tiles2 = [tile] * 17 + [0] * 14 + [tile] * 2 + [0] * 14 + [tile] * 2 + [0] * 14 + [tile] + [0] * 15 + [tile] + [
        0] * 16 + [0] * 16 + [0] * 16 + [tile] * 16
    tiles3 = [tile] * 13 + [0] * 2 + [tile] * 2 + [0] * 14 + [tile] * 2 + [0] * 12 + [tile] * 4 + [0] * 14 + [
        tile] * 2 + [0] * 14 + [tile] * 1 + [0] * 7 + [tile] * 2 + [0] * 6 + [tile] * 1 + [0] * 15 + [tile] * 1 + [
                 0] * 15 + [tile] * 17
    tiles4 = [tile] * 17 + [0] * 15 + [tile] + [0] * 15 + [tile] * 1 + [0] * 15 + [tile] + [0] * 5 + [tile] * 11 + [
        0] * 14 + [tile] * 5 + [0] * 11 + [tile] * 5 + [0] * 11 + [tile] * 14 + [0] * 2 + [tile]
    tiles5 = [tile] * 16 + [0] * 15 + [tile] + [0] * 15 + [tile] + [0] * 15 + [tile] * 12 + [0] * 4 + [tile] * 2 + [
        0] * 13 + [tile] * 3 + [0] * 12 + [tile] * 3 + [tile] + [0] * 11 + [tile] * 6 + [0] * 2 + [tile] * 12
    tiles6 = [tile] * 2 + [0] * 2 + [tile] * 13 + [0] * 14 + [tile] * 2 + [0] * 14 + [tile] * 2 + [0] + [tile] * 2 + [
        0] * 11 + [tile] * 2 + [0] * 5 + [tile] * 2 + [0] * 7 + [tile] * 2 + [0] * 14 + [tile] * 2 + [0] * 9 + [
                 tile] * 2 + [0] * 4 + [tile] + [0] * 15 + [tile] + [tile2] * 12 + [tile] * 3
    tiles7 = [tile] * 13 + [0] * 2 + [tile] * 2 + [0] * 14 + [tile] * 2 + [0] * 12 + [tile] * 4 + [0] * 14 + [
        tile] * 2 + [0] * 6 + [tile] * 3 + [tile] * 2 + [0] * 3 + [tile] * 2 + [0] * 14 + [tile] + [0] * 4 + [
                 tile] * 2 + [0] * 9 + [tile] + [0] * 15 + [tile] * 4 + [tile2] * 12 + [tile]
    tiles8 = [tile] * 13 + [0] * 2 + [tile] * 2 + [0] * 14 + [tile] * 2 + [0] * 13 + [tile] * 3 + [0] * 6 + [tile] + [
        0] * 2 + [tile] + [0] * 2 + [tile] * 2 + [tile] * 2 + [0] * 3 + [tile] + [tile2] * 8 + [tile] * 5 + [0] * 2 + [
                 tile] * 13 + [0] * 14 + [tile] * 2 + [0] * 14 + [tile] * 14 + [0] * 2 + [tile]
    tiles9 = [tile] * 17 + [0] * 14 + [tile] * 2 + [0] * 14 + [tile] * 2 + [0] * 4 + [tile] * 6 + [0] * 4 + [
        tile] * 2 + [0] * 6 + [tile] * 2 + [0] * 6 + [tile] * 5 + [0] * 3 + [tile] * 2 + [0] * 3 + [tile] * 4 + [
                 0] * 7 + [tile] * 2 + [0] * 6 + [tile] + [0] * 7 + [tile] * 2 + [0] * 6 + [tile] * 14 + [0] * 2 + [
                 tile]
    tiles10 = [tile] * 16 + [tile] * 5 + [0] * 6 + [tile] * 5 + [tile] * 3 + [0] * 10 + [tile] * 3 + [tile] * 2 + [
        0] * 12 + [tile] * 2 + [tile] + [0] * 14 + [tile] + [tile] + [0] * 14 + [tile] * 2 + [0] * 15 + [tile] + [
                  0] * 15 + [tile] * 16

    room = [level.Room(tiles1, 0, 0), level.Room(tiles2, 1, 0), level.Room(tiles3, 2, 0), level.Room(tiles4, 2, -1),
            level.Room(tiles5, 3, -1), level.Room(tiles6, 3, 0), level.Room(tiles7, 4, 0), level.Room(tiles8, 4, -1),
            level.Room(tiles9, 4, -2), level.Room(tiles10, 3, -2)]
    l = level.Level(room)

    x_offset = 0
    y_offset = 0
    target_x = 0
    target_y = 0

    fire_rate = 10

    pygame.mixer_music.load("Cave Music _) (1).wav")
    pygame.mixer_music.play(-1)

    won = False
    win_ticks = 500

    while not won:
        clock.tick(60)

        screen.fill((40, 40, 50))

        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_SPACE) and player.jump_count < 2:
                    player.jump()

        if pygame.mouse.get_pressed()[0] and fire_rate < 1:
            gun.shoot(mouse_pos[0], mouse_pos[1])
            fire_rate = 10

        fire_rate -= 1

        player.loop(60)
        x_offset, y_offset, target_x, target_y = apply_offset(screen, player, l, x_offset, y_offset, target_x, target_y)
        p.handle_move(player, l.rect_tiles)

        gun.update_offset(target_x, target_y)

        gun.x = player.rect.x - target_x + player.rect.width / 2
        gun.y = player.rect.y - target_y + player.rect.height / 2

        gun.bullet_run(l.rect_tiles)

        gun.draw(mouse_pos[0], mouse_pos[1])

        hit = enemy_handler.enemies_update(gun.bullets, target_x, target_y, player.rect.centerx, player.rect.centery)

        wall = enemy.bullet_hit_wall(l.rect_tiles, enemy_handler.shots)
        if wall is not None:
            enemy_handler.shots.remove(wall)

        death_objects = enemies + l.death_tiles + enemy_handler.shots

        objs = player.handle_death(death_objects)

        for obj in objs:
            if obj.__class__ == enemy.EnemyBullet:
                enemy_handler.shots.remove(obj)

        if hit is not None:
            for h in hit:
                if h in gun.bullets:
                    gun.bullets.remove(h)

        score.update(enemy_handler.enemies_killed * 2 - player.deaths)
        score.draw()

        for e in enemies:
            if e.__class__ == enemy.Boss:
                break
        else:
            if win_ticks == 500:
                win_ticks = 300
                pygame.mixer.Sound.play(pygame.mixer.Sound('Boss_Death.wav'))

        if win_ticks < 500:
            win_ticks -= 1
            if win_ticks < 1:
                won = True

        pygame.display.update()

main()