import os
import pygame as pg
import sys
from openingscreen import main_menu
from ending_screen import draw_end_screen
from game_clock import (game_clock, time_up)
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
    """
    Main function to run the game.
    """
    screen, WIDTH, HEIGHT = init_game()  # Initialize the game

    game_running = True
    while game_running:

        main_menu(screen, WIDTH, HEIGHT)

        screen.fill((0, 0, 0))
        blue = (0, 225, 0)
        red = (225, 0, 0)

        model = Model()
        view = View(model)
        player_one = MouseController(model, view)
        player_one.player = 1
        player_two = MouseController(model, view)
        player_two.player = 2
        running = True

        display_text(
            screen,
            "TO MOVE: FIRST SELECT A BUILDING YOU OWN",
            40,
            white,
            50,
            HEIGHT - 550,
        )
        display_text(
            screen,
            "THEN SELECT A BUILDING YOU DON'T OWN",
            40,
            white,
            50,
            HEIGHT - 450,
        )
        display_text(
            screen,
            "THEN TYPE A NUMBER FROM 1-9",
            40,
            white,
            50,
            HEIGHT - 350,
        )
        display_text(
            screen,
            "IF YOU SEND TO THE SAME BUILDING YOU"
            ,
            40,
            white,
            50,
            HEIGHT - 250,
        )

        display_text(
            screen,
            "SENT FROM, YOU ONLY GET +2" 
            ,
            40,
            white,
            50,
            HEIGHT - 200,
        )

        space_input(screen, WIDTH, HEIGHT, white, clock=False)
        try:
            clock = True
            while running:
                pg.event.pump()

                screen.fill((0, 0, 0))
                view.draw()  # Draw the initial state of the game
                game_clock(screen)
                display_text(
                    screen,
                    "Player 1 Choose Your Move (BLUE)",
                    40,
                    (255, 255, 255),
                    50,
                    HEIGHT - 550,
                )
                point_defined = False
                while point_defined is False:
                    player1_first_point = player_one.get_first_point(screen)
                    if player1_first_point is not None:
                        point_defined = True

                point_defined = False
                while point_defined is False:
                    player1_second_point = player_one.get_second_point(
                        player1_first_point, screen
                    )
                    if player1_second_point is not None:
                        point_defined = True

                player1_number = player_one.check_number(
                    model.oliners_count[player1_first_point], screen
                )
                if player1_first_point == player1_second_point:
                    player1_number = 2

                # WE HAVE PLAYER 1s MOVES STORED NOW
                space_input(screen, WIDTH, HEIGHT, white, clock)

                screen.fill((0, 0, 0))
                game_clock(screen)
                display_text(
                    screen,
                    "Pass the device to Player 2",
                    40,
                    (255, 255, 255),
                    50,
                    HEIGHT - 550,
                )
                space_input(screen, WIDTH, HEIGHT, white, clock)

                screen.fill((0, 0, 0))
                view.draw()
                game_clock(screen)
                display_text(
                    screen,
                    "Player 2 Choose Your Move (RED)",
                    40,
                    (255, 255, 255),
                    50,
                    HEIGHT - 550,
                )
                # Player 2's turn
                point_defined = False
                while point_defined is False:
                    player2_first_point = player_two.get_first_point(screen)
                    if player2_first_point is not None:
                        point_defined = True

                point_defined = False
                while point_defined is False:
                    player2_second_point = player_two.get_second_point(
                        player2_first_point, screen
                    )
                    if player2_second_point is not None:
                        point_defined = True

                player2_number = player_two.check_number(
                    model.oliners_count[player1_first_point], screen
                )
                if player2_first_point == player2_second_point:
                    player2_number = 2

                # WE HAVE PLAYER 2s MOVES NOW
                # Addresses bug if both players send to the same point
                if player2_first_point == player2_second_point:
                    model.oliners_count[player2_first_point] += 2
                if player1_first_point == player1_second_point:
                    model.oliners_count[player1_first_point] += 2
                #Works if they send to the same point
                if player1_second_point == player2_second_point:
                    if player1_number > player2_number:
                        diff = player1_number - player2_number

                        model.send_oliners(
                            player1_first_point, player1_second_point, diff
                        )
                        model.oliners_count[player1_first_point] -= player2_number
                        model.oliners_count[player2_first_point] -= player2_number
                        # Some spaghetti code but its fine trust
                    elif player1_number < player2_number:
                        diff = player2_number - player1_number
                        model.send_oliners(
                            player2_first_point,
                            player2_second_point,
                            diff,
                        )
                        model.oliners_count[player2_first_point] -= player1_number
                        model.oliners_count[player1_first_point] -= player1_number
                    else:
                        model.oliners_count[player1_first_point] -= player1_number
                        model.oliners_count[player2_first_point] -= player2_number
                else:
                    model.send_oliners(
                        player1_first_point, player1_second_point, player1_number
                    )
                    model.send_oliners(
                        player2_first_point, player2_second_point, player2_number
                    )

                model.check_negative()

                space_input(screen, WIDTH, HEIGHT, white, clock)

                screen.fill((0, 0, 0))
                game_clock(screen)
                display_text(
                    screen,
                    "Revealing Moves...",
                    40,
                    (255, 255, 255),
                    WIDTH // 2 - 100,
                    25,
                )
                pg.time.wait(1000)  # Wait for 1 second before revealing moves

                # Reveal both moves
                view.draw()
                winner = model.check_win()
                if winner > 0:
                    time = True
                    clock = False
                    running = False
                else:
                    model.add_oliners()
                    pg.display.flip()
                    space_input(screen, WIDTH, HEIGHT, white, clock)
                    screen.fill((0, 0, 0))
        except time_up:
            clock = False
            running = False
            time = False
        finally:
            # Ensure winner, time and clock are always defined
            if 'winner' not in locals():
                winner = 0   


        space_input(screen, WIDTH, HEIGHT, white, clock)

        if time == False:
            draw_end_screen(screen, WIDTH, HEIGHT, black, white, 0)
        else:
            draw_end_screen(screen, WIDTH, HEIGHT, black, white, winner)
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
