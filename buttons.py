from typing import List

import pygame
from enum_utils import ButtonState, SelectionState, button_state_to_selection_state
from parameters import Settings, Event

glob_settings = Settings()

class Button:
    # Static variable to make sure one button is selected at a time
    # Could be used to color them later on
    button_selected = False
    current_button = None

    def __init__(self, text, settings, screen, button_type, x=0, y=0):
        """

        :type button_type: ButtonState
        """
        self.screen = screen
        self.settings = settings
        self.button_type = button_type
        self.text = text

        self.font = pygame.font.SysFont(None, 25)

        self.selected = False

        self.x = x
        self.y = y
        self.rectangle = pygame.Rect(self.x, self.y, self.settings.bt_width, self.settings.bt_height)

        self.text_font = self.font.render(self.text, True, self.settings.bt_text_color)
        self.text_font_rect = self.text_font.get_rect()
        self.text_font_rect.center = self.rectangle.center

        self.text = text

    def update(self, x, y):
        self.x, self.y = x, y
        self.rectangle = pygame.Rect(self.x, self.y, self.settings.bt_width, self.settings.bt_height)

        # Update the text
        self.text_font_rect.center = self.rectangle.center

    def center(self, center_x, center_y):
        # TODO: consider self.x and self.y as they won't reflect the actual position
        self.rectangle.centerx = center_x
        self.rectangle.centery = center_y

        # Update the text
        self.text_font_rect.center = self.rectangle.center

    def show(self):
        pygame.draw.rect(self.screen, self.settings.bt_color, self.rectangle)

        # Show the text
        self.screen.blit(self.text_font, self.text_font_rect)

    def on_click(self):
        if self.selected:
            Button.button_selected = False
            Button.current_button = None
            self.selected = False

        elif not Button.button_selected:
            Button.button_selected = True
            Button.current_button = self
            self.selected = True

class ButtonGroup:
    buttons: List[Button]

    def __init__(self, screen, group="default"):
        self.screen = screen
        self.group = group

        self.selection_state = SelectionState.choosing_nothing

        self.buttons = []

        if self.group == "default":
            curr_x, curr_y = 0, 0
            curr_x = glob_settings.bt_start_x
            curr_y = glob_settings.bt_start_y

            self.buttons.append(Button("Start", glob_settings, self.screen, ButtonState.button_start, curr_x, curr_y))
            curr_x += glob_settings.bt_width + glob_settings.bt_x_gap

            self.buttons.append(Button("End", glob_settings, self.screen, ButtonState.button_end, curr_x, curr_y))
            curr_x += glob_settings.bt_width + glob_settings.bt_x_gap

            self.buttons.append(Button("Obstacles", glob_settings, self.screen, ButtonState.button_obstacles, curr_x, curr_y))
            curr_x += glob_settings.bt_width + glob_settings.bt_x_gap

            self.buttons.append(Button("Find Path", glob_settings, self.screen, ButtonState.button_find_path, curr_x, curr_y))
            curr_x += glob_settings.bt_width + glob_settings.bt_x_gap

            self.buttons.append(Button("Reset", glob_settings, self.screen, ButtonState.button_reset, curr_x, curr_y))

    def show(self):
        for button in self.buttons:
            button.show()

    def check_click(self, event):
        """

        :type event: Event
        """
        for button in self.buttons:
            if button.rectangle.collidepoint(event.x_pos, event.y_pos):
                self.selection_state = button_state_to_selection_state(button.button_type)


