import pygame
import os
from png_class import Image_Pack

class Text:
    def __init__(self,master,font_path,font_size,text:str,x:int,y:int,width:str,height:str,color:tuple[int,int,int]) -> None:
        self.font = pygame.font.Font(font_path,font_size)
        self.text_rect = pygame.rect.Rect(x,y,width,height)
        self.text = self.font.render(text,True,color)
        self.master = master
        

    def update(self):
        self.master.blit(self.text,self.text_rect)

    def update_text(self,text:str,color:tuple[int,int,int]):
        self.text = self.font.render(f"{text}",True,color)

class Player_IF:

    def __init__(self,master) -> None:
        self.master = master
        self.images = Image_Pack(self.master,fr"{os.getcwd()}\sprites\subweapons.png",2,2,(200,200)).get_images()
        self.images.reverse()

    def update(self,player):
        pygame.draw.rect(self.master, (0, 0, 0), pygame.Rect(0, 0, 800, 150))

        self.master.blit(self.images[player.weapon-1],(25,25))
        
        self.master.blit(self.images[3],(25,25))

        

        for i in range(player.hp):
            pygame.draw.rect(self.master, (235, 86, 75), pygame.Rect(150+i*30, 50, 20, 20),)
        
        for i in range(player.mp):
            pygame.draw.rect(self.master, (77, 166, 255), pygame.Rect(150+i*30, 75, 20, 20),)