import pygame

class Walker:
    def __init__(self, x, y, min_x, max_x, speed, size=32, health=10):
        self.min_x = min_x
        self.max_x = max_x
        self.speed_x = speed
        self.health = health
        self.hit = 0
        self.rect = pygame.Rect(x, y, size, size)
    def draw(self, screen):
        if self.hit > 0:
            pygame.draw.rect(screen, (255, 255, 255), self.rect)
            self.hit -= 1
        else:
            pygame.draw.rect(screen, (255, 0, 0), self.rect)

    def move(self):
        self.rect.x += self.speed_x

        if self.min_x > self.rect.x or self.rect.x > self.max_x:
            self.speed_x *= -1

    def update_hit(self, bullets):
        for bullet in bullets:
            if pygame.Rect.colliderect(bullet.rect, self.rect):
                self.health -= 1
                self.hit = 5
                return bullet

        return None

class Shooter:
    def __init__(self, x, y, min_x, max_x, speed, size=32, health=10):
        self.min_x = min_x
        self.max_x = max_x
        self.speed_x = speed
        self.health = health
        self.hit = 0
        self.rect = pygame.Rect(x, y, size, size)
    def draw(self, screen):
        if self.hit > 0:
            pygame.draw.rect(screen, (255, 255, 255), self.rect)
            self.hit -= 1
        else:
            pygame.draw.rect(screen, (255, 0, 0), self.rect)

    def move(self):
        self.rect.x += self.speed_x

        if self.min_x > self.rect.x or self.rect.x > self.max_x:
            self.speed_x *= -1

    def update_hit(self, bullets):
        for bullet in bullets:
            if pygame.Rect.colliderect(bullet.rect, self.rect):
                self.health -= 1
                self.hit = 5
                return bullet

        return None

class Enemies:
    def __init__(self, screen, enemies):
        self.screen = screen
        self.enemies = enemies

    def enemies_update(self, bullets):
        for enemy in self.enemies:
            enemy.move()
            enemy.draw(self.screen)
            hit = enemy.update_hit(bullets)

            if enemy.health <= 0:
                self.enemies.remove(enemy)

            if hit is not None:
                return hit

        return None