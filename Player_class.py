import pygame as pg

from pygame.locals import *
from Platform_class import Platform

HEIGHT = 600
WIDTH = 400
ACCELERATION = 0.5
FRIC = -0.12

VELOCITY = 8

vectors = pg.math.Vector2


class Player(pg.sprite.Sprite):
    image = pg.transform.scale(pg.image.load('assets/player.png'), (40, 50))

    def __init__(self, position):
        pg.sprite.Sprite.__init__(self)
        # Indicator of flipping image
        self.flip = False
        # Использую векторы, потому что так удобнее работать с осями
        self.position = vectors(position)
        self.width, self.height = self.image.get_width(), self.image.get_height()
        # Creating rectangle around the player
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.jumpCount = VELOCITY
        # Переменная отвеает за
        self.velocity = vectors((0, 0))
        self.acceleration = vectors((0, 0))
        # Индикаторы положения игрока
        self.on_wall = False
        self.in_the_air = False
        self.on_ground = False
        # первая переменная - направление, в которое будет прыгать игррок,
        # вторая - False, если игрок на стене,
        # и направлнение уже измененео,
        # True, если надо изменить
        self.change_direction = [1, False]

    # Drawing method
    def draw(self, screen):
        screen.blit(pg.transform.flip(self.image, self.flip, False), self.rect)
        # Drawing rectangle around player
        pg.draw.rect(screen, (0, 255, 0), self.rect, 2)

    def move(self):
        # Положение не должно меняться, если игрок на стене
        if not self.on_wall:
            self.acceleration = vectors((0, 0.5))
        else:
            self.acceleration = vectors((0, 0))
            self.velocity = vectors((0, 0))
            # Смена индикатора смены направления
            if not self.change_direction[1]:
                self.change_direction[1] = True
        keys = pg.key.get_pressed()
        if keys[K_d]:
            self.acceleration.x = ACCELERATION
            self.flip = False
        if keys[K_a]:
            self.acceleration.x = -ACCELERATION
            self.flip = True
        # изменение ускорения по х
        self.acceleration.x += self.velocity.x * FRIC
        # Изменение ускорения в обоих осях
        self.velocity += self.acceleration
        self.position += vectors((0, 0))
        # изменение положения
        self.position += self.velocity + 0.5 * self.acceleration
        # окончательно изменение позиции
        self.rect.midbottom = self.position

    def jump(self, group):
        # проверка на касание с объестом, от которого можно оттолкнуться
        hits = pg.sprite.spritecollideany(self, group)
        if hits:
            self.velocity.y = -12
            self.velocity.x = -10 * self.change_direction[0]
            self.in_the_air = True
            self.on_wall = False
            self.on_ground = False

    # запрет на падение вниз
    def update(self, group):
        hits = pg.sprite.spritecollideany(self, group)
        if hits and self.velocity.y > 0:
            self.position.y = hits.rect.top + 1
            self.velocity.y = 0

    def collisions(self, walls=pg.sprite.Group, platforms=pg.sprite.Group):
        collision_tolerance = 10
        keys = pg.key.get_pressed()
        platform = pg.sprite.spritecollideany(self, platforms)
        if type(platform) == Platform:
            self.on_ground = True
            self.in_the_air = False
        else:
            self.on_ground = False
        wall = pg.sprite.spritecollideany(self, walls)
        # проверка на касание стены
        if wall is not None:
            if self.rect.colliderect(wall.rect):
                # проверка на сторону, которой игрок касается
                if abs(self.rect.left - wall.rect.right) < collision_tolerance:
                    self.on_wall = True
                    self.in_the_air = False
                    wall.collected = True
                    # прыжок от стены
                    if keys[K_SPACE] and not self.in_the_air:
                        self.on_wall = False
                        if self.change_direction[1]:
                            self.change_direction[1] = False
                            self.change_direction[0] = -1
                            self.flip = False
                        self.position.x += 10
                        self.jump(walls)
                # здесь то же самое, только с другой стороны стены
                if abs(self.rect.right - wall.rect.left) < collision_tolerance:
                    self.on_wall = True
                    self.in_the_air = False
                    wall.collected = True
                    if keys[K_SPACE] and not self.in_the_air:
                        self.on_wall = False
                        if self.change_direction[1]:
                            self.change_direction[1] = False
                            self.change_direction[0] = 1
                            self.flip = True
                        self.position.x -= 10
                        self.jump(walls)
        else:
            self.on_wall = False

    def set_position(self, position):
        self.position = position[0] - self.rect.width // 2, position[1]
