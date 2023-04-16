import os
import pygame
from random import choice, randint
import time
import math
from png_class import Image_Pack

class Star:

    def __init__(self, master, x, y, t):
        self.duration = t
        size = choice([1, 2, 3])
        self.hit_box = pygame.rect.Rect(x, y, size, size)
        self.master = master
        self.dt = 0.0007
        self.c = (randint(200, 255), randint(200, 255), randint(200, 255))
        
    def update(self, dt):
        if dt % self.duration != 0:
            pygame.draw.rect(self.master, self.c, self.hit_box)


class Background:
    def __init__(self,master) -> None:
        
        self.asset_1 = Image_Pack(master,fr"{os.getcwd()}\sprites\night_assets.png",3,3,(300,300)).get_images()
        self.asset_2 = Image_Pack(master,fr"{os.getcwd()}\sprites\sunset_assets.png",3,3,(300,300)).get_images()
        self.asset_3 = Image_Pack(master,fr"{os.getcwd()}\sprites\day_assets.png",3,3,(300,300)).get_images()
        self.asset_main = self.asset_1
        self.montains = Image_Pack(master,fr"{os.getcwd()}\sprites\background_montains.png",3,1,(1000,600)).get_images()
        self.evening = False
        self.day = False
        self.night = False
        self.time_mvnt = False
        self.sun_hit_box =pygame.rect.Rect(0,0,100,100)
        self.master = master
        self.delta_scroll_const = 0.000025
        self.dt = 1
        self.y_puffer = 200
        self.cloud_value_list = [
        {"i":-3, "x":200,"y":200,"s":0.05},
        {"i":-2, "x":500,"y":350,"s":0.075},
        {"i":-4, "x":0,"y":150,"s":0.1},
        {"i":-2, "x":600,"y":100,"s":0.15},
        ]
        self.cloud_speed = 0.1
        self.star_list = [Star(master,randint(0,800),randint(0,800),randint(20,100)) for i in range(60)]
        self.day_time = 22
        time = self.time_minimization([0,6,8,12,19,21],self.day_time)
        self.background_color_per_time = {
            0:[0, 0, 0],
            6:[255,135,92],
            8:[77,166,255],
            12:[77,166,255],
            19:[255,135,102],
            21:[0, 0, 0],
        }
        self.montains_asset = 0
        self.bg_color = self.background_color_per_time[time]

    def time_minimization(self, nums: list[int], zahl: int) -> int:
        smallest_num = [x for x in nums if x <= zahl]
        return max(smallest_num, default=zahl) if smallest_num else zahl

    def update_cloud(self,scroll):
        
    
        for i in self.cloud_value_list:
            

            if 800 >= i["x"]-scroll[0]*i["s"] >= -150:

                self.master.blit(pygame.transform.flip(self.asset_main[i["i"]],False, False), (i["x"]-scroll[0]*i["s"], (i["y"]-scroll[1]*i["s"])+self.y_puffer))

            if  i["x"]-scroll[0]*i["s"] <= -150:
                i["x"] = 1000

            i["x"] -= self.cloud_speed

        

    def update(self,scroll,dt):
        
        if dt % 10 == 0:
            self.dt += 1
        if self.time_mvnt: 
            if dt % 300 == 0:
                self.day_time += 1

        self.time_cycle(scroll)
        self.background_obj(scroll)
        self.update_cloud(scroll)

        
    def curve_s(self,x):
        return (((x-350))**(2))/160 + 135


    def check_background_color(self):
        time = self.time_minimization([0,6,8,12,19,21],self.day_time)

        if self.dt % 2 == 0:  
            
            for i,j in enumerate(self.bg_color):
                if self.background_color_per_time[time][i] != j:
                    if j < self.background_color_per_time[time][i]:
                        self.bg_color[i] += 1
                    elif j > self.background_color_per_time[time][i]:
                        self.bg_color[i] -= 1

       
    def background_obj(self,scroll):

        self.master.blit(pygame.transform.flip(self.montains[self.montains_asset],False, False), (-100-scroll[0]*0.009, (200)+self.y_puffer))
        if self.evening:
            pygame.draw.rect(self.master,[230,125,82],pygame.rect.Rect(0,400+self.y_puffer,800,400))
        if self.day:
            pygame.draw.rect(self.master,[57,146,255],pygame.rect.Rect(0,400+self.y_puffer,800,400))


    def time_cycle(self,scroll):
        
        self.day = False
        self.night = False
        self.evening = False




        if self.day_time in [6,7,19,20]:
            self.evening = True
            
            self.montains_asset = 1
            self.asset_main = self.asset_2

        if  self.day_time in [21,22,23,24,0,1,2,3,4,5]:
            self.night = True
            self.montains_asset = 2
            self.asset_main = self.asset_1
        
        if self.day_time in [8,9,10,11,12,13,14,15,16,17,18]:
            self.day = True
            self.montains_asset = 0
            self.asset_main = self.asset_3
        
        if self.day_time >= 24:
            self.day_time = 0
               
        self.master.fill(self.bg_color)
        
        self.check_background_color()
        

        if self.night:
            for i in self.star_list:
                i.update(self.dt)

        if self.day or self.evening:
            
            self.sun_hit_box.x = round(((self.day_time)*(500/14))+100-(3000/14))
                
        else:
            self.sun_hit_box.x = 0
        
        self.master.blit(pygame.transform.flip(self.asset_main[self.dt % 5],False, False), (self.sun_hit_box.x-scroll[0]*self.delta_scroll_const, (self.curve_s(self.sun_hit_box.x) -scroll[1]*self.delta_scroll_const)))
        
            
