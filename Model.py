import pygame
import math


class Model:
    def __init__(self):
        """
        Initializes the game model with necessary attributes and settings.
        This includes setting up the Pygame environment, defining circle data,
        connections between circles, initial ownership of circles, and the count
        of Oliners at each circle.

        Attributes:
            screen_width (int): Width of the game screen.
            screen_height (int): Height of the game screen.
            screen (pygame.Surface): The Pygame display surface.
            connections (dict): A dictionary mapping each circle index to its
                connected circles.
            owners (dict): A dictionary mapping each circle index to its owner.
            oliners_count (list): A list tracking the number of Oliners at each
                circle.
            running (bool): A flag indicating whether the game is running.
        """
        # Initialize Pygame
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height)
        )
        pygame.display.set_caption("Game Network Map")

        # Connections (index of connected circles)
        self.connections = {
            0: [0, 1, 2],
            1: [0, 1, 2, 3, 4],
            2: [0, 1, 2, 3, 4],
            3: [1, 2, 3, 4, 5],
            4: [1, 2, 3, 4, 5],
            5: [3, 4, 5],
        }
        # Set who owns what point at the start. 0 is empty, 1 is player 1, etc.
        self.owners = {0: 1, 1: 0, 2: 0, 3: 0, 4: 0, 5: 2}
        # How many oliners are at each point at the start
        self.oliners_count = [10, 0, 0, 0, 0, 10]
        self.running = True

    def add_oliners(self):
        """
        Adds an Oliner to each owned building.
        This function iterates through the list of owners and increments the
        count of Oliners for each building that has an owner greater than 0.
        Returns:
            list(int): The updated count of Oliners at each point.
        """
        for index in range(len(self.oliners_count)):
            if self.owners[index] > 0:
                self.oliners_count[index] += 1
        return self.oliners_count

    def send_oliners(self, first_point, second_point, number_to_move):
        """
        Works out how Oliners are sent from building to building. Changes who
        owns what building
        NOTE: We can't input directly from controller to here within the class
        without changing inheritance structures. We can add the inputs in the
        update function instead, outside of the class
        Args:
            first_point (int): The point from which Oliners are sent
            second_point (int): The point to which Oliners are sent
            number_to_move (int): The number of Oliners to move
        Returns:
            list(int): The updated count of Oliners at each point
        """
        player = self.owners[first_point]
        self.oliners_count[first_point] -= number_to_move
        if self.owners[second_point] == player:
            self.oliners_count[second_point] += number_to_move
        elif self.oliners_count[second_point] > number_to_move:
            self.oliners_count[second_point] -= number_to_move
        elif self.oliners_count[second_point] == number_to_move:
            self.oliners_count[second_point] = 0
            self.owners[second_point] = player
        elif self.oliners_count[second_point] < number_to_move:
            self.oliners_count[second_point] = (
                number_to_move - self.oliners_count[second_point]
            )
            self.owners[second_point] = player
        return self.oliners_count

    def check_negative(self):
        """
        Checks if there are any negative numbers at a point.
        If so, the count is set to 0 and the owner is set to no one
        """
        for index, count in enumerate(self.oliners_count):
            if count < 0:
                self.oliners_count[index] = 0
                self.owners[index] = 0

    def check_win(self):
        """
        Checks if one player has won the game.
        Returns:
            int: 0 if no one has won, 1 if player 1 has won, 2 if player 2 has won
        """
        owner_in = list(self.owners.values())

        if 1 != owner_in[0] or 2 != owner_in[5]:
            if 2 == owner_in[0] and 1 == owner_in[5]:
                return 3
            elif 1 == owner_in[5]:
                return 1
            elif 2 == owner_in[0]:
                return 2
        else:
            return 0
        
