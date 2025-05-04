import os
import pygame as pg
from abc import ABC, abstractmethod
import sys
from game_clock import game_clock


class MouseController:
    """
    A controller class that handles mouse input for a turn-based game.
    It allows players to select circles, input numbers, and manage game interactions
    through mouse events. The controller interacts with the model and view to
    facilitate the game logic and rendering.

    Attributes:
        model (Model): The game model containing game state and logic.
        view (View): The game view for rendering the game state.
        circle_data (list): List of circle coordinates and sizes.
        connections (list): List of connections between circles.
        oliners_count (list): Count of Oliners at each circle.
        owners (list): List of owners for each circle.
        player (int): The current player number (1 or 2).
        run_game (bool): Flag to control game execution.
    """

    def __init__(self, model, view, run_game=True):
        """
        Initializes the MouseController with the model and view.
        Args:
            model (Model): The game model containing game state and logic.
            view (View): The game view for rendering the game state.
            run_game (bool): Flag to control game execution.
        """
        self.model = model
        self.view = view
        self.circle_data = view.circle_data
        self.connections = model.connections
        self.oliners_count = model.oliners_count
        self.owners = model.owners
        self.player = 0
        self.run_game = run_game  # Flag to control game execution

    def get_cursor_pos(self):
        """
        Gets the current position of the mouse cursor
        Returns:
            tuple: The x and y coordinates of the cursor
        """
        return pg.mouse.get_pos()

    def get_circle(self, player):
        """
        Checks if the cursor is over a viable circle

        Returns:
            viable_pos: a bool representing if the cursor is in a viable spot
            or not
            index: the index of the circle that the cursor if over from
            circle_data
        """
        cursor_pos = self.get_cursor_pos()
        for index, circle in enumerate(self.circle_data):
            x_dist = cursor_pos[0] - circle[0]
            y_dist = cursor_pos[1] - circle[1]
            if (x_dist**2 + y_dist**2) < 1200:  # Adjust the distance threshold as needed
                if self.owners[index] in player:
                    return index
        return None  # Return None if no valid circle is found

    def get_number(self):
        """
        Get a number input from the player. Returns None if no input is detected.

        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
    
            # Handle key press events
            if event.type == pg.KEYDOWN:
                if pg.K_1 <= event.key <= pg.K_9:  # Check for keys 1-9
                    return event.key - pg.K_0  # Return the number pressed
        return None  # No input detected

    def check_number(self, circle_max):
        """
        Get input number to move
        Args:
            circle_max (int): The maximum number of Oliners that can be moved
        Returns:
            int: The validated number of Oliners to move, or circle_max if input is invalid
        """
        number = None
        while number is None:
            number = self.get_number()
            if number is not None:
                try:
                    if number < 0 or number > circle_max:
                        return circle_max
                except ValueError:
                    print("Input not in range or not a number")
                    number = None  # Reset number to None to continue the loop
        return number

    def get_first_point(self):
        """
        Gets the origin of the blips to be moved. Waits for a mouse click
        and returns the index of the circle that was clicked on.
        Returns:
            int: The index of the circle that was clicked on
        """
        if not self.run_game:
            return 0  # Return a default value for testing

        on = True
        while on:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()          
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        return self.get_circle([self.player])
            # game_clock(screen)  # Call game clock only if running the game

    def get_second_point(self, first_point):
        """
        Draws the second point selection screen and waits for a mouse click
        Args:
            first_point (int): The index of the first point that was clicked on
        Returns:
            int: The index of the second circle that was clicked on
        """
        if not self.run_game:
            return 1  # Return a default value for testing

        circle_owner = [0, 1, 2]
        on = True
        while on:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        second_point = self.get_circle(circle_owner)
                        if second_point in self.connections[first_point]:
                            return second_point
            # game_clock(screen)  # Call game clock only if running the game

# WHAT WE NEED FROM MODEL
# The list of circle coordinates and circle sizes
# The list of connections of nodes
# The number of blips at each point
class KeyController:
    """ 
    A controller class that handles keyboard input for a turn-based game.
    It allows players to select circles, input numbers, and manage game interactions
    through keyboard events. The controller interacts with the model and view to
    facilitate the game logic and rendering.
    """

    def __init__(self):
        self.owners = []  # Initialize owners as an empty list

    def get_circle(self):
        """
        Checks if the cursor is over a viable circle

        Returns:
            viable_pos: a bool representing if the cursor is in a viable spot
            or not
            index: the index of the circle that the cursor if over from
            circle_data
        """
        index = input("Which circle do you want to select?")
        try:
            index = int(index)
            if index < 0 or index >= len(self.owners):  # Ensure index is within range
                raise ValueError("Input not in range")
        except ValueError:
            print("Input not in range or not a number")
            raise  # Re-raise the exception for the test to catch
        return index

    def get_number(self):
        """
        Get input number to move.
        Returns:
            int: The validated number of Oliners to move, or None if input is invalid
        """
        number = input("How many units do you want to move")
        try:
            number = int(number)
            if number < 0:
                raise ValueError("Input must be non-negative")
        except ValueError:
            print("Input not in range or not a number")
            return None  # Return None instead of exiting
        return number

    def get_first_point(self):
        """
        Gets the origin of the blips to be moved.
        Waits for a keyboard input and returns the index of the circle that was selected.
        Returns:
            int: The index of the circle that was selected
        """
        return self.get_circle()

    def get_second_point(self, first_point):
        """
        Get a second circle to move blips to. Checks if the circle is
        adjacent to the first one.
        Args:
            first_point (int): The index of the first point that was selected
        Returns:
            int: The index of the second circle that was selected
        """
        connections = {
            0: [1, 2],
            1: [0, 2, 3, 4],
            2: [0, 1, 3, 4],
            3: [1, 2, 4, 5],
            4: [1, 2, 3, 5],
            5: [3, 4],
        }
        second_circle = self.get_circle()
        if second_circle in connections[first_point]:
            return second_circle
        else:
            raise ValueError("Selected circle is not connected to the first point")
        # first circle/get_first_point will be overridden with in the game
        # function with what we want
