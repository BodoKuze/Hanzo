import pygame
import os
from png_class import Image_Pack
from math import sin


#Ey sry. Hab dir jetzt erstmal eine Vorlage gegeben für einen Gegner... 

class Bat:

    def __init__(self,master,x,y) -> None:
        self.master = master
        self.y = y
        self.hit_box = pygame.rect.Rect(x*50,y*50,50,50)
        self.image_list = Image_Pack(self.master,fr"{os.getcwd()}\sprites\bat.png",3,1,(50,150)).get_images() 
        self.image_list_when_hit = self.create_red_tiles(Image_Pack(self.master,fr"{os.getcwd()}\sprites\bat.png",3,1,(50,150)).get_images() ,(155,0,0))
        self.flip = True
        self.dt = 0
        self.spd = 3
        self.hp = 2
        self.cooldown = 0
        self.dmg = 2


    def update(self,dt,scroll,sword_hit_box:pygame.rect.Rect):
        self.update_app(scroll)
        self.get_hit(sword_hit_box)
        if dt % 10 == 0:
            self.dt += 1

        self.hit_box.x -= self.spd
        
        self.curve()


    
    def hit_box_cooldown(self):
        if  0 < self.cooldown < 10 :
            self.cooldown += 1
        else:
            self.cooldown = 0

    

    def get_hit(self,sword):
        self.hit_box_cooldown()
        if sword != None:
            if self.hit_box.colliderect(sword) and self.cooldown == 0:
                
                self.cooldown = 1
                self.hp -= 1
                print(self.hp)
        
    def create_red_tiles(self,image_list,color):
        
        new_image_list = []
        copy_image_list = image_list
        for image in copy_image_list:
            for x in range(image.get_width()):
                for y in range(image.get_height()):
                    r, g, b, a = image.get_at((x, y)) 
                    
                    new_r,new_g,new_b = color 
                    
                    
                    image.set_at((x, y), (new_r, new_g, new_b, a))
                    
            new_image_list.append(image)

        return new_image_list
        
    def update_app(self,scroll):
        if self.cooldown == 0:
            self.master.blit(pygame.transform.flip(self.image_list[self.dt % 3], self.flip, False), (self.hit_box.x-scroll[0], self.hit_box.y-scroll[1]))
            pygame.draw.rect(self.master,(255,0,0),pygame.rect.Rect(self.hit_box.x-scroll[0], self.hit_box.y-scroll[1], self.hit_box.width,self.hit_box.height),2)
        else:
            self.master.blit(pygame.transform.flip(self.image_list_when_hit[self.dt % 3], self.flip, False), (self.hit_box.x-scroll[0], self.hit_box.y-scroll[1]))
            pygame.draw.rect(self.master,(0,0,255),pygame.rect.Rect(self.hit_box.x-scroll[0], self.hit_box.y-scroll[1], self.hit_box.width,self.hit_box.height),2)
            

    def curve(self):
        self.hit_box.y = self.y + sin(self.hit_box.x/50)*150