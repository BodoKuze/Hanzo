import pygame

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
    
    def show_images(self, dt):
        self.master.blit(pygame.transform.flip(self.__image_list[self.showing_pos], False, False), (0, 0))

        if dt % 10 == 0:
            self.showing_pos += 1
            if self.showing_pos >= len(self.__image_list):
                self.showing_pos = 0
        
