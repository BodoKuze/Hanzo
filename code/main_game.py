#Hier kommt später die Hauptklasse rein in der 
#alle Objekte miteinader interagieren
import pygame
import os
from player import Player
from platforms import *
from camera import Camera

class Game:
    def __init__(self,master,width,height) -> None:
        self.master = master
        self.width = width
        self.height = height
        self.camera = Camera(self.width,self.height)

        self.p = pygame
        self.player = Player(master,self.p.K_w,self.p.K_s,self.p.K_a,self.p.K_d,self.p.K_SPACE,self.p.K_k,50,50)   
        self.delta_time = 0
        self.enemy_hitbox_list = []
        a = Image_Pack(self.master,fr"{os.getcwd()}\sprites\sprite_block.png",8,1,(50,400)).get_images()
        b = Image_Pack(self.master,fr"{os.getcwd()}\sprites\ds_block.png",6,1,(50,300)).get_images()
        self.platforms_hit_box_list = [Construction(master,0,10,40,1,a,[0]*16),movable_Platform(master,4,4,4,1,a,[5]*4,4,2),penetrable_Platform(master,0,4,4,1,a,[7]*4),destroy_Platform(master,12,4,4,1,b,[3]*4,1,3)]



    def update_main(self,e):
        self.delta_time += 1
        self.camera.update(self.player.hit_box)
        self.update_enteties(self.delta_time,e)
        self.platform_update()
        
        
    
    def platform_update(self):
        for i in self.platforms_hit_box_list:
            i.update(self.player,self.camera)


    def update_enteties(self,dt,e):
        self.player.update(self.delta_time,self.platforms_hit_box_list,None,e)