import pygame

class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height
    
    def apply(self, entity_rect:pygame.rect.Rect):
        return entity_rect.move(self.camera.topleft)

    def update(self, player_rect:pygame.rect.Rect):
        x = -player_rect.x + int(self.width / 2)
        y = -player_rect.y + int(self.height / 2)

        # Limit camera scrolling to game world size
        x = min(0, x)  # Left
        y = min(0, y)  # Top
        x = max(-(self.width - self.width), x)  # Right
        y = max(-(self.height - self.height), y)  # Bottom
        
        self.camera = pygame.Rect(x, y, self.width, self.height)

    