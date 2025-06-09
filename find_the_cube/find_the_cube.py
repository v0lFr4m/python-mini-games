import pygame
import sys
import random
from random import randrange
from pygame.locals import *


pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Find the Cube')

# Player color and box color
RED = random.randrange(0, 255)
GREEN = random.randrange(0, 255)
BLUE  = random.randrange(0, 255)

# Figure position

box_x = random.randrange(0 , 750 , 5)
box_y = random.randrange(0 , 550 , 5 )
box = Rect(box_x, box_y , 50 , 50) # x, y, w, h

# SCORE

player_score = 0
pygame.font.init()
font = pygame.font.Font("game_font.ttf" , 32)
font_x = 15
font_y = 15

# Options
pygame.font.init()
font_option = pygame.font.Font("game_font.ttf" , 1000)
font_option_x = 330
font_option_y = -5

# Set up game clock
clock = pygame.time.Clock()

# Player settings
player_width, player_height = 50, 50
player_x, player_y = width // 2, height // 2
player_speed = 5


def display_score (x , y):
    score_img = font.render(f"Total score : {str(player_score)}" , True , [255 , 255 , 255])
    screen.blit(score_img , (x , y))

def exit_message(x , y):
    score_img = font.render(f"To exit game press [ESCAPE]" , True , [67 , 67 , 67])
    print(RED)
    screen.blit(score_img , (x , y))

# Main game loop

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_x += player_speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_y -= player_speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_y += player_speed
    # press Escape button to exit !
    if keys[pygame.K_ESCAPE]:
        running = False


    # Fill screen with a color
    screen.fill((0, 0, 0))

    # Draw box
    box_pos = pygame.draw.rect(screen, (RED, GREEN, BLUE), box)

    # Draw player (represented by a rectangle)
    pygame.draw.rect(screen, (RED, GREEN, BLUE), (player_x, player_y, player_width, player_height))
    player_pos = player_x, player_y, player_width, player_height

    # Player get the box , change color of box and player

    if player_pos == box_pos:
        RED = random.randrange(0, 255)
        GREEN = random.randrange(0, 255)
        BLUE = random.randrange(0, 255)
        box_x = random.randrange(0, 750, 5)
        box_y = random.randrange(0, 550, 5)
        box = Rect(box_x, box_y, 50, 50)
        box_pos = pygame.Rect.move(box, box_x, box_y)
        pygame.draw.rect(screen, (RED, GREEN, BLUE), (player_x, player_y, player_width, player_height))
        player_score += 1

    # Display score on screen
    display_score(font_x , font_y)
    exit_message(font_option_x , font_option_y)


    # Update the screen
    pygame.display.flip()

    # Set frames per second (FPS)
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
