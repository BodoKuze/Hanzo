import os
import pygame
from main_game import Game

pygame.font.init()
pyg = pygame
FONT = pygame.font.Font(fr"{os.getcwd()}\font\EndlessBossBattleRegular-v7Ey.ttf",30)

FPS = 60
WIDTH = 800
HEIGHT = 800

pygame.display.set_caption("Hanzo")
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

game = Game(WIN,WIDTH,HEIGHT)

def main():
    clock = pygame.time.Clock()
    playing = True
    dt = 0

    while playing:
        dt += 1
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
        

        
        game.update_elias(event,clock)
        
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()