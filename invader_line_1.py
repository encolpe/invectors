import pygame

class Invader10(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 1
        self.max_health = 1
        self.velocity = 2
        self.image = pygame.image.load('assets/invader10.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.rect.y = 200

    def forward(self):
        self.rect.y += self.velocity

class Invader11(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 1
        self.max_health = 1
        self.velocity = 1
        self.image = pygame.image.load('assets/invader10.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = 740
        self.rect.y = 200

    def forward(self):
        self.rect.y += self.velocity

class Invader12(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 1
        self.max_health = 1
        self.velocity = 1
        self.image = pygame.image.load('assets/invader10.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = 680
        self.rect.y = 200

    def forward(self):
        self.rect.y += self.velocity

class Invader13(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 1
        self.max_health = 1
        self.velocity = 1
        self.image = pygame.image.load('assets/invader10.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = 620
        self.rect.y = 200

    def forward(self):
        self.rect.y += self.velocity

class Invader14(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 1
        self.max_health = 1
        self.velocity = 1
        self.image = pygame.image.load('assets/invader10.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = 560
        self.rect.y = 200

    def forward(self):
        self.rect.y += self.velocity

class Invader15(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 1
        self.max_health = 1
        self.velocity = 1
        self.image = pygame.image.load('assets/invader10.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 200

    def forward(self):
        self.rect.y += self.velocity


class Invader16(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 1
        self.max_health = 1
        self.velocity = 1
        self.image = pygame.image.load('assets/invader10.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = 440
        self.rect.y = 200

    def forward(self):
        self.rect.y += self.velocity


class Invader17(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 1
        self.max_health = 1
        self.velocity = 0
        self.image = pygame.image.load('assets/invader10.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = 380
        self.rect.y = 200

    def forward(self):
        self.rect.y += self.velocity


class Invader18(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 1
        self.max_health = 1
        self.velocity = 1
        self.image = pygame.image.load('assets/invader10.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = 320
        self.rect.y = 200

    def forward(self):
        self.rect.y += self.velocity


class Invader19(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 1
        self.max_health = 1
        self.velocity = 1
        self.image = pygame.image.load('assets/invader10.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = 260
        self.rect.y = 200

    def forward(self):
        self.rect.y += self.velocity


class Invader110(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 1
        self.max_health = 1
        self.velocity = 1
        self.image = pygame.image.load('assets/invader10.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 200

    def forward(self):
        self.rect.y += self.velocity





