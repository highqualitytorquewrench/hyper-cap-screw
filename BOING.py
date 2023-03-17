import sys
import pygame
from pygame.locals import *

# Initialize game
pygame.init()

# Constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PLATFORM_WIDTH = 100
PLATFORM_HEIGHT = 10
BALL_RADIUS = 10
GRAVITY = 1
BOUNCINESS = 0.8
PLATFORM_SPEED = 5

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Boing')

# Platform
platform = pygame.Rect(SCREEN_WIDTH // 2 - PLATFORM_WIDTH // 2, SCREEN_HEIGHT - PLATFORM_HEIGHT - 10, PLATFORM_WIDTH, PLATFORM_HEIGHT)

# Ball
ball_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
ball_speed = [2, 5]

clock = pygame.time.Clock()

while True:
    screen.fill(WHITE)

    # Draw platform
    pygame.draw.rect(screen, BLACK, platform)

    # Draw ball
    pygame.draw.circle(screen, BLACK, (int(ball_pos[0]), int(ball_pos[1])), BALL_RADIUS)

    # Update ball position and speed
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Ball collision with the wall
    if ball_pos[0] - BALL_RADIUS <= 0 or ball_pos[0] + BALL_RADIUS >= SCREEN_WIDTH:
        ball_speed[0] = -ball_speed[0]

    # Ball collision with the platform
    if platform.collidepoint(ball_pos[0], ball_pos[1] + BALL_RADIUS) and ball_speed[1] > 0:
        ball_speed[1] = -int(ball_speed[1] * BOUNCINESS)

    # Apply gravity
    ball_speed[1] += GRAVITY

    # Move the platform
    keys = pygame.key.get_pressed()
    if keys[K_LEFT] and platform.left > 0:
        platform.move_ip(-PLATFORM_SPEED, 0)
    if keys[K_RIGHT] and platform.right < SCREEN_WIDTH:
        platform.move_ip(PLATFORM_SPEED, 0)

    # Check events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Update display
    pygame.display.update()
    clock.tick(60)
