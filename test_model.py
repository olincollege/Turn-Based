"""model unit tests using pytest"""

import pytest
from model import Model


@pytest.fixture
def model():
    """Fixture to create a Model instance for testing."""
    return Model()


def test_initialization(model):
    """Test the initial state of the model.
    Args:
        model (Model): The model instance to test.
    """
    assert model.screen_width == 800
    assert model.screen_height == 600
    assert model.owners == {0: 1, 1: 0, 2: 0, 3: 0, 4: 0, 5: 2}
    assert model.oliners_count == [10, 0, 0, 0, 0, 10]


def test_add_oliners(model):
    """Test adding Oliners to owned buildings.
    Args:
        model (Model): The model instance to test.
    """
    updated_counts = model.add_oliners()
    assert updated_counts == [
        11,
        0,
        0,
        0,
        0,
        11,
    ]  # 1 added to each owned building


def test_send_oliners(model):
    """Test sending Oliners between buildings.
    Args:
        model (Model): The model instance to test.
    """
    model.send_oliners(0, 1, 5)  # Send 5 Oliners from building 0 to 1
    assert model.oliners_count[0] == 5  # Should have 5 left
    assert model.oliners_count[1] == 5  # Building 1 should now have 5 Oliners


def test_check_negative(model):
    """Test that negative Oliner counts are reset to zero.
    Args:
        model (Model): The model instance to test.
    """
    model.oliners_count = [10, 0, 0, 0, 0, 10]
    model.oliners_count[0] = -5  # Simulate a negative count
    model.check_negative()
    assert model.oliners_count[0] == 0  # Should be reset to 0
    assert model.owners[0] == 0  # Owner should also be reset


def test_check_win(model):
    """Test the win condition.
    Args:
        model (Model): The model instance to test.
    """
    model.owners = {0: 1, 1: 0, 2: 0, 3: 0, 4: 0, 5: 2}
    assert model.check_win() == 0  # No winner
    model.owners = {0: 2, 1: 0, 2: 0, 3: 0, 4: 0, 5: 1}
    assert model.check_win() == 3  # Both players have won
