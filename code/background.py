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
        self.y_puffer = 200
        self.cloud_value_list = [
        {"i":-3, "x":200,"y":200,"s":0.05},
        {"i":-2, "x":500,"y":350,"s":0.075},
        {"i":-4, "x":0,"y":150,"s":0.1},
        {"i":-2, "x":600,"y":100,"s":0.15},
        ]
        self.cloud_speed = 0.1
    

    def update_cloud(self,scroll,dt):
        
    
        for i in self.cloud_value_list:
            

        
            if 800 >= i["x"]-scroll[0]*i["s"] >= -150:

                self.master.blit(pygame.transform.flip(self.assets1[i["i"]],False, False), (i["x"]-scroll[0]*i["s"], (i["y"]-scroll[1]*i["s"])+self.y_puffer))

            if  i["x"]-scroll[0]*i["s"] <= -150:
                i["x"] = 1000

            i["x"] -= self.cloud_speed

    def update(self,scroll,dt):
        self.master.fill((22, 22, 13))
        

        if dt % 10 == 0:
            self.dt += 1
        
        

        self.master.blit(pygame.transform.flip(self.assets1[self.dt % 5],False, False), (self.__asset_size.x-scroll[0]*self.delta_scroll_const, (self.__asset_size.y-scroll[1]*self.delta_scroll_const) +self.y_puffer))
        self.update_cloud(scroll,self.dt)