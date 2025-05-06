"""Unit tests for the ending_screen module."""

from unittest.mock import Mock, patch
import pytest
from ending_screen import draw_end_screen

@pytest.mark.unit
def test_draw_end_screen():
    """Test the draw_end_screen function.
    This function tests the rendering of the end screen with different game outcomes.
   """
    with patch("pygame.font.SysFont") as mock_sysfont:
        # Mock the font and rendering behavior
        mock_font = Mock()
        mock_sysfont.return_value = mock_font
        mock_rendered_text = Mock()
        mock_font.render.return_value = mock_rendered_text

        # Create a mock screen
        screen = Mock()
        screen_width = 800
        screen_height = 600
        black = (0, 0, 0)
        white = (255, 255, 255)

        # Test for winner = 3 (draw due to both bases captured)
        draw_end_screen(screen, screen_width, screen_height, black, white, winner=3)
        mock_font.render.assert_any_call("Draw! Both players captured each other's bases.", True, white)

        # Test for winner = 0 (draw due to time running out)
        draw_end_screen(screen, screen_width, screen_height, black, white, winner=0)
        mock_font.render.assert_any_call("Draw! Time ran out!", True, white)

        # Test for winner = 1 (Player 1 wins)
        draw_end_screen(screen, screen_width, screen_height, black, white, winner=1)
        mock_font.render.assert_any_call("Winner: Player 1", True, white)

        # Test for winner = 2 (Player 2 wins)
        draw_end_screen(screen, screen_width, screen_height, black, white, winner=2)
        mock_font.render.assert_any_call("Winner: Player 2", True, white)
