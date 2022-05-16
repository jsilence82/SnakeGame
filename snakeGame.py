import pygame
import time
import random

pygame.init()

#set colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

#set window
dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_width))
pygame.display.set_caption('Snake Game')

game_over = False

clock = pygame.time.Clock()


#Game loop. While loop while game is running. Ends on snake or border collision.

while not game_over:
    for event in pygame.event.get():
        print(event)



pygame.quit()
quit()