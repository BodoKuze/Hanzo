from png_class import Image_Pack
import os
import pygame
from random import randint

class Star:

    def __init__(self,master,x,y,t) -> None:
        self.duration = t
        self.hit_box = pygame.rect.Rect(x,y,1,1)
        self.master = master
        self.dt = 0.0007

    def update(self,dt):
        if  dt % self.duration != 0:
            pygame.draw.rect(self.master, (255,255,255), self.hit_box)


class Background:
    def __init__(self,master) -> None:
        
        self.asset_1 = Image_Pack(master,fr"{os.getcwd()}\sprites\night_assets.png",3,3,(300,300)).get_images()
        self.asset_2 = Image_Pack(master,fr"{os.getcwd()}\sprites\sunset_assets.png",3,3,(300,300)).get_images()
        self.asset_3 = Image_Pack(master,fr"{os.getcwd()}\sprites\day_assets.png",3,3,(300,300)).get_images()
        self.asset_main = self.asset_1
        
        self.day = True
        self.night = False

        self.sun_hit_box =pygame.rect.Rect(0,0,100,100)
        self.moon_hit_box = pygame.rect.Rect(0,0,100,100)
        self.sun_h = 210
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
        self.bg_color = [22, 22, 13]
        self.star_list = [Star(master,randint(0,800),randint(0,800),randint(20,100)) for i in range(60)]
        self.moon_or_sun = True

    def update_cloud(self,scroll):
        
    
        for i in self.cloud_value_list:
            

            if 800 >= i["x"]-scroll[0]*i["s"] >= -150:

                self.master.blit(pygame.transform.flip(self.asset_main[i["i"]],False, False), (i["x"]-scroll[0]*i["s"], (i["y"]-scroll[1]*i["s"])+self.y_puffer))

            if  i["x"]-scroll[0]*i["s"] <= -150:
                i["x"] = 1000

            i["x"] -= self.cloud_speed

        

    def update(self,scroll,dt):

        self.master.fill(self.bg_color)
        
        if dt % 10 == 0:
            self.dt += 1


        for i in self.star_list:
            i.update(self.dt)




        
        
        self.master.blit(pygame.transform.flip(self.asset_main[self.dt % 5],False, False), (self.sun_hit_box.x-scroll[0]*self.delta_scroll_const, (self.sun_hit_box.y-scroll[1]*self.delta_scroll_const)))
        
        
        self.update_cloud(scroll)

        
        self.time_cycle()


    def to_night(self):
        
        if self.bg_color[0] >= 20:
            self.bg_color[0] -= 2
        if self.bg_color[1] >= 20:
            self.bg_color[1] -= 1
        if self.bg_color[2] >= 12:
            self.bg_color[2] -= 1 

        self.curve_m()

    def curve_s(self):
        
        if self.sun_hit_box.x < 450:
            
            self.sun_hit_box.x += 1
            self.sun_hit_box.y = (((self.sun_hit_box.x-350))**(2))/175 + self.sun_h

    def curve_m(self):
        
        if self.moon_hit_box.x < 450:
            
            self.moon_hit_box.x += 1
            self.moon_hit_box.y = (((self.moon_hit_box.x-350))**(2))/175 + self.sun_h
        

    def to_day(self):
        
        if self.bg_color[0] <= 77:
            self.bg_color[0] += 0.2 
        if self.bg_color[1] <= 166:
            self.bg_color[1] += 0.1
        if self.bg_color[2] <= 255:
            self.bg_color[2] += 0.2

        if self.bg_color[0] > 70:
            self.asset_main = self.asset_2
        if self.bg_color[2] >= 253:
            self.asset_main = self.asset_3

        self.curve_s()

    def time_cycle(self):
        if self.day:
            self.to_day()
        if self.night:
            self.to_night()
        

        