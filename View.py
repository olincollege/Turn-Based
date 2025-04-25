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

    