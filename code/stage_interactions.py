import pygame
from png_class import Image_Pack
import os


class Checkpoint:

    def __init__(self,master,x,y) -> None:
        self.master = master
        self.hit_box = pygame.rect.Rect(x*50,y*50,50,50)
        self.active = False
        self.dt = 0
        self.flip = False
        self.image_list=Image_Pack(self.master,fr"{os.getcwd()}\sprites\checkpoint.png",3,1,(50,150)).get_images() 

    def update(self,dt,scroll):

        
        if dt % 5 == 0:
            self.dt += 1



        if self.active:
            self.master.blit(pygame.transform.flip(self.image_list[self.dt % 3], self.flip, False), (self.hit_box.x-scroll[0], self.hit_box.y-scroll[1]))
        else:
            self.master.blit(pygame.transform.flip(self.image_list[0], self.flip, False), (self.hit_box.x-scroll[0], self.hit_box.y-scroll[1]))




class Level_Clear:

    def __init__(self) -> None:
        pass