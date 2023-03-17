import pygame
import sys
def check_button_click(objects):
    """Check the mouse clicks and react appropriately."""
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Check if objects were touched
            for obj in objects:
                if obj.rectangle.collidepoint(mouse_x, mouse_y):
                    obj.clicked()

        if event.type == pygame.QUIT:
            sys.exit()