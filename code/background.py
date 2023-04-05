from png_class import Image_Pack
import os
import pygame
from random import randint
from datetime import datetime

class Star:

    def __init__(self,master,x,y,t) -> None:
        self.duration = t
        size = randint(1,3)
        self.hit_box = pygame.rect.Rect(x,y,size,size)
        self.master = master
        self.dt = 0.0007
        self.c = (randint(200,255),randint(200,255),randint(200,255))
        
    def update(self,dt):
        if  dt % self.duration != 0:
            pygame.draw.rect(self.master, self.c, self.hit_box)


class Background:
    def __init__(self,master) -> None:
        
        self.asset_1 = Image_Pack(master,fr"{os.getcwd()}\sprites\night_assets.png",3,3,(300,300)).get_images()
        self.asset_2 = Image_Pack(master,fr"{os.getcwd()}\sprites\sunset_assets.png",3,3,(300,300)).get_images()
        self.asset_3 = Image_Pack(master,fr"{os.getcwd()}\sprites\day_assets.png",3,3,(300,300)).get_images()
        self.asset_main = self.asset_1
        
        self.night = False
        
        self.sun_hit_box =pygame.rect.Rect(0,0,100,100)
        
        self.master = master
        self.delta_scroll_const = 0.025
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

        self.day_time = 0
        time = self.time_minimization([0,4,8,12,16,20],self.day_time)
        self.background_color_per_time = {
            0:[0, 0, 0],
            6:[255,145,102],
            8:[77,166,255],
            12:[77,166,255],
            18:[255,145,102],
            20:[0, 0, 0],
        }
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


        self.day_time = datetime.now().hour
        
        if dt % 10 == 0:
            self.dt += 1

        self.time_cycle(scroll)
        
        
        
        self.update_cloud(scroll)

        
        


    

    def curve_s(self,x):
        return (((x-350))**(2))/175 + 210


    def check_background_color(self):
        time = self.time_minimization([0,6,8,12,18,20],self.day_time)

        if self.dt % 2 == 0:  
            

            for i,j in enumerate(self.bg_color):
                if self.background_color_per_time[time][i] != j:
                    if j < self.background_color_per_time[time][i]:
                        self.bg_color[i] += 1
                    elif j > self.background_color_per_time[time][i]:
                        self.bg_color[i] -= 1


                
   
            


    def time_cycle(self,scroll):
        
        if 8 < self.day_time < 18:
            self.night = False
        else:
            self.night = True
        
        if self.day_time >= 24:
            self.day_time = 0
        


        
        self.master.fill(self.bg_color)
        
        self.check_background_color()
        

        if self.night:
            for i in self.star_list:
                i.update(self.dt)

        self.sun_hit_box.x = (self.day_time*50)-300
        
        if self.time_minimization([0,6,8,12,18,20],self.day_time) in [6,18]:
            self.asset_main = self.asset_2
            self.master.blit(pygame.transform.flip(self.asset_2[self.dt % 5],False, False), (self.sun_hit_box.x-scroll[0]*self.delta_scroll_const, (self.curve_s(self.sun_hit_box.x) -scroll[1]*self.delta_scroll_const)))
        else:
            self.master.blit(pygame.transform.flip(self.asset_3[self.dt % 5],False, False), (self.sun_hit_box.x-scroll[0]*self.delta_scroll_const, (self.curve_s(self.sun_hit_box.x)-scroll[1]*self.delta_scroll_const)))
            
            if  self.day_time in [20,21,22,23,0,1,2,3,4,5]:
                self.asset_main = self.asset_1
            else:
                self.asset_main = self.asset_3