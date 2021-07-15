import pygame
from projectile_player import ProjectilePlayer

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 3
        self.max_health = 3
        self.attack = 1
        self.velocity = 10
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/ufo.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = 510
        self.rect.y= 600

    def launch_projectile(self):
        self.all_projectiles.add(ProjectilePlayer(self))

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

