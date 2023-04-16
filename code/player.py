import pygame
import os
from png_class import Image_Pack, Blit_Block
from pygame.locals import *
from label import Player_IF
from sound import *

class Player:
    def __init__(self,master,up,down,left,rigth,jump,attack,sub,x:int,y:int,flipped=False) -> None:
        self.master = master
        self.control = [up,down,left,rigth,jump,attack,sub]
        self.x_when_flipped = x+ 50
        self.y_when_flipped = y+ 50

        self.moving = False
        self.speed = 5
        self.dt = 0
        self.image_list = Image_Pack(self.master,fr"{os.getcwd()}\sprites\char.png",5,10,(500,500)).get_images()
        self.shadow_image_list1 = self.create_shadow(Image_Pack(self.master,fr"{os.getcwd()}\sprites\char.png",5,10,(500,500)).get_images(),(0,0,50))
        self.shadow_image_list2 = self.create_shadow(Image_Pack(self.master,fr"{os.getcwd()}\sprites\char.png",5,10,(500,500)).get_images(),(0,0,100))
        self.shadow_image_list3 = self.create_shadow(Image_Pack(self.master,fr"{os.getcwd()}\sprites\char.png",5,10,(500,500)).get_images(),(0,0,150))
        
        self.shadow_image_list1b = self.create_shadow(Image_Pack(self.master,fr"{os.getcwd()}\sprites\char.png",5,10,(500,500)).get_images(),(50,0,0))
        self.shadow_image_list2b = self.create_shadow(Image_Pack(self.master,fr"{os.getcwd()}\sprites\char.png",5,10,(500,500)).get_images(),(100,0,0))
        self.shadow_image_list3b = self.create_shadow(Image_Pack(self.master,fr"{os.getcwd()}\sprites\char.png",5,10,(500,500)).get_images(),(150,0,0))
        
        self.collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
        
        self.frame_switch = 10
        self.image_counter = 0
        self.dt_falling = 0
        self.attack = False
        self.attack_duration = 3
        self.attack_cooldown = 0
        self.dt_for_sword = 0
        self.Immunity_frames = 0
        self.flip = flipped
        self.in_air = False

        self.hit_box = pygame.Rect(x,y,50,100)
        self.shadow_hit_box1 = pygame.Rect(x,y,50,100)
        self.shadow_hit_box2 = pygame.Rect(x,y,50,100)
        self.shadow_hit_box3 = pygame.Rect(x,y,50,100)

        self.player_if = Player_IF(master)
        
        
        self.atk_buffer = 0
        self.dgy = 0
        
        self.jump_height = 16
        
        self.check_point = [x,y]
       
        self.gravity = 10
        self.ducking = False
        self.air_timer = 0
        self.jump_hold = False
        self.vertical_mv = 0
        self.falling = False
        self.jump = False
        self.movement = [0,0]

        self.sword = None
        self.movement_list = [(x,y) for i in range(10)]
        self.true_scroll = [0,0]

        self.weapon = 1
        self.hp = 10
        self.mp = 10
        self.dmg_cooldown = 0

        self.sword_sfx = Sound_Effect("sword")
        self.check_point_sfx = Sound_Effect("checkpoint")
        self.player_falling = Sound_Effect("falling")
        self.damage_sfx = Sound_Effect("ronin_hit")
        
    def update_movement_list(self):
        
        
        del self.movement_list[-1]
        self.movement_list = [((self.hit_box.x,self.hit_box.y))] + self.movement_list



    def update_alucard_sd(self):
        
        self.shadow_hit_box1.x,self.shadow_hit_box1.y = self.movement_list[3]
        self.shadow_hit_box2.x,self.shadow_hit_box2.y = self.movement_list[2]
        self.shadow_hit_box3.x,self.shadow_hit_box3.y = self.movement_list[1]




    def create_shadow(self,image_list:list,color:tuple[int,int,int]):
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
    
    
    def blit_player(self,image_list,img,flip,x,y,scroll):
        
        self.master.blit(pygame.transform.flip(image_list[img[self.image_counter]], flip, False), (x-scroll[0], y-scroll[1]))
        
        
        if self.flip:
            self.master.blit(pygame.transform.flip(image_list[img[self.image_counter]+1], flip, False), (x-50-scroll[0], y-scroll[1]))
        else:
            self.master.blit(pygame.transform.flip(image_list[img[self.image_counter]+1], flip, False), (x+50-scroll[0], y-scroll[1]))






    def update_app(self,dt,scroll):
        
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
        
        if self.attack and self.air_timer == 0:
            img = actions_frames["slash"]

        
        if self.air_timer > 0:
            img = actions_frames["in_air"]


        if self.attack and self.air_timer > 0:
            img = actions_frames["attack_air"] 
        
        if self.dmg_cooldown % 2 == 0:
        
            if self.speed == 5:
                self.blit_player(self.shadow_image_list1,img,self.flip,self.shadow_hit_box1.x,self.shadow_hit_box1.y,scroll)
                self.blit_player(self.shadow_image_list2,img,self.flip,self.shadow_hit_box2.x,self.shadow_hit_box2.y,scroll)
                self.blit_player(self.shadow_image_list3,img,self.flip,self.shadow_hit_box3.x,self.shadow_hit_box3.y,scroll)
            else:
                self.blit_player(self.shadow_image_list1b,img,self.flip,self.shadow_hit_box1.x,self.shadow_hit_box1.y,scroll)
                self.blit_player(self.shadow_image_list2b,img,self.flip,self.shadow_hit_box2.x,self.shadow_hit_box2.y,scroll)
                self.blit_player(self.shadow_image_list3b,img,self.flip,self.shadow_hit_box3.x,self.shadow_hit_box3.y,scroll)

            
            self.blit_player(self.image_list,img,self.flip,self.hit_box.x,self.hit_box.y,scroll)

            pygame.draw.rect(self.master,(0,0,0),pygame.rect.Rect(self.hit_box.x-scroll[0], self.hit_box.y-scroll[1], self.hit_box.width,self.hit_box.height),2)


    def sword_attack(self,scroll):

    
        if self.attack:
            if self.atk_buffer == 0:
                
                self.image_counter = 0

            self.atk_buffer += 1
            
            if self.atk_buffer == 1:
                self.sword_sfx.play()

            if self.atk_buffer % 3 == 0 and self.atk_buffer < 9:
                self.image_counter += 1

            if self.atk_buffer == 20:
                self.attack = False
                self.atk_buffer = 0


            if not self.flip:
                self.sword = pygame.rect.Rect(self.hit_box.x+50,self.hit_box.y+10,50,30)
            if self.flip:
                self.sword = pygame.rect.Rect(self.hit_box.x-50,self.hit_box.y+10,50,30)
                
            pygame.draw.rect(self.master,(0,255,0),pygame.rect.Rect(self.sword.x-scroll[0],self.sword.y-scroll[1],self.sword.width,self.sword.height) ,2)

        else:
            self.atk_buffer = 0
            self.sword = None
    
    def jumping(self):
        if self.jump_hold:
            if self.air_timer <= self.jump_height:
                self.vertical_mv = -12
                self.air_timer += 1
            
            if self.air_timer > self.jump_height:
                self.jump = False

    def set_new_check_point(self,stage_i):
        for i in stage_i:
            if self.hit_box.colliderect(i.hit_box):
                if not i.active:
                    self.check_point = [i.hit_box.x,i.hit_box.y-50]
                    self.hp = 10
                    self.mp = 10
                    self.check_point_sfx.play()
                    i.active = True

    def update(self, dt, list_objects, list_enteties,stage_i):
        if dt % self.frame_switch == 0:
            self.dt += 1
        
        self.true_scroll[0] += (self.hit_box.x-self.true_scroll[0]-375)/20
        self.true_scroll[1] += (self.hit_box.y-self.true_scroll[1]-500)/20

        scroll = self.true_scroll.copy()

        scroll[0] = int(scroll[0])
        scroll[1] = int(scroll[1])

        keys = pygame.key.get_pressed()
        self.moving = False
        self.attack = False
        self.falling = False
        self.ducking = False
        
        # Bewegungsrichtung
        self.movement = [0, 0]

        if keys[self.control[0]] and self.atk_buffer == 0:
            pass  # TODO: Türen Betreten
            
        if keys[self.control[2]] and self.atk_buffer == 0:
            self.movement[0] += -1 * self.speed
            self.moving = True
            self.flip = True

        if keys[self.control[3]] and self.atk_buffer == 0:
            self.movement[0] += 1 * self.speed
            self.moving = True
            self.flip = False

        if keys[self.control[1]] and self.atk_buffer == 0:
            self.ducking = True
        
        if keys[self.control[5]] and not self.attack and self.attack_cooldown == 0:
            if self.weapon == 1:
                self.attack = True
        
        if keys[self.control[4]] and self.collision_types['bottom']:
            
            self.jump_hold = True
        if not keys[self.control[4]]:
            self.jump_hold = False

        if keys[self.control[6]] and not self.attack and self.mp >= 0:
            self.speed = 8
            if dt % 40 == 0:
                self.mp -= 1
        else:
            if dt % 200 == 0 and self.mp < 10:
                self.mp += 1
            self.speed = 5

        


        self.movement[1] += self.vertical_mv
        self.vertical_mv += self.gravity

        if self.vertical_mv > 12:
            self.vertical_mv = 12

        self.collision_types,self.hit_box = self.move(self.hit_box,self.movement, list_objects)
        
        if self.collision_types['bottom']:
            
            self.air_timer = 0
            self.vertical_mv = 0
        
        if self.hit_box.y >= 750:
            self.hit_box.y = self.check_point[1]
            self.hit_box.x = self.check_point[0]
            self.player_falling.play()
            self.hp -= 1
        
        

        self.update_app(self.dt,scroll)
        self.update_movement_list()
        self.update_alucard_sd()
        self.sword_attack(scroll)
        self.jumping()
        self.hit_with_en(list_enteties)
        self.set_new_check_point(stage_i)

        return scroll

    def damage_cooldown(self):
        if  0 < self.dmg_cooldown < 120:
            self.dmg_cooldown += 1
        else:
            self.dmg_cooldown = 0


    def hit_with_en(self,ent):
        self.damage_cooldown()
        for i in ent:
            if self.hit_box.colliderect(i.hit_box) and self.dmg_cooldown == 0:
                self.dmg_cooldown = 1
                self.hp -= i.dmg
                self.damage_sfx.play()



    def if_collision(self, list_objects: list):
        hit_list = []
        
        for tile in list_objects:
            if self.hit_box.colliderect(tile.hit_box) and not isinstance(tile,Blit_Block):
                hit_list.append(tile.hit_box)
            
        
        return hit_list

    def move(self,hit_box, movement, tiles):
        hit_box.x += movement[0]
        hit_list = self.if_collision(tiles)
        
        collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
        

        for tile in hit_list:
            if movement[0] > 0:
                hit_box.right = tile.left
                collision_types['right'] = True
            elif movement[0] < 0:
                hit_box.left = tile.right
                collision_types['left'] = True

        hit_box.y += movement[1]
        hit_list = self.if_collision(tiles)

        for tile in hit_list:
            if movement[1] > 0:
                hit_box.bottom = tile.top
                collision_types['bottom'] = True
            elif movement[1] < 0:
                hit_box.top = tile.bottom
                collision_types['top'] = True

        
        

        return collision_types,hit_box