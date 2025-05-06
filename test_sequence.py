"""Test for the space_input function in the sequence module."""

from unittest.mock import patch
import pytest
import pygame as pg
from sequence import space_input


@pytest.mark.parametrize("key", [pg.K_SPACE])
def test_space_input_exits_on_space(key):
    """Test the space_input function to ensure it exits on space key press.
    Args:
        key (int): The key to simulate (space key).
    """
    # Initialize Pygame
    pg.init()

    # Create a dummy screen for rendering
    screen = pg.display.set_mode((800, 600), pg.HIDDEN)

    # Mock the pg.event.get() function to simulate a space key press
    with patch(
        "pygame.event.get",
        return_value=[pg.event.Event(pg.KEYDOWN, {"key": key})],
    ):
        # Call the space_input function and ensure it exits without errors
        space_input(screen, 800, 600, (255, 255, 255), True, None)

    # Quit Pygame
    pg.quit()
