import pygame
import button

pygame.init()

# create game window
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
# pos fixed (in %) or free (in px)
position = "fixed"

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

# game variables
game_started = False
menu_state = "main"

# define fonts
font = pygame.font.SysFont("resources/fonts/Inter/static/Inter-Light.ttf", 30)

# define colours
TEXT_COL = (255, 255, 255)

# load button images
resume_img = pygame.image.load("img/btn_options.png").convert_alpha()
arrow_left_img = pygame.image.load("img/btn_arrow_left.png").convert_alpha()
arrow_right_img = pygame.image.load("img/btn_arrow_right.png").convert_alpha()
options_img = pygame.image.load("img/btn_options.png").convert_alpha()
quit_img = pygame.image.load("img/btn_options.png").convert_alpha()
video_img = pygame.image.load('img/btn_options.png').convert_alpha()
audio_img = pygame.image.load('img/btn_options.png').convert_alpha()
keys_img = pygame.image.load('img/btn_options.png').convert_alpha()
back_img = pygame.image.load('img/btn_options.png').convert_alpha()

# create button instances
if position == 'free':
    resume_button = button.Button(304, 125, resume_img, 0.5)
    options_button = button.Button(297, 250, options_img, 0.5)
    quit_button = button.Button(336, 375, quit_img, 0.5)
    video_button = button.Button(226, 75, video_img, 0.5)
    audio_button = button.Button(225, 200, audio_img, 0.5)
    keys_button = button.Button(246, 325, keys_img, 0.5)
    back_button = button.Button(332, 450, back_img, 0.5)
elif position == 'fixed':
    print(SCREEN_WIDTH // 2 - resume_img.get_width() // 2, resume_img.get_height())
    options_button = button.Button(SCREEN_WIDTH // 2 - resume_img.get_width() // 2,
                                   0.75 * SCREEN_HEIGHT - options_img.get_height() // 2, resume_img, 1)
    arrow_left = button.Button(SCREEN_WIDTH // 2 - options_img.get_width() // 2 - 1.3 * arrow_left_img.get_width(),
                               0.75 * SCREEN_HEIGHT - options_img.get_height() // 3, arrow_left_img, 1)
    arrow_right = button.Button(SCREEN_WIDTH // 2 + options_img.get_width() // 2 + 0.35 * arrow_left_img.get_width(),
                                0.75 * SCREEN_HEIGHT - options_img.get_height() // 3, arrow_right_img, 1)
    resume_button = button.Button(SCREEN_WIDTH // 2 - resume_img.get_width() // 2, 250, options_img, 1)
    quit_button = button.Button(SCREEN_WIDTH // 2 - resume_img.get_width() // 2, 375, quit_img, 1)
    video_button = button.Button(SCREEN_WIDTH // 2 - resume_img.get_width() // 2, 75, video_img, 1)
    audio_button = button.Button(SCREEN_WIDTH // 2 - resume_img.get_width() // 2, 200, audio_img, 1)
    keys_button = button.Button(SCREEN_WIDTH // 2 - resume_img.get_width() // 2, 325, keys_img, 1)
    back_button = button.Button(SCREEN_WIDTH // 2 - resume_img.get_width() // 2, 450, back_img, 1)


def draw_text(text, font, text_col, x, y, pos="left"):
    if pos == "left":
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))
    elif pos == "center":
        text = font.render(text, True, text_col)
        text_rect = text.get_rect(center=(x, y))
        screen.blit(text, text_rect)


# game loop
run = True
while run:

    screen.fill((52, 78, 91))

    # check if game is paused
    if game_started == True:
        # check menu state
        if menu_state == "main":
            # draw pause screen buttons
            if resume_button.draw(screen):
                game_started = False
            if options_button.draw(screen):
                menu_state = "options"
            if arrow_left.draw(screen):
                print("Next option")
            if arrow_right.draw(screen):
                print("Previous option")
            if quit_button.draw(screen):
                run = False
        # check if the options menu is open
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
    else:
        text1, text2 = "Нажмите пробел", "для остановки"
        if len(text1) * 5 < SCREEN_WIDTH // 2: # Проверяю длину текста, чтобы он не выходил за границы
            draw_text(text1,  font, TEXT_COL, SCREEN_WIDTH // 2, 250, "center")
            draw_text(text2, font, TEXT_COL, SCREEN_WIDTH // 2, 350, "center")

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_started = True
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
