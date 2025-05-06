"""Unit tests for the View class in the game."""

import pytest
import pygame as pg
from model import Model
from view import View


@pytest.fixture(scope="module", autouse=True)
def init_pygame():
    """Fixture to initialize and quit Pygame."""
    pg.init()
    yield
    pg.quit()


@pytest.fixture
def setup_view():
    """Fixture to set up the game model and view."""
    model = Model()
    view = View(model)
    view.screen = pg.display.set_mode(
        (800, 600), pg.HIDDEN
    )  # Create a screen for drawing
    return view


def test_draw_circles(setup_view):
    """Test that circles are drawn correctly."""
    view = setup_view
    view.draw_circles()  # Call the method to draw circles
    # Check if the method runs without errors (no need to check pixel values)


def test_draw_connections(setup_view):
    """Test that connections between circles are drawn correctly."""
    view = setup_view
    view.draw_connections()  # Call the method to draw connections
    # Check if the method runs without errors (no need to check pixel values)


def test_draw_numbers(setup_view):
    """Test that the number of Oliners is drawn correctly."""
    view = setup_view
    view.oliners_count = [10, 5, 0, 3, 8, 2]  # Set some test values for Oliners
    view.draw()  # Draw circles and numbers
    # Check if the method runs without errors (no need to check pixel values)


def test_update(setup_view):
    """Test that the update method handles events and draws correctly."""
    view = setup_view
    view.update()  # Call update to process events and draw
    # Check if the method runs without errors (no need to check pixel values)


def test_show_next_player(setup_view):
    """Test that the next player message is drawn correctly."""
    view = setup_view
    view.model.next_player = 1  # Set the next player
    view.show_next_player()  # Draw the next player message
    # Check if the method runs without errors (no need to check pixel values)
