import pygame

class Player_Dead:

    def __init__(self,master,x,y) -> None:
        self.master = master
        self.circle_list = [pygame.rect.Rect(x,y,50,50) for i in range(8)]
        self.spd = 0

    def activeate_animation(self,dt,scroll):
        
        self.circle_list[0].x += self.spd
        self.circle_list[0].y += self.spd

        self.circle_list[1].x += self.spd


        self.circle_list[2].x -= self.spd
        self.circle_list[2].y += self.spd

        self.circle_list[3].x -= self.spd

        self.circle_list[4].x -= self.spd
        self.circle_list[4].y -= self.spd

        self.circle_list[5].y -= self.spd

        self.circle_list[6].x += self.spd
        self.circle_list[6].y -= self.spd

        self.circle_list[7].y += self.spd

        

        if dt % 4 == 0:
            self.spd += 1
            color = (255,255,235)
        else:
            color = (115,39,92)

        for i in self.circle_list:
            pygame.draw.rect(self.master,color,pygame.rect.Rect(i.x-scroll[0],i.y-scroll[1],i.width,i.height),0,25)

