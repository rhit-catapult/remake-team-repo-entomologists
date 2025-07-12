import pygame
import sys
import random
import time

class Gun:
    def __init__(self, screen, x, y, image, bullet_speed_x, bullet_speed_y, bullet_damage, mouse_pos):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.bullet_speed_x = bullet_speed_x
        self.bullet_speed_y = bullet_speed_y
        self.bullet_damage = bullet_damage
        self.mouse_pos = mouse_pos

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    gun = Gun(screen, 100, 100, "Pistol.png", 10, 0, 100)

    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        gun.draw()

        mouse_pos = pygame.mouse.get_pos()

        pygame.draw.circle(screen, (255, 0, 0), mouse_pos, 5)

        pygame.display.update()

main()