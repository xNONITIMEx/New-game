import pygame as pg

HEIGHT = 600
WIDTH = 400


class Platform(pg.sprite.Sprite):
    image = pg.transform.scale(pg.image.load('horizontal_wall.png'), (WIDTH, 20))

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.position = 0, HEIGHT - 20
        self.rect = self.image.get_rect()
        self.rect.topleft = self.position

    def draw(self, screen):
        screen.blit(self.image, self.position)
        pg.draw.rect(screen, 'red', self.rect, 2)
