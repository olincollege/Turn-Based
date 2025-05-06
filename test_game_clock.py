"""Test the game_clock function for correct behavior."""

import pytest
import pygame as pg
from game_clock import game_clock, TimeUp

def test_game_clock():
    """Test the game_clock function for correct behavior."""
    # Initialize Pygame
    pg.init()

    # Create a dummy screen for rendering
    screen = pg.display.set_mode((800, 600), pg.HIDDEN)

    # Simulate a game_time that causes elapsed time to be negative
    game_time = -300000000 #Sets to a time where the game clock will be negative

    # Assert that TimeUp is raised
    with pytest.raises(TimeUp):
        game_clock(screen, game_time)

    # Quit Pygame
    pg.quit()
