import pygame
import sys
import tiles as level

class Player:
    GRAVITY = 1
    HIT_COLOR = pygame.Color("white")

    def __init__(self, x, y, width, height):
        self.start = (x, y)
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
        self.fall_count = 0
        self.jump_count = 0
        self.surface = pygame.Surface((self.rect.width, self.rect.height))
        self.hit_surface = pygame.Surface((self.rect.width, self.rect.height))
        self.hit_surface.fill(self.HIT_COLOR)
        self.player_health = 10
        self.hit = 0
        self.deaths = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def jump(self):
        if 0.5 > self.y_vel > -0.5 or self.jump_count > 0:
            self.y_vel = -self.GRAVITY * 8
            self.jump_count += 1

        if self.jump_count == 1:
            self.fall_count = 0

    def loop(self, fps):
        self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
        self.move(self.x_vel, self.y_vel)

        self.fall_count += 1

    def landed(self):
        self.fall_count = 0
        self.y_vel = 0
        self.jump_count = 0

    def hit_head(self):
        self.y_vel *= -0.5

    def handle_death(self, objects):
        obj = []
        for danger in objects:
            if danger.__class__ == pygame.Rect:
                if pygame.Rect.colliderect(danger, self.rect):
                    obj.append(danger)
                    self.player_health -= 5
                    self.hit = 5
            else:
                if pygame.Rect.colliderect(danger.rect, self.rect):
                    obj.append(danger)
                    self.player_health -= 1
                    self.hit = 5

        if self.player_health < 1:
            self.player_health = 10
            self.rect.x = self.start[0]
            self.rect.y = self.start[1]
            self.deaths += 1

        return obj


    def draw(self, screen, x_offset, y_offset):
        surface = self.surface
        surface.fill((abs(self.player_health - 10) * 255 // 10, 0, self.player_health * 255 // 10))
        if self.hit > 0:
            surface = self.hit_surface
            self.hit -= 1

        screen.blit(surface, (self.rect.x - x_offset, self.rect.y - y_offset))


def handle_move(player, objects):
    keys = pygame.key.get_pressed()

    col_left = collide(player, objects, -5)
    col_right = collide(player, objects, 5)

    player.x_vel = 0
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and not col_left:
        player.move_left(5)
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and not col_right:
        player.move_right(5)

    handle_vertical(player, objects, player.y_vel)

def handle_vertical(player, objects, dy):
    collisions = []
    for rect in objects:
        if pygame.Rect.colliderect(player.rect, rect):
            if dy > 0:
                player.rect.bottom = rect.top
                player.landed()
            elif dy < 0:
                player.rect.top = rect.bottom
                player.hit_head()

        collisions.append(rect)

    return collisions

def collide(player, objects, dx):
    player.move(dx, 0)

    collision = None

    for rect in objects:
        if pygame.Rect.colliderect(player.rect, rect):
            collision = rect

    player.move(-dx, 0)
    return collision

# This function is called when you run this file, and is used to test the Character class individually.
# When you create more files with different classes, copy the code below, then
# change it to properly test that class
def test_player():
    pygame.init()
    pygame.display.set_caption("Platformer Test")
    screen = pygame.display.set_mode((1024, 576))
    clock = pygame.time.Clock()

    player = Player(100, 100, 32, 32)

    tile = level.Tile(0,screen)
    tiles = [tile]*17 + [0]*14 + [tile]*2 + [0]*14 + [tile]*2 + [0]*14 + [tile]*2 + [0]*15 + [tile] + [0]*15 + [tile] + [0]*15 + [tile] + [0]*15 + [tile] * 17
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

        handle_move(player, room.rect_tiles)
        player.draw(screen)
        room.draw()
        pygame.display.update()


# Testing the classes
# click the green arrow to the left or run "Current File" in PyCharm to test this class
if __name__ == "__main__":
    test_player()
