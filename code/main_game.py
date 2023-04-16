#Hier kommt später die Hauptklasse rein in der 
#alle Objekte miteinader interagieren
import pygame
import os
from player import Player
from platforms import *
from enemy import *
from map_class import *
from background import Background
from label import Text
from maps import *
from vfx import *

class Game:
    def __init__(self,master,width,height) -> None:
        self.font_path = fr"{os.getcwd()}\font\EndlessBossBattleRegular-v7Ey.ttf"
        self.master = master
        self.width = width
        self.height = height
        self.scroll = [0,0]
        self.enemy_vfx_list = []
        
        self.p = pygame
        self.player = Player(master,self.p.K_w,self.p.K_s,self.p.K_a,self.p.K_d,self.p.K_SPACE,self.p.K_k,self.p.K_j,250,0)   
        self.player_effect = None
        self.delta_time = 0
        self.bg = Background(master)
        self.text = Text(master,self.font_path,30,"60",0,0,100,50,(0,0,0))

        assets = Image_Pack(self.master,fr"{os.getcwd()}\sprites\sp1.png",6,2,(100,300)).get_images()
        
        self.test_time = 0 
        
        self.map1 = Map(master,map,assets)
        
        self.platform_list,self.enemy_list,self.stage_i = self.map1.create_block_map()


        


    def update_bg(self):
        self.bg.update(self.scroll,self.delta_time)

        

    def update_fg(self,clock,player):
        self.player.player_if.update(player)
        self.update_label(clock)
    


    def update(self,e,clock):
        self.delta_time += 1
        self.update_bg()
        
        self.platform_update()

        self.update_fg(clock,self.player)

        self.update_enteties(e)
        
    def update_enteties(self,e):
        
        for num,i in enumerate(self.enemy_list):
            if -50 <= i.hit_box.x-self.scroll[0] <800 and -50 <= i.hit_box.y-self.scroll[1] <800:
                i.update(self.delta_time,self.scroll,self.player.sword)     
                
                if (isinstance(i,Bat) and i.hit_box.x-self.scroll[0] < -50):
                    del self.enemy_list[num]

                if i.hp <= 0:
                    self.enemy_vfx_list.append(Enemy_Dead(self.master,i.hit_box.x,i.hit_box.y))
                    del self.enemy_list[num]

        for num,i in enumerate(self.enemy_vfx_list):
            i.animation(self.scroll)

            if i.done:
                del self.enemy_vfx_list[num]

        
        if self.player.hp > 0:
        
            self.scroll = self.player.update(self.delta_time,self.platform_list,self.enemy_list,self.stage_i,e)
        
        elif self.player_effect == None:
            self.player_effect = Player_Dead(self.master,self.player.hit_box.x,self.player.hit_box.y)
        
        else:
            self.player_effect.animation(self.delta_time,self.scroll)








        

    def platform_update(self):
        
        for i in self.platform_list:
            if -50 <= i.hit_box.x-self.scroll[0] <800 and -50 <= i.hit_box.y-self.scroll[1] <800 or isinstance(i,destroy_Platform):
                
                i.update(self.player,self.scroll)

        for i in self.stage_i:
            if -50 <= i.hit_box.x-self.scroll[0] <800 and -50 <= i.hit_box.y-self.scroll[1] <800 or isinstance(i,destroy_Platform):

                i.update(self.delta_time,self.scroll)


    def update_label(self,clock):
        
        self.text.update_text(round(clock.get_fps()),(255,255,255))
        self.text.update()