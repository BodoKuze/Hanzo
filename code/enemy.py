import pygame
import os
from png_class import Image_Pack
from math import sin


#Ey sry. Hab dir jetzt erstmal eine Vorlage gegeben für einen Gegner... 

class Bat:

    def __init__(self,master,x,y) -> None:
        self.master = master
        self.y = y
        self.hit_box = pygame.rect.Rect(x,y,50,50)
        self.image_list = Image_Pack(self.master,fr"{os.getcwd()}\sprites\bat.png",3,1,(50,150)).get_images() 
        self.flip = False
        self.dt = 0
        self.spd = 2

    def update(self,dt,scroll):
        self.update_app(scroll)

        if dt % 10 == 0:
            self.dt += 1

        self.hit_box.x += self.spd

        if self.hit_box.x > 800:
            self.hit_box.x = -500

        self.curve()
    

    def update_app(self,scroll):
        self.master.blit(pygame.transform.flip(self.image_list[self.dt % 3], self.flip, False), (self.hit_box.x-scroll[0], self.hit_box.y-scroll[1]))
        pygame.draw.rect(self.master,(255,0,0),pygame.rect.Rect(self.hit_box.x-scroll[0], self.hit_box.y-scroll[1], self.hit_box.width,self.hit_box.height),2)

    def curve(self):
        self.hit_box.y = self.y + sin(self.hit_box.x/50)*150