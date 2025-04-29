import pygame
import math

class Model:
    def __init__(self, screen_width=800, screen_height=600):
        # Initialize Pygame
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Game Network Map")


        # Connections (index of connected circles)
        self.connections = {
            0: [1, 2], 1: [0, 2, 3, 4], 2: [0, 1, 3, 4],
            3: [1, 2, 4, 5], 4: [1, 2, 3, 5], 5: [3, 4]
        }



