""" Main game file that initializes the game, handles the main loop, and manages game states."""

import sys
import pygame as pg
from openingscreen import main_menu, help_screen
from ending_screen import draw_end_screen
from game_clock import game_clock, TimeUp
from sequence import display_text, init_game, space_input
from controller import MouseController
from model import Model
from view import View

def main():
    """
    Main function to run the game.
    """
    screen, width, height = init_game()  # Initialize the game
    black = (0, 0, 0)
    white = (255, 255, 255)

    game_running = True
    while game_running:

        current_screen = "main_menu"
        while current_screen == "main_menu":
            current_screen = main_menu(screen, width, height)
        if current_screen == "help":
            current_screen = help_screen(screen, width, height)
        elif current_screen == "play":

            screen.fill((0, 0, 0))

            game_model = Model()
            game_view = View(game_model)
            player_one = MouseController(game_model, game_view)
            player_one.player = 1
            player_two = MouseController(game_model, game_view)
            player_two.player = 2
            running = True

            display_text(
                screen,
                "TO MOVE: FIRST SELECT A BUILDING YOU OWN",
                white,
                50,
                height - 550,
            )
            display_text(
                screen,
                "THEN SELECT ANOTHER BUILDING",
                white,
                50,
                height - 450,
            )
            display_text(
                screen,
                "THEN TYPE A NUMBER FROM 1-9",
                white,
                50,
                height - 350,
            )
            display_text(
                screen,
                "IF YOU SEND TO THE SAME BUILDING YOU",
                white,
                50,
                height - 250,
            )

            display_text(
                screen,
                "SENT FROM, YOU ONLY GET +2",
                white,
                50,
                height - 200,
            )

            space_input(screen, width, height, white, clock=False)
            try:
                clock = True
                while running:
                    pg.event.pump()

                    screen.fill((0, 0, 0))
                    game_view.draw()  # Draw the initial state of the game
                    game_clock(screen)
                    display_text(
                        screen,
                        "Player 1 Choose Your Move (BLUE)",
                        (255, 255, 255),
                        width // 2 - 225,
                        25,
                    )
                    point_defined = False
                    while point_defined is False:
                        player1_first_point = player_one.get_first_point()
                        if player1_first_point is not None:
                            point_defined = True

                    point_defined = False
                    while point_defined is False:
                        player1_second_point = player_one.get_second_point(
                            player1_first_point
                        )
                        if player1_second_point is not None:
                            point_defined = True

                    player1_number = player_one.check_number(
                        game_model.oliners_count[player1_first_point]
                    )
                    if player1_first_point == player1_second_point:
                        player1_number = 2

                    # WE HAVE PLAYER 1s MOVES STORED NOW
                    space_input(screen, width, height, white, clock)

                    screen.fill((0, 0, 0))
                    game_clock(screen)
                    display_text(
                        screen,
                        "Pass the device to Player 2",
                        white,
                        width // 2 - 175,
                        25,
                    )
                    space_input(screen, width, height, white, clock)

                    screen.fill((0, 0, 0))
                    game_view.draw()
                    game_clock(screen)
                    display_text(
                        screen,
                        "Player 2 Choose Your Move (RED)",
                        white,
                        width // 2 - 225,
                        25,
                    )
                    # Player 2's turn
                    point_defined = False
                    while point_defined is False:
                        player2_first_point = player_two.get_first_point()
                        if player2_first_point is not None:
                            point_defined = True

                    point_defined = False
                    while point_defined is False:
                        player2_second_point = player_two.get_second_point(
                            player2_first_point
                        )
                        if player2_second_point is not None:
                            point_defined = True

                    player2_number = player_two.check_number(
                        game_model.oliners_count[player1_first_point]
                    )
                    if player2_first_point == player2_second_point:
                        player2_number = 2

                    # WE HAVE PLAYER 2s MOVES NOW
                    # Addresses bug if both players send to the same point
                    if player2_first_point == player2_second_point:
                        game_model.oliners_count[player2_first_point] += 2
                    if player1_first_point == player1_second_point:
                        game_model.oliners_count[player1_first_point] += 2
                    #Works if they send to the same point
                    if player1_second_point == player2_second_point:
                        if player1_number > player2_number:
                            diff = player1_number - player2_number

                            game_model.send_oliners(
                                player1_first_point, player1_second_point, diff
                            )
                            game_model.oliners_count[player1_first_point] -= player2_number
                            game_model.oliners_count[player2_first_point] -= player2_number
                            # Some spaghetti code but its fine trust
                        elif player1_number < player2_number:
                            diff = player2_number - player1_number
                            game_model.send_oliners(
                                player2_first_point,
                                player2_second_point,
                                diff,
                            )
                            game_model.oliners_count[player2_first_point] -= player1_number
                            game_model.oliners_count[player1_first_point] -= player1_number
                        else:
                            game_model.oliners_count[player1_first_point] -= player1_number
                            game_model.oliners_count[player2_first_point] -= player2_number
                    else:
                        game_model.send_oliners(
                            player1_first_point, player1_second_point, player1_number
                        )
                        game_model.send_oliners(
                            player2_first_point, player2_second_point, player2_number
                        )

                    game_model.check_negative()

                    space_input(screen, width, height, white, clock)

                    screen.fill((0, 0, 0))
                    game_clock(screen)
                    display_text(
                        screen,
                        "Revealing Moves...",
                        white,
                        width // 2 - 125,
                        25,
                    )
                    pg.time.wait(1000)  # Wait for 1 second before revealing moves

                    # Reveal both moves
                    game_view.draw()
                    winner = game_model.check_win()
                    if winner > 0:
                        time = True
                        clock = False
                        running = False
                    else:
                        game_model.add_oliners()
                        pg.display.flip()
                        space_input(screen, width, height, white, clock)
                        screen.fill((0, 0, 0))
            except TimeUp:
                clock = False
                running = False
                time = False
            finally:
                # Ensure winner, time and clock are always defined
                if 'winner' not in locals():
                    winner = 0

            space_input(screen, width, height, white, clock)

            if time is False:
                draw_end_screen(screen, width, width, black, white, 0)
            else:
                draw_end_screen(screen, width, width, black, white, winner)
            pg.time.wait(1000)

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
