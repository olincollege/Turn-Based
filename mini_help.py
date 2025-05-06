""" The mini_help module provides a brief overview of the game mechanics and controls for players. """

from sequence import display_text

def mini_help(screen, height, white):
    """Display a mini help screen with game instructions.
    Args:
        screen: The pygame screen to draw on.
        height: The height of the screen.
        white: The color white for the text.
    """
    display_text(
                screen,
                "TO MOVE: FIRST SELECT A BUILDING YOU OWN",
                white,
                30,
                height - 550,
            )
    display_text(
                screen,
                "THEN SELECT ANOTHER BUILDING",
                white,
                30,
                height - 475,
            )
    display_text(
                screen,
                "THEN TYPE A NUMBER FROM 1-9",
                white,
                30,
                height - 400,
            )
    display_text(
                screen,
                "IF YOU SEND TO THE SAME BUILDING YOU",
                white,
                30,
                height - 325,
            )

    display_text(
                screen,
                "SENT FROM, YOU ONLY GET +2",
                white,
                30,
                height - 250,
            )
    display_text(
                screen,
                "SENDING MORE OLINERS THAN YOU HAVE IN ONE",
                white,
                30,
                height - 175,
            )
    display_text(
                screen,
                "BUILDING WILL SEND THE MAX NUMBERS OF OLINERS""",
                white,
                30,
                height - 150,
            )
