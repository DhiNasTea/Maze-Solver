import pygame
import sys
from parameters import Event


def check_button_click(objects, bt_dashboard_state):
    """Check the mouse clicks and react appropriately."""
    for event in pygame.event.get():
        curr_event = None
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            curr_event = Event(mouse_x, mouse_y, bt_dashboard_state)

            # Check if any component was clicked clicked
            for obj in objects:
                obj.check_click(curr_event)

            # Check if buttons were clicked

        if event.type == pygame.QUIT:
            sys.exit()
