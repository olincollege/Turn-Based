import os
import pygame as pg
import sys
from openingscreen import main_menu
from ending_screen import draw_end_screen
from game_clock import game_clock
from sequence import get_player_input, display_text, init_game, get_font, draw_move_buttons, reveal_moves, space_input
from ControllerTest import MouseController
from Model import Model
from View import View
# # Initialize Pygame
# pg.init()

# Screen setup
screen_width = 800
screen_height = 600
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Game")

black = (0, 0, 0)
white = (255, 255, 255)

def main():
    screen, WIDTH, HEIGHT = init_game()  # Initialize the game

    game_running = True
    while game_running:

        main_menu(screen, WIDTH, HEIGHT) 

        screen.fill((0, 0, 0))
        #game_clock()

        # We need to fix the game clock

        # Player 1's turn
        model = Model()
        view = View(model)
        player_one = MouseController(model, view)
        player_two = MouseController(model, view)

        player1_move = player_one.move()
        model.send_oliners(player1_move[0], player1_move[1], player1_move[2])

        space_input(screen, WIDTH, HEIGHT, white)

        screen.fill((0, 0, 0))
        display_text(screen, "Pass the device to Player 2", 40, (255, 255, 255), 50, HEIGHT // 2)
        pg.display.flip()
        space_input(screen, WIDTH, HEIGHT, white)

        screen.fill((0, 0, 0))
        # Player 2's turn
        player2_move = player_two.move()
        model.send_oliners(player2_move[0], player2_move[1], player2_move[2])
        space_input(screen, WIDTH, HEIGHT, white)
        
        screen.fill((0, 0, 0))
        display_text(screen, "Revealing Moves...", 40, (255, 255, 255), 50, HEIGHT // 2)
        pg.display.flip()
        pg.time.wait(1000)  # Wait for 1 second before revealing moves

        # Reveal both moves
        view.draw()
        space_input(screen, WIDTH, HEIGHT, white)

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
                        waiting_for_input = False
                        game_running = False  # Quit the game

    pg.quit()

if __name__ == "__main__":
    main()  # Start with the main menu
