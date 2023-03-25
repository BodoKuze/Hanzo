import pygame
from player import Player
from png_class import Image_Pack





class Construction:

    def __init__(self,master,x,y,width,height,PNG:list,set_image:list[int]) -> None:
        self.hit_box = pygame.rect.Rect(x*50,y*50,width*50,height*50)
        self.master = master
        self.PNG = PNG
        self.set_image = set_image
        

    def update(self,Player:Player,scroll:list[int,int]):
        self.update_app(scroll) 
        
        
    def update_app(self,scroll):
        
        for i,j in enumerate(self.set_image):
            self.master.blit(self.PNG[j], ((self.hit_box.x + i*50)-scroll[0], (self.hit_box.y)-scroll[1]))

        pygame.draw.rect(self.master,(0,0,0),pygame.rect.Rect(self.hit_box.x-scroll[0],self.hit_box.y-scroll[1],self.hit_box.width,self.hit_box.height),2)
        
class penetrable_Platform(Construction):

    def __init__(self, master, x, y, width, height, PNG: list,set_image) -> None:
        super().__init__(master, x, y, width, height, PNG, set_image)
        self.hit_box = pygame.rect.Rect(x*50,y*50,width*50,height*50)
        self.height = height
        self.going_trough = False

    def update(self,Player:Player,scroll:list[int,int]):
        

        if Player.hit_box.y+Player.player_size[1]-1 > self.hit_box.y:
            self.going_trough = True
            self.hit_box.height = 0

        else:
            self.hit_box.height = 50
            self.going_trough = False

        self.update_app(scroll)
        

    def update_app(self,scroll:list[int,int]):

        
        for i,j in enumerate(self.set_image):
            self.master.blit(self.PNG[j], (self.hit_box.x-scroll[0] + i*50, self.hit_box.y-scroll[1]))



        if self.going_trough:
            pygame.draw.rect(self.master,(255,0,0),pygame.rect.Rect(self.hit_box.x-scroll[0],self.hit_box.y-scroll[1],self.hit_box.width,self.hit_box.height),2)
        if not self.going_trough:
            pygame.draw.rect(self.master,(0,0,0),pygame.rect.Rect(self.hit_box.x-scroll[0],self.hit_box.y-scroll[1],self.hit_box.width,self.hit_box.height),2)    
    
class movable_Platform(Construction):

    def __init__(self, master, x, y, width, height, PNG: list, set_image: list[int],distance_blocks:int,speed:int):
        super().__init__(master, x, y, width, height, PNG, set_image)
        self.__x = x*50
        
        self.distance_blocks = distance_blocks
        self.speed = speed

    def player_movement(self,hit_box:pygame.rect.Rect):
        return self.hit_box.y == hit_box.y + hit_box.height and self.hit_box.x - hit_box.width <= hit_box.x <= self.hit_box.x + self.hit_box.width

    def update(self, Player: Player,scroll:list[int,int]):
        
        
        self.hit_box.x += self.speed

        if self.__x + self.distance_blocks*50  == self.hit_box.x:
            self.speed *= -1


        if self.hit_box.x == self.__x:
            self.speed *= -1

        if self.player_movement(Player.hit_box):
            Player.hit_box.x += self.speed

        self.update_app(scroll)
        
    def update_app(self,scroll:list[int,int]):
        return super().update_app(scroll)
    
class destroy_Platform(Construction):
    

    def __init__(self, master, x, y, width, height, PNG: list, set_image: list[int],sec:int,rec:int) -> None:
        super().__init__(master, x, y, width, height, PNG, set_image)
        
        
        self.height = height
        self.hit_box = pygame.rect.Rect(x*50,y*50,width*50,height*50)
        self.hbc = 0
        self.__time = sec * 60
        self.time = self.__time
        self.__recover_time = rec
        self.touched = False

    def player_movement(self,hit_box:pygame.rect.Rect):
        return self.hit_box.y == hit_box.y + hit_box.height and self.hit_box.x - hit_box.width <= hit_box.x <= self.hit_box.x + self.hit_box.width 

    def update(self, Player: Player,scroll:list[int,int]):
        
        self.if_standing_on(Player.hit_box)
        self.update_app(scroll)

    def update_app(self,scroll:list[int,int]):

        image = 0
        block_blit = True

        if self.time == self.__time:
            image = 0

        elif self.time >= self.__time * (3/4):
            image = 1

        elif self.time >= self.__time * (2/4):
            image = 2
        
        elif self.time >= self.__time * (1/4):
            image = 3
        
        else:
            image = 4

        if block_blit:
            for i,j in enumerate(self.set_image):
                self.master.blit(self.PNG[image], (self.hit_box.x + i*50 - scroll[0], self.hit_box.y- scroll[1]))

        if self.hbc >= 255:
            self.hbc = 255

        print(self.time)
        
        pygame.draw.rect(self.master,(round(self.hbc),round(self.hbc),round(self.hbc)),pygame.rect.Rect(self.hit_box.x-scroll[0],self.hit_box.y-scroll[1],self.hit_box.width,self.hit_box.height),2)    
        




            
    def if_standing_on(self,hit_box:pygame.rect.Rect):
        
        if self.player_movement(hit_box):
            self.touched = True


        if self.touched:
            self.time -= 1
            self.hbc += (255)/(self.__time)

            if self.time == 0:
                self.hit_box.height = 0

            elif self.time <= self.__recover_time * -60:
                self.touched = False
                self.time = self.__time
                self.hit_box.height = 50
                self.hbc = 0



        
   