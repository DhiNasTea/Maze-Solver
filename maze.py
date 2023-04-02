import pygame
from parameters import Settings
from board import Board
from events import check_button_click
from buttons import ButtonGroup
from enum_utils import *


clock = pygame.time.Clock()

settings = Settings()
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))



def run_game():

    # Initialize and set up the screen
    pygame.init()
    pygame.display.set_caption("Race a Maze")

    # Array of components
    components = []

    board = Board(screen, settings.board_width, settings.board_height)
    components.append(board)

    button_dashboard = ButtonGroup(screen)
    components.append(button_dashboard)

    while True:
        screen.fill(settings.bg_color)

        # Show the board
        board.show()

        # Show the buttons
        button_dashboard.show()

        # Check for mouse clicks
        check_button_click(components, button_dashboard.selection_state)

        # Check if the maze is to be solved
        if button_dashboard.selection_state == SelectionState.choosing_final_path:
            board.solve()
            button_dashboard.selection_state = SelectionState.choosing_nothing
        # Restarting the board
        elif button_dashboard.selection_state == SelectionState.choosing_reset:
            components = []

            board = Board(screen, settings.board_width, settings.board_height)
            components.append(board)

            button_dashboard = ButtonGroup(screen)
            components.append(button_dashboard)

            button_dashboard.selection_state = SelectionState.choosing_nothing

        # Refresh screen.
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60



run_game()
