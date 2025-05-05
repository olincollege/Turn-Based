import pytest
import pygame
from opening_screen import main_menu

@pytest.mark.parametrize(
    "event, expected_result",
    [
        (pygame.event.Event(pygame.MOUSEBUTTONDOWN, {"pos": (400, 120)}), "play"),  # Adjusted position for "Play"
        (pygame.event.Event(pygame.MOUSEBUTTONDOWN, {"pos": (400, 300)}), "help"),  # Adjusted position for "Help"
        (pygame.event.Event(pygame.MOUSEBUTTONDOWN, {"pos": (400, 420)}), "quit"),  # Adjusted position for "Quit"
        (pygame.event.Event(pygame.QUIT), "quit"),  # Quit event
    ],
)
def test_main_menu(event, expected_result):
    # Initialize Pygame
    pygame.init()

    # Create a hidden display
    pygame.display.set_mode((800, 600), pygame.HIDDEN)
    screen = pygame.display.get_surface()  # Get the hidden display surface
    screen_width = 800
    screen_height = 600

    # Inject the event into Pygame's event queue
    pygame.event.post(event)

    # Handle SystemExit for quit cases
    if expected_result == "quit":
        with pytest.raises(SystemExit):
            main_menu(screen, screen_width, screen_height, test_mode=True)
    else:
        # Call the main_menu function with test_mode=True
        result = main_menu(screen, screen_width, screen_height, test_mode=True)

        # Assert the result
        assert result == expected_result

    # Quit Pygame
    pygame.quit()