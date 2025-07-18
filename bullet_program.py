import pygame
import sys

class Bullet:
    #origin is a tuple that contains coordinates (x,y)
    def __init__(self,screen,x=100,y=200,speed_x=6,speed_y=0,image = 'placeholder',damage=10):
        self.screen = screen
        self.image = image
        #Unsure if collision is necessary to create upon initialization.
        self.x = x
        self.y = y
        self.origin_x = x
        self.speed_x = speed_x
        self.speed_y = speed_y
        # hitbox is here for init
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.damage = damage
        self.pew = pygame.mixer.Sound('pewpew.wav')
        pygame.mixer.Sound.play(self.pew)


    def draw(self, x_offset, y_offset):
        if self.image == 'placeholder':
            pygame.draw.line(self.screen,(255,100,100),(self.x,self.y),(self.x+25,self.y),5)
            self.rect = pygame.Rect(self.x, self.y, 25, 5)

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

def debug():
    pygame.init()
    clock = pygame.time.Clock()

    pygame.display.init()
    pygame.display.set_caption('Bullet Debug')
    screen = pygame.display.set_mode((800,600))
    test_bullet = Bullet(screen,speed_y=2,image='Pistol.png')
    test_bullet2 = Bullet(screen,100,75,6)

    test_rect = pygame.rect.Rect(600,0,100,600)
    rectangles = []
    rectangles.append(test_rect)
    bullets = []
    bullets.append(test_bullet)
    bullets.append(test_bullet2)

    screen.fill((255,255,255))
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((255,255,255))
        pygame.draw.rect(screen,(255,0,0),test_rect)
        pygame.display.update()


if __name__ == "__main__":
    debug()



