import pygame
import sys
import random
import time
import math
import bullet_program

class Gun:
    def __init__(self, screen, x, y, image, bullet_speed, bullet_damage):
        self.screen = screen
        self.pos_x = x
        self.pos_y = y
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.image_flipped = pygame.transform.flip(self.image, False, True)
        self.bullet_speed = bullet_speed
        self.bullet_damage = bullet_damage
        self.bullets = []
        self.image_rect = self.image.get_rect(center=(self.x, self.y))

    def draw(self, mouse_pos_x, mouse_pos_y):#draws the gun and calculats which way it should face and what it's angle should be
        drawn_image = self.image
        if mouse_pos_x > self.x:
            drawn_image = self.image_flipped
        dx = mouse_pos_x - self.image_rect.centerx
        dy = mouse_pos_y - self.image_rect.centery
        angle = math.degrees(math.atan2(-dy,dx))
        drawn_image = pygame.transform.rotate(drawn_image, angle -180)
        self.image_rect = self.image.get_rect(center=self.image_rect.center)
        self.screen.blit(drawn_image, self.image_rect)

    def shoot(self, mouse_pos_x, mouse_pos_y):
        dx = mouse_pos_x - self.image_rect.centerx
        dy = mouse_pos_y - self.image_rect.centery
        angle = math.degrees(math.atan2(-dy, dx))
        bullet_speed_x = math.cos(angle)*mouse_pos_x - self.image_rect.center[0] * self.bullet_speed
        bullet_speed_y = math.sin(angle)*mouse_pos_y - self.image_rect.center[1] * self.bullet_speed
        bullet = bullet_program.Bullet(self.screen, self.image_rect.center[0], self.image_rect.center[1], bullet_speed_x, bullet_speed_y)
        self.bullets.append(bullet)

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    mouse_pos = pygame.mouse.get_pos()
    gun = Gun(screen, 200, 200, "Pistol.png", 100, 100)

    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)

        gun.draw(mouse_pos[0], mouse_pos[1])

        pygame.draw.circle(screen, (255, 0, 0), (gun.image_rect.center),5)

        mouse_pos = pygame.mouse.get_pos()

        pygame.draw.circle(screen, (255, 0, 0), mouse_pos, 5)

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("BANG")
            #gun.shoot(mouse_pos[0], mouse_pos[1])

        pygame.display.update()

main()