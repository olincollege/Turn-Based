import pygame
import math


class Model:
    def __init__(self):
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
            0: [1, 2],
            1: [0, 2, 3, 4],
            2: [0, 1, 3, 4],
            3: [1, 2, 4, 5],
            4: [1, 2, 3, 5],
            5: [3, 4],
        }
        # Set who owns what point at the start. 0 is empty, 1 is player 1, etc.
        self.owners = {0: 1, 1: 0, 2: 0, 3: 2, 4: 0, 5: 0}
        # How many oliners are at each point at the start
        self.oliners_count = [5, 5, 5, 5, 5, 5]
        self.running = True

    def add_oliners(self):
        """
        Adds an Oliner to each owned building
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
