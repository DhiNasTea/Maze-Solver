import pygame
from parameters import Settings
from board import Board
from events import check_button_click

clock = pygame.time.Clock()

settings = Settings()
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))


def run_game():
    # Initialize and set up the screen
    pygame.init()
    pygame.display.set_caption("Race a Maze")

    board = Board(screen, settings.board_height, settings.board_width)


    while True:
        screen.fill(settings.bg_color)

        # Show the board
        board.show()

        check_button_click(board.squares)

        # Refresh screen.
        pygame.display.flip()




run_game()
