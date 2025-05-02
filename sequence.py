import pygame as pg
import sys
from game_clock import game_clock

def init_game():
    pg.init()
    WIDTH, HEIGHT = 800, 600
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("Turn-Based Game")
    return screen, WIDTH, HEIGHT

def display_text(screen, text, size, color, x, y):
    """Utility function to display text on the screen."""
    font = get_font(size)
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

def space_input(screen, screen_width, screen_height, white):
    """Wait for the player to press the space key while updating the game clock."""
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
        game_clock(screen)

        # Display the "Press Spacebar" message
        font = pg.font.SysFont(None, 24)
        title_text = font.render("Press Spacebar to Continue", True, white)
        title_rect = title_text.get_rect(center=(screen_width // 2, screen_height - 50))
        screen.blit(title_text, title_rect)

        # Update the display
        pg.display.flip()