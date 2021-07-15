import pygame

class ProjectilePlayer(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.velocity = 20
        self.attack = 1
        self.image = pygame.image.load('assets/projectile_player.png')
        self.image = pygame.transform.scale(self.image, (150, 60))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x - 45
        self.rect.y = player.rect.y - 30

    def move(self):
        self.rect.y -= self.velocity

