"""Test cases for the controller module."""

import pytest
import pygame as pg
from controller import MouseController, KeyController
from model import Model
from view import View

@pytest.fixture(scope="module", autouse=True)
def init_pygame():
    """Fixture to initialize and quit Pygame."""
    pg.init()
    # Do not create a display surface
    yield
    pg.quit()

@pytest.fixture
def setup_game():
    """Fixture to set up the game model, view, and controller."""
    model = Model()
    view = View(model)
    controller = MouseController(model, view, run_game=False)  # Set run_game to False
    return controller, view

@pytest.fixture
def key_controller():
    """Fixture to set up the KeyController."""
    controller = KeyController()
    controller.owners = [1, 0, 0]  # Set up owners for testing
    return controller

def test_get_circle_invalid_mouse(setup_game):
    """Test the get_circle method with an invalid circle.
    Args:
        setup_game: The fixture that sets up the game model, view, and controller.
    """
    controller, _ = setup_game
    pg.mouse.set_pos(500, 500)  # Position outside any circle
    assert controller.get_circle([1]) is None  # Should return None

def test_get_first_point_valid_mouse(setup_game, monkeypatch):
    """Test the get_first_point method with valid input.
    Args:
        setup_game: The fixture that sets up the game model, view, and controller.
        monkeypatch: The pytest fixture to modify built-in functions.
    """
    controller, view = setup_game
    monkeypatch.setattr('builtins.input', lambda _: '0')  # Simulate input
    result = controller.get_first_point(view, game_time=0)  # Call the method without screen
    assert result == 0  # Should return the selected circle index

def test_get_first_point_invalid_mouse(setup_game, monkeypatch):
    """Test the get_first_point method with invalid input.
    Args:
        setup_game: The fixture that sets up the game model, view, and controller.
        monkeypatch: The pytest fixture to modify built-in functions.
    """
    controller, view = setup_game
    monkeypatch.setattr('builtins.input', lambda _: '10')  # Simulate invalid input
    result = controller.get_first_point(view, game_time=0)  # Call the method without screen
    assert result == 0

def test_get_second_point_valid_mouse(setup_game, monkeypatch):
    """Test the get_second_point method with valid input.
    Args:
        setup_game: The fixture that sets up the game model, view, and controller.
        monkeypatch: The pytest fixture to modify built-in functions.
    """
    controller, view = setup_game
    controller.get_first_point(view, game_time=0)  # Set first point
    monkeypatch.setattr('builtins.input', lambda _: '1')  # Simulate input
    result = controller.get_second_point(0, view, game_time=0)  # Call the method without screen
    assert result == 1  # Should return the selected circle index

def test_get_circle_valid_key(key_controller, monkeypatch):
    """Test the get_circle method with valid input.
    Args:
        key_controller: The fixture that sets up the KeyController.
        monkeypatch: The pytest fixture to modify built-in functions.
    """
    monkeypatch.setattr('builtins.input', lambda _: '1')  # Simulate valid input
    result = key_controller.get_circle()  # Call the method
    assert result == 1  # Should return the selected circle index

def test_get_circle_invalid_key(key_controller, monkeypatch):
    """Test the get_circle method with invalid input.
    Args:
        key_controller: The fixture that sets up the KeyController.
        monkeypatch: The pytest fixture to modify built-in functions.
    """
    monkeypatch.setattr('builtins.input', lambda _: '10')  # Simulate invalid input
    with pytest.raises(ValueError):
        key_controller.get_circle()  # Should raise ValueError

def test_get_number_valid_key(key_controller, monkeypatch):
    """Test the get_number method with valid input.
    Args:
        key_controller: The fixture that sets up the KeyController.
        monkeypatch: The pytest fixture to modify built-in functions.
    """
    monkeypatch.setattr('builtins.input', lambda _: '5')  # Simulate valid input
    result = key_controller.get_number()  # Call the method
    assert result == 5  # Should return the input number

def test_get_number_invalid_key(key_controller, monkeypatch):
    """Test the get_number method with invalid input.
    Args:
        key_controller: The fixture that sets up the KeyController.
        monkeypatch: The pytest fixture to modify built-in functions.
    """
    monkeypatch.setattr('builtins.input', lambda _: '-1')  # Simulate invalid input
    result = key_controller.get_number()  # Call the method
    assert result is None  # Should return None

def test_get_first_point_key(key_controller, monkeypatch):
    """Test the get_first_point method with valid input.
    Args:
        key_controller: The fixture that sets up the KeyController.
        monkeypatch: The pytest fixture to modify built-in functions.
    """
    monkeypatch.setattr('builtins.input', lambda _: '2')  # Simulate valid input
    result = key_controller.get_first_point()  # Call the method
    assert result == 2  # Should return the selected circle index

def test_get_second_point_valid_key(key_controller, monkeypatch):
    """Test the get_second_point method with valid input.
    Args:
        key_controller: The fixture that sets up the KeyController.
        monkeypatch: The pytest fixture to modify built-in functions.
    """
    monkeypatch.setattr('builtins.input', lambda _: '1')  # Simulate valid input
    result = key_controller.get_second_point(0)  # Call the method
    assert result == 1  # Should return the selected circle index

def test_get_second_point_invalid_key(key_controller, monkeypatch):
    """Test the get_second_point method with invalid input.
    Args:
        key_controller: The fixture that sets up the KeyController.
        monkeypatch: The pytest fixture to modify built-in functions.
    """
    monkeypatch.setattr('builtins.input', lambda _: '10')  # Simulate invalid input
    with pytest.raises(ValueError):
        key_controller.get_second_point(0)  # Should raise ValueError
