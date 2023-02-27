import pygame
import sys
import os
import random

from player import Player
from tiles import Tile
from camera import Camera


FPS = 50
SIZE = WIDTH, HEIGHT = 600, 800
CELL_SIZE = CELL_WIDTH, CELL_HEIGHT = 50, 50

CELLS_IN_ROW = WIDTH // CELL_WIDTH

pygame.init()
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
wall_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
spikes = pygame.sprite.Group()

random_images = ['empty_top', 'empty_bot', 'empty', 'empty']

SCORE = 0

pygame.font.init()
PIXEL_FONT = pygame.font.Font('Early GameBoy.ttf', 70)


# Функция остановки игры
def terminate():
    pygame.quit()
    sys.exit()


# Загрузка спрайтов
def load_image(name, colorkey=None, size=CELL_SIZE):
    fullname = os.path.join('assets', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.transform.scale(pygame.image.load(fullname), size)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


# Загрузка уровня
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
    load_level('level3.txt'),
    # load_level('level4.txt'),
    # load_level('level5.txt'),
    # load_level('level6.txt'),
    # load_level('level7.txt'),
)

# Генерация уровня
def generate_level(level):
    new_player, x, y = None, None, None
    playerx, playery = None, None
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
            elif level[y][x] == '<':
                Tile('left_spike', x, y, tile_images, all_sprites, spikes)
            elif level[y][x] == '>':
                Tile('right_spike', x, y, tile_images, all_sprites, spikes)
            elif level[y][x] == '@':
                Tile(random.choice(random_images), x, y, tile_images, all_sprites)
                playerx = x
                playery = y

    if playerx and playery:
        new_player = Player(playerx, playery, player_image, wall_group, spikes, all_sprites,  player_group)
    # вернем игрока, а также размер поля в клетках
    return new_player, x, y

tile_images = {
    'left_spike': pygame.transform.scale(load_image('left_spike.png'), CELL_SIZE),
    'right_spike': pygame.transform.scale(load_image('right_spike.png'), CELL_SIZE),
    'mid_wall': pygame.transform.scale(load_image('wall2_mid.png'), CELL_SIZE),
    'top_wall': pygame.transform.scale(load_image('wall2_top.png'), CELL_SIZE),
    'bot_wall': pygame.transform.scale(load_image('wall2_bot.png'), CELL_SIZE),
    'empty_top': pygame.transform.scale(load_image('bg_top_cloud.png'), CELL_SIZE),
    'empty_bot': pygame.transform.scale(load_image('bg_bot_cloud.png'), CELL_SIZE),
    'empty': pygame.transform.scale(load_image('bg_empty.png'), CELL_SIZE)
}
player_image = load_image('player.png', size=(300, 100))
# Загрузка всех уровней в игру


def main(SCORE):
    global player

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
    game_started = False
    running = True
    while running:
        text = PIXEL_FONT.render(str(int(SCORE / CELLS_IN_ROW)), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (WIDTH // 2, 100)

        spike = pygame.sprite.spritecollideany(player, spikes)
        # Проверка для останвоки игры
        if spike or (player.rect.midbottom[1] > HEIGHT and game_started):
            running = False

        if not player.is_moving and game_started:
            player.rect.y += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT or spike:
                running = False
                break
            if event.type == pygame.KEYDOWN:
                # Прыжок игрока
                if event.key == pygame.K_LEFT:
                    player.start_moving("left")
                    game_started = True
                elif event.key == pygame.K_RIGHT:
                    game_started = True
                    player.start_moving("right")
                if event.key == pygame.K_ESCAPE:
                    terminate()
                    return SCORE / CELLS_IN_ROW
        # Скольжение по стене
        collide = pygame.sprite.spritecollideany(player, wall_group)
        if collide:
            print('touching')
            player.rect.y += 1

        screen.fill("white")
        all_sprites.draw(screen)
        screen.blit(text, textRect)

        all_sprites.update()
        camera.update(player)
        # Засчитыывание очка
        for sprite in all_sprites:
            camera.apply(sprite)
            if type(sprite) is not Player and not sprite.counted and sprite.rect.y > HEIGHT:
                SCORE += 1
                sprite.counted = True
        pygame.display.flip()
        clock.tick(FPS)
    return SCORE / CELLS_IN_ROW
