#Hier kommt später die Hauptklasse rein in der 
#alle Objekte miteinader interagieren
import pygame
from player import Player
from platforms import *

class Game:
    def __init__(self,master,width,height) -> None:
        self.master = master
        self.width = width
        self.height = height
        self.p = pygame
        self.player = Player(master,self.p.K_w,self.p.K_s,self.p.K_a,self.p.K_d,self.p.K_SPACE,self.p.K_k,50,50)   
        self.delta_time = 0
        self.enemy_hitbox_list = []
        self.platforms_hit_box_list = [Building(master,0,500,800,50,None,None),Building(master,300,200,200,50,None,None),penetrable_Platform(master,0,200,200,50,None,None)]

    def update_main(self,e):
        self.delta_time += 1

        self.update_enteties(self.delta_time,e)
        self.platform_update()

    def platform_update(self):
        for i in self.platforms_hit_box_list:
            i.update(self.player)


    def update_enteties(self,dt,e):
        self.player.update(self.delta_time,self.platforms_hit_box_list,None,e)