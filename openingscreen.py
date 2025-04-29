import pygame
import sys

# Initialize Pygame and set up screen dimensions and colors
def init_game():
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Main Menu")
    return screen, WIDTH, HEIGHT

def get_font(size):
    """Returns a Pygame font object of the given size."""
    return pygame.font.Font(None, size)

def play(screen, HEIGHT):
    """Dummy play screen."""
    running = True
    while running:
        screen.fill((100, 200, 100))
        text = get_font(40).render("Game Screen - Press ESC to return", True, (255, 255, 255))
        screen.blit(text, (50, HEIGHT // 2 - 20))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        pygame.display.flip()

def options(screen, HEIGHT):
    """Dummy options screen."""
    running = True
    while running:
        screen.fill((100, 100, 200))
        text = get_font(40).render("Options - Press ESC to return", True, (255, 255, 255))
        screen.blit(text, (80, HEIGHT // 2 - 20))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        pygame.display.flip()

def main_menu(screen, WIDTH, HEIGHT):
    """Displays the main menu and handles button interaction."""
    font = get_font(50)

    # Button dimensions
    button_width = 200
    button_height = 60

    # Button centered on the screen
    buttons = {
        "Play": pygame.Rect((WIDTH - button_width) // 2, 100, button_width, button_height),
        "Options": pygame.Rect((WIDTH - button_width) // 2, 180, button_width, button_height),
        "Quit": pygame.Rect((WIDTH - button_width) // 2, 260, button_width, button_height)
    }

    running = True
    while running:
        screen.fill((200, 200, 200))  # Fill the screen with gray

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if buttons["Play"].collidepoint(event.pos):
                    play(screen, HEIGHT)
                elif buttons["Options"].collidepoint(event.pos):
                    options(screen, HEIGHT)
                elif buttons["Quit"].collidepoint(event.pos):
                    running = False

        for text, rect in buttons.items():
            pygame.draw.rect(screen, (0, 0, 0), rect)  # Draw button background
            label = font.render(text, True, (255, 255, 255))  # Render button text
            label_rect = label.get_rect(center=rect.center)  # Center the text
            screen.blit(label, label_rect)  # Draw the text on the button

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    screen, WIDTH, HEIGHT = init_game()  # Initialize the game
    main_menu(screen, WIDTH, HEIGHT)  # Start the main menu

