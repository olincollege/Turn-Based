"""Main menu for the game, displaying the title and instructions.
This module initializes Pygame, sets up the main menu screen,
and waits for the player to press the space key to continue"""

import sys
import pygame as pg
from game_clock import game_clock

# Initialize Pygame and set up screen dimensions and colors
def init_game():
    """Initializes Pygame and sets up the game screen."""
    pg.init()
    pg.mixer.init()
    width, height = 800, 600
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption("Main Menu")
    return screen, width, height


def display_text(screen, text, color, x_val, y_val):
    """Utility function to display text on the screen.
    Args:
        screen (pygame.Surface): The Pygame screen to draw on.
        text (str): The text to display.
        size (int): The font size.
        color (tuple): The color of the text (R, G, B).
        x_val (int): The x-coordinate for the text position.
        y_val (int): The y-coordinate for the text position.
    """
    font = get_font(40)
    label = font.render(text, True, color)
    screen.blit(label, (x_val, y_val))
    pg.display.flip()

def get_font(size):
    """Returns a pygame font object with the given size.
    Args:
        size (int): The font size.
    Returns:
        pygame.font.Font: A Pygame font object."""
    return pg.font.Font(None, size)


def space_input(screen, screen_width, screen_height, white, clock):
    """Wait for the player to press the space key while updating the game clock.
    Args:
        screen (pygame.Surface): The Pygame screen to draw on.
        screen_width (int): The width of the screen.
        screen_height (int): The height of the screen.
        white (tuple): The color white for text rendering.
        clock (bool): Whether to update the game clock.
    """
    waiting = True
    while waiting:
        # Handle events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                waiting = False  # Exit the loop when SPACE is pressed

        # Update and display the game clock
        if clock:
            game_clock(screen)

        # Display the "Press Spacebar" message
        font = pg.font.SysFont(None, 24)
        title_text = font.render("Press Spacebar to Continue", True, white)
        title_rect = title_text.get_rect(
            center=(screen_width // 2, screen_height - 50)
        )
        screen.blit(title_text, title_rect)

        # Update the display
        pg.display.flip()
