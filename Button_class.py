import pygame as pg


class Button:
    image: pg.image

    def __init__(self, image, x, y, text_input, main_font):
        self.image = image
        self.main_font = main_font
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center=(x, y))
        self.text_input = text_input
        self.text = self.main_font.render(self.text_input, True, 'white')
        self.text_rect = self.text.get_rect(center=(x, y))

    def update(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def check_for_input(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def change_color(self, position):
        if self.check_for_input(position):
            self.text = self.main_font.render(self.text_input, True, 'green')
        else:
            self.text = self.main_font.render(self.text_input, True, 'white')
