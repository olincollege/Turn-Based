import os
import pygame as pg
import sys

# Initialize Pygame
pg.init()

# Screen setup
screen_width = 800
screen_height = 600
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

def main_menu(screen, WIDTH, HEIGHT):
    """Displays the main menu and handles button interaction."""
    def get_font(size):
        return pg.font.Font(None, size)

    font = get_font(50)

    # Button dimensions
    button_width = 200
    button_height = 60

    # Button centered on the screen
    buttons = {
        "Play": pg.Rect((WIDTH - button_width) // 2, 100, button_width, button_height),
        "Options": pg.Rect((WIDTH - button_width) // 2, 180, button_width, button_height),
        "Quit": pg.Rect((WIDTH - button_width) // 2, 260, button_width, button_height)
    }

    running = True
    while running:
        screen.fill((200, 200, 200))  # Fill the screen with gray

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            elif event.type == pg.MOUSEBUTTONDOWN:
                if buttons["Play"].collidepoint(event.pos):
                    # Call the main function directly when Play is clicked
                    main()
                elif buttons["Options"].collidepoint(event.pos):
                    # Placeholder for options action
                    pass
                elif buttons["Quit"].collidepoint(event.pos):
                    running = False

        for text, rect in buttons.items():
            pg.draw.rect(screen, (0, 0, 0), rect)  # Draw button background
            label = font.render(text, True, (255, 255, 255))  # Render button text
            label_rect = label.get_rect(center=rect.center)  # Center the text
            screen.blit(label, label_rect)  # Draw the text on the button

        pg.display.flip()

    pg.quit()
    sys.exit()

def init_game():
    pg.init()
    WIDTH, HEIGHT = 600, 400
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
    button_width = 200
    button_height = 60
    button_a = pg.Rect((screen.get_width() - button_width) // 2, 100, button_width, button_height)
    button_b = pg.Rect((screen.get_width() - button_width) // 2, 180, button_width, button_height)
    button_c = pg.Rect((screen.get_width() - button_width) // 2, 260, button_width, button_height)

    pg.draw.rect(screen, (0, 0, 0), button_a)
    pg.draw.rect(screen, (0, 0, 0), button_b)
    pg.draw.rect(screen, (0, 0, 0), button_c)

    display_text(screen, "Move A", 30, (255, 255, 255), button_a.x + 50, button_a.y + 15)
    display_text(screen, "Move B", 30, (255, 255, 255), button_b.x + 50, button_b.y + 15)
    display_text(screen, "Move C", 30, (255, 255, 255), button_c.x + 50, button_c.y + 15)

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

def main():
    screen, WIDTH, HEIGHT = init_game()  # Initialize the game

    game_running = True
    while game_running:
        # Player 1's turn
        player1_move = get_player_input(screen)
        
        screen.fill((0, 0, 0))
        display_text(screen, "Pass the device to Player 2", 40, (255, 255, 255), 50, HEIGHT // 2)
        pg.display.flip()
        pg.time.wait(2000)  # Wait for 2 seconds before switching

        # Player 2's turn
        player2_move = get_player_input(screen)
        
        screen.fill((0, 0, 0))
        display_text(screen, "Revealing Moves...", 40, (255, 255, 255), 50, HEIGHT // 2)
        pg.display.flip()
        pg.time.wait(1000)  # Wait for 1 second before revealing moves

        # Reveal both moves
        reveal_moves(screen, player1_move, player2_move)

        # Option to continue or quit
        screen.fill((200, 200, 200))
        display_text(screen, "Press R to play again or Q to quit", 30, (0, 0, 0), 50, HEIGHT // 2)
        pg.display.flip()

        waiting_for_input = True
        while waiting_for_input:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_r:
                        waiting_for_input = False  # Restart the game
                    elif event.key == pg.K_q:
                        game_running = False  # Quit the game

    pg.quit()

if __name__ == "__main__":
    main_menu(screen, screen_width, screen_height)  # Start with the main menu