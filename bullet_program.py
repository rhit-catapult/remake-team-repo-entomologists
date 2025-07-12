import pygame
import sys
pygame.init()
class Bullet:
    #origin is a tuple that contains coordinates (x,y)
    def __init__(self,screen,image = 'placeholder',x=100,y=200,speed_x=6,speed_y=0):
        self.screen = screen
        self.image = image
        #Unsure if collision is necessary to create upon initialization.
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y


    def draw(self):
        if self.image == 'placeholder':
            pygame.draw.line(self.screen,(255,100,100),(self.x,self.y),(self.x+25,self.y),5)
        else:
            self.screen.blit(self.image,(self.x, self.y))
            hitbox = pygame.image.load(self.image).get_rect()

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y



def debug():
    pygame.init()
    clock = pygame.time.Clock()

    pygame.display.init()
    pygame.display.set_caption('Bullet Debug')
    screen = pygame.display.set_mode((800,600))
    test_bullet = Bullet(screen)
    screen.fill((255,255,255))
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((255,255,255))
        test_bullet.move()
        test_bullet.draw()
        pygame.display.update()
debug()




