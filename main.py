import pygame as pg

from Player_class import Player
from levels.start import start_pos
from Platform_class import Platform


SIZE = WIDTH, HEIGHT = 400, 600
FPS = 60

# Original velocity
VELOCITY = 10

platforms = pg.sprite.Group()


# Main function
def main():
    pg.init()
    screen = pg.display.set_mode(SIZE)

    run = True
    
    clock = pg.time.Clock()
    # Creating player object
    player = Player((0, 0))
    platform = Platform()
    platforms.add(platform)

    wall_width = 20
    wall_height = 80

    starting_player_x = WIDTH // 2 + wall_width - 40
    starting_player_y = HEIGHT - 20

    player.set_position((starting_player_x, starting_player_y))

    while run:
        # Drawing process
        screen.fill((255, 255, 255))
        start_pos.draw(screen)
        player.draw(screen)
        platform.draw(screen)
        for wall in start_pos:
            pg.draw.rect(screen, 'blue', wall.rect, 2)
        # Player moving
        player.update(platforms)
        player.move()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    player.jump(platforms)
                    print('space pressed')

        pg.display.flip()
        clock.tick(FPS)
    pg.quit()


if __name__ == '__main__':
    main()
