import os
import pygame as pg
from abc import ABC, abstractmethod

class GameController(ABC):
    """
    
    """
    def __init__(self, model, circles):
        """
        
        """
        self._model = model
        self._circles = circles
    
    @property
    def model(self):
        """
        
        """
        return self._model
    
    @property
    def circles(self):
        """
        
        """
        return self._circles
    
    @abstractmethod
    def move(self):
        """
        """

class MouseController(GameController):
    """

    """

    def get_cursor_pos(self):
        """
        Docstring
        """
        
        self.pos = pg.mouse.get_pos()

    def check_if_viable(self):
        """
        Checks if the cursor is over a viable circle

        Returns:
            viable_pos: a bool representing if the cursor is in a viable spot
            or not
            index: the index of the circle that the cursor if over from
            circle_data
        """
        viable_pos = False
        circles = [
            (400, 100, 30), (200, 200, 30), (600, 200, 30),
            (200, 400, 30), (600, 400, 30), (400, 500, 30)
        ]
        # Eventually we will want to load the circles from the model class
        for index, circle in enumerate(circles):
            x_dist = self.pos[0] - circle[0]
            y_dist = self.pos[1] - circle[1]
            if (x_dist**2 + y_dist**2) < 900:
                # 900 assumes all circles will have radius of 30
                viable_pos = True
                return viable_pos, index

    def get_number(self):
        """
        Get input number to move
        """
        number = input("How many units do you want to move")
        try:
            number = int(number)
            if not isinstance(number, int):
                raise ValueError
            elif number < 0:
                raise ValueError
            #elif number > cirle_max
                #raise ValueError
        except(ValueError):
            print("Input not in range or not a number")

    def get_click(self):
        """
        Docstring
        """
        #if pg.MOUSEBUTTONDOWN
