from typing import List

from enum_utils import SquareState
import sys
from parameters import Settings

# For testing
import pygame

settingss = Settings()

class Vertex:
    def __init__(self, row, column, value=sys.maxsize):
        """

        :type square_state: SquareState
        """
        self.visited = False
        self.row, self.column = row, column

        # Signifying that there's no path to it directly
        self.distance = value

        # Store the vertex with min dist that led to this one
        self.previous = None

        # We are getting the row and column from the vertex number
        # true_row = (num - 1) // self.height  # height == nb. rows
        # true_width = (num - 1) % self.width  # width = nb. columns


class Dijkstra:
    grid: List[List[Vertex]]

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
        self.grid = [[Vertex(row, column) for column in range(self.V)]
                     for row in range(self.V)]
        self.width = board.width
        self.height = board.height

        # Populating each row with the appropriate value
        for vertex in range(self.V):
            # Populate grid
            self.populate(vertex)

    # Returns, vertices neighbours to the one given
    # Tested this, in theory
    def neighbours(self, x_pos, y_pos):
        if not (0 <= x_pos < self.width and 0 <= y_pos < self.height):
            return None

        neighbours = []

        # The maximum number of squares we can return is 8,
        # considering they are all legally reachable

        row_limit = self.height - 1
        column_limit = self.width - 1
        for y in range(max(0, x_pos - 1), min(x_pos + 1, column_limit) + 1):
            for x in range(max(0, y_pos - 1), min(y_pos + 1, row_limit) + 1):
                if x != x_pos or y != y_pos:
                    neighbours.append([x, y])

        return neighbours

    # TODO: test this
    def populate(self, vertex):
        # Get all neighbours
        true_row = vertex // self.width  # width == nb. columns
        true_col = vertex - true_row * self.width
        curr_neighbours = self.neighbours(true_col, true_row)

        # Set distance from this Vertex to neighbours
        self.grid[vertex][vertex].distance = 0

        for neighbour in curr_neighbours:
            row, column = neighbour[0], neighbour[1]

            # Get vertex number from coordinates
            neighbour_vertex = row * self.width + column

            # Get type of the current neighbour
            square = self.board.squares[row][column]

            if square.state == SquareState.obstacle_low:
                self.grid[vertex][neighbour_vertex].distance = settingss.obstacle_low
            elif square.state == SquareState.obstacle_mid:
                self.grid[vertex][neighbour_vertex].distance = settingss.obstacle_mid
            elif square.state == SquareState.obstacle_high:
                self.grid[vertex][neighbour_vertex].distance = settingss.obstacle_high
            elif square.state == SquareState.wall:
                self.grid[vertex][neighbour_vertex].distance = sys.maxsize
            else:
                self.grid[vertex][neighbour_vertex].distance = 1

    def minDistance(self, dist, spt_set):

        # Initialize minimum distance for next node
        min_start = sys.maxsize

        min_index = -1

        # Search not nearest vertex not in the
        # shortest path tree
        for v in range(self.V):
            if dist[v] < min_start and spt_set[v] == False:
                min_start = dist[v]
                min_index = v

        return min_index

    def printSolution(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(node, "\t\t", dist[node])

    def solve(self, start):
        """

        :type start: int
        vertex number of starting position
        """
        dist = [sys.maxsize] * self.V
        dist[start] = 0
        VisitedSet = [False] * self.V

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minDistance(dist, VisitedSet)

            # Put the minimum distance vertex in the
            # shortest path tree
            VisitedSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.V):
                if (0 < self.grid[u][v].distance < sys.maxsize and
                        VisitedSet[v] == False and
                        dist[v] > dist[u] + self.grid[u][v].distance):
                    dist[v] = dist[u] + self.grid[u][v].distance
                    self.grid[v][0].previous = u

        self.printSolution(dist)

    def __str__(self):
        ret_str = "Printing the distance matrix:\n"
        for row in self.grid:
            string = "\t["
            for vertex in row:
                if string != "\t[":
                    string += ", "
                string += str(vertex.distance)
            string += "\t]\n"
            ret_str += string
        return ret_str


# Testing
"""
if __name__ == "__main__":
    settingss = Settings()
    screen = pygame.display.set_mode((settingss.screen_width, settingss.screen_height))
    boardd = Board(screen, 3, 3)

    algo1 = Dijkstra(boardd, settingss)

    print("should be 8, actual: " + str(len(algo1.neighbours(1, 1))))
    print("should be 5, actual: " + str(len(algo1.neighbours(0, 1))))
    print("should be 3, actual: " + str(len(algo1.neighbours(2, 0))))

    print(algo1)
    algo1.solve(4)
"""

