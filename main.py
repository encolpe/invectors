import pygame
import profile
from game import Game
pygame.init()

# definir une clock
clock = pygame.time.Clock()
FPS = 60

# generer la fenetre
pygame.display.set_caption("Space Invader")
screen = pygame.display.set_mode((1080, 720))

# fond d'ecran
background = pygame.image.load('assets/bgblue.jpg')
background = pygame.transform.scale(background, (1080, 720))

# banniere
banner = pygame.image.load('assets/title.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = 300
banner_rect.y = 0

# button play
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (700, 700))
play_button_rect = play_button.get_rect()
play_button_rect.x = 200
play_button_rect.y = 300


def main():
    game = Game()
    running = True
    while running:

        screen.blit(background, (0, 0))

        if game.is_playing:
            game.update(screen)
        else:
            screen.blit(play_button, play_button_rect)
            screen.blit(banner, banner_rect)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True

                if event.key == pygame.K_SPACE:
                    game.player.launch_projectile()
            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):
                    game.start()

        clock.tick(FPS)


if __name__ == '__main__':
    profile.run('main()')
