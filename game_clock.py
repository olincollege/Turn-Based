"""The Overall Game Clock Module"""

import pygame as pg


def game_clock(screen, game_time):
    """
    A simple game clock that displays a countdown timer in Pygame.
    The timer starts at 5 minutes (300 seconds) and counts down to zero.
    """
    # Initialize Pygame
    pg.init()
    # Timer setup
    start_time = 300000  # 5 minutes in milliseconds

    # Clock and font setup
    clock = pg.time.Clock()
    font = pg.font.Font(None, 36)

    if game_time is None:
        game_time = 0

    # Calculate elapsed time
    current_time = pg.time.get_ticks() - game_time
    elapsed_time = start_time - current_time
    if elapsed_time < 0:
        elapsed_time = 0  # Prevent negative time
        raise TimeUp()
    elapsed_time_ms = elapsed_time / 1000.0

    # Convert to minutes and seconds
    minutes = int(elapsed_time_ms / 60)
    seconds = int(elapsed_time_ms % 60)
    time_string = f"{minutes}:{seconds}"  # Format as MM:SS

    # Clear the clock area by drawing a background rectangle
    clock_background = pg.Rect(0, 0, 100, 40)
    pg.draw.rect(screen, (0, 0, 0), clock_background)

    # Render the timer text
    time_text = font.render(time_string, True, (255, 255, 255))
    time_rect = time_text.get_rect(center=(45, 30))

    # Draw the timer text
    screen.blit(time_text, time_rect)

    # Update the display
    pg.display.update(time_rect)

    # Cap the frame rate
    clock.tick(60)

    return elapsed_time  # Return elapsed time in seconds


class TimeUp(Exception):
    """Custom exception to indicate that the game time has run out."""
