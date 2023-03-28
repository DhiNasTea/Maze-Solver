import pygame
from parameters import Settings
from board import Board
from events import check_button_click
from enum_utils import *


clock = pygame.time.Clock()

settings = Settings()
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

global game_state
game_state = SelectionState.choosing_nothing

def run_game():
    global game_state
    # Initialize and set up the screen
    pygame.init()
    pygame.display.set_caption("Race a Maze")

    # Array of components
    components = []

    board = Board(screen, settings.board_width, settings.board_height)
    components.append(board)


    while True:
        screen.fill(settings.bg_color)

        # Show the board
        board.show()

        check_button_click(components)

        # Refresh screen.
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60



run_game()
