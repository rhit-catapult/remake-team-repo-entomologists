import pygame

class Walker:
    def __init__(self, x, y, min_x, max_x, speed, size):
        self.x = x
        self.y = y
        self.min_x = min_x
        self.max_x = max_x
        self.speedx = speed
        self.health = 5
        self.hitbox = pygame.Rect(self.x, self.y, size, size)
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox)

    def move(self):
        self.x += self.speedx

        if self.min_x > self.x > self.max_x:
            self.speedx *= -1

    def update_hit(self, bullets):
        for bullet in bullets:
            if pygame.Rect.colliderect(bullet.rect, self.hitbox):
                self.health -= 1
                return bullet

        return None

class Enemies:
    def __init__(self, screen, enemies):
        self.screen = screen
        self.enemies = enemies

    def enemies_update(self, bullets):
        for enemy in self.enemies:
            enemy.draw(self.screen)
            enemy.move()
            hit = enemy.update_hit(bullets)

            if enemy.health <= 0:
                self.enemies.remove(enemy)

            if hit is not None:
                return hit

        return None