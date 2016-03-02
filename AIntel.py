###########################################################################################################
# File Name: AIntel.py
# Purpose: This module contains the AI class for the Tic Tac Toe game and needs the Board class to work.
# Author: Ishwar Agarwal
# Last Date Modified: 12/11/2015
# Acknowledgements:
###########################################################################################################

from Boards import TicTacToe
import random


class AI(TicTacToe):
    """Artificial Intelligence Class for playing the Tic Tac Toe game against human player.

    The class allows the computer to become first or second player in the Tic Tac Toe game.
    The intelligence of the class is based on an aplha beta algorithm, implemented using a
    recursive function self.aplhabeta that takes advantage of the runtime tree. The class
    inherits properties from the TicTacToe class in the Boards module.

    Attributes:
        _aiPlayer: This represents if the computer will be X_VAL or O_VAL in the game.
        _humanPlayer: This represents the human player's value in the game (opposite of  aiPlayer).
        _board: This is a copy of the TicTacToe board class that is passed into the object,
                while initializing the class.
    """

    def __init__(self, player='O', board=TicTacToe(3)):
        self._aiPlayer = player
        self._board = board

        if self._aiPlayer == self._board.X_VAL:
            self._humanPlayer = self._board.O_VAL
        else:
            self._humanPlayer = self._board.X_VAL

    def get_opponent(self, player):
        """Returns the opponent of the player passed in the function.

        Args:
            player: Player should be _aiPlayer or _humanPlayer to work
                    as expected.
        """
        if player == self._aiPlayer:
            return self._humanPlayer
        if player == self._humanPlayer:
            return self._aiPlayer

    def alphabeta(self, player, alpha, beta):
        """Returns if computer is winning, losing, or drawing in the current state of the game board.

        It is a recursive function that takes advantage of the runtime tree. It places X_VAL and O_VAL
        alternatively in the game board temporarily until the board is filled to search all possible
        states of the board could be possible. It assigns -1 if computer looses, +1 if computer wins,
        and 0 if it draws, when the board is filled and backtracks to determine a valoue of the initial
        board state.

        Args:
            player: This tells who is the next player in the game. The value has to be _aiPlayer or
                    _humanPlayer for this function to work as expected.
            alpha: The initial value has to be worst negative value a player can have, anything less than -1
            beta: The initial value has to be best positive value a player can have, anything greater than +1

        Returns:
            It returns an integer. -1 if to the board if the initial board state causes
            the computer to loose, +1 if the computer can win, and 0 if the computer can draw.
        """

        # the base case
        if self._board.game_over():
            if self._board.X_won():     # checks if X won
                return -1
            elif self._board.tied():    # checks if game is tied
                return 0
            elif self._board.O_won():   # checks if O won
                return 1

        # The following section of the function recursively calls to create a runtime tree.

        # This loop creates child function calls of the root function call
        # It loops through all the available positions in the current board state
        for move in self._board.available_moves():
            # following line temporarily makes a move and changes the current board set
            self._board.make_move(move, player)
            # recursive call to the function by changing the player each time the call happens
            val = self.alphabeta(self.get_opponent(player), alpha, beta)
            # when each recursive call ends, the following line resets the board to its previous state
            self._board.make_move(move, self._board.NO_VAL)

            # The following code assigns value to its parent state based on the value of end state
            # and who's turn it is in the game. It assumes that human is the smartest player and can
            # always win the game.
            if player == self._aiPlayer:
                if val > alpha:
                    alpha = val
                if alpha >= beta:
                    return beta
            if player == self._humanPlayer:
                if val < beta:
                    beta = val
                if beta <= alpha:
                    return alpha
        if player == self._aiPlayer:
            return alpha
        if player == self._humanPlayer:
            return beta

    def get_move(self, player):
        """Returns the best move computer can play for the current board state.

        This functions temporarily places a O_VAL at every available position
        and calls the recursive function to see if it would win or loose the computer
        chose that temporary position. And then it stores the best moves in a list and returns
        a random choice from the list.

        Args:
            Player: It has to be the value of the computer player, either X_VAL or O_VAL
                depending on who goes first in the game.
        """
        a = -2  # assign a to be a worst negative value
        choices = []    # stires the best choices the computer can have

        # This following two lines is a heuristic approach to return results on a 4X4
        # Tic Tac Toe game board. Since the optimal algorithm is very slow on the 4X4
        # matrix, it is going to return random results for the first 2 rounds of the game.
        if len(self._board.available_moves()) > 11:
            return random.choice(self._board.available_moves())

        # This loop temporarily places a move on the board for computer
        for move in self._board.available_moves():
            self._board.make_move(move, player)
            # The recursive function is called to get the value of new state
            val = self.alphabeta(self.get_opponent(player), -2, 2)
            self._board.make_move(move, self._board.NO_VAL)     # removes the temporary move
            if val > a:     # if the returned value is greater than the worst value
                a = val     # set val as the new worst value
                choices = [move]    # set the move that caused the change to be the only element in the list
            elif val == a:  # else if it is equal to new worst value append it to the list.
                choices.append(move)
        return random.choice(choices)

