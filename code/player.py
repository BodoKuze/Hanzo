import pygame
import os
from png_class import *

class Player:
    def __init__(self,master,up,down,left,rigth,jump,attack,x,y,flipped=False) -> None:
        self.master = master
        self.control = [up,down,left,rigth,jump,attack]
        self.x = x
        self.y = y

        self.x_when_flipped = x+ 50
        self.y_when_flipped = y+ 50

        self.player_size = 50
        self.moving = False
        self.speed = 5
        self.dt = 0
        self.image_list = Image_Pack(self.master,fr"{os.getcwd()}\sprites\char.png",5,10,(500,500)).get_images()
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
        self.has_flipped = False
        self.in_air = False
        self.hit_box = pygame.Rect(self.x,self.y,50,50)
        self.items = None
        self.item_holding_counter = 0
        
        self.atk_buffer = 0

        self.dgy = 0

        self.jump_height = 20
        self.dj = 0
        self.djtime = 0
        self.gravity = 4
        self.falling = False
        self.jump = False
        self.movement = [0,0]
        
        

    def update_player_holding(self):
        if self.items != None:
            
            self.item_holding_counter += 1

            if self.item_holding_counter == 500:
                self.items = None
                self.item_holding_counter = 0
    #Bewegungen
    def update_app(self,dt):
        
        actions_frames = {
            "idle" : [0,2],
            "running" : [12,14,16],
            "slash" : [4,6,8,],
            "sub" : [4,10],
            "ducking" : [18],
            "d_slash" : [20,22,24],
            "d_item" : [18,24],
            "jump" : [34],
            "in_air" : [26,28,30,32],
            "attack_air" : [34,36,38],
            "item_air" : [40,42]
        }
        
        if not self.moving and not self.attack:
            img = actions_frames["idle"]
            self.image_counter = dt % len(img)
              
        elif self.moving and not self.attack:
            img = actions_frames["running"]
            self.image_counter = dt % len(img)
            
        
        elif self.attack:
            img = actions_frames["slash"]
            
        
        
            
        
        self.master.blit(pygame.transform.flip(self.image_list[img[self.image_counter]], self.flip, False), (self.x, self.y))
        
        
        if self.flip:
            self.master.blit(pygame.transform.flip(self.image_list[img[self.image_counter+1]], self.flip, False), (self.x, self.y))
        else:
            self.master.blit(pygame.transform.flip(self.image_list[img[self.image_counter+1]], self.flip, False), (self.x, self.y))


        pygame.draw.rect(self.master,(255,255,255),self.hit_box,2)


    def jumping(self):
        if self.jump:
            self.djtime += 1
            self.dj = self.hit_box.y

            self.hit_box.y -= (self.gravity/2)*self.djtime



            if self.dj - self.hit_box.y == self.jump_height:
                self.jump = False
                self.falling = True
                self.djtime = 0
            

            
    



    def sword_attack(self):
        
        
        if self.attack:
            self.movement = [0,0]

            if self.atk_buffer == 0:
                self.image_counter = 0

            self.atk_buffer += 1

            if self.atk_buffer % 3 == 0 and self.atk_buffer < 9:
                self.image_counter += 1

            

            if self.atk_buffer == 20:
                self.attack = False
                self.atk_buffer = 0

        else:
            self.atk_buffer = 0
            

        
        

    def apply_gravity(self):
        if not self.jump and self.y+100 <= 500:
            self.dgy += 1
            
            #print((self.gravity/2)*self.dgy)
            self.hit_box.y += (self.gravity/2)*self.dgy

        else:
            self.dgy = 0
            



    def update(self,dt,list_objects):
        
        if dt % self.frame_switch == 0:
            self.dt +=1


        keys = pygame.key.get_pressed()
        self.moving = False
        
        
        #Bewegungsrichtung
        
        self.movement = [0,0]

        if keys[self.control[0]] and self.attack_cooldown == 0:
            
            self.movement[1] = -1
            self.moving = True

        elif keys[self.control[2]] and self.attack_cooldown == 0:
            
            self.movement[0] = -1
            self.moving = True
            self.flip = True

        elif keys[self.control[3]] and self.attack_cooldown == 0:
            
            self.movement[0] = 1
            self.moving = True
            self.flip = False


        
                
        elif keys[self.control[1]] and self.attack_cooldown == 0:
           
            self.movement[1] = 1
            self.moving = True



        if keys[self.control[5]] and not self.attack :
            self.attack = True
            
        if keys[self.control[4]] and not self.attack :
            self.jump = True
        
        
        
        

        


        if 0 not in self.movement:
            self.movement[0] = (self.movement[0]*self.speed)/(2**(1/2))
            self.movement[1] = (self.movement[1]*self.speed)/(2**(1/2))
        else:
            self.movement[0]*=self.speed
            self.movement[1]*=self.speed

        
        

        
        
        
        self.sword_attack()
        self.move(self.movement,list_objects)
        self.jumping()
        self.apply_gravity()



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

        
        
        self.x, self.y = self.hit_box.x , self.hit_box.y
