import pygame

class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity_rect:pygame.rect.Rect):
        return pygame.rect.Rect(entity_rect.x-self.camera.x,entity_rect.y-self.camera.y,entity_rect.width,entity_rect.height)

    def update(self, player_rect:pygame.rect.Rect,dt):
        
        
        
        
        self.camera.x += (player_rect.x-self.camera.x-(self.width//2))//10
        
        

    