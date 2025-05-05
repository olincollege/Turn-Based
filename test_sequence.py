import pytest
import pygame as pg
from sequence import space_input
from unittest.mock import patch

@pytest.mark.parametrize("key", [pg.K_SPACE])
def test_space_input_exits_on_space(key):
    # Initialize Pygame
    pg.init()

    # Create a dummy screen for rendering
    screen = pg.display.set_mode((800, 600), pg.HIDDEN)

    # Mock the pg.event.get() function to simulate a space key press
    with patch("pygame.event.get", return_value=[pg.event.Event(pg.KEYDOWN, {"key": key})]):
        # Call the space_input function and ensure it exits without errors
        try:
            space_input(screen, 800, 600, (255, 255, 255), True, None)
        except Exception as e:
            pytest.fail(f"space_input raised an unexpected exception: {e}")

    # Quit Pygame
    pg.quit()