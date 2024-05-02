import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
STAR_COUNT = int(WIDTH * HEIGHT * 0.001)
BUTTON_FONT_SIZE = 32
START_BUTTON_COLOR = WHITE
OPTION_BUTTON_COLOR = (255, 165, 0)
SOUND_BUTTON_COLOR = (0, 255, 0)
MUTE_BUTTON_COLOR = (255, 0, 0)
DIFFICULTY_BUTTON_COLOR = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

stars = []

for i in range(STAR_COUNT):
    star = {
        'x': random.randint(0, WIDTH),
        'y': random.randint(0, HEIGHT),
        'speed': random.randint(1, 3)
    }
    stars.append(star)

start_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 200, 50)
option_button = pygame.Rect(WIDTH - 150, HEIGHT - 150, 100, 50)

sound_button = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2, 100, 50)
mute_button = pygame.Rect(WIDTH // 2 + 50, HEIGHT // 2, 100, 50)

easy_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 100, 200, 50)
medium_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 200, 50)
hard_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 100, 200, 50)

sound_level = 0.1

running = True
show_options = False
show_difficulty = False
while running:
    pygame.time.Clock().tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not show_options and not show_difficulty and start_button.collidepoint(event.pos):
                show_difficulty = True
            if not show_options and not show_difficulty and option_button.collidepoint(event.pos):
                show_options = True
            if show_options and sound_button.collidepoint(event.pos):
                sound_level += 0.01
                if sound_level > 1.0:
                    sound_level = 1.0
                print("Sound button clicked! Sound level: {:.0%}".format(sound_level))
            if show_options and mute_button.collidepoint(event.pos):
                sound_level = 0.0
                print("Mute button clicked! Sound level: {:.0%}".format(sound_level))
            if show_difficulty and easy_button.collidepoint(event.pos):
                print("Easy button clicked!")
            if show_difficulty and medium_button.collidepoint(event.pos):
                print("Medium button clicked!")
            if show_difficulty and hard_button.collidepoint(event.pos):
                print("Hard button clicked!")

    for star in stars:
        star['y'] += star['speed']
        if star['y'] > HEIGHT:
            star['y'] = 0

    screen.fill(BLACK)
    for star in stars:
        pygame.draw.rect(screen, WHITE, pygame.Rect(star['x'], star['y'], 2, 2))

    if not show_options and not show_difficulty:
        pygame.draw.rect(screen, START_BUTTON_COLOR, start_button)
        pygame.draw.rect(screen, OPTION_BUTTON_COLOR, option_button)

        start_button_text = pygame.font.Font(None, BUTTON_FONT_SIZE).render("Start", True, BLACK)
        option_button_text = pygame.font.Font(None, BUTTON_FONT_SIZE).render("Options", True, BLACK)
        screen.blit(start_button_text, (WIDTH // 2 - 100 + (start_button.width - start_button_text.get_width()) // 2, HEIGHT // 2 + (start_button.height - start_button_text.get_height()) // 2))
        screen.blit(option_button_text, (WIDTH - 150 + (option_button.width - option_button_text.get_width()) // 2, HEIGHT - 150 + (option_button.height - option_button_text.get_height()) // 2))
    elif show_options:
        pygame.draw.rect(screen, SOUND_BUTTON_COLOR, sound_button)
        pygame.draw.rect(screen, MUTE_BUTTON_COLOR, mute_button)

        sound_button_text = pygame.font.Font(None, BUTTON_FONT_SIZE).render("Sound: {:.0%}".format(sound_level), True, BLACK)
        mute_button_text = pygame.font.Font(None, BUTTON_FONT_SIZE).render("Mute", True, BLACK)
        screen.blit(sound_button_text, (WIDTH // 2 - 150 + (sound_button.width - sound_button_text.get_width()) // 2, HEIGHT // 2 + (sound_button.height - sound_button_text.get_height()) // 2))
        screen.blit(mute_button_text, (WIDTH // 2 + 50 + (mute_button.width - mute_button_text.get_width()) // 2, HEIGHT // 2 + (mute_button.height - mute_button_text.get_height()) // 2))
    elif show_difficulty:
        pygame.draw.rect(screen, DIFFICULTY_BUTTON_COLOR, easy_button)
        pygame.draw.rect(screen, DIFFICULTY_BUTTON_COLOR, medium_button)
        pygame.draw.rect(screen, DIFFICULTY_BUTTON_COLOR, hard_button)

        easy_button_text = pygame.font.Font(None, BUTTON_FONT_SIZE).render("Easy", True, BLACK)
        medium_button_text = pygame.font.Font(None, BUTTON_FONT_SIZE).render("Medium", True, BLACK)
        hard_button_text = pygame.font.Font(None, BUTTON_FONT_SIZE).render("Hard", True, BLACK)
        screen.blit(easy_button_text, (WIDTH // 2 - 100 + (easy_button.width - easy_button_text.get_width()) // 2, HEIGHT // 2 - 100 + (easy_button.height - easy_button_text.get_height()) // 2))
        screen.blit(medium_button_text, (WIDTH // 2 - 100 + (medium_button.width - medium_button_text.get_width()) // 2, HEIGHT // 2 + (medium_button.height - medium_button_text.get_height()) // 2))
        screen.blit(hard_button_text, (WIDTH // 2 - 100 + (hard_button.width - hard_button_text.get_width()) // 2, HEIGHT // 2 + 100 + (hard_button.height - hard_button_text.get_height()) // 2))

    pygame.display.flip()

pygame.quit()