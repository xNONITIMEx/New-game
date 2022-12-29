import pygame as pg


class Wall(pg.sprite.Sprite):
    image = pg.transform.scale(pg.image.load('wall.png'), (20, 80))

    def __init__(self, position, *walls):
        pg.sprite.Sprite.__init__(self, *walls)
        self.collected = False
        self.position = position
        self.rect = self.image.get_rect()
        self.rect.center = position

    def draw(self, screen):
        screen.blit(self.image)

    def update(self):
        self.rect.y += 3