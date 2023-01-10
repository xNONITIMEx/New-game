import pygame as pg

from pygame.locals import *

HEIGHT = 600
WIDTH = 400
ACCELERATION = 0.5
FRIC = -0.12

VELOCITY = 8

vectors = pg.math.Vector2


class Player(pg.sprite.Sprite):
    image = pg.transform.scale(pg.image.load('player.png'), (40, 50))

    def __init__(self, position):
        pg.sprite.Sprite.__init__(self)
        # Indicator of flipping image
        self.flip = False
        self.position = vectors(position)
        self.width, self.height = self.image.get_width(), self.image.get_height()
        # Creating rectangle around the player
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.x_direction = 1
        self.jumpCount = VELOCITY
        self.swap_x_direction = False
        self.velocity = vectors((0, 0))
        self.acceleration = vectors((0, 0))
        self.touching_wall = False

        # Indicator of jumping process
        self.is_jump = False
        # Distance of moving up and down, kind of velocity

    # Drawing method
    def draw(self, screen):
        screen.blit(pg.transform.flip(self.image, self.flip, False), self.rect)
        # Drawing rectangle around player
        pg.draw.rect(screen, (0, 255, 0), self.rect, 2)

    def move(self):
        if not self.touching_wall:
            self.acceleration = vectors((0, 0.5))
        else:
            self.acceleration = vectors((0, 0))
            self.velocity = vectors((0, 0))
        keys = pg.key.get_pressed()
        if keys[K_d]:
            self.acceleration.x = ACCELERATION
            self.flip = False
        if keys[K_a]:
            self.acceleration.x = -ACCELERATION
            self.flip = True
        self.acceleration.x += self.velocity.x * FRIC
        self.velocity += self.acceleration
        self.position += vectors((0, 0))
        self.position += self.velocity + 0.5 * self.acceleration
        if self.position.x > WIDTH:
            self.position.x = 0
        if self.position.x < 0:
            self.position.x = WIDTH
        self.rect.midbottom = self.position

    def jump(self, group):
        hits = pg.sprite.spritecollideany(self, group)
        if hits:
            self.velocity.y = -12
            self.velocity.x = -12

    def update(self, group):
        hits = pg.sprite.spritecollideany(self, group)
        if hits and self.velocity.y > 0:
            self.position.y = hits.rect.top + 1
            self.velocity.y = 0

    def relationships_with_walls(self, walls: pg.sprite.Group):
        collision_tolerance = 30
        keys = pg.key.get_pressed()
        wall = pg.sprite.spritecollideany(self, walls)
        if wall is not None:
            if self.rect.colliderect(wall.rect):
                if abs(self.rect.left - wall.rect.right) < collision_tolerance:
                    self.touching_wall = True
                    wall.collected = True
                    if keys[K_SPACE]:
                        pass
                if abs(self.rect.right - wall.rect.left) < collision_tolerance:
                    self.touching_wall = True
                    wall.collected = True
                    if keys[K_SPACE]:
                        pass
                if abs(self.rect.bottom - wall.rect.top) < collision_tolerance:
                    self.touching_wall = True
                    if keys[K_SPACE]:
                        pass
        else:
            self.touching_wall = False

    def set_position(self, position):
        self.position = position[0] - self.rect.width // 2, position[1]
