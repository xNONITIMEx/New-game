import pygame as pg
# from main import HEIGHT, WIDTH
from pygame.locals import *

HEIGHT = 600
WIDTH = 400

VELOCITY = 11


class Player(pg.sprite.Sprite):
    image = pg.transform.scale(pg.image.load('player.png'), (40, 50))

    def __init__(self, position):
        pg.sprite.Sprite.__init__(self)
        # Indicator of flipping image
        self.flip = False
        self.x, self.y = position
        self.width, self.height = self.image.get_width(), self.image.get_height()
        # Creating rectangle around the player
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.x_direction = 1

        # Indicator of jumping process
        self.is_jump = False
        # Distance of moving up and down, kind of velocity
        self.jump_offset = VELOCITY

    # Drawing method
    def draw(self, screen):
        screen.blit(pg.transform.flip(self.image, self.flip, False), self.rect)
        # Drawing rectangle around player
        pg.draw.rect(screen, (0, 255, 0), self.rect, 2)

    def move(self):
        keys = pg.key.get_pressed()
        # Delta x and delta y variables
        dx = 0
        dy = 0

        # Process of jumping
        # Info was taken from
        # https://www.techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/jumping/

        # Check if player is not jumping
        if self.is_jump is False:
            # Switching jumping indicator to True
            if keys[K_SPACE]:
                self.is_jump = True
                self.x_direction *= -1
            print('false')
        else:
            # If velocity is lower than original velocity (VELOCITY)
            if self.jump_offset >= -VELOCITY:
                # If direction is positive, player goes up. If it's negative, player goes down
                direction = 1
                if self.jump_offset < 0:
                    direction = -1
                # Deducting amount of pixels, which is counting by multiplying quadratic velocity to
                # coefficient which controls the amplitude of jump to
                # direction
                dy -= (self.jump_offset ** 2) * 0.4 * direction
                dx += 9 * self.x_direction
                # Reducing velocity
                self.jump_offset -= 1
            else:
                self.jump_offset = VELOCITY
                self.is_jump = False
        # Moving by x-axis
        # if keys[K_d] and self.x <= WIDTH - self.width:
        #     dx = 3
        #     self.flip = False
        # if keys[K_a] and self.x >= 0:
        #     dx = -3
        #     self.flip = True
        # Prohibiting player to move out of screen
        if self.rect.top + dy <= 0:
            dy = 10
            self.is_jump = False
        # Adding amount of pixels we will move to
        self.rect.y += dy
        self.rect.x += dx

    def relationships_with_walls(self, walls: pg.sprite.Group):
        collision_tolerance = 10
        keys = pg.key.get_pressed()
        wall = pg.sprite.spritecollideany(self, walls)
        if wall is not None:
            if self.rect.colliderect(wall.rect):
                if abs(self.rect.left - wall.rect.right) < collision_tolerance:
                    self.is_jump = False
                    if keys[K_SPACE]:
                        self.is_jump = True
                        self.rect.x += 5
                if abs(self.rect.right - wall.rect.left) < collision_tolerance:
                    self.is_jump = False
                    wall.collected = True
                    if keys[K_SPACE]:
                        self.is_jump = True
                        self.rect.x -= 5
                if abs(self.rect.bottom - wall.rect.top) < collision_tolerance:
                    print('bottom to top')
                    self.is_jump = False
                    if keys[K_SPACE]:
                        print('space pressed')
                        self.is_jump = True

        #     right_player_side = self.rect.x + self.image.get_width() // 2
        #     left_player_side = self.rect.x - self.image.get_width() // 2
        #     right_wall_side = self.rect.x - self.image.get_width() // 2
        #     left_wall_side = self.rect.x - self.image.get_width() // 2
        #     if right_wall_side <= left_player_side:
        #         self.is_jump = False
        #         self.x_direction = -1
        #     if left_wall_side >= right_player_side:
        #         self.is_jump = False
        #         self.x_direction = 1
        if self.is_jump:
            # walls.update()
            pass

    def set_position(self, position):
        self.rect.x, self.rect.y = position[0] - self.rect.width // 2, position[1] - self.rect.height // 2
