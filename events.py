import pygame
import sys


def check_button_click(objects):
    global game_state
    """Check the mouse clicks and react appropriately."""
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Check if squares were clicked
            for obj in objects:
                obj.check_click(game_state)

            # Check if buttons were clicked

        if event.type == pygame.QUIT:
            sys.exit()