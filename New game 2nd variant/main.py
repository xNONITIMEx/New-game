import pygame
import sys
import os
import random

from player import Player
from tiles import Tile
from camera import Camera


FPS = 50
SIZE = WIDTH, HEIGHT = 400, 600
CELL_SIZE = CELL_WIDTH, CELL_HEIGHT = 50, 50
pygame.init()
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
wall_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
random_images = ['empty_top', 'empty_bot', 'empty', 'empty']


def terminate():
    pygame.quit()
    sys.exit()


def load_image(name, colorkey=None):
    fullname = os.path.join('assets', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def load_level(filename):
    filename = "levels/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    temp = list(map(lambda x: x.ljust(max_width, '.'), level_map))
    return [list(line) for line in temp]


level_presets = (
    load_level('level1.txt'),
    load_level('level2.txt'),
    load_level('level3.txt')
)


def generate_level(level):
    new_player, x, y = None, None, None
    playerx, playery = None, None
    c = 0
    if '@' in level[-1]:
        for y in range(len(level)):
            for x in range(len(level[y])):
                if level[y][x] == '.':
                    Tile(random.choice(random_images), x, y, tile_images, all_sprites)
                elif level[y][x] == '-':
                    Tile('top_wall', x, y, tile_images, wall_group, all_sprites)
                elif level[y][x] == '|':
                    Tile('mid_wall', x, y, tile_images, wall_group, all_sprites)
                elif level[y][x] == '_':
                    Tile('bot_wall', x, y, tile_images, wall_group, all_sprites)
                elif level[y][x] == '@':
                    Tile(random.choice(random_images), x, y, tile_images, all_sprites)
                    playerx = x
                    playery = y

    if playerx and playery:
        new_player = Player(playerx, playery, player_image, wall_group, all_sprites,  player_group)
    # вернем игрока, а также размер поля в клетках
    return new_player, x, y


tile_images = {
    'mid_wall': pygame.transform.scale(load_image('wall2_mid.png'), CELL_SIZE),
    'top_wall': pygame.transform.scale(load_image('wall2_top.png'), CELL_SIZE),
    'bot_wall': pygame.transform.scale(load_image('wall2_bot.png'), CELL_SIZE),
    'empty_top': pygame.transform.scale(load_image('bg_top_cloud.png'), CELL_SIZE),
    'empty_bot': pygame.transform.scale(load_image('bg_bot_cloud.png'), CELL_SIZE),
    'empty': pygame.transform.scale(load_image('bg_empty.png'), CELL_SIZE)
}
player_image = pygame.transform.scale(load_image('player.png'), (40, 50))

levels = list()
for _ in range(10):
    levels.extend(level_presets)
random.shuffle(levels)
level = list()
for lev in levels:
    level.extend(lev)
level.extend(load_level('level0.txt'))
player, level_x, level_y = generate_level(level)
camera = Camera()

count = 0


def main():
    global player
    global count
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.start_moving("left")
                elif event.key == pygame.K_RIGHT:
                    player.start_moving("right")

        screen.fill("white")
        all_sprites.update()
        all_sprites.draw(screen)
        camera.update(player)
        for sprite in all_sprites:
            camera.apply(sprite)
            if type(sprite) is not Player and not sprite.counted and sprite.rect.y > HEIGHT:
                count += 1
                sprite.counted = True
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    main()
    print(count)
    print(count / 8)
    # end_screen()
    terminate()
