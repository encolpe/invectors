import pygame
from invader_line_2 import Invader20, Invader21, Invader22, Invader23, Invader24, Invader25
from invader_line_2 import Invader26, Invader27, Invader28, Invader29, Invader210

class ApparitionLine2:

    def __init__(self):
        self.all_invaders20 = pygame.sprite.Group()
        self.all_invaders21 = pygame.sprite.Group()
        self.all_invaders22 = pygame.sprite.Group()
        self.all_invaders23 = pygame.sprite.Group()
        self.all_invaders24 = pygame.sprite.Group()
        self.all_invaders25 = pygame.sprite.Group()
        self.all_invaders26 = pygame.sprite.Group()
        self.all_invaders27 = pygame.sprite.Group()
        self.all_invaders28 = pygame.sprite.Group()
        self.all_invaders29 = pygame.sprite.Group()
        self.all_invaders210 = pygame.sprite.Group()

    def dessin(self, screen):
        self.all_invaders20.draw(screen)
        self.all_invaders21.draw(screen)
        self.all_invaders22.draw(screen)
        self.all_invaders23.draw(screen)
        self.all_invaders24.draw(screen)
        self.all_invaders25.draw(screen)
        self.all_invaders26.draw(screen)
        self.all_invaders27.draw(screen)
        self.all_invaders28.draw(screen)
        self.all_invaders29.draw(screen)
        self.all_invaders210.draw(screen)

    def spawn_invader(self):
        self.all_invaders20.add(Invader20())
        self.all_invaders21.add(Invader21())
        self.all_invaders22.add(Invader22())
        self.all_invaders23.add(Invader23())
        self.all_invaders24.add(Invader24())
        self.all_invaders25.add(Invader25())
        self.all_invaders26.add(Invader26())
        self.all_invaders27.add(Invader27())
        self.all_invaders28.add(Invader28())
        self.all_invaders29.add(Invader29())
        self.all_invaders210.add(Invader210())