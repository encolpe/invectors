import pygame
from invader_line_3 import Invader30, Invader31, Invader32, Invader33, Invader34, Invader35
from invader_line_3 import Invader36, Invader37, Invader38, Invader39, Invader310

class ApparitionLine3:

    def __init__(self):
        self.all_invaders30 = pygame.sprite.Group()
        self.all_invaders31 = pygame.sprite.Group()
        self.all_invaders32 = pygame.sprite.Group()
        self.all_invaders33 = pygame.sprite.Group()
        self.all_invaders34 = pygame.sprite.Group()
        self.all_invaders35 = pygame.sprite.Group()
        self.all_invaders36 = pygame.sprite.Group()
        self.all_invaders37 = pygame.sprite.Group()
        self.all_invaders38 = pygame.sprite.Group()
        self.all_invaders39 = pygame.sprite.Group()
        self.all_invaders310 = pygame.sprite.Group()

    def dessin(self, screen):
        self.all_invaders30.draw(screen)
        self.all_invaders31.draw(screen)
        self.all_invaders32.draw(screen)
        self.all_invaders33.draw(screen)
        self.all_invaders34.draw(screen)
        self.all_invaders35.draw(screen)
        self.all_invaders36.draw(screen)
        self.all_invaders37.draw(screen)
        self.all_invaders38.draw(screen)
        self.all_invaders39.draw(screen)
        self.all_invaders310.draw(screen)

    def spawn_invader(self):
        self.all_invaders30.add(Invader30())
        self.all_invaders31.add(Invader31())
        self.all_invaders32.add(Invader32())
        self.all_invaders33.add(Invader33())
        self.all_invaders34.add(Invader34())
        self.all_invaders35.add(Invader35())
        self.all_invaders36.add(Invader36())
        self.all_invaders37.add(Invader37())
        self.all_invaders38.add(Invader38())
        self.all_invaders39.add(Invader39())
        self.all_invaders310.add(Invader310())