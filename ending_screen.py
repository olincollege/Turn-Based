import pygame

def draw_end_screen(screen, screen_width, screen_height, black, white, winner):
    """Draw the end screen."""
    screen.fill(black)

    font = pygame.font.SysFont(None, 48)
    title_text = font.render("Game Over!", True, white)
    if not winner.strip():
        prompt_text = font.render("Time Ran Out!", True, white)
    else:
        prompt_text = font.render(f"Winner: {winner}", True, white)

    title_rect = title_text.get_rect(center=(screen_width // 2, screen_height // 2 - 40))
    prompt_rect = prompt_text.get_rect(center=(screen_width // 2, screen_height // 2 + 40))

    screen.blit(title_text, title_rect)
    screen.blit(prompt_text, prompt_rect)

    pygame.display.flip()