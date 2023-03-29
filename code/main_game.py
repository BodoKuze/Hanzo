#Hier kommt später die Hauptklasse rein in der 
#alle Objekte miteinader interagieren
import pygame
import os
from player import Player
from platforms import *
from background import Background

class Game:
    def __init__(self,master,width,height) -> None:
        self.master = master
        self.width = width
        self.height = height
        self.scroll = [0,0]
        self.p = pygame
        self.player = Player(master,self.p.K_w,self.p.K_s,self.p.K_a,self.p.K_d,self.p.K_SPACE,self.p.K_k,100,100)   
        self.delta_time = 0
        self.enemy_hitbox_list = []
        self.bg = Background(master)

        a = Image_Pack(self.master,fr"{os.getcwd()}\sprites\sprite_block.png",8,1,(50,400)).get_images()
        b = Image_Pack(self.master,fr"{os.getcwd()}\sprites\ds_block.png",6,1,(50,300)).get_images()
        
        self.platforms_hit_box_list = [
            Construction(master,0,10,8,1,a,[0]*8),
            movable_Platform(master,8,10,3,1,a,[2]*3,8,2),
            Construction(master,20,10,3,1,a,[1]*3),
            penetrable_Platform(master,20,7,3,1,a,[7]*3),
            penetrable_Platform(master,20,4,3,1,a,[7]*3),
            penetrable_Platform(master,20,1,3,1,a,[7]*3),
            destroy_Platform(master,-3,10,3,1,b,[0]*3,1,4),
            ]

    def update_bg(self):
        self.bg.update(self.scroll,self.delta_time)

    def update_main(self,e):
        self.delta_time += 1
        self.update_bg()

        self.update_enteties(e)

        self.platform_update()
        
    def update_enteties(self,e):
        self.scroll = self.player.update(self.delta_time,self.platforms_hit_box_list,None,e)

    def platform_update(self):
        
        for i in self.platforms_hit_box_list:
            i.update(self.player,self.scroll)