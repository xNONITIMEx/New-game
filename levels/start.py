import pygame as pg
from Wall_class import Wall


WIDTH, HEIGHT = 400, 600

wall_width = 19
wall_height = 80
start_pos = pg.sprite.Group()
wall1 = Wall((WIDTH // 2 - 80 - wall_width // 2, HEIGHT - wall_height * 0.5 - 20), start_pos)
wall2 = Wall((WIDTH // 2 + 80, HEIGHT - wall_height * 0.5 - 20), start_pos)
wall3 = Wall((WIDTH // 2 - 80 - wall_width // 2, HEIGHT - wall_height * 1.5 - 20), start_pos)
wall4 = Wall((WIDTH // 2 + 80, HEIGHT - wall_height * 1.5 - 20), start_pos)
wall5 = Wall((WIDTH // 2 - 80 - wall_width // 2, HEIGHT - wall_height * 2.5 - 20), start_pos)
wall6 = Wall((WIDTH // 2 + 80, HEIGHT - wall_height * 2.5 - 20), start_pos)

