import pygame
import os
from png_class import *

class Player:
    def __init__(self,master,up,down,left,rigth,jump,attack,x,y,flipped=False) -> None:
        self.master = master
        self.control = [up,down,left,rigth,jump,attack]
        self.x = x
        self.y = y
        self.player_size = 50
        self.moving = False
        self.speed = 5
        self.dt = 0
        self.image_list = Image_Pack(self.master,fr"{os.getcwd()}\sprites\char.png",5,5,(500,500)).get_images()
        self.gravity = 3
        self.frame_switch = 10
        self.sprites = []
        self.frame_counter = 0
        self.image_counter = 0
        self.dt_falling = 0
        self.attack = False
        self.attack_duration = 3
        self.attack_cooldown = 0
        self.time = 0
        self.dt_for_sword = 0
        self.Immunity_frames = 0
        self.flip = flipped
        self.in_air = False
        self.hit_box = pygame.Rect(self.x,self.y,50,50)
        self.items = None
        self.item_holding_counter = 0
        self.gravity = 0
        self.animation_buffer = 0
        self.falling = False
        self.movement = [0,0]
        
        

    def update_player_holding(self):
        if self.items != None:
            
            self.item_holding_counter += 1

            if self.item_holding_counter == 500:
                self.items = None
                self.item_holding_counter = 0
    
    def update_app(self,dt):
        
        actions_frames = {
            "idle" : [0,1],
            "running" : [6,7,8],
            "slash" : [2,3,4,],
            "sub" : [2,5],
            "ducking" : [9],
            "d_slash" : [10,11,12],
            "d_item" : [9,12],
            "jump" : [17],
            "in_air" : [13,14,15,16],
            "attack_air" : [17,18,19],
            "item_air" : [20,21]
        }
        
        if not self.moving:
            img = actions_frames["idle"]
            self.image_counter = dt % len(img)
              
        if self.moving:
            img = actions_frames["running"]
            self.image_counter = dt % len(img)
            
        
        if self.attack:
            img = actions_frames["slash"]
            if self.animation_buffer % 20 == 0:
                self.image_counter = self.animation_buffer % len(img)
            self.animation_buffer += 1
            self.attack_duration -= 1

            self.animation_buffer += 1
        else:
            self.animation_buffer = 0
        

        self.master.blit(pygame.transform.flip(self.image_list[img[self.image_counter]], self.flip, False), (self.x, self.y))
        self.hit_box = pygame.Rect(self.x,self.y,50,50)
        pygame.draw.rect(self.master,(255,255,255),self.hit_box,2)

    def sword_attack(self,active):
        
        if active and self.attack_cooldown == 0:
            self.attack = True
            self.attack_duration = 20
            self.attack_cooldown = 30
            self.speed = 2
        elif self.attack_cooldown > 0:
            self.attack_cooldown -= 1
        else:
            self.attack = False
            self.speed = 5

    def apply_garvity(self,dt):
        if self.falling:
            if dt % 10:
                self.dt_falling += 0
            self.y += 0
            



    def update(self,dt,list_objects):
        
        if dt % self.frame_switch == 0:
            self.dt +=1


        keys = pygame.key.get_pressed()
        self.moving = False
        
        
        #Bewegungsrichtung
        
        self.movement = [0,0]


        if keys[self.control[2]]:
            
            self.movement[0] = -1
            self.moving = True
            self.flip = True

        if keys[self.control[3]]:
            
            self.movement[0] = 1
            self.moving = True
            self.flip = False


        if keys[self.control[0]]:
            
            self.movement[1] = -1
            self.moving = True
                
        if keys[self.control[1]]:
           
            self.movement[1] = 1
            self.moving = True

        
            
        self.sword_attack(keys[self.control[4]])
        
        print(self.attack)

        


        if 0 not in self.movement:
            self.movement[0] = (self.movement[0]*self.speed)/(2**(1/2))
            self.movement[1] = (self.movement[1]*self.speed)/(2**(1/2))
        else:
            self.movement[0]*=self.speed
            self.movement[1]*=self.speed

        
        

        
        


        self.move(self.movement,list_objects)
        self.update_app(self.dt)
        self.update_player_holding()
        
        
    


    

    def if_collision(self,list_objects:list[pygame.Rect]):
        hit_list = []
        if self.items != "inv":
            for tile in list_objects:
                if self.hit_box.colliderect(tile):
                    hit_list.append(tile)
        return hit_list

    def move(self, movement, tiles):
        
        self.hit_box.x += movement[0]
        hit_list = self.if_collision(tiles)
       

        for tile in hit_list:
            if movement[0] > 0:
                self.hit_box.right = tile.left

            elif movement[0] < 0:
                self.hit_box.left = tile.right

        self.hit_box.y += movement[1]

        hit_list = self.if_collision(tiles)
        
        for tile in hit_list:
            if movement[1] > 0:
                self.hit_box.bottom = tile.top

            elif movement[1] < 0:
                self.hit_box.top = tile.bottom


        self.x,self.y = self.hit_box.x,self.hit_box.y
