import pygame as pg


class Wall(pg.sprite.Sprite):
    image = pg.image.load('wall.png')

    def __init__(self, position):
        pg.sprite.Sprite.__init__(self)
        self.collected = False
        self.position = position
        self.rect = self.image.get_rect()
        self.rect.center = position

    def draw(self, screen):
        screen.blit(self.image)

    def update(self):
        pass
