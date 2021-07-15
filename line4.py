import pygame
from invader_line_4 import Invader40, Invader41, Invader42, Invader43, Invader44, Invader45
from invader_line_4 import Invader46, Invader47, Invader48, Invader49, Invader410

class ApparitionLine4:

    def __init__(self):
        self.all_invaders40 = pygame.sprite.Group()
        self.all_invaders41 = pygame.sprite.Group()
        self.all_invaders42 = pygame.sprite.Group()
        self.all_invaders43 = pygame.sprite.Group()
        self.all_invaders44 = pygame.sprite.Group()
        self.all_invaders45 = pygame.sprite.Group()
        self.all_invaders46 = pygame.sprite.Group()
        self.all_invaders47 = pygame.sprite.Group()
        self.all_invaders48 = pygame.sprite.Group()
        self.all_invaders49 = pygame.sprite.Group()
        self.all_invaders410 = pygame.sprite.Group()

    def dessin(self, screen):
        self.all_invaders40.draw(screen)
        self.all_invaders41.draw(screen)
        self.all_invaders42.draw(screen)
        self.all_invaders43.draw(screen)
        self.all_invaders44.draw(screen)
        self.all_invaders45.draw(screen)
        self.all_invaders46.draw(screen)
        self.all_invaders47.draw(screen)
        self.all_invaders48.draw(screen)
        self.all_invaders49.draw(screen)
        self.all_invaders410.draw(screen)

    def spawn_invader(self):
        self.all_invaders40.add(Invader40())
        self.all_invaders41.add(Invader41())
        self.all_invaders42.add(Invader42())
        self.all_invaders43.add(Invader43())
        self.all_invaders44.add(Invader44())
        self.all_invaders45.add(Invader45())
        self.all_invaders46.add(Invader46())
        self.all_invaders47.add(Invader47())
        self.all_invaders48.add(Invader48())
        self.all_invaders49.add(Invader49())
        self.all_invaders410.add(Invader410())