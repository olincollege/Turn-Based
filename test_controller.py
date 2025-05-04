import pytest
import pygame as pg
from Controller import MouseController, KeyController
from Model import Model
from View import View

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

def test_get_cursor_pos(setup_game):
    controller, _ = setup_game
    pg.mouse.set_pos(100, 100)  # Set mouse position for testing
    assert controller.get_cursor_pos() == (100, 100)  # Check if cursor position is retrieved correctly

def test_get_circle_valid(setup_game):
    controller, _ = setup_game
    controller.owners[0] = 1  # Set owner for testing
    pg.mouse.set_pos(controller.circle_data[0][0], controller.circle_data[0][1])  # Position over circle
    assert controller.get_circle([1]) == 0  # Should return index of the circle

def test_get_circle_invalid(setup_game):
    controller, _ = setup_game
    pg.mouse.set_pos(500, 500)  # Position outside any circle
    assert controller.get_circle([1]) is None  # Should return None

def test_check_number_valid(setup_game, monkeypatch):
    controller, view = setup_game
    monkeypatch.setattr('builtins.input', lambda _: '3')  # Simulate input
    result = controller.check_number(5)  # Call the method without screen
    assert result == 3  # Should return the input number

def test_check_number_invalid(setup_game, monkeypatch):
    controller, view = setup_game
    monkeypatch.setattr('builtins.input', lambda _: '10')  # Simulate input greater than max
    result = controller.check_number(5)  # Call the method without screen
    assert result == 5  # Should return circle_max

def test_get_first_point_valid(setup_game, monkeypatch):
    controller, view = setup_game
    monkeypatch.setattr('builtins.input', lambda _: '0')  # Simulate input
    result = controller.get_first_point()  # Call the method without screen
    assert result == 0  # Should return the selected circle index

def test_get_first_point_invalid(setup_game, monkeypatch):
    controller, view = setup_game
    monkeypatch.setattr('builtins.input', lambda _: '10')  # Simulate invalid input
    with pytest.raises(ValueError):
        controller.get_first_point()  # Should raise ValueError

def test_get_second_point_valid(setup_game, monkeypatch):
    controller, view = setup_game
    controller.get_first_point()  # Set first point
    monkeypatch.setattr('builtins.input', lambda _: '1')  # Simulate input
    result = controller.get_second_point(0)  # Call the method without screen
    assert result == 1  # Should return the selected circle index

def test_get_second_point_invalid(setup_game, monkeypatch):
    controller, view = setup_game
    controller.get_first_point()  # Set first point
    monkeypatch.setattr('builtins.input', lambda _: '3')  # Simulate invalid input
    with pytest.raises(ValueError):
        controller.get_second_point(0)  # Should raise ValueError

def test_get_circle_valid(key_controller, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '1')  # Simulate valid input
    result = key_controller.get_circle()  # Call the method
    assert result == 1  # Should return the selected circle index

def test_get_circle_invalid(key_controller, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '10')  # Simulate invalid input
    with pytest.raises(ValueError):
        key_controller.get_circle()  # Should raise ValueError

def test_get_number_valid(key_controller, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '5')  # Simulate valid input
    result = key_controller.get_number()  # Call the method
    assert result == 5  # Should return the input number

def test_get_number_invalid(key_controller, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '-1')  # Simulate invalid input
    result = key_controller.get_number()  # Call the method
    assert result is None  # Should return None

def test_get_first_point(key_controller, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '2')  # Simulate valid input
    result = key_controller.get_first_point()  # Call the method
    assert result == 2  # Should return the selected circle index

def test_get_second_point_valid(key_controller, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '1')  # Simulate valid input
    result = key_controller.get_second_point(0)  # Call the method
    assert result == 1  # Should return the selected circle index

def test_get_second_point_invalid(key_controller, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '10')  # Simulate invalid input
    with pytest.raises(ValueError):
        key_controller.get_second_point(0)  # Should raise ValueError
