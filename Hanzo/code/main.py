from player import * 
from png_class import Image_Pack
import os
from random import randint
import pygame

pygame.font.init()
pyg = pygame
FONT = pygame.font.Font(fr"{os.getcwd()}\Hanzo\font\EndlessBossBattleRegular-v7Ey.ttf",30)
FPS = 60
WIDTH = 800
HEIGHT = 600

pygame.display.set_caption("Panic Run")
WIN = pygame.display.set_mode((WIDTH,HEIGHT))


Ninja = Player(WIN,pyg.K_w,pyg.K_s,pyg.K_a,pyg.K_d,pyg.K_SPACE,pyg.K_KP_ENTER,50,50) 

def main():
    clock = pygame.time.Clock()
    spielen = True
    dt = 3
    dt_anim = 0
    while spielen:
        dt += 1
        clock.tick(FPS)
        
        WIN.fill((0, 0, 0))

        Ninja.update(dt,[pygame.Rect(0,0,0,0)])
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                spielen = False

        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()