import pygame as pg
from pygame.locals import *
from Player_class import Player

SIZE = WIDTH, HEIGHT = 400, 600
FPS = 60

# Original velocity
VELOCITY = 10


# Main function
def main():
    pg.init()
    screen = pg.display.set_mode(SIZE)

    run = True
    
    clock = pg.time.Clock()
    # Saving images to variables
    player_image = pg.image.load('player.png').convert()
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
