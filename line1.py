import pygame
from invader_line_1 import Invader10, Invader11, Invader12, Invader13, Invader14, Invader15
from invader_line_1 import Invader16, Invader17, Invader18, Invader19, Invader110

class ApparitionLine1:

    def __init__(self):
        self.all_invaders10 = pygame.sprite.Group()
        self.all_invaders11 = pygame.sprite.Group()
        self.all_invaders12 = pygame.sprite.Group()
        self.all_invaders13 = pygame.sprite.Group()
        self.all_invaders14 = pygame.sprite.Group()
        self.all_invaders15 = pygame.sprite.Group()
        self.all_invaders16 = pygame.sprite.Group()
        self.all_invaders17 = pygame.sprite.Group()
        self.all_invaders18 = pygame.sprite.Group()
        self.all_invaders19 = pygame.sprite.Group()
        self.all_invaders110 = pygame.sprite.Group()

    def dessin(self, screen):
        self.all_invaders10.draw(screen)
        self.all_invaders11.draw(screen)
        self.all_invaders12.draw(screen)
        self.all_invaders13.draw(screen)
        self.all_invaders14.draw(screen)
        self.all_invaders15.draw(screen)
        self.all_invaders16.draw(screen)
        self.all_invaders17.draw(screen)
        self.all_invaders18.draw(screen)
        self.all_invaders19.draw(screen)
        self.all_invaders110.draw(screen)

    def spawn_invader(self):
        self.all_invaders10.add(Invader10())
        self.all_invaders11.add(Invader11())
        self.all_invaders12.add(Invader12())
        self.all_invaders13.add(Invader13())
        self.all_invaders14.add(Invader14())
        self.all_invaders15.add(Invader15())
        self.all_invaders16.add(Invader16())
        self.all_invaders17.add(Invader17())
        self.all_invaders18.add(Invader18())
        self.all_invaders19.add(Invader19())
        self.all_invaders110.add(Invader110())
