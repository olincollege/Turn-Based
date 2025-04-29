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
        # Set who owns what point at the start. 0 is empty, 1 is player 1, etc.
        self.owners = {0 : 1, 1 : 0, 2 : 0, 3 : 1, 4 : 0, 5 : 0}
        # How many oliners are at each point at the start
        self.oliners = [5, 5, 5, 5, 5, 5]

        self.running = True

    def calculate_edge_point(self, x1, y1, x2, y2, radius):
        """Calculate the point on the edge of a circle closest to another point."""
        angle = math.atan2(y2 - y1, x2 - x1)
        edge_x = x1 + radius * math.cos(angle)
        edge_y = y1 + radius * math.sin(angle)
        return edge_x, edge_y

    def draw_circles(self):
        """Draw circles with only an outline."""
        for x, y, radius in self.circle_data:
            pygame.draw.circle(self.screen, self.white, (x, y), radius, 1)

    def draw_connections(self):
        """Draw connections between circles."""
        for circle_index, connected_indices in self.connections.items():
            for connected_index in connected_indices:
                # Get coordinates and radii of connected circles
                start_x, start_y, start_radius = self.circle_data[circle_index]
                end_x, end_y, end_radius = self.circle_data[connected_index]

                # Calculate edge points
                start_edge = self.calculate_edge_point(start_x, start_y, end_x, end_y, start_radius)
                end_edge = self.calculate_edge_point(end_x, end_y, start_x, start_y, end_radius)

                # Draw line between edge points
                pygame.draw.line(self.screen, self.white, start_edge, end_edge, 2)

    def run(self):
        """Main game loop."""
        while self.running:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Clear the screen
            self.screen.fill(self.black)

            # Draw circles and connections
            self.draw_circles()
            self.draw_connections()

            # Update the display
            pygame.display.flip()

    def 

        # Quit Pygame
        pygame.quit()

# Instantiate and run the game
# if __name__ == "__main__":
#     game = Model()
#     game.run()
