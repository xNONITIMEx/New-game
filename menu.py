import button
import pygame
import os
import sys
from main import terminate

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
# pos fixed (in %) or free (in px)
position = "fixed"

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

game_started = False
menu_state = "main"

FONT_ARIAL_BLACK_30 = pygame.font.SysFont("arialblack", 30)
FONT_INTER_LIGHT_30 = pygame.font.Font("Inter-Light.ttf", 30)
FONT_INTER_BLACK_30 = pygame.font.Font("Inter-Light.ttf", 30)
FONT_INTER_REGULAR_40 = pygame.font.Font("resources/fonts/Inter/static/Inter-Regular.ttf", 40)
FONT_INTER_REGULAR_50 = pygame.font.Font("resources/fonts/Inter/static/Inter-Regular.ttf", 50)

TEXT_COL = (255, 255, 255)

# Инициализация списков для работы со слайдерами (sliders), кнопками, меняющимся текстом и т.д.
display_greetings = ['Тык-тык', 'Тук-тук', 'Тач-тач', 'Клик-клик', 'Ту-ту-тук', 'Ты дятел?', 'Бесит да?']
list_main_button_slider = ['Настройки', 'Персонажи', 'О разработке', 'Выйти']
current_setting = list_main_button_slider[0]

# load button images
wallpaper1_img = pygame.image.load("img/wallpaper1.png").convert_alpha()
arrow_left_img = pygame.image.load("img/btn_arrow_left.png").convert_alpha()
arrow_right_img = pygame.image.load("img/btn_arrow_right.png").convert_alpha()
options_img = pygame.image.load("img/horizontal_wide_button.png").convert_alpha()
menu_options_img = pygame.image.load("img/menu_settings.png").convert_alpha()
folder_img = pygame.image.load("img/btn_settings_folder.png").convert_alpha()
volume_img = pygame.image.load("img/btn_settings_volume.png").convert_alpha()
support_img = pygame.image.load("img/btn_settings_support.png").convert_alpha()
level_1_img = pygame.image.load("img/btn_settings_level_1.png").convert_alpha()
level_2_img = pygame.image.load("img/btn_settings_level_2.png").convert_alpha()
level_3_img = pygame.image.load("img/btn_settings_level_3.png").convert_alpha()
level_4_img = pygame.image.load("img/btn_settings_level_4.png").convert_alpha()

quit_img = pygame.image.load("img/btn_options.png").convert_alpha()
video_img = pygame.image.load('img/btn_options.png').convert_alpha()
audio_img = pygame.image.load('img/btn_options.png').convert_alpha()
keys_img = pygame.image.load('img/btn_options.png').convert_alpha()
back_img = pygame.image.load('img/btn_options.png').convert_alpha()

if position == 'free':
    resume_button = button.Button(304, 125, options_img, 0.5)
    options_button = button.Button(297, 250, options_img, 0.5)
    quit_button = button.Button(336, 375, quit_img, 0.5)
    video_button = button.Button(226, 75, video_img, 0.5)
    audio_button = button.Button(225, 200, audio_img, 0.5)
    keys_button = button.Button(246, 325, keys_img, 0.5)
    back_button = button.Button(332, 450, back_img, 0.5)
elif position == 'fixed':
    print(SCREEN_WIDTH // 2 - options_img.get_width() // 2, options_img.get_height())
    options_button = button.Button(SCREEN_WIDTH // 2 - options_img.get_width() // 2,
                                   0.75 * SCREEN_HEIGHT - options_img.get_height() // 2, options_img, 1)
    surf_button_options = pygame.Surface(options_button.rect.size)
    arrow_left = button.Button(SCREEN_WIDTH // 2 - 1.5 * options_img.get_width() // 2,
                               0.75 * SCREEN_HEIGHT - options_img.get_height() // 3, arrow_left_img, 1)
    arrow_right = button.Button(SCREEN_WIDTH // 2 + options_img.get_width() // 2 + 0.35 * arrow_right_img.get_width(),
                                0.75 * SCREEN_HEIGHT - options_img.get_height() // 3, arrow_right_img, 1)
    menu_options = button.Button(SCREEN_WIDTH // 2 - menu_options_img.get_width() // 2, SCREEN_HEIGHT * 0.325,
                                 menu_options_img, 1)
    btn_menu_settings_volume = button.Button(SCREEN_WIDTH * 0.22, SCREEN_HEIGHT * 0.46, volume_img, 1)
    btn_menu_settings_folder = button.Button(SCREEN_WIDTH * 0.43, SCREEN_HEIGHT * 0.46, folder_img, 1)
    btn_menu_settings_support = button.Button(SCREEN_WIDTH * 0.64, SCREEN_HEIGHT * 0.46, support_img, 1)
    btn_menu_settings_level_1 = button.Button(SCREEN_WIDTH * 0.15, SCREEN_HEIGHT * 0.66, level_1_img, 1)
    btn_menu_settings_level_2 = button.Button(SCREEN_WIDTH * 0.52, SCREEN_HEIGHT * 0.66, level_2_img, 1)
    btn_menu_settings_level_3 = button.Button(SCREEN_WIDTH * 0.15, SCREEN_HEIGHT * 0.8, level_3_img, 1)
    btn_menu_settings_level_4 = button.Button(SCREEN_WIDTH * 0.52, SCREEN_HEIGHT * 0.8, level_4_img, 1)

    resume_button = button.Button(SCREEN_WIDTH // 2 - options_img.get_width() // 2, 250, options_img, 1)
    quit_button = button.Button(SCREEN_WIDTH // 2 - options_img.get_width() // 2, 375, quit_img, 1)
    video_button = button.Button(SCREEN_WIDTH // 2 - options_img.get_width() // 2, 75, video_img, 1)
    audio_button = button.Button(SCREEN_WIDTH // 2 - options_img.get_width() // 2, 200, audio_img, 1)
    keys_button = button.Button(SCREEN_WIDTH // 2 - options_img.get_width() // 2, 325, keys_img, 1)
    back_button = button.Button(SCREEN_WIDTH // 2 - options_img.get_width() // 2, 450, back_img, 1)


def draw_text(text, font, text_col, x, y, pos="left"):
    if pos == "left":
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))
    elif pos == "center":
        text = font.render(text, True, text_col)
        text_rect = text.get_rect(center=(x, y))
        screen.blit(text, text_rect)


def change_slider_position(data, direction):
    global pos
    print(len(data), pos)
    if len(data) - 1 > pos >= 0 and direction == "next":
        pos += 1
        print(1, "pos=", pos)
    elif len(data) - 1 >= pos >= 0 and direction == "previous":
        if pos == 0:
            pos = len(data) - 1
        else:
            pos -= 1
        print(2, "pos=", pos)
    else:
        pos = 0
        print(3, "pos=", pos)
    return data[pos]


pos = 0


def menu():
    run = True
    global game_started
    global menu_state
    global current_setting
    score = 0
    while run:
        screen.blit(wallpaper1_img, wallpaper1_img.get_rect())
        if not game_started:
            text1, text2 = "Нажмите пробел", "для продолжения"

            if menu_state == "main":
                options_button.draw(screen)
                arrow_left.draw(screen)
                arrow_right.draw(screen)
                draw_text(current_setting, FONT_INTER_REGULAR_40,
                          (217, 102, 102), SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.745, "center")
                # draw_text(list_main_button_slider[0], FONT_INTER_REGULAR_40, (217, 102, 102),
                #           SCREEN_WIDTH // 2, 594, "center")
                # text3 = FONT_INTER_BLACK_30.render("Помогите!", True, (217, 102, 102))
                if len(text1) * 5 < SCREEN_WIDTH // 2:  # Проверяю длину текста, чтобы он не выходил за границы
                    draw_text(text1, FONT_INTER_LIGHT_30, TEXT_COL, SCREEN_WIDTH // 2, 200, "center")
                    draw_text(text2, FONT_INTER_LIGHT_30, TEXT_COL, SCREEN_WIDTH // 2, 250, "center")
                # draw pause screen buttons
                if options_button.on_click():
                    menu_state = "options"
                if arrow_left.on_click():
                    current_setting = change_slider_position(list_main_button_slider, "previous")
                    options_button.set_type(current_setting)
                    print(current_setting)
                    print("Next option")
                if arrow_right.on_click():
                    current_setting = change_slider_position(list_main_button_slider, "next")
                    options_button.set_type(current_setting)
                    print(current_setting)
                    # draw_text(current_setting, FONT_INTER_LIGHT_30,
                    #           (217, 102, 102), 50, 450, "center")
                    print("Previous option")
                if quit_button.on_click() and quit_button.get_type() == 'Выйти':
                    print('clicked')
                    os.quit()
                    pygame.quit()
            if menu_state == "options":
                # draw the different options buttons
                if video_button.draw(screen):
                    print("Video Settings")
                if audio_button.draw(screen):
                    print("Audio Settings")
                if keys_button.draw(screen):
                    print("Change Key Bindings")
                if back_button.draw(screen):
                    menu_state = "main"
                if options_button.get_type() == "Настройки":
                    menu_options.draw(screen)
                    draw_text("Настройки", FONT_INTER_REGULAR_50,
                              (246, 76, 76), SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.4, "center")
                    btn_menu_settings_volume.draw(screen)
                    if btn_menu_settings_volume.on_click():
                        level_volume = 0
                    btn_menu_settings_folder.draw(screen)
                    if btn_menu_settings_folder.on_click():
                        path = os.path.abspath('./')
                        os.system(f'start {os.path.realpath(path)}')
                        # path = "C:/Users"
                        # path = os.path.realpath(path)
                        # os.startfile(path)
                    btn_menu_settings_support.draw(screen)
                    draw_text("Уровни", FONT_INTER_REGULAR_50,
                              (246, 76, 76), SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.6, "center")
                    btn_menu_settings_level_1.draw(screen)
                    btn_menu_settings_level_2.draw(screen)
                    btn_menu_settings_level_3.draw(screen)
                    btn_menu_settings_level_4.draw(screen)
                elif options_button.get_type() == "Выйти":
                    sys.exit(0)


                # draw the different options buttons
                # if video_button.draw(screen):
                #     print("Video Settings")
                # if audio_button.draw(screen):
                #     print("Audio Settings")
                # if keys_button.draw(screen):
                #     print("Change Key Bindings")
                # if back_button.draw(screen):
                #     menu_state = "main"
        else:
            from main import main
            score = main(score)
            game_started = False
            print(score)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_started = True
                if event.key == pygame.K_ESCAPE:
                    if menu_state == 'main':
                        run = False
                    elif menu_state == 'options':
                        menu_state = 'main'
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    menu()