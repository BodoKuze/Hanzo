from png_class import Image_Pack
import os
import pygame
from random import randint

class Background:
    def __init__(self,master) -> None:
        self.assets1 = Image_Pack(master,fr"{os.getcwd()}\sprites\night_assets.png",3,3,(300,300)).get_images()
        self.__asset_size = pygame.rect.Rect(250,50,100,100)
        self.master = master
        self.delta_scroll_const = 0.025
        self.dt = 0
        self.cloud_value_list = [{"i":randint(1,3)*-1, "x":randint(0,400),"y":randint(0,400),"s":randint(2,6)/10} for i in range(7)]

        

    def update_cloud(self,scroll):
        for i in self.cloud_value_list:
            self.master.blit(pygame.transform.flip(self.assets1[i["i"]],False, False), (i["x"]-scroll[0]*i["s"], i["y"]-scroll[1]*i["s"]))


    def update(self,scroll,dt):
        self.master.fill((22, 22, 13))
        

        if dt % 10 == 0:
            self.dt += 1
        
        self.master.blit(pygame.transform.flip(self.assets1[0],False, False), (self.__asset_size.x-scroll[0]*self.delta_scroll_const, self.__asset_size.y-scroll[1]*self.delta_scroll_const))
        self.update_cloud(scroll)