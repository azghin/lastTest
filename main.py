import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Pygame Example")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player settings
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT - player_size
player_speed = 5

# Enemy settings
enemy_size = 50
enemy_x = random.randint(0, WIDTH - enemy_size)
enemy_y = 0
enemy_speed = 3

clock = pygame.time.Clock()

def game_over():
    font = pygame.font.SysFont(None, 55)
    text = font.render('Game Over!', True, RED)
    screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2 - 30))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = 0
        enemy_x = random.randint(0, WIDTH - enemy_size)

    # Collision detection
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)
    if player_rect.colliderect(enemy_rect):
        game_over()

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, player_rect)
    pygame.draw.rect(screen, RED, enemy_rect)
    pygame.display.flip()
    clock.tick(60)