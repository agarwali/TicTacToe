################################################################################################################
# File Name: test.py
# Purpose: It contains unit test for different methods I created for this project
# Author: Ishwar Agarwal
# Last Date Modified: 12/11/2015
#################################################################################################################

import numpy
from Boards import TicTacToe
import sys
import unittest


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def main():
    three = TicTacToe(3)
    three.board = numpy.array([['X', 'O', 'X'],
                               ['O', 'X', 'O'],
                               ['O', 'X', 'X']])

    test(three.available_moves() == [])
    test(three.game_over() == True)
    test(three.tied() == False)
    test(three.X_won() == True)
    test(three.O_won() == False)
    test(three.winner() == 'X')


main()