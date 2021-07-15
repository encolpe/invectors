import pygame
from invader_line_5 import Invader50, Invader51, Invader52, Invader53, Invader54, Invader55
from invader_line_5 import Invader56, Invader57, Invader58, Invader59, Invader510

class ApparitionLine5:

    def __init__(self):
        self.all_invaders50 = pygame.sprite.Group()
        self.all_invaders51 = pygame.sprite.Group()
        self.all_invaders52 = pygame.sprite.Group()
        self.all_invaders53 = pygame.sprite.Group()
        self.all_invaders54 = pygame.sprite.Group()
        self.all_invaders55 = pygame.sprite.Group()
        self.all_invaders56 = pygame.sprite.Group()
        self.all_invaders57 = pygame.sprite.Group()
        self.all_invaders58 = pygame.sprite.Group()
        self.all_invaders59 = pygame.sprite.Group()
        self.all_invaders510 = pygame.sprite.Group()

    def dessin(self, screen):
        self.all_invaders50.draw(screen)
        self.all_invaders51.draw(screen)
        self.all_invaders52.draw(screen)
        self.all_invaders53.draw(screen)
        self.all_invaders54.draw(screen)
        self.all_invaders55.draw(screen)
        self.all_invaders56.draw(screen)
        self.all_invaders57.draw(screen)
        self.all_invaders58.draw(screen)
        self.all_invaders59.draw(screen)
        self.all_invaders510.draw(screen)

    def spawn_invader(self):
        self.all_invaders50.add(Invader50())
        self.all_invaders51.add(Invader51())
        self.all_invaders52.add(Invader52())
        self.all_invaders53.add(Invader53())
        self.all_invaders54.add(Invader54())
        self.all_invaders55.add(Invader55())
        self.all_invaders56.add(Invader56())
        self.all_invaders57.add(Invader57())
        self.all_invaders58.add(Invader58())
        self.all_invaders59.add(Invader59())
        self.all_invaders510.add(Invader510())