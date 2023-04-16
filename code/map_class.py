import pygame
from platforms import *
from enemy import *
import os
from png_class import Image_Pack, Blit_Block
from stage_interactions import *

class Map:

    def __init__(self,master,block_map:list[int],assets) -> None:
        
        self.master = master
        self.block_map = block_map
        self.block_rect_map = []
        self.entety_map = []
        self.stage_i = []
        self.destructive_platform_sprites = Image_Pack(self.master,fr"{os.getcwd()}\sprites\ds_block.png",6,1,(50,300)).get_images()
        self.assets = assets
        self.lvl_clear = None

    def create_block_map(self):
        for y,row in enumerate(self.block_map):
            for x,block in enumerate(row):
                match block:
                    case 1:
                        self.block_rect_map.append(Construction(self.master,x,y,self.assets[0]))
                    case 2:
                        self.block_rect_map.append(Blit_Block(self.master,x,y,self.assets[0]))
                    case 3:
                        self.block_rect_map.append(penetrable_Platform(self.master,x,y,self.assets[8]))
                    case 4:
                        self.block_rect_map.append(destroy_Platform(self.master,x,y))
                    case 5:
                        self.block_rect_map.append(movable_Platform(self.master,x,y,self.assets[6]))
                    case 6:
                        self.block_rect_map.append(Construction(self.master,x,y,self.assets[1]))
                    case 7:
                        self.block_rect_map.append(Construction(self.master,x,y,self.assets[7]))
                    case 8:
                        self.block_rect_map.append(Blit_Block(self.master,x,y,self.assets[3]))
                    case 9:
                        self.block_rect_map.append(Blit_Block(self.master,x,y,self.assets[4]))
                    case 10:
                        self.entety_map.append(Bat(self.master,x,y))
                    case 11:
                        self.entety_map.append(Ronin(self.master,x,y))
                    case 12:
                        self.stage_i.append(Checkpoint(self.master,x,y))
                    case 13:
                        self.lvl_clear = Level_Clear(x,y)

        return self.block_rect_map,self.entety_map,self.stage_i,self.lvl_clear