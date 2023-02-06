import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y, tile_images, *groups):
        super().__init__(*groups)
        self.image = tile_images[tile_type]
        self.tile_type = tile_type
        self.rect = self.image.get_rect().move(
           self.image.get_width() * pos_x, self.image.get_height() * pos_y)
        self.counted = False
