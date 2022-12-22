import pygame as pg
# from main import HEIGHT, WIDTH
from pygame.locals import *

HEIGHT = 600
WIDTH = 400

VELOCITY = 10


class Player:
    image = pg.image.load('player.png')

    def __init__(self, position):
        # Indicator of flipping image
        self.flip = False
        self.x, self.y = position
        self.width, self.height = self.image.get_width(), self.image.get_height()
        # Creating rectangle around the player
        self.rect = self.image.get_rect()
        self.rect.center = position

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
                # Reducing velocity
                self.jump_offset -= 1
            else:
                self.jump_offset = VELOCITY
                self.is_jump = False
        # Moving by x-axis
        if keys[K_d] and self.x <= WIDTH - self.width:
            dx = 5
            self.flip = False
        if keys[K_a] and self.x >= 0:
            dx = -5
            self.flip = True
        # Prohibiting player to move out of screen
        if self.rect.top + dy <= 0:
            dy = 10
            self.is_jump = False
        # Adding amount of pixels we will move to
        self.rect.y += dy

    def set_position(self, position):
        self.rect.x, self.rect.y = position[0] - self.rect.width // 2, position[1] - self.rect.height // 2

