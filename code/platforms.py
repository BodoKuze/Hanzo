import pygame
from player import Player
from png_class import Image_Pack





class Construction:

    def __init__(self,master,x,y,width,height,PNG:Image_Pack,set_image:list[int]) -> None:
        self.hit_box = pygame.rect.Rect(x,y,width,height)
        self.master = master

    def update(self,Player:Player):
        self.update_app()
        
    def update_app(self):
        pygame.draw.rect(self.master,(0,0,0),self.hit_box,2)

    def get_hit_box(self):
        return self.hit_box

class penetrable_Platform(Construction):

    def __init__(self, master, x, y, width, height, PNG: Image_Pack,set_image) -> None:
        super().__init__(master, x, y, width, height, PNG, set_image)
        self.__hit_box = pygame.rect.Rect(x,y,width,height)
        self.hit_box = self.__hit_box
        self.going_trough = False

    def update(self,Player:Player):
        
        if Player.hit_box.y+Player.player_size[0]-1 > self.__hit_box.y:
            self.going_trough = True
            self.hit_box = None

        else:
            self.hit_box = self.__hit_box
            self.going_trough = False

        self.update_app()
        

    def update_app(self):
        if self.going_trough:
            pygame.draw.rect(self.master,(255,255,255),self.__hit_box,2)
        if not self.going_trough:
            pygame.draw.rect(self.master,(0,0,0),self.__hit_box,2)    
    
    def get_hit_box(self):
        return self.hit_box
    
class movable_Platform(Construction):

    def __init__(self, master, x, y, width, height, PNG: Image_Pack, set_image: list[int],distance_blocks:int,speed:int):
        super().__init__(master, x, y, width, height, PNG, set_image)
        self.__x = x
        
        self.distance_blocks = distance_blocks
        self.speed = speed

    def player_movement(self,hit_box:pygame.rect.Rect):
        return self.hit_box.y == hit_box.y + hit_box.height and self.hit_box.x <= hit_box.x <= self.hit_box.x + self.hit_box.width

    def update(self, Player: Player):
         
        self.hit_box.x += self.speed

        if self.__x + self.distance_blocks * 50 == self.hit_box.x:
            self.speed *= -1


        if self.hit_box.x == self.__x:
            self.speed *= -1

        if self.player_movement(Player.hit_box):
            Player.hit_box.x += self.speed

        self.update_app()
        
    def update_app(self):
        return super().update_app()
    
class destroy_Platform(Construction):
    

    def __init__(self, master, x, y, width, height, PNG: Image_Pack, set_image: list[int],sec:int,rec:int) -> None:
        super().__init__(master, x, y, width, height, PNG, set_image)
        
        
        self.__hit_box = pygame.rect.Rect(x,y,width,height)
        self.hit_box = self.__hit_box
        self.hbc = 0
        self.__time = sec * 60
        self.time = self.__time
        self.__recover_time = rec
        self.touched = False

    def update(self, Player: Player):
        self.if_standing_on(Player.hit_box)
        self.update_app()


    def update_app(self):
        if self.hbc >= 255:
            self.hbc = 255

        pygame.draw.rect(self.master,(round(self.hbc),round(self.hbc),round(self.hbc)),self.__hit_box,2)
        
            
    def if_standing_on(self,hit_box:pygame.rect.Rect):
        if self.__hit_box.y == hit_box.y + hit_box.height and self.__hit_box.x <= hit_box.x <= self.__hit_box.x + self.__hit_box.width:
            self.touched = True


        if self.touched:
            self.time -= 1
            self.hbc += (255)/(self.__time)
            
            if self.time == 0:
                self.hit_box = None

            elif self.time <= self.__recover_time * -60:
                self.touched = False
                self.time = self.__time
                self.hit_box = self.__hit_box
                self.hbc = 0



        
   