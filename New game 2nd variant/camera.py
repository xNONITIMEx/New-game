import pygame


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        from main import player
        # if type(obj) is not Player:
        obj.rect.x += self.dx
        # if self.previous_point < player.rect.y:
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        from main import HEIGHT, WIDTH
        current_point = target.rect.y
        if target:
            self.dx = -(target.rect.x + target.rect.w // 2 - WIDTH // 2)
            if target.dir_y > 0:
                self.dy = 0
            else:
                self.dy = -(target.rect.y + target.rect.h // 2 - HEIGHT // 2)
