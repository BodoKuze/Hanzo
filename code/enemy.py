import pygame
import os
from png_class import Image_Pack

class Enemy:
    def __init__(self, master,x:int,y:int,flipped=False) -> None:
        self.master = master
        self.x_when_flipped = x+ 50
        self.y_when_flipped = y+ 50
        self.moving = False
        self.speed = 5
        self.image_list = Image_Pack(self.master,fr"{os.getcwd()}\sprites\Placehold1.png",5,10,(500,500)).get_images()
        self.collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
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
        self.hit_box = pygame.Rect(x,y,50,100)
        self.items = None
        self.item_holding_counter = 0
        self.jumpleft = 0
        self.max_jumps = 2
        self.atk_buffer = 0
        self.dgy = 0
        self.on_ground = True
        self.jump_height = 20
        self.dj = 0
        self.djtime = 0
        self.gravity = 10
        self.air_timer = 0
        self.jump_hold = False
        self.vertical_mv = 0
        self.falling = False
        self.jump = False
        self.movement = [0,0]
        self.jump_time = 3.5
        self.jump_speed = 5
        self.sword = None
        self.movement_list = [(x,y) for i in range(10)]
        self.true_scroll = [0,0]
        
    # def update_movement_list(self):
        
    #     del self.movement_list[-1]
    #     self.movement_list = [((self.hit_box.x,self.hit_box.y))] + self.movement_list
        
    def blit_player(self,image_list,img,flip,x,y,scroll):
        
        self.master.blit(pygame.transform.flip(image_list[img[self.image_counter]], flip, False), (x-scroll[0], y-scroll[1]))
        
        
        if self.flip:
            self.master.blit(pygame.transform.flip(image_list[img[self.image_counter]+1], flip, False), (x-50-scroll[0], y-scroll[1]))
        else:
            self.master.blit(pygame.transform.flip(image_list[img[self.image_counter]+1], flip, False), (x+50-scroll[0], y-scroll[1]))
    
    def update_app(self,scroll):
        
        actions_frames = {
            "idle" : [0],
            # "running" : [12,14,16],
            # "slash" : [4,6,8,],
            # "sub" : [4,10],
            # "ducking" : [18],
            # "d_slash" : [20,22,24],
            # "d_item" : [18,24],
            # "jump" : [34],
            # "in_air" : [26,28,30,32],
            # "attack_air" : [34,36,38],
            # "item_air" : [40,42]
        }
        
        if not self.moving and not self.attack:
            img = actions_frames["idle"]
            #self.image_counter = dt % len(img)
              
        elif self.moving and not self.attack:
            img = actions_frames["running"]
            #self.image_counter = dt % len(img)    
        
        if self.attack and self.air_timer == 0:
            img = actions_frames["slash"]

        
        # if self.air_timer > 0:
        #     img = actions_frames["in_air"]


        # if self.attack and self.air_timer > 0:
        #     img = actions_frames["attack_air"] 
        
        
        

        #self.blit_player(self.shadow_image_list1,img,self.flip,self.shadow_hit_box1.x,self.shadow_hit_box1.y,scroll)
        #self.blit_player(self.shadow_image_list2,img,self.flip,self.shadow_hit_box2.x,self.shadow_hit_box2.y,scroll)
        #self.blit_player(self.shadow_image_list3,img,self.flip,self.shadow_hit_box3.x,self.shadow_hit_box3.y,scroll)
        self.blit_player(self.image_list,img,self.flip,self.hit_box.x,self.hit_box.y,scroll)
        



        

        
        

        #pygame.draw.rect(self.master,(255,255,255),self.hit_box,2)
        pygame.draw.rect(self.master,(0,0,0),pygame.rect.Rect(self.hit_box.x-scroll[0], self.hit_box.y-scroll[1], self.player_size[0],self.player_size[1]),2)

    def update(self, dt, list_objects):
        if dt % self.frame_switch == 0:
            self.dt += 1

        self.true_scroll[0] += (self.hit_box.x-self.true_scroll[0]-375)/20
        self.true_scroll[1] += (self.hit_box.y-self.true_scroll[1]-350)/20

        scroll = self.true_scroll.copy()

        scroll[0] = int(scroll[0])
        scroll[1] = int(scroll[1])




        #keys = pygame.key.get_pressed()
        self.moving = False
        self.attack = False
        self.falling = False
        
        # Bewegungsrichtung
        self.movement = [0, 0]

        self.movement[1] += self.vertical_mv
        self.vertical_mv += self.gravity

        if self.vertical_mv > 12:
            self.vertical_mv = 12



        self.collision_types,self.hit_box = self.move(self.hit_box,self.movement, list_objects)
        
        if self.collision_types['bottom']:
            
            self.air_timer = 0
            self.vertical_mv = 0
        

        
        

        self.update_app(scroll)
        # self.update_player_holding()
        # self.update_movement_list()
        # self.update_alucard_sd()
        # self.sword_attack(scroll)
        # self.jumping()
        

        return scroll


#e1 = Enemy()
#print(e1.image_list)
