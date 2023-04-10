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


class Game:
    def __init__(self,master,width,height) -> None:
        self.font_path = fr"{os.getcwd()}\font\EndlessBossBattleRegular-v7Ey.ttf"
        self.master = master
        self.width = width
        self.height = height
        self.scroll = [0,0]
        self.p = pygame
        self.player = Player(master,self.p.K_w,self.p.K_s,self.p.K_a,self.p.K_d,self.p.K_SPACE,self.p.K_k,100,100)   
        self.delta_time = 0
        self.bg = Background(master)
        self.text = Text(master,self.font_path,30,"60",0,0,100,50,(0,0,0))
        asse = Image_Pack(self.master,fr"{os.getcwd()}\sprites\sprite_block.png",8,1,(50,400)).get_images()
        
        self.test_time = 0 
        a = [[1,1,1,1,1,1,1,1,1,1,1],
             [1,1,1,1,1,1,1,1,1,1,1]]
        self.map1 = Map(master,a,None,None,asse)
        
        self.platform_list = self.map1.create_block_map()

        self.enemy_list = []

    def update_bg(self):
        self.bg.update(self.scroll,self.delta_time)

    def update_fg(self,clock,player):
        self.player.player_if.update(player)
        self.update_label(clock)

    def update(self,e,clock):
        self.delta_time += 1
        self.update_bg()

        self.update_enteties(e)

        self.platform_update()

        keys = pygame.key.get_pressed()
        if keys[ pygame.K_h]:
            self.test_time += 1
            if self.test_time >= 240:
                self.test_time = 0
        if keys[ pygame.K_g]:
            print(self.bg.moon_hit_box.x)

        self.bg.day_time = self.test_time // 10

        self.update_fg(clock,self.player)
        
    def update_enteties(self,e):
        self.scroll = self.player.update(self.delta_time,self.platform_list,None,e)
        
        for i in self.enemy_list:
            i.update(self.delta_time,self.scroll)     


    def platform_update(self):
        
        for i in self.platform_list:
            i.update(self.player,self.scroll)

    def update_label(self,clock):
        
        self.text.update_text(round(clock.get_fps()),(255,255,255))
        self.text.update()