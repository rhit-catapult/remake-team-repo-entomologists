import pygame
import math


class Boss:
    def __init__(self, x, y, min_x, max_x, speed, size=64, shoot=False):
        self.min_x = min_x
        self.max_x = max_x
        self.speed_x = speed
        self.start_y = y
        self.end_y = y - 300
        self.speed_y = 2
        self.health = 35
        self.hit = 0
        self.shoot = shoot
        self.rect = pygame.Rect(x, y, size, size)
        self.bullets = []
        self.ticks = 30
        self.image = pygame.image.load('pixil-frame-0.png')
        self.image_hit = pygame.image.load('pixil-frame-0 (1).png')

    def draw(self, screen, x_offset, y_offset):
        if self.hit > 0:
            screen.blit(self.image, (self.rect.x - x_offset, self.rect.y - y_offset))
            self.hit -= 1
        else:
            screen.blit(self.image_hit, (self.rect.x - x_offset, self.rect.y - y_offset))
    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.start_y < self.rect.y or self.rect.y < self.end_y:
            self.speed_y *= -1

        if self.min_x > self.rect.x or self.rect.x > self.max_x:
            self.speed_x *= -1
    def update_hit(self, bullets):
        shot = []
        for bullet in bullets:
            if pygame.Rect.colliderect(bullet.rect, self.rect):
                self.health -= 1
                self.hit = 5
                shot.append(bullet)

        return shot

    def fire(self, x_off, y_off, screen, px, py):
        if self.ticks < 1:
            self.ticks = 30
            dx = px - self.rect.centerx
            dy = py - self.rect.centery
            angle = math.atan2(-dy, dx)
            bullet_speed_x = 5 * math.cos(angle)
            bullet_speed_y = -1 * 5 * math.sin(angle)

            return EnemyBullet(screen, self.rect.centerx, self.rect.centery, bullet_speed_x, bullet_speed_y)
        onscreen = 1024 > self.rect.x - x_off > 0 and 576 > self.rect.y - y_off > 0
        if onscreen:
            self.ticks -= 1
        else:
            self.ticks = 30
        return None
class Walker:
    def __init__(self, x, y, min_x, max_x, speed, size=32, shoot=False):
        self.min_x = min_x
        self.max_x = max_x
        self.speed_x = speed
        self.health = 10
        self.hit = 0
        self.rect = pygame.Rect(x, y, size, size)
        self.shoot = shoot
        self.bullets = []
        self.ticks = 50

    def draw(self, screen, x_offset, y_offset):
        if self.hit > 0:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(self.rect.x - x_offset, self.rect.y - y_offset, self.rect.width, self.rect.height))
            self.hit -= 1
        else:
            screen.blit(pygame.image.load("enemy_sprit.png"), pygame.Rect(self.rect.x - x_offset, self.rect.y - y_offset, self.rect.width, self.rect.height))

    def move(self):
        self.rect.x += self.speed_x

        if self.min_x > self.rect.x or self.rect.x > self.max_x:
            self.speed_x *= -1

    def update_hit(self, bullets):
        shot = []
        for bullet in bullets:
            if pygame.Rect.colliderect(bullet.rect, self.rect):
                self.health -= 1
                self.hit = 5
                shot.append(bullet)

        return shot

    def fire(self, x_off, y_off, screen, px, py):
        onscreen = 1024 > self.rect.x - x_off > 0 and 576 > self.rect.y - y_off > 0
        if self.ticks < 1 and onscreen:
            self.ticks = 50
            dx = px - self.rect.centerx
            dy = py - self.rect.centery
            angle = math.atan2(-dy, dx)
            bullet_speed_x = 5 * math.cos(angle)
            bullet_speed_y = -1 * 5 * math.sin(angle)
            return EnemyBullet(screen, self.rect.centerx, self.rect.centery, bullet_speed_x, bullet_speed_y)

        if onscreen:
            self.ticks -= 1
        else:
            self.ticks = 50
        return None


class Enemies:
    def __init__(self, screen, enemies):
        self.screen = screen
        self.enemies = enemies
        self.shots = []
        self.enemies_killed = 0

    def enemies_update(self, bullets, x, y, px, py):
        hit = []

        for enemy in self.enemies:
            enemy.move()
            enemy.draw(self.screen, x, y)
            if enemy.shoot:
                b = enemy.fire(x, y, self.screen, px, py)
                if b is not None:
                    self.shots.append(b)

            h = enemy.update_hit(bullets)

            if h is not None:
                for q in h:
                    hit.append(q)

            if enemy.health <= 0:
                self.enemies.remove(enemy)
                self.enemies_killed += 1

        for s in self.shots:
            s.move()
            s.draw(x, y)

        return hit

def bullet_hit_wall(level, bullets):
    for bullet in bullets:
        if bullet.collision(level):
            return bullet

    return None

class EnemyBullet:
    def __init__(self,screen,x=100,y=200,speed_x=6.0,speed_y=0.0,image = 'placeholder'):
        self.screen = screen
        self.image = image
        self.x = x
        self.y = y
        self.origin_x = x
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.pew = pygame.mixer.Sound('pewpew.wav')
        pygame.mixer.Sound.play(self.pew)


    def draw(self, x_offset, y_offset):
        if self.image == 'placeholder':
            pygame.draw.circle(self.screen,(255,100,100),(self.rect.centerx - x_offset, self.rect.centery - y_offset),10)
            self.rect = pygame.Rect(self.x, self.y, 10, 10)

        else:
            self.screen.blit(pygame.transform.scale(pygame.image.load(self.image),(7,7)), (self.x - x_offset, self.y - y_offset))

            self.rect = pygame.Rect(self.x, self.y, 5, 5)


    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def collision(self,rectangles):
        for rectangle in rectangles:
            if pygame.Rect.colliderect(self.rect, rectangle):
                return True

        return False