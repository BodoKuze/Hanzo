import pygame
from platforms import *
import os
from png_class import Image_Pack

class Map:

    def __init__(self,master,block_map:list[int],add_map:list[int],enemy_map:list[int],assets) -> None:
        
        self.master = master
        self.block_map = block_map
        self.enemy_map = enemy_map
        self.add_map = add_map
        self.block_rect_map = []
        self.block_add_map = []
        self.destructive_platform_sprites = Image_Pack(self.master,fr"{os.getcwd()}\sprites\ds_block.png",6,1,(50,300)).get_images()
        self.assets = assets
        self.dec = Image_Pack(self.master,fr"{os.getcwd()}\sprites\decoration.png",6,1,(50,300)).get_images()
        self.dec2 = Image_Pack(self.master,fr"{os.getcwd()}\sprites\background_tiles.png",3,1,(50,300)).get_images()

    def create_block_map(self):
        for y,row in enumerate(self.block_map):
            for x,block in enumerate(row):
                match block:
                    case 1:
                        self.block_rect_map.append(Construction(self.master,-3+x,1+y,self.assets[0]))
                    case 2:
                        self.block_rect_map.append(Construction(self.master,-3+x,1+y,self.assets[5]))
                    case 3:
                        self.block_rect_map.append(penetrable_Platform(self.master,-3+x,1+y,self.assets[7]))

        
        return self.block_rect_map
    
    def create_add_map(self):
        for y,row in enumerate(self.add_map):
            for x,block in enumerate(row):
                match block:    
                    case 1:
                        self.block_add_map.append(Blit_Block(self.master,-3+x,1+y,self.assets,5))
                    case 3:
                        self.block_add_map.append(Blit_Block(self.master,-3+x,1+y,self.dec2,0))
                    case 4:
                        self.block_add_map.append(Blit_Block(self.master,-3+x,1+y,self.dec2,1))
                    case 5:
                        self.block_add_map.append(Blit_Block(self.master,-3+x,1+y,self.dec2,2))

                    case "A":
                        self.block_add_map.append(Blit_Block(self.master,-3+x,1+y,self.dec,0))
                    case "B":
                        self.block_add_map.append(Blit_Block(self.master,-3+x,1+y,self.dec,1))
                    case "C":
                        self.block_add_map.append(Blit_Block(self.master,-3+x,1+y,self.dec,2))
                    case "D":
                        self.block_add_map.append(Blit_Block(self.master,-3+x,1+y,self.dec,3))
                    case "E":
                        self.block_add_map.append(Blit_Block(self.master,-3+x,1+y,self.dec,4))
                    case "F":
                        self.block_add_map.append(Blit_Block(self.master,-3+x,1+y,self.dec,5))
        
        return self.block_add_map