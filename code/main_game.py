#Hier kommt später die Hauptklasse rein in der 
#alle Objekte miteinader interagieren
import pygame
import os
from player import Player
from platforms import *
from enemy import *

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
        a = Image_Pack(self.master,fr"{os.getcwd()}\sprites\sprite_block.png",8,1,(50,400)).get_images()
        b = Image_Pack(self.master,fr"{os.getcwd()}\sprites\ds_block.png",6,1,(50,300)).get_images()
        
        self.platform_list = [
            Construction(master,0,10,8,1,a,[0]*8),
            movable_Platform(master,8,10,3,1,a,[2]*3,8,2),
            Construction(master,20,10,3,1,a,[1]*3),
            penetrable_Platform(master,20,7,3,1,a,[7]*3),
            penetrable_Platform(master,20,4,3,1,a,[7]*3),
            penetrable_Platform(master,20,1,3,1,a,[7]*3),
            destroy_Platform(master,-3,10,3,1,b,[0]*3,1,4),
            Construction(master,-100,10,97,1,a,[0]*97),
            ]
        
        self.enemy_list = [
            Bat(self.master,0,300)
        ]

    def update_bg(self):
        self.bg.update(self.scroll,self.delta_time)

    def update_fg(self,clock,player):
        self.player.player_if.update(player)
        self.update_label(clock)

    def update_elias(self,e,clock):
        self.delta_time += 1
        self.update_bg()

        self.update_enteties(e)

        self.platform_update()

        

        self.update_fg(clock,self.player)


    def update_andre(self,e,clock):
        self.delta_time += 1
        self.update_bg()

        self.update_enteties(e)

        self.platform_update()

        self.update_label(clock)
        
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