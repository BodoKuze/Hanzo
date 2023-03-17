import pygame
from player import Player
from png_class import Image_Pack





class Building:

    def __init__(self,master,x,y,width,height,PNG:Image_Pack,set_image:list[int]) -> None:
        self.hit_box = pygame.rect.Rect(x,y,width,height)
        self.master = master

    def update(self,Player:Player):
        self.update_app()
        
    def update_app(self):
        pygame.draw.rect(self.master,(0,0,0),self.hit_box,2)

    def get_hit_box(self):
        return self.hit_box

class penetrable_Platform(Building):

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