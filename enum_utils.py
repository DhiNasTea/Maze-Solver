class SquareState:
    """Enum for all the possible states for a square in the board"""

    # All squares start as default
    default = 1

    # Not usable in a path
    obstacle_low = 2
    obstacle_mid = 3
    obstacle_high = 4

    # Starting point of path
    start = 5

    # Ending point of path
    end = 6

    # Part of a path
    path = 7

    # Part of the current mouse selection
    selected = 8

    # Wall
    wall = 9

class SelectionState:
    """An enum for all the possible states of selection """

    # Nothing should happen on click
    choosing_nothing = 1

    # Selected square is the starting point
    choosing_start = 2

    # Selected square is the ending point
    choosing_end = 3

    # Selected square is an obstacle of low level obstruction
    choosing_obstacle_low = 4

    # Selected square is an obstacle of mid level obstruction
    choosing_obstacle_mid = 5

    # Selected square is an obstacle of high level obstruction
    choosing_obstacle_high = 6

    # Selected square is possibly in the optimal path
    choosing_possible_path = 7

    # Selected square is in the optimal path
    choosing_final_path = 8

    # Selected square is not reachable
    choosing_wall = 9
