"""End screen module for a game using Pygame."""

import pygame

def draw_end_screen(screen, screen_width, screen_height, black, white, winner):
    """Draw the end screen.
    This function displays the end screen with a message indicating the game result.
    It shows the winner or if the game ended in a draw, and prompts the user to exit or play again.
    
    Args:
        screen: The pygame screen to draw on.
        screen_width: The width of the screen.
        screen_height: The height of the screen.
        black: The color black for the background.
        white: The color white for the text.
        winner: The index of the winning player (1 or 2), or 3 for a draw.
    """
    screen.fill(black)

    font = pygame.font.SysFont(None, 48)
    title_text = font.render("Game Over! Press Q to exit or R to play again.", True, white)
    if winner == 3:
        prompt_text = font.render("Draw! Both players captured each other's bases.", True, white)
    elif winner == 0:
        prompt_text = font.render("Draw! Time ran out!", True, white)
    else:
        prompt_text = font.render(f"Winner: Player {winner}", True, white)

    title_rect = title_text.get_rect(center=(screen_width // 2, screen_height // 2 - 40))
    prompt_rect = prompt_text.get_rect(center=(screen_width // 2, screen_height // 2 + 40))

    screen.blit(title_text, title_rect)
    screen.blit(prompt_text, prompt_rect)

    pygame.display.flip()
