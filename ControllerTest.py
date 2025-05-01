import os
import pygame as pg
from abc import ABC, abstractmethod

# class GameController(ABC):
#     """
    
#     """
#     def __init__(self, model, circles):
#         """
        
#         """
#         self.model = model
#         self.circles = circles
    
#     @property
#     def model(self):
#         """
        
#         """
#         return self.model
    
#     @property
#     def circles(self):
#         """
        
#         """
#         return self._circles
    
#     @abstractmethod
#     def get_first_point(self):
#         """
#         """

#     @abstractmethod
#     def get_second_point(self):
#         """
#         """

#     @abstractmethod
#     def get_number(self):
#         """
#         """

    

class MouseController():
    """

    """

    def __init__(self, model, view):
        """
        
        """
        self.model = model
        self.view = view
        self.circle_data = view.circle_data
        self.connections = model.connections
        self.oliners_count = model.oliners_count

    def get_cursor_pos(self):
        """
        Docstring
        """
        
        return pg.mouse.get_pos()

    def get_circle(self):
        """
        Checks if the cursor is over a viable circle

        Returns:
            viable_pos: a bool representing if the cursor is in a viable spot
            or not
            index: the index of the circle that the cursor if over from
            circle_data
        """
        for index, circle in enumerate(self.circle_data):
            x_dist = self.get_cursor_pos()[0] - circle[0]
            y_dist = self.get_cursor_pos()[1] - circle[1]
            if (x_dist**2 + y_dist**2) < 900: # and (index in player_owned):
                # 900 assumes all circles will have radius of 30
                return index

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
        return number
    
    def get_first_point(self):
        """
        Gets the origin of the blips to be moved
        """
        return self.get_circle()
    
    def get_second_point(self):
        """
         Get a second circle to move blips to. Checks if the circle is 
         adjacent to the first one.
        """   
        second_circle = self.get_circle()
        if second_circle in self.connections[self.get_first_point()]:
            return second_circle
        else:
            raise ValueError
        #first circle/get_first_point will be overridden in the game function

    def get_click(self):
        """
        Docstring
        """
        #if pg.MOUSEBUTTONDOWN

    def move(self):
        #Get key press
        first_point = self.get_first_point()
        second_point = self.get_second_point
        number = self.get_number()
        if number > self.oliners_count[first_point]:
            print("Input not in range or not a number")
            raise ValueError
        return [first_point, second_point, number]


# WHAT WE NEED FROM MODEL
# The list of circle coordinates and circle sizes
# The list of connections of nodes
# The number of blips at each point
class KeyController():
    """
    """

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
            if not isinstance(index, int):
                raise ValueError
            elif index < 0: 
            #or index > len(connections):
                raise ValueError
        except(ValueError):
            print("Input not in range or not a number")
        return index

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
        return number
    
    def get_first_point(self):
        """
        Gets the origin of the blips to be moved
        """
        return self.get_circle()
    
    def get_second_point(self, first_point):
        """
         Get a second circle to move blips to. Checks if the circle is 
         adjacent to the first one.
        """   
        connections = {
            0: [1, 2], 1: [0, 2, 3, 4], 2: [0, 1, 3, 4],
            3: [1, 2, 4, 5], 4: [1, 2, 3, 5], 5: [3, 4]
        }
        second_circle = self.get_circle()
        if second_circle in connections[first_point]:
            return second_circle
        else:
            raise ValueError
        #first circle/get_first_point will be overridden with in the game
        #function with what we want
