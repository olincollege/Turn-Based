import pygame as pg
from Model import Model
import math


class View:
    """
    View class for rendering the game.
    """

    def __init__(self, model):
        """
        Initialize the view with the model.
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
            print(position)
            self.draw_numbers(value, position, player_color)

    def draw_numbers(self, count, position, player_color):
        """
        Write the number of Oliners at each building
        """
        font = pg.font.Font("freesansbold.ttf", 40)
        text = font.render(f"{count}", True, self.white, player_color)
        text_rect = text.get_rect()
        text_rect.center = (position[0], position[1])
        self.screen.blit(text, text_rect)
        print(text_rect.topleft)

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
        Display "Player _ is next, please move the computer
        """
        x = self.model.screen_width
        y = self.model.screen_height
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
        text_rect.center = (x // 2, y)

    def calculate_edge_point(self, x1, y1, x2, y2, radius):
        """Calculate the point on the edge of a circle closest to another point."""
        angle = math.atan2(y2 - y1, x2 - x1)
        edge_x = x1 + radius * math.cos(angle)
        edge_y = y1 + radius * math.sin(angle)
        return edge_x, edge_y

    def draw_circles(self):
        """Draw circles with only an outline."""
        for x, y, radius in self.circle_data:
            pg.draw.circle(self.screen, self.white, (x, y), radius, 1)

    def draw_connections(self):
        """Draw connections between circles."""
        for circle_index, connected_indices in self.model.connections.items():
            for connected_index in connected_indices:
                # Get coordinates and radii of connected circles
                start_x, start_y, start_radius = self.circle_data[circle_index]
                end_x, end_y, end_radius = self.circle_data[connected_index]

                # Calculate edge points
                start_edge = self.calculate_edge_point(
                    start_x, start_y, end_x, end_y, start_radius
                )
                end_edge = self.calculate_edge_point(
                    end_x, end_y, start_x, start_y, end_radius
                )

                # Draw line between edge points
                pg.draw.line(self.screen, self.white, start_edge, end_edge, 2)
