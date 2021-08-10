import pygame

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800

TYPE_SMALL = 1
TYPE_MIDDLE = 2
TYPE_BIG = 3

class Bullet(pygame.sprite.Sprite):
    def __init__(self, BULLET_IMAGES, initial_position):
        pygame.sprite.Sprite.__init__(self)
        self.image = BULLET_IMAGES
        self.rect = self.image.get_rect()
        self.rect.midbottom = initial_position
        self.speed = 10

    def move(self):
        self.rect.top -= self.speed

class Opponent(pygame.sprite.Sprite):
    def __init__(self, AIRCRAFT_IMAGES, AIRCRAFT_PLAYER, initial_position):
        pygame.sprite.Sprite.__init__(self)
        self.image = []
        for i in range(len(AIRCRAFT_PLAYER)):
            self.image.append(AIRCRAFT_IMAGES.subsurface(AIRCRAFT_PLAYER[i]).convert_alpha())
        self.rect = AIRCRAFT_PLAYER[0]
        self.rect.topleft = initial_position
        self.speed = 8
        self.bullets = pygame.sprite.Group()
        self.img_index = 0
        self.is_hit = False

    def shoot(self, BULLET_IMAGES):
        bullet = Bullet(BULLET_IMAGES, self.rect.midtop)
        self.bullets.add(bullet)

    def moveUp(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        else:
            self.rect.top -= self.speed

    def moveDown(self):
        if self.rect.top >= SCREEN_HEIGHT - self.rect.height:
            self.rect.top = SCREEN_HEIGHT - self.rect.height
        else:
            self.rect.top += self.speed

    def moveLeft(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed

    def moveRight(self):
        if self.rect.left >= SCREEN_WIDTH - self.rect.width:
            self.rect.left = SCREEN_WIDTH - self.rect.width
        else:
            self.rect.left += self.speed

class Challenger(pygame.sprite.Sprite):
    def __init__(self, opponent_resource, opponent_down_resources, init_pos):
       pygame.sprite.Sprite.__init__(self)
       self.image = opponent_resource
       self.rect = self.image.get_rect()
       self.rect.topleft = init_pos
       self.down_imgs = opponent_down_resources
       self.speed = 2
       self.down_index = 0

    def move(self):
        self.rect.top += self.speed