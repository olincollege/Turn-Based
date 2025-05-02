import os
import pygame as pg
import sys
from openingscreen import main_menu
from ending_screen import draw_end_screen
from game_clock import game_clock
from sequence import (
    display_text,
    init_game,
    space_input,
)
from Controller import MouseController
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
        blue = (0, 225, 0)
        red = (225, 0, 0)
        # game_clock()

        # We need to fix the game clock

        # Player 1's turn
        model = Model()
        model_temp = Model()
        view = View(model)
        view_temp = View(model_temp)
        player_one = MouseController(model, view)
        player_one.player = 1
        player_two = MouseController(model, view)
        player_two.player = 2
        view.draw()  # Draw the initial state of the game
        pg.display.flip()  # Update the display
        running = True
        while running is True:
            view.draw()  # Draw the initial state of the game
            pg.display.flip()  # Update the display
            display_text(
                screen,
                "Player 1 Choose Your Move",
                40,
                (255, 255, 255),
                50,
                HEIGHT // 2,
            )
            pg.display.flip()
            pg.time.wait(2000)
            player1_first_point = player_one.get_first_point()
            print(player1_first_point)
            player1_second_point = player_one.get_second_point(
                player1_first_point
            )
            print(player1_second_point)
            player1_number = player_one.check_number()
            print(player1_number)
            model.send_oliners(
                player1_first_point, player1_second_point, player1_number
            )

            pg.display.flip()
            space_input(screen, WIDTH, HEIGHT, white)

            screen.fill((0, 0, 0))
            display_text(
                screen,
                "Pass the device to Player 2",
                40,
                (255, 255, 255),
                50,
                HEIGHT // 2,
            )
            pg.display.flip()
            space_input(screen, WIDTH, HEIGHT, white)

            screen.fill((0, 0, 0))
            view_temp.draw()
            pg.display.flip()
            # Player 2's turn
            player2_first_point = player_two.get_first_point()
            print(player2_first_point)
            player2_second_point = player_one.get_second_point(
                player2_first_point
            )
            print(player2_second_point)
            player2_number = player_two.check_number()
            print(player2_number)
            model.send_oliners(
                player2_first_point, player2_second_point, player2_number
            )
            space_input(screen, WIDTH, HEIGHT, white)

            screen.fill((0, 0, 0))
            display_text(
                screen,
                "Revealing Moves...",
                40,
                (255, 255, 255),
                50,
                HEIGHT // 2,
            )
            pg.display.flip()
            pg.time.wait(1000)  # Wait for 1 second before revealing moves

            # Reveal both moves
            view.draw()
            winner = model.check_win()
            if winner > 0:
                display_text(
                    screen,
                    f"Player {winner} Wins!!",
                    40,
                    (255, 255, 255),
                    50,
                    HEIGHT // 2,
                )
                pg.time.wait(1000)
                running = False
            else:
                model_temp.send_oliners(
                    player1_first_point, player1_second_point, player1_number
                )
                model_temp.send_oliners(
                    player2_first_point, player2_second_point, player2_number
                )
                model_temp.add_oliners()
                model.add_oliners()
                pg.display.flip()
                space_input(screen, WIDTH, HEIGHT, white)
                screen.fill((0, 0, 0))

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
