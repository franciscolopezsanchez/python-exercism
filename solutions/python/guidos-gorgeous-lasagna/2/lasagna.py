"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate the total time needed for preparation in minutes

    :param number_of_layers: int - the number of layers added to the lasagna.
    :return: int - minutes you would spend preparing.

    Function that takes the number of layers in the lasagna as an argument 
    and returns how many minutes the lasagna will take to bake
    based on the `PREPARATION_TIME`.
    """
    return PREPARATION_TIME * number_of_layers


def elapsed_time_in_minutes(number_of_layers, elapsed_baked_time):
    """Calculate the total elapsed time (prepping + baking) in minutes

    :param number_of_layers: int - the number of layers added to the lasagna
    :elapsed_bake_time: int - the number of minutes the lasagna has spent baking in the oven already
    :return: int - the total minutes you have been in the kitchen cooking.

    Function that takes the number of layers and the elapsed baked time already  
    and returns how many minutes has passed since you started cooking.
    """
    return elapsed_baked_time + preparation_time_in_minutes(number_of_layers)
