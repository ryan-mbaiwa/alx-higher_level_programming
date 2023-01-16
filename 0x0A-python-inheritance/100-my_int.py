#!/usr/bin/python3
"""

A module that inherits from class int in another module

"""


class MyInt(int):
    """ Class that inherits from class int"""

    def __eq__(self, other):
        """ Method that returns != check """
        return int.__ne__(self, other)

    def __ne__(self, other):
        """ Method that returns == check """
        return int.__eq__(self, other)
