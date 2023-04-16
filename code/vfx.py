import pygame

class Player_Dead:

    def __init__(self,master,x,y) -> None:
        self.master = master
        self.circle_list = [pygame.rect.Rect(x,y,50,50) for i in range(8)]
        self.spd = 0

    def animation(self,dt,scroll):
        
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


class Enemy_Dead:
    
    def __init__(self, master, x, y):
        self.master = master
        self.x = x
        self.y = y
        self.radius = 25
        self.alpha = 255
        self.done = False

    def animation(self, scroll):

        

        self.radius += 8
        alpha = max(255 - self.radius, 0)
        color = (235, 86, 75) 

        if alpha <= 0:
            self.done = True
            return

        surface = pygame.Surface((self.radius*2, self.radius*2), pygame.SRCALPHA) 
        pygame.draw.circle(surface, color, (self.radius, self.radius), self.radius)
        surface.set_alpha(alpha) 

        self.master.blit(surface, (self.x - scroll[0] - self.radius, self.y - scroll[1] - self.radius)) 
            
        


    
        