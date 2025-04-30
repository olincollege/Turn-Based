import pygame as pg
import sys

def init_game():
    pg.init()
    WIDTH, HEIGHT = 800, 600
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("Turn-Based Game")
    return screen, WIDTH, HEIGHT

def get_font(size):
    """Returns a Pygame font object of the given size."""
    return pg.font.Font(None, size)

def display_text(screen, text, size, color, x, y):
    """Utility function to display text on the screen."""
    font = get_font(size)
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

def draw_move_buttons(screen):
    """Draw buttons for player moves."""
    button_width = 400
    button_height = 100
    button_a = pg.Rect((screen.get_width() - button_width) // 2, 100, button_width, button_height)
    button_b = pg.Rect((screen.get_width() - button_width) // 2, (screen.get_height() - button_height) // 2, button_width, button_height)
    button_c = pg.Rect((screen.get_width() - button_width) // 2, 400, button_width, button_height)

    pg.draw.rect(screen, (0, 0, 0), button_a)
    pg.draw.rect(screen, (0, 0, 0), button_b)
    pg.draw.rect(screen, (0, 0, 0), button_c)

    # Get font and calculate text height for proper centering
    font = get_font(50)
    text_a = font.render("Move A", True, (255, 255, 255))
    text_b = font.render("Move B", True, (255, 255, 255))
    text_c = font.render("Move C", True, (255, 255, 255))

    # Center the text vertically within each button
    text_a_y = button_a.y + (button_a.height - text_a.get_height()) // 2
    text_b_y = button_b.y + (button_b.height - text_b.get_height()) // 2
    text_c_y = button_c.y + (button_c.height - text_c.get_height()) // 2

    # Display the text
    display_text(screen, "Move A", 50, (255, 255, 255), (screen.get_width() - text_a.get_width()) // 2, text_a_y)
    display_text(screen, "Move B", 50, (255, 255, 255), (screen.get_width() - text_b.get_width()) // 2, text_b_y)
    display_text(screen, "Move C", 50, (255, 255, 255), (screen.get_width() - text_c.get_width()) // 2, text_c_y)

    return button_a, button_b, button_c

def get_player_input(screen):
    """Get input from the player using mouse clicks."""
    button_a, button_b, button_c = draw_move_buttons(screen)
    move = None

    while move is None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if button_a.collidepoint(event.pos):
                    move = "A"
                elif button_b.collidepoint(event.pos):
                    move = "B"
                elif button_c.collidepoint(event.pos):
                    move = "C"

        pg.display.flip()

    return move

def reveal_moves(screen, player1_move, player2_move):
    """Display both players' moves."""
    screen.fill((0, 0, 0))
    display_text(screen, f"Player 1 Move: {player1_move}", 40, (255, 255, 255), 50, 100)
    display_text(screen, f"Player 2 Move: {player2_move}", 40, (255, 255, 255), 50, 150)
    pg.display.flip()
    pg.time.wait(2000)  # Wait for 2 seconds to show moves

def space_input(screen, screen_width, screen_height, white):
    """Wait for the player to press the space key."""
    font = pg.font.SysFont(None, 24)
    title_text = font.render("Press Spacebar to Continue", True, white)
    title_rect = title_text.get_rect(center=(screen_width // 2, 550))
    screen.blit(title_text, title_rect)
    pg.display.update(title_rect)
    
    waiting = True
    while waiting:
        for event in pg.event.get():
            if event.type == pg.QUIT:  # Allow the user to quit the game
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                waiting = False  # Exit the loop when SPACE is pressed