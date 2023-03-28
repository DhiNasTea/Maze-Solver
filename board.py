import pygame
from parameters import Settings
from enum_utils import *

settings = Settings()

class Square:
    def __init__(self, x, y, width, color_def=settings.sq_color_default, color_cli=settings.sq_color_clicked):
        self.x_pos = x - 1
        self.y_pos = y - 1
        self.width = width
        self.color_def = color_def
        self.color_cli = color_cli

        self.color = self.color_def

        self.rectangle = pygame.Rect(0, 0, self.width, self.width)

        self.state = SquareState.default

    def update(self, top_x, top_y):
        self.rectangle = pygame.Rect(top_x + self.x_pos * self.width,
                                     top_y + self.y_pos * self.width,
                                     settings.sq_width, settings.sq_width)

    def on_click(self):
        global game_state
        # Nothing should happen on click
        if game_state == SelectionState.choosing_nothing:
            return

        # We are selecting the starting point
        if self.state == SquareState.selected:
            self.state = SquareState.default
            self.color = self.color_def
        elif self.state == SquareState.default:
            self.state = SquareState.selected
            self.color = self.color_cli
        else:
            self.state = SquareState.default
            self.color = self.color_def

class Board:

    def __init__(self, screen, width=settings.board_width, height=settings.board_height):
        self.screen = screen

        self.height = height
        self.width = width

        # To iterate over the squares, the first
        # for loop will give us horizontal rows
        self.squares = []

        self.generate()

    def generate(self):
        """Generate the list that holds the squares"""
        self.squares = []
        for y in range(1, self.height + 1):     # y-axis
            row = []
            for x in range(1, self.width + 1):  # x-axis
                square = Square(x, y, settings.sq_width)
                square.update(settings.board_topx, settings.board_topy)
                row.append(square)
            self.squares.append(row)

    def show(self):
        """Draw the board on the screen."""
        for row in self.squares:
            for square in row:
                pygame.draw.rect(self.screen, square.color, square.rectangle)

    def check_click(self, x_pos, y_pos):
        """Determine if a square was clicked on"""
        global game_state
        for row in self.squares:
            for square in row:
                if square.collidepoint(x_pos, y_pos):
                    square.on_click(game_state)
                    return
