import pygame
import sys

pygame.init()

# Set up screen and colors
WIDTH, HEIGHT = 600, 400
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Main Menu")


def get_font(size):
    """Returns a Pygame font object of the given size."""
    return pygame.font.Font(None, size)


def play():
    """Dummy play screen."""
    running = True
    while running:
        screen.fill((100, 200, 100))
        text = get_font(40).render("Game Screen - Press ESC to return", True, WHITE)
        screen.blit(text, (50, HEIGHT // 2 - 20))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        pygame.display.flip()


def options():
    """Dummy options screen."""
    running = True
    while running:
        screen.fill((100, 100, 200))
        text = get_font(40).render("Options - Press ESC to return", True, WHITE)
        screen.blit(text, (80, HEIGHT // 2 - 20))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        pygame.display.flip()


def main_menu():
    """Displays the main menu and handles button interaction."""
    font = get_font(50)

    # Button rects
    buttons = {
        "Play": pygame.Rect(200, 100, 200, 60),
        "Options": pygame.Rect(200, 180, 200, 60),
        "Quit": pygame.Rect(200, 260, 200, 60)
    }

    running = True
    while running:
        screen.fill(GRAY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if buttons["Play"].collidepoint(event.pos):
                    play()
                elif buttons["Options"].collidepoint(event.pos):
                    options()
                elif buttons["Quit"].collidepoint(event.pos):
                    running = False

        for text, rect in buttons.items():
            pygame.draw.rect(screen, BLACK, rect)
            label = font.render(text, True, WHITE)
            label_rect = label.get_rect(center=rect.center)
            screen.blit(label, label_rect)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main_menu()
