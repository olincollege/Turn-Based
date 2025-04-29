import os
import pygame as pg
import game_clock
from ending_screen import draw_end_screen  # Import the standalone function

# Initialize Pygame
pg.init()

# Screen setup
screen_width = 800
screen_height = 600
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Set up the game clock
    elapsed_time = game_clock.game_clock()

    if elapsed_time <= 0:
        # Timer has reached zero, stop the game --> show the end screen
        draw_end_screen(screen, screen_width, screen_height, black, white, "")  # Call the standalone function

        # Wait for user input to exit the end screen
        end_screen_active = True
        while end_screen_active:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                    end_screen_active = False
                elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    running = False
                    end_screen_active = False

pg.quit()