import pygame

JUMP_HEIGHT = 200
JUMP_SPEED = 6


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, image, walls, spikes, *groups):
        from main import CELL_WIDTH, CELL_HEIGHT
        super().__init__(*groups)
        self.image = image
        self.pos_x, self.pos_y = pos_x, pos_y
        self.rect = self.image.get_rect().move(CELL_WIDTH * pos_x + 15, CELL_HEIGHT * pos_y + 10)
        self.is_moving = self.going_up = self.double_jump = False
        self.moving_dir = None
        self.jump_height = JUMP_HEIGHT
        self.l_double_jumped = False
        self.r_double_jumped = False
        self.walls = walls
        self.spikes = spikes

        self.jump_speed = JUMP_SPEED

        self.tracking_tile = None
        self.dir_y = 0

    def start_moving(self, direction):
        if self.is_moving:
            return
        self.is_moving = self.going_up = True
        self.moving_dir = direction
        self.jump_height = self.rect.y - JUMP_HEIGHT

    def stop_moving(self):
        if not self.is_moving:
            return

        self.is_moving = self.going_up = False
        self.moving_dir = self.jump_height = None

    def move(self, diff):
        if self.going_up:
            if diff < 400:
                return -15
            elif diff < 150:
                return -3
            else:
                self.going_up = False
                return -1
        else:
            if diff < 350:
                return 10
            elif diff < 150:
                return 5
            else:
                return 4

    def update(self):
        keys = pygame.key.get_pressed()
        wall = pygame.sprite.spritecollideany(self, self.walls)
        # Высота, на которую должен прыгнуть игрок
        diff = 100
        self.dir_y = 0
        if not self.is_moving:
            return
        # Изменение диффа
        if type(self.tracking_tile) is not int and self.tracking_tile:
            diff = abs(self.tracking_tile.rect.y - self.jump_height)
        elif type(self.tracking_tile) is int:
            diff = abs(self.tracking_tile - self.jump_height)
        # Двойной прыжок
        if keys[pygame.K_LEFT] and not self.l_double_jumped:
            self.l_double_jumped = True
            self.moving_dir = 'left'
            self.tracking_tile = self.rect.y
        if keys[pygame.K_RIGHT] and not self.r_double_jumped:
            self.r_double_jumped = True
            self.moving_dir = 'right'
            self.tracking_tile = self.rect.y

        self.dir_y = self.move(diff)
        # Подъем точки отсчета вместе с игроком
        if type(self.tracking_tile) is int:
            self.tracking_tile += abs(self.dir_y)

        if wall:
            self.dir_y += 1

        dir_x = JUMP_SPEED if self.moving_dir == "right" else -JUMP_SPEED
        self.rect = self.rect.move(dir_x, self.dir_y)
        # Проверка касания стены
        if wall:
            self.stop_moving()
            self.tracking_tile = wall
            self.l_double_jumped = False
            self.r_double_jumped = False
            # Если касание стены внизу
            if self.rect.collidepoint(wall.rect.midbottom) or self.rect.collidepoint(wall.rect.bottomleft) or self.rect.collidepoint(wall.rect.bottomright):
                from main import WIDTH
                if wall.rect.x > WIDTH // 2:
                    self.rect.right = wall.rect.left
                else:
                    self.rect.left = wall.rect.right