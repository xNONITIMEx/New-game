import pygame as pg
from Player_class import Player
from Wall_class import Wall
from levels.start import start_pos


SIZE = WIDTH, HEIGHT = 400, 600
FPS = 60

# Original velocity
VELOCITY = 10

all_walls = pg.sprite.Group()


# Main function
def main():
    pg.init()
    screen = pg.display.set_mode(SIZE)

    run = True
    
    clock = pg.time.Clock()
    # Saving images to variables
    # Saving parameters of images
    # Player starting coordinates
    # Creating player object
    player = Player((0, 0))
    wall = Wall((0, 0))

    player_width, player_height = player.width, player.height
    wall_width = 19
    wall_height = 80

    starting_player_x = WIDTH // 2 + wall_width - 40
    starting_player_y = HEIGHT - player_height // 2

    player.set_position((starting_player_x, starting_player_y))

    while run:
        # Drawing process
        screen.fill((255, 255, 255))
        # wall.draw(screen, (WIDTH // 2 - 40 - wall_width, HEIGHT - wall_height))
        # wall.draw(screen, (WIDTH // 2 + 40, HEIGHT - wall_height))
        # wall.draw(screen, (WIDTH // 2 - 40 - wall_width, HEIGHT - wall_height * 2))
        # wall.draw(screen, (WIDTH // 2 + 40, HEIGHT - wall_height * 2))
        all_walls.add(wall)
        all_walls.update()
        start_pos.update()
        start_pos.draw(screen)
        all_walls.draw(screen)
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
