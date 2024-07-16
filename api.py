import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Game Variables
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
snake_direction = (1, 0)  # Initial direction: right
snake_speed = 8
food_position = (10, 10)  # Initial food position
score = 0
game_over = False

# Bonus food settings
bonus_food_active = False
bonus_food_position = (-1, -1)
bonus_food_value = 0

# Cheat code flag
cheat_code_active = False

# Pygame screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Xenzia')

# Function to reset the game
def reset_game():
    global snake, snake_direction, game_over, food_position, score, bonus_food_active, bonus_food_position, bonus_food_value, cheat_code_active
    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
    snake_direction = (1, 0)
    food_position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    score = 0
    game_over = False
    bonus_food_active = False
    bonus_food_position = (-1, -1)
    bonus_food_value = 0
    cheat_code_active = False

# Function to draw the snake
def draw_snake(snake):
    for i, segment in enumerate(snake):
        # Head
        if i == 0:
            pygame.draw.circle(screen, GREEN, (int(segment[0] * GRID_SIZE + GRID_SIZE / 2), int(segment[1] * GRID_SIZE + GRID_SIZE / 2)), int(GRID_SIZE / 2))
            pygame.draw.circle(screen, BLACK, (int(segment[0] * GRID_SIZE + GRID_SIZE / 2), int(segment[1] * GRID_SIZE + GRID_SIZE / 2)), int(GRID_SIZE / 3))
            pygame.draw.circle(screen, YELLOW, (int(segment[0] * GRID_SIZE + GRID_SIZE / 2 + GRID_SIZE / 6), int(segment[1] * GRID_SIZE + GRID_SIZE / 2 - GRID_SIZE / 6)), int(GRID_SIZE / 6))
            pygame.draw.circle(screen, BLACK, (int(segment[0] * GRID_SIZE + GRID_SIZE / 2 + GRID_SIZE / 6), int(segment[1] * GRID_SIZE + GRID_SIZE / 2 - GRID_SIZE / 6)), int(GRID_SIZE / 12))
        else:
            # Body
            pygame.draw.circle(screen, GREEN, (int(segment[0] * GRID_SIZE + GRID_SIZE / 2), int(segment[1] * GRID_SIZE + GRID_SIZE / 2)), int(GRID_SIZE / 2))

# Function to draw the bonus food
def draw_bonus_food():
    if bonus_food_active:
        pygame.draw.circle(screen, BLUE, (int(bonus_food_position[0] * GRID_SIZE + GRID_SIZE / 2), int(bonus_food_position[1] * GRID_SIZE + GRID_SIZE / 2)), int(GRID_SIZE / 2))

# Function to handle game over
def game_over_screen():
    font = pygame.font.SysFont(None, 48)
    text = font.render("Game Over! Press SPACE to restart", True, WHITE)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, text_rect)

# Function to handle collision with food
def handle_food_collision():
    global score, snake_speed, bonus_food_active, bonus_food_position, bonus_food_value

    score += 1
    snake_speed += 0.5  # Increase speed slightly with each food eaten

    if score == 10:
        bonus_food_active = True
        bonus_food_value = 1
        place_bonus_food()

    elif score == 20:
        bonus_food_active = True
        bonus_food_value = 4
        place_bonus_food()

    elif score == 50:
        bonus_food_active = True
        bonus_food_value = 10
        place_bonus_food()

    return True

# Function to place bonus food
def place_bonus_food():
    global bonus_food_position
    while True:
        x = random.randint(0, GRID_WIDTH - 1)
        y = random.randint(0, GRID_HEIGHT - 1)
        if (x, y) not in snake and (x, y) != food_position:
            bonus_food_position = (x, y)
            break

# Function to handle collision with bonus food
def handle_bonus_food_collision():
    global snake, bonus_food_active, bonus_food_value
    snake = snake[:-bonus_food_value]
    bonus_food_active = False
    bonus_food_value = 0

# Cheat code function
def activate_cheat_code():
    global cheat_code_active
    cheat_code_active = True

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction = (1, 0)
            elif event.key == pygame.K_SPACE and game_over:
                reset_game()
            elif event.key == pygame.K_0 and not cheat_code_active:
                activate_cheat_code()

    if not game_over:
        # Update snake position
        snake_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])

        # Check for cheat code activation
        if cheat_code_active:
            snake_head = food_position  # Move snake instantly to food position
            cheat_code_active = False  # Deactivate cheat code after use

        # Check game over conditions
        if (snake_head[0] < 0 or snake_head[0] >= GRID_WIDTH or
                snake_head[1] < 0 or snake_head[1] >= GRID_HEIGHT or
                snake_head in snake[1:]):
            game_over = True

        if not game_over:
            snake.insert(0, snake_head)
            if snake_head == food_position:
                if handle_food_collision():
                    food_position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            elif snake_head == bonus_food_position:
                handle_bonus_food_collision()
            else:
                snake.pop()

            # Clear screen
            screen.fill(BLACK)

            # Draw snake
            draw_snake(snake)

            # Draw food
            pygame.draw.rect(screen, RED, (food_position[0] * GRID_SIZE, food_position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

            # Draw bonus food if active
            draw_bonus_food()

            # Draw score
            font = pygame.font.SysFont(None, 24)
            score_text = font.render(f"Score: {score}", True, WHITE)
            screen.blit(score_text, (10, 10))

    else:
        # Game over screen
        game_over_screen()

    # Update display
    pygame.display.update()

    # Adjust game speed
    pygame.time.Clock().tick(snake_speed)
