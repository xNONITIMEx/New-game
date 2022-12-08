import pygame as pg
from pygame.locals import *

SIZE = WIDTH, HEIGHT = 400, 600
FPS = 60

GRAVITY = 0.5

# Original velocity
VELOCITY = 10


# Player class
class Player:
    def __init__(self, player_image, position):
        self.player_image = player_image
        # Indicator of flipping image
        self.flip = False
        self.x, self.y = position
        self.width, self.height = player_image.get_width(), player_image.get_height()
        # Creating rectangle around the player
        self.rect = self.player_image.get_rect()
        self.rect.center = position

        # Indicator of jumping process
        self.is_jump = False
        # Distance of moving up and down, kind of velocity
        self.jump_offset = VELOCITY

    # Drawing method
    def draw(self, screen):
        screen.blit(pg.transform.flip(self.player_image, self.flip, False), self.rect)
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
        if self.rect.left + dx <= 0:
            dx = -self.rect.left
        if self.rect.right + dx >= WIDTH:
            dx = WIDTH - self.rect.right
        if self.rect.top + dy <= 0:
            dy = 10
            self.is_jump = False
        # Adding amount of pixels we will move to
        self.rect.x += dx
        self.rect.y += dy

# Main function
def main():
    pg.init()
    screen = pg.display.set_mode(SIZE)

    run = True
    
    clock = pg.time.Clock()
    # Saving images to variables
    player_image = pg.image.load('testing_animation.jpg').convert()
    wall_image = pg.image.load('wall.png').convert()
    # Saving parameters of images
    player_width = player_image.get_width()
    player_height = player_image.get_height()
    wall_width = wall_image.get_width()
    wall_height = wall_image.get_height()
    # Player starting coordinates
    starting_player_x = WIDTH // 2 + wall_width - 40
    starting_player_y = HEIGHT - player_height // 2
    # Creating player object
    player = Player(player_image, (starting_player_x, starting_player_y))

    while run:
        # Drawing process
        screen.fill((255, 255, 255))
        screen.blit(wall_image, (WIDTH // 2 - 40 - wall_width, HEIGHT - wall_height))
        screen.blit(wall_image, (WIDTH // 2 + 40, HEIGHT - wall_height))
        screen.blit(wall_image, (WIDTH // 2 - 40 - wall_width, HEIGHT - wall_height * 2))
        screen.blit(wall_image, (WIDTH // 2 + 40, HEIGHT - wall_height * 2))
        player.draw(screen)
        # Player moving
        player.move()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        pg.display.flip()
        clock.tick(FPS)
    pg.quit()


if __name__ == '__main__':
    main()
