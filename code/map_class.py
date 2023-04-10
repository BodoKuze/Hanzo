import pygame
from platforms import *
import os
from png_class import Image_Pack

class Map:

    def __init__(self,master,block_map:list[int],enemy_map:list[int],add_map:list[int],assets) -> None:
        
        self.master = master
        self.block_map = block_map
        self.enemy_map = enemy_map
        self.add_map = add_map
        self.block_rect_map = []
        self.destructive_platform_sprites = Image_Pack(self.master,fr"{os.getcwd()}\sprites\ds_block.png",6,1,(50,300)).get_images()
        self.assets = assets


    def create_block_map(self):
        for y,row in enumerate(self.block_map):
            for x,block in enumerate(row):
                match block:
                    case 1:
                        self.block_rect_map.append(Construction(self.master,-3+x,4+y,self.assets[0]))

        return self.block_rect_map