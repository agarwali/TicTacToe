## Synopsis
An artificially intelligent Tic Tac Toe gaming application where the computer is unbeatable.

## Code Example
The application is built using python and the user interface is implemented using Python's Tkinter library
Below is the list of files and their purpose:
* Main.py - the main application
* Boards.py - contains classes that creates the game board
* AIntel.py - contains classes with methods that contains artificial intelligence functionaly
* TicTacToeApp.py - contains the page and frame controller for the UI
* Pages.py - contains the templates, i.e. pages and frames to be rendered by the controller
* test.py - contains unit tests for the boards and AI classes
* Main_development.py - can be used for developement purposes, since it runs the game without any UI

## Motivation
The main motivation was to build a game for my final project for my Data Structures course.
The power of recursion was very interesting, so I wanted to explore it in depth. Also, I wanted to challenge myself by learning a new concept not taught in the class. So, I learned about Decision Tress, and use that concept, and the Mini-Max algorithm to make this project.
The desired outcome of this project was to create an artificially intelligent game with and user interface.

## Installation
To run this application you will need Python 2.7 and the following libraries
 * NumPy
 * Tkinter
To run the application with UI you have to run the Main.py file.

## Issues
The game works properly for the 3X3 game board, however it requires enormous amount of computation power to calculate correct moves for the AI in a 4x4 game board.
Possible approaaches are to use a differenc heuristic algorithm



