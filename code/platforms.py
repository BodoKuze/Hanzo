import pygame
from player import Player
from png_class import Image_Pack

import os
        




class Construction:

    def __init__(self,master,x:int,y:int,image) -> None:
        self.hit_box = pygame.rect.Rect(x*50,y*50,50,50)
        self.master = master
        self.image = image
        

    def update(self,Player:Player,scroll:list[int,int]):
        self.update_app(scroll) 
        
        
    def update_app(self,scroll):
        
        
        if -50<= self.hit_box.x-scroll[0] <800 or -50<= self.hit_box.y-scroll[1] <800:
            self.master.blit(self.image, ((self.hit_box.x)-scroll[0], (self.hit_box.y)-scroll[1]))

            





class penetrable_Platform():

    def __init__(self, master, x, y,image) -> None:

        self.hit_box = pygame.rect.Rect(x*50,y*50,50,50)
        self.height = 50
        self.master = master
        self.going_trough = False
        self.image = image

    def update(self,Player:Player,scroll:list[int,int]):
        

        if (Player.hit_box.y+Player.hit_box.height-1 > self.hit_box.y) or (Player.ducking):
            self.going_trough = True
            self.hit_box.height = 0

        else:
            self.hit_box.height = 50
            self.going_trough = False

        self.update_app(scroll)
        

    def update_app(self,scroll:list[int,int]):

        
        
        if -50<= self.hit_box.x-scroll[0] <800 or -50<= self.hit_box.y-scroll[1] <800:
            self.master.blit(self.image, (self.hit_box.x-scroll[0], self.hit_box.y-scroll[1]))



        
    
class movable_Platform(Construction):

    def __init__(self, master, x, y, image):
        self.hit_box = pygame.rect.Rect(x*50,y*50,50,50)
        self.master = master
        self.__x = x*50
        self.image = image
        self.distance_blocks = 5
        self.speed = 2

    def player_movement(self,hit_box:pygame.rect.Rect):
        return self.hit_box.y == hit_box.y + hit_box.height and self.hit_box.x - hit_box.width <= hit_box.x <= self.hit_box.x + self.hit_box.width

    def update(self, Player: Player,scroll:list[int,int]):
        
        
        self.hit_box.x += self.speed

        if self.__x + self.distance_blocks*50  >= self.hit_box.x:
            self.speed *= -1
        
        

        if self.hit_box.x >= self.__x:
            self.speed *= -1

        if self.player_movement(Player.hit_box):
            Player.hit_box.x += self.speed

        self.update_app(scroll)
        
    def update_app(self,scroll:list[int,int]):
        return super().update_app(scroll)
    
class destroy_Platform(Construction):
    

    def __init__(self, master, x, y) -> None:
        self.master = master
        self.height = 50
        self.hit_box = pygame.rect.Rect(x*50,y*50,50,50)
        self.hbc = 0
        self.__time = 20
        self.time = self.__time
        self.__recover_time = 6
        self.touched = False
        self.image_list = Image_Pack(self.master,fr"{os.getcwd()}\sprites\ds_block.png",6,1,(50,300)).get_images()

    def player_movement(self,hit_box:pygame.rect.Rect):
        return self.hit_box.y == hit_box.y + hit_box.height and self.hit_box.x - hit_box.width <= hit_box.x <= self.hit_box.x + self.hit_box.width 

    def update(self, Player: Player,scroll:list[int,int]):
        
        self.if_standing_on(Player.hit_box)
        self.update_app(scroll)

    def update_app(self,scroll:list[int,int]):

        image = 0
        block_blit = True

        if self.time == self.__time:
            image = 0

        elif self.time >= self.__time * (3/4):
            image = 1

        elif self.time >= self.__time * (2/4):
            image = 2
        
        elif self.time >= self.__time * (1/4):
            image = 3
        
        else:
            image = 4

        if block_blit:
            self.master.blit(self.image_list[image], (self.hit_box.x  - scroll[0], self.hit_box.y- scroll[1]))

        if self.hbc >= 255:
            self.hbc = 255
        
        
        

    


            
    def if_standing_on(self,hit_box:pygame.rect.Rect):
        
        if self.player_movement(hit_box):
            self.touched = True


        if self.touched:
            self.time -= 1
            self.hbc += (255)/(self.__time)

            if self.time == 0:
                self.hit_box.height = 0

            elif self.time <= self.__recover_time * -60:
                self.touched = False
                self.time = self.__time
                self.hit_box.height = 50
                self.hbc = 0



        
   