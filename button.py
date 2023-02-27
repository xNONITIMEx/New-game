import pygame


# button class
class Button:
    def __init__(self, x, y, image, scale, type="Настройки"):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.type = type
        self.clicked = False

    def on_click(self):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()
        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        return action

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def set_type(self, type):
        self.type = type

    def get_type(self):
        return self.type