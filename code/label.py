import pygame

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