import pygame

class Image_Pack:
    def __init__(self,master:pygame.display, path, rows, columns, resize=None):
        self.path = path
        self.rows = rows
        self.columns = columns
        self.resize = resize
        self.image = pygame.image.load(path)
        self.master = master
        if self.resize:
            self.image = pygame.transform.scale(self.image, resize)
        
        self.width = self.image.get_width() // self.columns
        self.height = self.image.get_height() // self.rows
        self.__image_list = []
        self.creat_image()

        self.showing_pos = 1

    def creat_image(self):    
        
        for i in range(self.rows):
            for j in range(self.columns):
                x = j * self.width
                y = i * self.height
                rect = pygame.Rect(x, y, self.width, self.height)
                self.__image_list.append(self.image.subsurface(rect))
        
    def get_images(self) -> list:
        return self.__image_list

        
class Blit_Block:

    def __init__(self,master,x:int,y:int,image) -> None:
        self.master = master

        self.img = image
        self.hit_box = pygame.rect.Rect(x*50,y*50,50,50)
        
        
    def update(self,igonre:None,scroll):
            
        if -50<= self.hit_box.x-scroll[0] <800 or -50<= self.hit_box.y-scroll[1] <800:
            self.master.blit(self.img, ((self.hit_box.x)-scroll[0], (self.hit_box.y)-scroll[1]))
