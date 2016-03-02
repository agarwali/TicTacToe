from tictactoe import *
from Boards import TTT_Board
from Tkinter import Tk
from GUI import GUI

def main():

    print board.board
    while not board.game_over():
        player_move_x = int(raw_input("Next X Move: "))
        player_move_y = int(raw_input("Next Y Move: "))

        player_move = (player_move_x, player_move_y)
        if not player_move in board.available_moves():
            continue
        board.make_move(player_move, new_ai._humanPlayer)
        print board.board
        computer_move = new_ai.get_move(new_ai._aiPlayer)
        board.make_move(computer_move, new_ai._aiPlayer)
        new_GUI.update()
        print board.board

        if board.game_over():
            break

    print "winner is", board.winner()
    root.mainloop()
    print new_GUI.user_move

main()