import os
import pygame as pg
import sys
from openingscreen import main_menu
from ending_screen import draw_end_screen
from game_clock import game_clock

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

def main():
    screen, WIDTH, HEIGHT = init_game()  # Initialize the game

    game_running = True
    while game_running:

        main_menu(screen, WIDTH, HEIGHT) 

        screen.fill((0, 0, 0))
        game_clock()

        # We need to fix the game clock

        # Player 1's turn
        player1_move = get_player_input(screen)
        waiting_for_input = True
        while waiting_for_input:
            for event in pg.event.get():  # Iterate through the event queue
                if event.type == pg.KEYDOWN:  # Check for key press
                    if event.key == pg.K_SPACE:  # Check if SPACE was pressed
                        waiting_for_input = False

        screen.fill((0, 0, 0))
        display_text(screen, "Pass the device to Player 2", 40, (255, 255, 255), 50, HEIGHT // 2)
        pg.display.flip()
        waiting_for_input = True
        while waiting_for_input:
            for event in pg.event.get():  # Iterate through the event queue
                if event.type == pg.KEYDOWN:  # Check for key press
                    if event.key == pg.K_SPACE:  # Check if SPACE was pressed
                        waiting_for_input = False

        screen.fill((0, 0, 0))
        # Player 2's turn
        player2_move = get_player_input(screen)
        waiting_for_input = True
        while waiting_for_input:
            for event in pg.event.get():  # Iterate through the event queue
                if event.type == pg.KEYDOWN:  # Check for key press
                    if event.key == pg.K_SPACE:  # Check if SPACE was pressed
                        waiting_for_input = False
        
        screen.fill((0, 0, 0))
        display_text(screen, "Revealing Moves...", 40, (255, 255, 255), 50, HEIGHT // 2)
        pg.display.flip()
        pg.time.wait(1000)  # Wait for 1 second before revealing moves

        # Reveal both moves
        reveal_moves(screen, player1_move, player2_move)

        waiting_for_input = True
        while waiting_for_input:
            for event in pg.event.get():  # Iterate through the event queue
                if event.type == pg.KEYDOWN:  # Check for key press
                    if event.key == pg.K_SPACE:  # Check if SPACE was pressed
                        waiting_for_input = False

        # Option to continue or quit
        draw_end_screen(screen, WIDTH, HEIGHT, black, white, "")

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
    main()  # Start with the main menu