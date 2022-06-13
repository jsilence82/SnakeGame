import pygame
import random

pygame.init()

# set colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)

# set window
dis_width = 400
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_width))

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 0

font_style = pygame.font.SysFont("Helvetica", 18)
score_font = pygame.font.SysFont("Helvetica", 35)


def user_score(score):
    value = score_font.render("Score: " + str(score), True, white)
    dis.blit(value, [0, 0])


def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])


def message(msg, msg2, color):
    msg = font_style.render(msg, True, color)
    msg2 = font_style.render(msg2, True, color)
    dis.blit(msg, [dis_width / 8, dis_height / 8])
    dis.blit(msg2, [dis_width / 8, dis_height / 4])


# Game loop. While loop while game is running. Ends on snake or border collision.
def game_loop():
    game_over = False
    game_close = False

    # Setting initial snake_head in the middle of the screen. Length of snake is 1 and
    # speed set to 7 (increases with each food eaten).
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0
    snake_list = []
    length_of_snake = 1
    snake_speed = 7

    # Random placement of food.
    food_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:  # End game screen message and key presses to re-start or quit
            dis.fill(black)
            message("You Lost! Your score: {}".format(length_of_snake - 1), "N: New Game or Q:Quit", white)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_n:
                        game_loop()

        # Assigning key presses for in game.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Game over if snake goes off-screen
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, red, [food_x, food_y, snake_block, snake_block])
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # If snake head runs into itself, end game.
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        snake(snake_block, snake_list)
        user_score(length_of_snake - 1)

        pygame.display.update()

        # If food is eaten, randomly place new piece of food, increase length of snake and its speed
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
            snake_speed += 1

        clock.tick(snake_speed)
    pygame.quit()
    quit()


game_loop()
