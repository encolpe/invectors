import pygame
from invader_line_6 import Invader60, Invader61, Invader62, Invader63, Invader64, Invader65
from invader_line_6 import Invader66, Invader67, Invader68, Invader69, Invader610

class ApparitionLine6:

    def __init__(self):
        self.all_invaders60 = pygame.sprite.Group()
        self.all_invaders61 = pygame.sprite.Group()
        self.all_invaders62 = pygame.sprite.Group()
        self.all_invaders63 = pygame.sprite.Group()
        self.all_invaders64 = pygame.sprite.Group()
        self.all_invaders65 = pygame.sprite.Group()
        self.all_invaders66 = pygame.sprite.Group()
        self.all_invaders67 = pygame.sprite.Group()
        self.all_invaders68 = pygame.sprite.Group()
        self.all_invaders69 = pygame.sprite.Group()
        self.all_invaders610 = pygame.sprite.Group()

    def dessin(self, screen):
        self.all_invaders60.draw(screen)
        self.all_invaders61.draw(screen)
        self.all_invaders62.draw(screen)
        self.all_invaders63.draw(screen)
        self.all_invaders64.draw(screen)
        self.all_invaders65.draw(screen)
        self.all_invaders66.draw(screen)
        self.all_invaders67.draw(screen)
        self.all_invaders68.draw(screen)
        self.all_invaders69.draw(screen)
        self.all_invaders610.draw(screen)

    def spawn_invader(self):
        self.all_invaders60.add(Invader60())
        self.all_invaders61.add(Invader61())
        self.all_invaders62.add(Invader62())
        self.all_invaders63.add(Invader63())
        self.all_invaders64.add(Invader64())
        self.all_invaders65.add(Invader65())
        self.all_invaders66.add(Invader66())
        self.all_invaders67.add(Invader67())
        self.all_invaders68.add(Invader68())
        self.all_invaders69.add(Invader69())
        self.all_invaders610.add(Invader610())