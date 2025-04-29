import pygame as pg
from Model import Model

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
        self.clock = model.clock
        self.running = True

    def draw(self):
        """
        Draw the circles and connections on the screen.
        """
        self.model.draw_circles()
        self.model.draw_connections()
        
    def update(self):
        """
        Update the display and handle events.
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
        
        self.screen.fill(self.model.black)
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
        font = pg.font.Font('freesansbold.ttf', 32)

        text = font.render(f'{self.model.next_player} is next, \
        please give them the computer', True, black, white)
        text_rect = text.get_rect()
        text_rect.center = (x // 2, y)

    