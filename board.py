import pygame
from parameters import Settings

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

        self.was_clicked = False

    def update(self, top_x, top_y):
        self.rectangle = pygame.Rect(top_x + self.x_pos * self.width,
                                     top_y + self.y_pos * self.width,
                                     settings.sq_width, settings.sq_width)

    def clicked(self):
        if self.was_clicked:
            self.color = self.color_def
        else:
            self.color = self.color_cli

        self.was_clicked = not self.was_clicked

class Board:

    def __init__(self, screen, height=settings.board_height, width=settings.board_width):
        self.screen = screen

        self.height = height
        self.width = width

        self.squares = []

        self.generate()

    def generate(self):
        """Generate the list that holds the squares"""
        self.squares = []
        for i in range(1, self.width + 1):
            for j in range(1, self.height + 1):
                square = Square(i, j, settings.sq_width)
                square.update(settings.board_topx, settings.board_topy)
                self.squares.append(square)

    def show(self):
        """Draw the board on the screen."""
        for square in self.squares:
            pygame.draw.rect(self.screen, square.color, square.rectangle)


