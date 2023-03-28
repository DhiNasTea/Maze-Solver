from enum_utils import SquareState
import sys
from parameters import Settings

# For testing
import pygame
from board import Board

class Vertex:
    def __init__(self, square_state):
        """

        :type square_state: SquareState
        """
        self.visited = False

        # Signifying that there's no path to it directly
        self.distance = None

        # Store the vertex with min dist that led to this one
        self.previous = None

        # We are getting the row and column from the vertex number
        # true_row = (num - 1) // self.height  # height == nb. rows
        # true_width = (num - 1) % self.width  # width = nb. columns

class Dijkstra:
    def __init__(self, board, settings):
        """

        :type settings: Settings
        :type board: Board
        """
        self.settings = settings
        self.board = board

        self.V = board.width * board.height

        # Vertical axis is the starting Vertex and the
        # row associated to it is the distance from that
        # to the other ones
        self.grid = [[sys.maxsize for column in range(self.V)]
                     for row in range(self.V)]
        self.width = board.width
        self.height = board.height

        # Populating each row with the appropriate value
        for vertex in range(self.V):
            # Populate grid
            self.populate(vertex)



    # Returns, vertices neighbours to the one given
    def neighbours(self, x_pos, y_pos):
        if not (0 <= x_pos < self.width and 0 <= y_pos < self.height):
            return None

        neighbours = []

        # The maximum number of squares we can return is 8,
        # considering they are all legally reachable

        row_limit = self.height - 1
        column_limit = self.width - 1
        for x in range(max(0, x_pos - 1), min(x_pos + 1, row_limit) + 1):
            for y in range(max(0, y_pos - 1), min(y_pos + 1, column_limit) + 1):
                if x != x_pos or y != y_pos:
                    neighbours.append([x, y])

        return neighbours

    def populate(self, vertex):
        # Get all neighbours
        true_row = vertex // self.height  # height == nb. rows
        true_width = vertex % self.width  # width = nb. columns
        curr_neighbours = self.neighbours(true_row, true_width)

        # Set distance from this Vertex to neighbours
        self.grid[vertex][vertex] = 0

        for neighbour in curr_neighbours:
            row, column = neighbour[0], neighbour[1]

            # Get vertex number from coordinates
            neighbour_vertex = row * self.width + column

            # Get type of the current neighbour
            square = self.board[row][column]

            if square.state == SquareState.obstacle_low:
                self.grid[vertex][neighbour_vertex] = settingss.obstacle_low
            elif square.state == SquareState.obstacle_mid:
                self.grid[vertex][neighbour_vertex] = settingss.obstacle_mid
            elif square.state == SquareState.obstacle_high:
                self.grid[vertex][neighbour_vertex] = settingss.obstacle_high
            elif square.state == SquareState.wall:
                self.grid[vertex][neighbour_vertex] = sys.maxsize
            else:
                self.grid[vertex][neighbour_vertex] = 1



# Testing
if __name__ == "__main__":
    settingss = Settings()
    screen = pygame.display.set_mode((settingss.screen_width, settingss.screen_height))
    boardd = Board(screen, 3, 3)

    algo1 = Dijkstra(boardd)

    print("should be 8, actual: " + str(len(algo1.neighbours(1, 1))))
    print("should be 5, actual: " + str(len(algo1.neighbours(0, 1))))
    print("should be 3, actual: " + str(len(algo1.neighbours(2, 0))))
