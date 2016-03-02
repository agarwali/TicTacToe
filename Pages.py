######################################################################################################################
# File Name: Pages.py
# Purpose: It contains the page classes that are essentially frames to change the window
#           controlled by the TicApp Class in the module TicTacToeApp.py
# Author: Ishwar Agarwal
# Last Date Modified: 12/11/2015
# Acknowledgements: The idea for updating the Tic Tac Toe game board was obtained obtained from
# https://www.leaseweb.com/labs/2013/12/python-tictactoe-tk-minimax-ai/?utm_source=leaseweblabs.com&utm_medium=referral&utm_campaign=redirect
#####################################################################################################################

from Tkinter import Tk, Button, Label, Frame, PhotoImage
from tkFont import Font
from Boards import TicTacToe
from AIntel import AI

# the following set of text attributes are to be reused
TITLE_FONT = ("Helvetica", 18, "bold")
SUB_TITLE_FONT = ("Helvetica", 8)
BIG_BUTTON_FONT = ("Helvetica", 12)
X_O_FONT = ("Helvetica", 32)

board_size = 3
single_player = None
first_player = None


class StartPage(Frame):
    """Contains everything to be shown on start page
    """
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        label = Label(self, text="Tic Tac Toe", font=("Helvetica", 24, "bold"))
        label.pack(side="top", fill="x", pady=0)
        label = Label(self, text="The ultimate Tic Tac Toe Game.", font=SUB_TITLE_FONT)
        label.pack(side="top", fill="x", pady=5)
        label = Label(self, text="", font=SUB_TITLE_FONT)
        label.pack(side="top", fill="x", pady=20)

        button1 = Button(self, text="Single Player", width=20, height=2, font=BIG_BUTTON_FONT,
                         command=lambda: self.select_player('single'))
        button2 = Button(self, text="Multi Player", width=20, height=2, font=BIG_BUTTON_FONT,
                         command=lambda: self.select_player('multi'))
        button3 = Button(self, text="Instructions", width=20, height=2, font=BIG_BUTTON_FONT,
                         command=lambda: controller.show_frame(Instructions))
        button4 = Button(self, text="Quit", width=20, height=2, font=BIG_BUTTON_FONT,
                         command=lambda: self.close_window())
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()

    def select_player(self, val):
        global single_player
        if val == 'single':
            single_player = True
        else:
            single_player = False
        self.controller.show_frame(BoardSize)

    def close_window(self):
        self.quit()


class BoardSize(Frame):
    """Contains everything to be shown on choosing board page
    """
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Choose a Board Size", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        label = Label(self, text="", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=20)

        button = Button(self, text="3 X 3", width=20, height=2, font=BIG_BUTTON_FONT,
                        command=lambda: self.set_size(3))
        button.pack()
        button = Button(self, text="4 X 4", width=20, height=2, font=BIG_BUTTON_FONT,
                        command=lambda: self.set_size(4))
        button.pack()
        button = Button(self, text="Go Back", width=20, height=2, font=BIG_BUTTON_FONT,
                        command=lambda: controller.show_frame(StartPage))
        button.pack()

    def set_size(self, val):
        global single_player
        if val == 3 and single_player == True:
            self.controller.show_frame(Ai3X3)
        if val == 4 and single_player == True:
            self.controller.show_frame(Ai4X4)
        if val == 3 and single_player == False:
            self.controller.show_frame(Multi3X3)
        if val == 4 and single_player == False:
            self.controller.show_frame(Multi4X4)


class Instructions(Frame):
    """Contains everything to show on Instructions page
    """
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Instructions", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        label = Label(self, text="You play on a 3X3  or 4X4 game board.\n"
                                 "The object of Tic Tac Toe is to get\n "
                                 "three in a row, column or diagonal in a \n"
                                 "3X3 Tic Tac Toe board. While you have to \n"
                                 "get four in a row, column or diagonal in a \n"
                                 "4X4 Tic Tac Toe board. The first player is \n"
                                 "known as X and the second is O.\n "
                                 "Players alternate placing Xs and Os on the \n"
                                 "game board until either opponent has \n"
                                 "won or all square are filled.", font=SUB_TITLE_FONT)
        label.pack(side="top", fill="x", pady=20)
        button = Button(self, text="Go to the Start page",
                        command=lambda: controller.show_frame(StartPage))
        button.pack()




class Ai3X3(Frame):
    """Contains everything to show on a 3X3 single player game board page
    """
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.size = None
        self.first_player = None
        self._board = TicTacToe(3)
        self.new_ai = AI('O', self._board)
        self.buttons = {}

        label = Label(self, text="Tic Tac Toe", font=TITLE_FONT)
        label.grid(row=0, column=0, columnspan=3)
        self.status = Label(self, text='Your Turn')
        self.status.grid(row=1, column=0, columnspan=3)
        for x in range(self._board.size):
            for y in range(self._board.size):
                handler = lambda x=x,y=y: self.move(x,y)
                button = Button(self, command=handler, font=X_O_FONT, width=5, height=2)
                button.grid(row=x+2, column=y)
                self.buttons[x,y] = button
        handler = lambda: self.reset()
        button = Button(self, text='Reset', command=handler)
        button.grid(row=self._board.size+3, column=2,  sticky="WE")
        button = Button(self, text="Go to the start page",
                        command=lambda: self.start_and_reset())
        button.grid(row=self._board.size+3, column=0, columnspan=2, sticky="WE")
        self.update()

    def start_and_reset(self):
        self.reset()
        self.controller.show_frame(StartPage)

    def reset(self):
        self._board = TicTacToe(3)
        self.new_ai = AI('O', self._board)
        self.update()

    def move(self, x, y):
        self.config(cursor="watch")
        self.update()
        self._board.make_move((x,y),self.new_ai._humanPlayer)
        # print self._board.board
        self.update()
        if not self._board.game_over():
            self.status['text'] = 'Please wait..'
            computer_move = self.new_ai.get_move(self.new_ai._aiPlayer)
            self._board.make_move(computer_move, self.new_ai._aiPlayer)
            self.update()
        self.config(cursor="")

    def update(self):
        for x in range(self._board.size):
            for y in range(self._board.size):
                text = self._board.get_value(x,y)
                self.buttons[x,y]['text'] = text
                self.buttons[x,y]['disabledforeground'] = 'black'
                if text == self._board.NO_VAL:
                    self.buttons[x,y]['state'] = 'normal'
                else:
                    self.buttons[x,y]['state'] = 'disabled'

        if self._board.game_over():
            winner = self._board.winner()
            if winner == self.new_ai._humanPlayer:
                win_msg = 'You won'
            elif winner == self.new_ai._aiPlayer:
                win_msg = 'Computer won'
            elif winner == None:
                win_msg = 'Draw'

            # print win_msg
            self.status ['text'] = win_msg
            # self.app.update()
            for x,y in self.buttons:
                self.buttons[x,y]['state'] = 'disabled'

            if not self._board.tied():
                for (x,y) in self._board.winning_combos:
                    self.buttons[x,y]['disabledforeground'] = 'red'
                    self.status ['text'] = win_msg
        else:
            self.status ['text'] = 'Your turn'


class Multi3X3(Frame):
    """Contains everything to show on a 3X3 multi player game board page
    """
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self._board = TicTacToe(board_size)
        self.startplayer = self._board.X_VAL
        self.currentPlayer = self.startplayer
        self.buttons = {}

        label = Label(self, text="Tic Tac Toe", font=TITLE_FONT)
        label.grid(row=0, column=0, columnspan=3)
        self.status = Label(self, text='Player ' + self.currentPlayer + "'s Turn")
        self.status.grid(row=1, column=0, columnspan=3, sticky="WE")
        for x in range(self._board.size):
            for y in range(self._board.size):
                handler = lambda x=x,y=y: self.move(x,y)
                button = Button(self, command=handler, font=X_O_FONT, width=5, height=2)
                button.grid(row=x+2, column=y)
                self.buttons[x,y] = button
        handler = lambda: self.reset()
        button = Button(self, text='Reset', command=handler)
        button.grid(row=self._board.size+3, column=2,  sticky="WE")
        button = Button(self, text="Go to the start page",
                           command=lambda: self.start_and_reset())
        button.grid(row=self._board.size+3, column=0, columnspan=2, sticky="WE")
        self.update()

    def start_and_reset(self):
        self.reset()
        self.controller.show_frame(StartPage)

    def reset(self):
        self._board = TicTacToe(3)
        self.startplayer = self._board.get_opponent(self.startplayer)
        self.update()

    def move(self,x,y):
        self.config(cursor="watch")
        self._board.make_move((x,y),self.currentPlayer)
        self.currentPlayer = self._board.get_opponent(self.currentPlayer)
        self.update()
        self.config(cursor="")

    def update(self):
        for x in range(self._board.size):
            for y in range(self._board.size):
                text = self._board.get_value(x,y)
                self.buttons[x,y]['text'] = text
                self.buttons[x,y]['disabledforeground'] = 'black'
                if text == self._board.NO_VAL:
                    self.buttons[x,y]['state'] = 'normal'
                else:
                    self.buttons[x,y]['state'] = 'disabled'

        if self._board.game_over():
            winner = self._board.winner()
            if winner == self._board.X_VAL:
                win_msg = 'Player X won'
            elif winner == self._board.O_VAL:
                win_msg = 'Player O won'
            elif winner == None:
                win_msg = 'Draw'

            # print win_msg
            self.status['text'] = win_msg
            # self.app.update()
            for x,y in self.buttons:
                self.buttons[x,y]['state'] = 'disabled'

            if not self._board.tied():
                for (x,y) in self._board.winning_combos:
                    self.buttons[x,y]['disabledforeground'] = 'red'
                    self.status ['text'] = win_msg

        else:
            self.status['text'] = 'Player ' + self.currentPlayer + "'s Turn"


class Ai4X4(Frame):
    """Contains everything to show on a 4X4 single player game board page
    """
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.size = None
        self.first_player = None
        self._board = TicTacToe(4)
        self.new_ai = AI('O', self._board)
        self.buttons = {}

        # status = lambda: self.get_status()
        label = Label(self, text="Tic Tac Toe", font=TITLE_FONT)
        label.grid(row=0, column=0, columnspan=4)
        self.status = Label(self, text='Your Turn')
        self.status.grid(row=1, column=0, columnspan=self._board.size, sticky="WE")
        for x in range(self._board.size):
            for y in range(self._board.size):
                handler = lambda x=x,y=y: self.move(x,y)
                button = Button(self, command=handler, font=X_O_FONT, width=3, height=1)
                button.grid(row=x+2, column=y)
                self.buttons[x,y] = button
        handler = lambda: self.reset()
        button = Button(self, text='Reset', command=handler)
        button.grid(row=self._board.size+3, column=2, columnspan=2, sticky="WE")
        button = Button(self, text="Go to the start page",
                        command=lambda: self.start_and_reset())
        button.grid(row=self._board.size+3, column=0, columnspan=2, sticky="WE")
        label = Label(self, text="The 4X4 Single Player is a beta version. It might take computer\n"
                                 "some time to play. We appreciate your patience.", font=SUB_TITLE_FONT)
        label.grid(row=8, column=0, columnspan=4)
        self.update()

    def start_and_reset(self):
        self.reset()
        self.controller.show_frame(StartPage)

    def reset(self):
        self._board = TicTacToe(4)
        self.new_ai = AI('O', self._board)
        self.update()

    def move(self,x,y):
        self.config(cursor="watch")
        self.update()
        self._board.make_move((x,y),self.new_ai._humanPlayer)
        # print self._board.board
        self.update()
        if not self._board.game_over():
            self.status['text'] = 'Please wait..'
            self.update()
            computer_move = self.new_ai.get_move(self.new_ai._aiPlayer)
            self._board.make_move(computer_move, self.new_ai._aiPlayer)
            # print self._board.board
            self.update()
            self.status ['text'] = 'Your turn'
        self.config(cursor="")

    def update(self):
        for x in range(self._board.size):
            for y in range(self._board.size):
                text = self._board.get_value(x,y)
                self.buttons[x,y]['text'] = text
                self.buttons[x,y]['disabledforeground'] = 'black'
                if text == self._board.NO_VAL:
                    self.buttons[x,y]['state'] = 'normal'
                else:
                    self.buttons[x,y]['state'] = 'disabled'

        if self._board.game_over():
            winner = self._board.winner()
            if winner == self.new_ai._humanPlayer:
                win_msg = 'You won'
            elif winner == self.new_ai._aiPlayer:
                win_msg = 'Computer won'
            elif winner == None:
                win_msg = 'Draw'

            # print win_msg
            self.status ['text'] = win_msg
            # self.app.update()
            for x,y in self.buttons:
                self.buttons[x,y]['state'] = 'disabled'

            if not self._board.tied():
                for (x,y) in self._board.winning_combos:
                    self.buttons[x,y]['disabledforeground'] = 'red'
                    self.status ['text'] = win_msg


class Multi4X4(Frame):
    """Contains everything to show on a 4X4 multi player game board page
    """
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self._board = TicTacToe(4)
        self.startplayer = self._board.X_VAL
        self.currentPlayer = self.startplayer
        self.buttons = {}


        # status = lambda: self.get_status()
        label = Label(self, text="Tic Tac Toe", font=TITLE_FONT)
        label.grid(row=0, column=0, columnspan=4)
        self.status = Label(self, text='Your Turn')
        self.status.grid(row=1, column=0, columnspan=self._board.size, sticky="WE")
        for x in range(self._board.size):
            for y in range(self._board.size):
                handler = lambda x=x,y=y: self.move(x,y)
                button = Button(self, command=handler, font=X_O_FONT, width=3, height=1)
                button.grid(row=x+2, column=y)
                self.buttons[x,y] = button
        handler = lambda: self.reset()
        button = Button(self, text='Reset', command=handler)
        button.grid(row=self._board.size+3, column=2, columnspan=2, sticky="WE")
        button = Button(self, text="Go to the start page",
                           command=lambda: self.start_and_reset())
        button.grid(row=self._board.size+3, column=0, columnspan=2, sticky="WE")
        self.update()

    def start_and_reset(self):
        self.reset()
        self.controller.show_frame(StartPage)

    def reset(self):
        self._board = TicTacToe(4)
        self.startplayer = self._board.get_opponent(self.startplayer)
        self.update()

    def move(self,x,y):
        self.config(cursor="watch")
        self._board.make_move((x,y),self.currentPlayer)
        self.currentPlayer = self._board.get_opponent(self.currentPlayer)
        self.update()
        self.config(cursor="")

    def update(self):
        for x in range(self._board.size):
            for y in range(self._board.size):
                text = self._board.get_value(x,y)
                self.buttons[x,y]['text'] = text
                self.buttons[x,y]['disabledforeground'] = 'black'
                if text == self._board.NO_VAL:
                    self.buttons[x,y]['state'] = 'normal'
                else:
                    self.buttons[x,y]['state'] = 'disabled'

        if self._board.game_over():
            winner = self._board.winner()
            if winner == self._board.X_VAL:
                win_msg = 'Player X won'
            elif winner == self._board.O_VAL:
                win_msg = 'Player O won'
            elif winner == None:
                win_msg = 'Draw'

            # print win_msg
            self.status ['text'] = win_msg
            # self.app.update()
            for x,y in self.buttons:
                self.buttons[x,y]['state'] = 'disabled'

            if not self._board.tied():
                for (x,y) in self._board.winning_combos:
                    self.buttons[x,y]['disabledforeground'] = 'red'
                    self.status ['text'] = win_msg
        else:
            self.status ['text'] = 'Player ' + self.currentPlayer + "'s Turn"