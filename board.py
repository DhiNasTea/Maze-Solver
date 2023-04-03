from typing import List, Any

import pygame
from parameters import Settings
from enum_utils import *
from parameters import Event
from algos import Dijkstra

settings = Settings()

class Square:

    def __init__(self, x, y, width, color_def=settings.sq_color_default, color_cli=settings.sq_color_clicked):
        """
        :type x: int => the column starting at 1
        :type y: int => the row starting at 1
        """
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

    """
    We are assuming the logic that prevents multiple squares
    from being a type that should be unique is implemented in the caller
    """
    def on_click(self, bt_dashboard_state):
        # TODO: have a function that changes the squarestate
        if bt_dashboard_state == SelectionState.choosing_nothing:
            return

        # We are forcing squares back to default
        elif bt_dashboard_state == SelectionState.choosing_default:
            self.state = SquareState.default
            self.color = settings.sq_color_default

        # We are selecting the starting point
        elif bt_dashboard_state == SelectionState.choosing_start:
            # We are un-selecting the start square
            if self.state == SquareState.start:
                self.state = SquareState.default
                self.color = settings.sq_color_default
            # We are selecting a start square
            else:
                self.state = SquareState.start
                self.color = settings.sq_color_start

        elif bt_dashboard_state == SelectionState.choosing_end:
            # We are un-selecting the end square
            if self.state == SquareState.end:
                self.state = SquareState.default
                self.color = settings.sq_color_default
            # We are selecting an end square
            else:
                self.state = SquareState.end
                self.color = settings.sq_color_end

        elif bt_dashboard_state == SelectionState.choosing_obstacle_mid:
            # We are un-selecting an obstacle
            if self.state == SquareState.obstacle_mid:
                self.state = SquareState.default
                self.color = settings.sq_color_default
            # We are selecting a mid obstacle
            else:
                self.state = SquareState.obstacle_mid
                self.color = settings.sq_color_obstacle_mid
        elif bt_dashboard_state == SelectionState.choosing_wall:
            # We are un-selecting a wall
            if self.state == SquareState.wall:
                self.state = SquareState.default
                self.color = settings.sq_color_default
            # We are selecting a wall
            else:
                self.state = SquareState.wall
                self.color = settings.sq_color_wall
        elif bt_dashboard_state == SelectionState.choosing_final_path:
            self.state = SquareState.path
            self.color = settings.sq_color_path
        # Unknown
        else:
            print("Unknown SelectionState in Button.onClick()")


class Board:

    def __init__(self, screen, width=settings.board_width, height=settings.board_height):
        self.screen = screen

        self.height = height
        self.width = width

        self.curr_start_square, self.curr_end_square = None, None

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

    def clear_square(self, row, column):
        self.squares[row][column].on_click(SelectionState.choosing_default)

    def highlight_path(self, vertex):
        column = vertex % self.width
        row = vertex // self.width

        self.squares[row][column].on_click(SelectionState.choosing_final_path)

    def show(self):
        """Draw the board on the screen."""
        for row in self.squares:
            for square in row:
                pygame.draw.rect(self.screen, square.color, square.rectangle)

    def check_click(self, event):
        """Determine if a square was clicked on
        :type event: Event
        """
        for row in self.squares:
            for square in row:
                if square.rectangle.collidepoint(event.x_pos, event.y_pos):
                    # Making sure there's only one start square
                    if event.bt_state == SelectionState.choosing_start:
                        if self.curr_start_square is not None and self.curr_start_square.state == SquareState.start:
                            self.clear_square(self.curr_start_square.y_pos, self.curr_start_square.x_pos)
                        self.curr_start_square = square

                    # Making sure there's only one end square
                    elif event.bt_state == SelectionState.choosing_end:
                        if self.curr_end_square is not None and self.curr_end_square.state == SquareState.end:
                            self.clear_square(self.curr_end_square.y_pos, self.curr_end_square.x_pos)
                        self.curr_end_square = square

                    square.on_click(event.bt_state)
                    return

    def solve(self):
        vertex_start = self.curr_start_square.x_pos + self.width * self.curr_start_square.y_pos
        algo = Dijkstra(self, settings)
        algo.solve(vertex_start)

        # Draw the path :)
        vertex_end = self.curr_end_square.x_pos + self.width * self.curr_end_square.y_pos

        curr_vertex = algo.grid[vertex_end][0]
        path = [vertex_end]
        while curr_vertex.previous is not None:
            path.append(curr_vertex.previous)
            curr_vertex = algo.grid[curr_vertex.previous][0]

        print(path)

        # We will make all the square in between green
        if len(path) > 2:
            path = path[1:-1] # removing the start and end vertices

            for vertex in path:
                self.highlight_path(vertex)
