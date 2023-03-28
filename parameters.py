class Settings:
    """A class to store all the settings of the Maze"""
    def __init__(self, center=True):
        """Initialize the game's settings"""

        # Screen size
        self.screen_width = 960
        self.screen_height = 600

        # Background Color
        self.bg_color = (50, 50, 50)

        # Square attributes
        self.sq_color_clicked = (10, 10, 10)
        self.sq_color_default = (247, 238, 203)
        self.sq_color_path = (150, 238, 100)
        self.sq_width = 50

        # Board width and height
        self.board_width = 16
        self.board_height = 8
        self.board_topx = self.sq_width
        self.board_topy = self.sq_width

        # Obstacles values
        self.obstacle_low = 3
        self.obstacle_mid = 6
        self.obstacle_high = 9

        # Update screen size to look centered
        if center:
            self.screen_width = (self.board_width + 2) * self.sq_width
            # adding additional space in the bottom for buttons
            self.screen_height = (self.board_height + 3) * self.sq_width


