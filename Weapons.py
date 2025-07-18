import pygame
import sys
import random
import time
import math
import bullet_program

class Gun:
    def __init__(self, screen, x, y, image, bullet_speed, bullet_damage):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.image_flipped = pygame.transform.flip(self.image, False, True)
        self.bullet_speed = bullet_speed
        self.bullet_damage = bullet_damage
        self.bullets = []
        self.image_rect = self.image.get_rect(center=(self.x, self.y))
        self.offset_x = 0
        self.offset_y = 0

    def update_offset(self, x, y):
        self.offset_x = x
        self.offset_y = y

    def draw(self, mouse_pos_x, mouse_pos_y):#draws the gun and calculats which way it should face and what it's angle should be
        self.image_rect = self.image.get_rect(center=(self.x, self.y))
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
        image = 'Blue_Bullet.png'
        dx = mouse_pos_x - self.image_rect.centerx
        dy = mouse_pos_y - self.image_rect.centery
        angle = math.atan2(-dy, dx)
        bullet_speed_x = self.bullet_speed * math.cos(angle)
        bullet_speed_y = -1 * self.bullet_speed * math.sin(angle)
        bullet = bullet_program.Bullet(self.screen,
                                       self.x + self.offset_x,
                                       self.y + self.offset_y,
                                       bullet_speed_x,
                                       bullet_speed_y,
                                       image,
                                       self.bullet_damage)
        self.bullets.append(bullet)

    def bullet_run(self, rects):
        for bullet in self.bullets:
            bullet.move()
            bullet.draw(self.offset_x, self.offset_y)
            if bullet.collision(rects):
                self.bullets.remove(bullet)


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    mouse_pos = pygame.mouse.get_pos()
    gun = Gun(screen, 200, 200, "Pistol.png", 100, 100)

    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                gun.shoot(mouse_pos[0], mouse_pos[1])
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)

        gun.bullet_run()

        gun.draw(mouse_pos[0], mouse_pos[1])

        #pygame.draw.circle(screen, (255, 0, 0), (gun.image_rect.center),5)

        mouse_pos = pygame.mouse.get_pos()

        #pygame.draw.circle(screen, (255, 0, 0), mouse_pos, 5)

        pygame.display.update()

# main()