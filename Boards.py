###########################################################################################################
# File Name: Boards.py
# Purpose: This module contains the TicTacToe class for the Tic Tac Toe game.
# Author: Ishwar Agarwal
# Last Date Modified: 12/10/2015
# Acknowledgements: Line 150-151 has been obtained from questions in StackOverflow.
#     http://stackoverflow.com/questions/6313308/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python
###########################################################################################################


import numpy
import random


class TicTacToe(object):
    """A Tic-Tac-Toe game board created using numpy array

    The game board is easily adjustable to create a NxN matrix,
    where N is the size that has to passed in to the class. The default size is 3x3.

    The class contains methods to set and get values at each position in the board.
    It also has methods, for checking, if game is over, if there is a winner, who is the winner.

    Attributes:
        size: Stores the size of the tic tac toe board
        X_VAL: This sets how we want to represent the x-value in the game board(numpy array).
        O_VAL: This sets how we want to represent the o-value in the game board.
        NO_VAL: This sets how we want to represent an empty position on the game board.
        winning_combos: This stores the winning positions in the board if the game is won.
        board: A 2-D Numpy array which is the database to record the value of each position
                of the game board. It is initialized with every position having self.NO_VAL.
    """

    def __init__(self, size=3):
        self.size = size
        self.X_VAL = 'X'
        self.O_VAL = 'O'
        self.NO_VAL = ''
        self.winning_combos = []
        self.board = numpy.array([[self.NO_VAL for i in range(size)] for i in range(size)])

    def available_moves(self):
        """Returns a list of tuples where each tuple is a location of an empty spot on the board.

        e.g. [(a,b), (c,d)] a is the row and b is the column position in self.board
        where there is an empty position.
        """
        moves = []
        for i in range(self.size):  # go through each row
            for j in range(self.size):  # go through each column
                _item = self.board.item((i, j))
                if _item == self.NO_VAL:    # if the spot is empty append it to the moves list
                    moves.append((i, j))
        return moves

    def game_over(self):
        """Returns True if the game is over.

        Game is over when either it is a draw(i.e. all the blocks on board are filled up),
        or there is a winner(i.e. X-wins or O-wins).
        """
        if self.available_moves() == []:
            return True
        if self.winner() is not None:
            return True
        return False

    def X_won(self):
        """Returns a True bool value if X_VAL wins the game
        """
        return self.winner() == self.X_VAL

    def O_won(self):
        """Returns a True bool value if O_VAL wins the game
        """
        return self.winner() == self.O_VAL

    def tied(self):
        """Returns a True bool value if the game is tied.
        """
        return self.game_over() and self.winner() is None   # Checks if game is over and there is no winner

    def winner(self):
        """Returns the winner of the game if there is a winner, else returns None type.
        """
        if self.check_winner(self.X_VAL):   # checks if X_VAL is winner
            return self.X_VAL
        elif self.check_winner(self.O_VAL):  # checks if O_VAL is winner
            return self.O_VAL
        else:
            return None

    def check_winner(self, player):
        """ Returns a True boolean value if the passed player is winner, else False

        The function checks all the rows, columns and diagonal of the matrix to see if player is all in one row,
        one column or all in one diagonals
        e.g In this array   [[X, O, X],
                            [X, X, X],
                            [X, O, O]]
            if player is equal to X_VAL it returns True. If player = O_VAL it returns False.

        Args:
            player: Player has to be either self.X_VAL or self.O_VAL, otherwise function will
                    not work as expected.
        """

        state = False   # start with False state, and when there is a win change it to True

        # Check all the rows of the matrix
        for row in range(self.size):
            winning_combos = []     # create a list that will contain positions of winning row, column, or diagonal
            counter = 0
            for column in range(self.size):
                if self.board[row, column] == player:
                    counter += 1    # counts the number of time player is in that row
                    winning_combos.append((row, column))
                if counter == self.size:    # checks if player has occupied the entire row
                    state = True    # Change the state
                    self.winning_combos = winning_combos    # if the player wins save this row in self.winning_combos
                    return state

        # Check all the columns of the matrix
        for column in range(self.size):
            winning_combos = []
            counter = 0
            for row in range(self.size):
                if self.board[row, column] == player:
                    counter += 1    # counts the number of time player is in that column
                    winning_combos.append((row, column))
                if counter == self.size:    # checks if player has occupied the entire column
                    state = True
                    self.winning_combos = winning_combos
                    return state

        winning_combos = []     # reset winning_combos
        # Check the negative diagonal of the matrix
        counter = 0     # reset counter
        for i in range(self.size):
            if self.board[i, i] == player:
                counter += 1    # counts the number of time player is in the negative diagonal
                winning_combos.append((i, i))
            if counter == self.size:    # checks if player has occupied the entire diagonal
                state = True
                self.winning_combos = winning_combos
                return state

        winning_combos = []
        # Check the positive diagonal of the matrix,
        counter = 0
        for i in range(self.size-1, -1, -1):    # goes through each position in the positive diagonal
            if self.board[self.size-1-i, i] == player:
                counter += 1    # counts the number of time player is in the positive diagonal
                winning_combos.append((self.size-1-i, i))
            if counter == self.size:    # checks if player has occupied the entire diagonal
                state = True
                self.winning_combos = winning_combos
                return state

        return state    # if the player does not win, then it returns False bool type value

    def make_move(self, pos, value):
        """Sets the given position on self.board numpy array with the given value

        Args:
            pos: an integer or a tuple that represents the index of self.board
            value: any data type that has to be set at that position

        Raises:
            IndexError: if the pos is out of range in self.board
        """
        self.board.itemset(pos, value)

    def get_value(self, x, y):
        """Returns the value of a given position in self.board.

        Args:
            x = row index of the position in self.board
            y = column index of the position in self.board

        Raises:
            IndexError: if the x, y is out of range in self.board
        """
        return self.board.item((x, y))

    def get_opponent(self, player):
        """Switches and returns the given player in the game board

        Args:
            player: player should be equal to either self.X_VAL or self.O_VAL
        """
        if player == self.X_VAL:
            return self.O_VAL
        if player == self.O_VAL:
            return self.X_VAL
