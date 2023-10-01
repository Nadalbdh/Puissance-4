# Connect Four Game

This repository contains Python code for a Connect Four game implemented using Pygame and NumPy. Connect Four is a classic two-player connection game in which the players take turns dropping colored discs from the top into a vertically suspended grid. The objective of the game is to be the first to form a horizontal, vertical, or diagonal line of four of one's discs.

## Introduction

Connect Four is a popular strategy game that can be played by two players. The game provides a grid where players take turns dropping their discs (represented by colors) into the grid columns. The discs fall to the lowest available position within the column. The player who first forms a sequence of four discs in a row (horizontally, vertically, or diagonally) wins the game.

## Code Description

The code in this repository consists of several components:

### Grille Class

The `Grille` class represents the game board. It includes methods for checking the validity of a move, placing a disc, checking for a win, and more.

### Fenetre Class

The `Fenetre` class manages the graphical user interface (GUI) of the game. It uses Pygame to display the game grid and handle user interactions.

### Main Game Loop

The `main` function initializes the game, handles player turns, and checks for a win or draw.

## How to Play

1. Run the script to start the Connect Four game.
2. Two players take turns clicking on the columns where they want to drop their discs.
3. The game will display the board with each player's discs.
4. The first player to form a sequence of four discs in a row wins the game.
5. If the board becomes full without a winner, the game ends in a draw.
