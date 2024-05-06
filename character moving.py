import pygame
pygame.init()

WIDTH, HEIGHT = 600, 600
SPEED = 1

screen = pygame.display.set_mode((WIDTH, HEIGHT))

character = pygame.image.load(r'C:\Users\HP\Downloads\pdf2png\Lost in space\Lost in space-1.png')  

CHARACTER_SIZE = (90, 90)
character = pygame.transform.scale(character, CHARACTER_SIZE)

character_rect = character.get_rect() 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_rect.x -= SPEED
    if keys[pygame.K_RIGHT]:
        character_rect.x += SPEED
    if keys[pygame.K_UP]:
        character_rect.y -= SPEED
    if keys[pygame.K_DOWN]:
        character_rect.y += SPEED

    screen.fill((0, 0, 0))
    screen.blit(character, character_rect)

    pygame.display.flip()

pygame.quit()