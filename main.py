import pygame as pg
from pygame.locals import *

SIZE = WIDTH, HEIGHT = 400, 600
FPS = 60

GRAVITY = 0.5


class Player:
    def __init__(self, player_image, position):
        self.player_image = player_image
        self.flip = False
        self.x, self.y = position
        self.width, self.height = player_image.get_width(), player_image.get_height()
        self.rect = self.player_image.get_rect()
        self.rect.center = position

        self.is_jump = False
        self.vel_y = 0
        self.keys = pg.key.get_pressed()
        self.mass = 10

    def draw(self, screen):
        screen.blit(pg.transform.flip(self.player_image, self.flip, False), self.rect)
        pg.draw.rect(screen, (0, 255, 0), self.rect, 2)

    def move(self):
        keys = pg.key.get_pressed()

        dx = 0
        dy = 0

        print(self.vel_y)
        if keys[K_SPACE] and self.vel_y >= -5:
            self.vel_y -= 2
        if keys[K_d] and self.x <= WIDTH - self.width:
            dx = 5
            self.flip = False
        if keys[K_a] and self.x >= 0:
            dx = -5
            self.flip = True
        self.vel_y += GRAVITY
        dy += self.vel_y

        if self.rect.left + dx <= 0:
            dx = -self.rect.left
        if self.rect.right + dx >= WIDTH:
            dx = WIDTH - self.rect.right
        if self.rect.bottom + dy >= HEIGHT:
            dy = 0
            self.vel_y = 0

        self.rect.x += dx
        self.rect.y += dy


def main():
    pg.init()
    screen = pg.display.set_mode(SIZE)

    run = True
    
    clock = pg.time.Clock()
    player_image = pg.image.load('testing_animation.jpg').convert()
    wall_image = pg.image.load('wall.png').convert()
    
    player_width = player_image.get_width()
    player_height = player_image.get_height()
    wall_width = wall_image.get_width()
    wall_height = wall_image.get_height()

    starting_player_x = WIDTH // 2 + wall_width - 40
    starting_player_y = HEIGHT - player_height // 2

    player = Player(player_image, (starting_player_x, starting_player_y))

    while run:
        screen.fill((255, 255, 255))
        screen.blit(wall_image, (WIDTH // 2 - 40 - wall_width, HEIGHT - wall_height))
        screen.blit(wall_image, (WIDTH // 2 + 40, HEIGHT - wall_height))
        screen.blit(wall_image, (WIDTH // 2 - 40 - wall_width, HEIGHT - wall_height * 2))
        screen.blit(wall_image, (WIDTH // 2 + 40, HEIGHT - wall_height * 2))

        player.move()
        player.draw(screen)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        pg.display.flip()
        clock.tick(FPS)
    pg.quit()


if __name__ == '__main__':
    main()
