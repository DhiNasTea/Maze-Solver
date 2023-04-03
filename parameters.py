from enum_utils import SelectionState


class Settings:
    """A class to store all the settings of the Maze"""
    def __init__(self, center=True):
        """Initialize the game's settings"""

        # Screen size
        self.screen_width = 960
        self.screen_height = 700

        # Colors
        self.color_black = (10, 10, 10)
        self.light_beige = (247, 238, 203)
        self.beige = (255, 204, 153)
        self.green_path = (150, 238, 100)
        self.dark_grey = (50, 50, 50)
        self.burgundy = (128, 0, 32)
        self.midnight_blue = (25, 25, 112)
        self.cool_grey = (140, 146, 172)
        self.gray = (128, 128, 128)
        self.pewter = (233, 234, 236)

        # Background Color
        self.bg_color = self.dark_grey

        # Square attributes
        self.sq_color_clicked = self.color_black
        self.sq_color_default = self.light_beige
        self.sq_color_start = self.midnight_blue
        self.sq_color_end = self.burgundy
        self.sq_color_obstacle_high= self.cool_grey
        self.sq_color_obstacle_mid = self.gray
        self.sq_color_obstacle_low = self.pewter
        self.sq_color_path = self.green_path
        self.sq_color_wall = self.color_black
        self.sq_width = 50

        # Board width and height
        self.board_width = 17
        self.board_height = 8
        self.board_topx = self.sq_width
        self.board_topy = self.sq_width

        # Buttons
        self.bt_width = 100
        self.bt_height = 40
        self.bt_color = self.beige
        self.bt_text_color = (30, 30, 30)
        self.bt_start_x = self.sq_width
        self.bt_start_y = (1 + self.board_height) * self.sq_width + 20  # +20 to give space between button and board
        self.bt_x_gap = 50
        self.bt_y_gap = None

        # Obstacles values
        self.obstacle_low = 3
        self.obstacle_mid = 6
        self.obstacle_high = 9

        # Update screen size to look centered
        if center:
            self.screen_width = (self.board_width + 2) * self.sq_width
            # adding additional space in the bottom for buttons
            self.screen_height = (self.board_height + 3) * self.sq_width

class Event:
    """Store relvant information about a game event"""
    # TODO: abstract this to more than a mouse click event
    def __init__(self, x_pos, y_pos, bt_state):
        """

        :type bt_state: SelectionState
        """
        self.x_pos, self.y_pos = x_pos, y_pos
        self.bt_state = bt_state



