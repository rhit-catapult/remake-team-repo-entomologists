import pygame
import sys
pygame.init()
class Bullet:
    #origin is a tuple that contains coordinates (x,y)
    def __init__(self,screen,x=100,y=200,speed_x=6,speed_y=0,image = 'placeholder'):
        self.screen = screen
        self.image = image
        #Unsure if collision is necessary to create upon initialization.
        self.x = x
        self.y = y
        self.origin_x = x
        self.speed_x = speed_x
        self.speed_y = speed_y
        # hitbox is here for init
        self.hitbox = pygame.Rect(0,0,0,0)

    def draw(self):
        if self.image == 'placeholder':
            pygame.draw.line(self.screen,(255,100,100),(self.x,self.y),(self.x+25,self.y),5)
            self.hitbox = pygame.Rect(self.x,self.y,25,5)

        else:
            self.screen.blit(pygame.image.load(self.image),(self.x, self.y))

            self.hitbox = (pygame.image.load(self.image)).get_rect()

            self.hitbox.move_ip(self.x,self.y)


    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        
    def collision(self,rectangles):
        for rectangle in rectangles:
            if pygame.Rect.colliderect(self.hitbox, rectangle):
                return True
        else:
            return False

def bullet_update(bullets,rectangles):
    for bullet in bullets:
        remove_bullet = False
        bullet.move()
        bullet.draw()
        if bullet.collision(rectangles):
            remove_bullet = True


        if bullet.x > bullet.origin_x + 1000:

            remove_bullet = True
        if remove_bullet:
            bullets.remove(bullet)
            del bullet


def debug():
    pygame.init()
    clock = pygame.time.Clock()

    pygame.display.init()
    pygame.display.set_caption('Bullet Debug')
    screen = pygame.display.set_mode((800,600))
    test_bullet = Bullet(screen,image='Pistol.png')
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
        bullet_update(bullets,rectangles)
        pygame.display.update()
debug()




