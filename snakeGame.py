# Classic snake video game using pygame.

import pygame
from random import randrange

pygame.init()

# Set game window dimensions
display_width = 400
display_height = 400
display = pygame.display.set_mode((display_width, display_width))
pygame.display.set_caption("The Snake")

# Set colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)

# Setting game clock
clock = pygame.time.Clock()

# Game fonts
font_style = pygame.font.SysFont("Helvetica", 18)
score_font = pygame.font.SysFont("Helvetica", 20)
nom_font = pygame.font.SysFont("Helvetica", 12)


# Score rendering during the game
def user_score(score, snake_speed):
    value = score_font.render("Score: " + str((score * 10) * (snake_speed - 7)), True, black)
    display.blit(value, [0, 0])


def speed_show(snake_speed):
    speed = score_font.render("Speed: " + str(snake_speed - 6), True, black)
    display.blit(speed, [300, 0])


# Defines block size of the snake and adds on to the length after food is eaten.
def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, green, [x[0], x[1], snake_block, snake_block])


# Game over screen
def message(msg, msg2, color):
    msg = font_style.render(msg, True, color)
    msg2 = font_style.render(msg2, True, color)
    display.blit(msg, [display_width / 8, display_height / 8])
    display.blit(msg2, [display_width / 8, display_height / 4])


# Randomly generates a piece of food. Used after game initialization and when snake eats a food
def place_food(snake_block):
    food_x = round(randrange(0, display_width - snake_block) / 10.0) * 10.0
    food_y = round(randrange(0, display_height - snake_block) / 10.0) * 10.0
    return food_x, food_y


# Nom-nom animation if snake eats food
def nom_nom(nom, snake_x, snake_y):
    if nom:
        nom_display = nom_font.render("nom nom", True, black)
        display.blit(nom_display, [snake_x + 5, snake_y + 5])
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(30)


def game_loop():
    game_running = True
    game_close = False

    # Setting initial snake_head in the middle of the screen. Length of snake is 1 and
    # speed set to 7 and block size of snake is set to 10(length and speed increases with each food eaten).
    snake_x = display_width / 2
    snake_y = display_height / 2
    x_change = 0
    y_change = 0
    snake_list = []
    length_of_snake = 1
    snake_speed = 7
    snake_block = 10

    # Initial placement of food.
    food_x = place_food(snake_block)[0]
    food_y = place_food(snake_block)[1]

    while game_running:

        while game_close:  # End game screen message and key presses to re-start or quit
            display.fill(white)
            message("Game Over! Your score: {}"
                    .format(str(((length_of_snake - 1) * 10) * (snake_speed - 7))),
                    "N: New Game or Q: Quit", black)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_running = False
                        game_close = False
                    if event.key == pygame.K_n:
                        game_loop()

        # Assigning key presses for in game. Using arrow keys for movement.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        # Game over if snake goes off-screen
        if snake_x >= display_width or snake_x < 0 or snake_y >= display_height or snake_y < 0:
            game_close = True

        snake_x += x_change
        snake_y += y_change
        display.fill(white)
        pygame.draw.rect(display, red, [food_x, food_y, snake_block, snake_block])
        snake_head = [snake_x, snake_y]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # If snake head runs into itself, end game.
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        snake(snake_block, snake_list)
        user_score(length_of_snake - 1, snake_speed)
        speed_show(snake_speed)

        pygame.display.update()

        # If food is eaten, randomly place new piece of food, increase length of snake and its speed. Snake also says
        # 'nom-nom'
        if snake_x == food_x and snake_y == food_y:
            nom = True
            nom_nom(nom, snake_x, snake_y)
            food_x = place_food(snake_block)[0]
            food_y = place_food(snake_block)[1]
            length_of_snake += 1
            snake_speed += 1

        clock.tick(snake_speed)
    pygame.quit()
    quit()


game_loop()
