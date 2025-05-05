"""This module contains the main menu and help screen for the game."""

import sys
import pygame
from sequence import get_font

def help_screen(screen, width, height):
    """Help screen.
    Displays the game rules and controls.
    Args:
        screen (pygame.Surface): The Pygame screen to draw on.
        height (int): The height of the screen.
    """
    running = True
    white = (255, 255, 255)

    # Define the help text as a list of lines
    help_text = [
        "Game Rules",
        "The game is played on a grid representing Olin buildings. Players take turns sending Oliners between buildings. Both players will make their choices",
        "in how and where they move their Oliners before the actions of both players occur. This simultaneous game-dynamic ensures that players have to make",
        "predictive moves based on their opponent. The goal is to control the opponent's home-base while still holding control of your own before time is up(5 minutes).",
        "",
        "Players can send Oliners from one building to another by selecting the source and destination buildings and specifying the number of Oliners to send.",
        "It is only possible to send Oliners from one building to another if both buildings are connected. The game ends when one or both players capture",
        "each other's home-base, or when the time runs out.",
        "If the amount of Oliners for both players, in one building, is equal, then the building is captured by the player who sent the Oliners last.",
        "",
        "Game Controls",
        "- To send Oliners, select the source building, then the destination building, and specify the number of Oliners to send.",
        "- To select a building, click on it with the mouse.",
        "- To select the number of Oliners to send, type in the number using the keyboard.",
        "- Press the spacebar to confirm your selection and send the Oliners.",
    ]

    while running:
        screen.fill((0, 0, 0))  # Background color

        # Render and display each line of text
        y_offset = 25  # Start rendering text 50 pixels from the top
        for i, line in enumerate(help_text):
            if i in [0, 10]:  # Titles
                font = get_font(25)  # Larger font for titles
            else:
                font = get_font(15)  # Smaller font for regular text

            rendered_text = font.render(line, True, white)
            screen.blit(rendered_text, (25, y_offset))  # Render text with padding
            y_offset += 35  # Move down for the next line
        font = get_font(30)
        title_text = font.render("Press Spacebar to Go Back to Main Menu", True, white)
        title_rect = title_text.get_rect(
            center=(width // 2, height - 25)
        )
        screen.blit(title_text, title_rect)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                pygame.event.get()
                return "main_menu"  # Return to main menu
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False  # Exit the help screen

        pygame.display.flip()  # Update the display


def main_menu(screen, width, height, test_mode=False):
    """Displays the main menu and handles button interaction.
    Args:
        screen (pygame.Surface): The Pygame screen to draw on.
        width (int): The width of the screen.
        height (int): The height of the screen.
        test_mode (bool): If True, the function will not wait for user input.
    """
    font = get_font(50)

    # Button dimensions
    button_width = 400
    button_height = 100

    # Button centered on the screen
    buttons = {
        "Play": pygame.Rect((width - button_width) // 2, 100, button_width, button_height),
        "Help": pygame.Rect((width - button_width) // 2, (height - button_height) // 2, button_width, button_height),
        "Quit": pygame.Rect((width - button_width) // 2, 400, button_width, button_height)
    }
    if not test_mode:
        pygame.event.get()  # Clear the event queue

    while True:
        screen.fill((200, 200, 200))  # Fill the screen with gray

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if buttons["Play"].collidepoint(event.pos):
                    return "play"  # Return play signal
                if buttons["Help"].collidepoint(event.pos):
                    return "help"  # Return help signal
                if buttons["Quit"].collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        for text, rect in buttons.items():
            pygame.draw.rect(screen, (0, 0, 0), rect)  # Draw button background
            label = font.render(text, True, (255, 255, 255))  # Render button text
            label_rect = label.get_rect(center=rect.center)  # Center the text
            screen.blit(label, label_rect)  # Draw the text on the button

        pygame.display.flip()

        # For tests
        if test_mode:
            break
