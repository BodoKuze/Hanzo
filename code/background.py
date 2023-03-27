from png_class import Image_Pack
import os
import pygame

class Background:
    def __init__(self,master) -> None:
        self.assets1 = Image_Pack(master,fr"{os.getcwd()}\sprites\night_assets.png",3,3,(900,900)).get_images()
        self.__asset_size = pygame.rect.Rect(50,50,300,300)
        self.master = master

    def update(self,scroll):
        
        self.master.blit(pygame.transform.flip(self.assets1[0], False, False), (self.__asset_size.x-scroll[0]*self.__asset_size.x, self.__asset_size.y-scroll[0]*self.__asset_size.y))