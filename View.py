"""view class for rendering the game using Pygame."""

import math
import pygame as pg


class View:
    """
    view class for rendering the game.

    Attributes:
        model (Model): The game model containing game state and logic.
        screen (pygame.Surface): The Pygame screen for rendering.
        running (bool): Flag to indicate if the game is running.
        circle_data (list): List of circle coordinates and sizes.
        white (tuple): Color for the circles.
        black (tuple): Color for the background.
        red (tuple): Color for player 2.
        blue (tuple): Color for player 1.
        oliners_count (list): Count of Oliners at each circle.
        font (pygame.font.Font): Font for rendering text.
    """

    def __init__(self, model):
        """
        Initialize the view with the model.
        Args:
            model (Model): The game model containing game state and logic.
        """
        self.model = model
        self.screen = model.screen
        self.running = True
        # Circle data (x, y, radius)
        self.circle_data = [
            (400, 100, 30),
            (200, 200, 30),
            (600, 200, 30),
            (200, 400, 30),
            (600, 400, 30),
            (400, 500, 30),
        ]

        # Colors
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.blue = (0, 0, 255)
        self.oliners_count = model.oliners_count
        self.font = pg.font.Font(None, 10)

    def draw(self):
        """
        Draw the circles and connections on the screen.
        """
        self.draw_circles()
        self.draw_connections()
        for index, value in enumerate(self.oliners_count):
            if self.model.owners[index] == 1:
                player_color = self.blue
            elif self.model.owners[index] == 2:
                player_color = self.red
            else:
                player_color = self.black
            position = list(self.circle_data[index])
            self.draw_numbers(value, position, player_color)

    def draw_numbers(self, count, position, player_color):
        """
        Write the number of Oliners at each building
        Args:
            count (int): The number of Oliners at the building.
            position (tuple): The (x, y) position to draw the text.
            player_color (tuple): The color of the player owning the building.
        """
        font = pg.font.Font("freesansbold.ttf", 40)
        text = font.render(f"{count}", True, self.white, player_color)
        text_rect = text.get_rect()
        text_rect.center = (position[0], position[1])
        self.screen.blit(text, text_rect)

    def update(self):
        """
        Update the display and handle events.
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

        self.screen.fill(self.black)
        self.draw()
        pg.display.flip()

    def show_next_player(self):
        """
        Display "Player _ is next, please move the computer".
        """
        x_val = self.model.screen_width
        y_val = self.model.screen_height
        black = (0, 0, 0)
        white = (225, 225, 225)
        font = pg.font.Font("freesansbold.ttf", 32)

        text = font.render(
            f"{self.model.next_player} is next,         please give them the"
            " computer",
            True,
            black,
            white,
        )
        text_rect = text.get_rect()
        text_rect.center = (x_val // 2, y_val)

    def calculate_edge_point(self, x_1, y_1, x_2, y_2):
        """Calculate the point on the edge of a circle closest to another point.
        Args:
            x1, y1: Coordinates of the first circle's center.
            x2, y2: Coordinates of the second circle's center.
            radius: Radius of the first circle.
        Returns:
            tuple: Coordinates of the edge point on the first circle.
        """
        angle = math.atan2(y_2 - y_1, x_2 - x_1)
        edge_x = x_1 + 30 * math.cos(angle)
        edge_y = y_1 + 30 * math.sin(angle)
        return edge_x, edge_y

    def draw_circles(self):
        """Draw circles with only an outline."""
        for x_val, y_val, radius in self.circle_data:
            pg.draw.circle(self.screen, self.white, (x_val, y_val), radius, 1)

    def draw_connections(self):
        """Draw connections between circles."""
        for circle_index, connected_indices in self.model.connections.items():
            for connected_index in connected_indices:
                # Get coordinates and radii of connected circles
                start_x, start_y = self.circle_data[circle_index][:-1]
                end_x, end_y = self.circle_data[connected_index][:-1]

                # Calculate edge points
                start_edge = self.calculate_edge_point(
                    start_x, start_y, end_x, end_y
                )
                end_edge = self.calculate_edge_point(
                    end_x, end_y, start_x, start_y
                )

                # Draw line between edge points
                pg.draw.line(self.screen, self.white, start_edge, end_edge, 2)
