# settings.py
import os
# Paths for sound files
script_dir = os.path.dirname(os.path.abspath(__file__))
click_sound_path = os.path.join(script_dir, 'sounds', 'click_sound.mp3')
water_flow_sound_path = os.path.join(script_dir, 'sounds', 'water.mp3')

# Scoring constants
MAX_SCORE = 100           # Starting score
PATH_LENGTH_PENALTY = 1   # Points deducted per extra step beyond optimal
MODIFICATION_PENALTY = 3  # Points deducted per terrain modification

# Define levels with terrain configurations and target scores
levels = [
    # Level 1: Basic Level
    {
        "terrain": [
            [3, 3, 2, 1, 0],
            [3, -1, -1, 1, 0],
            [4, 4, 2, 2, 0],
            [5, -1, 3, -1, 1],
            [5, 4, 3, 2, 1],
        ],
        "origin": (0, 0),
        "drain": (4, 4),
        "target_score": 40,       # Minimum score to complete the level
        "optimal_path_length": 7  # Shortest possible path length
    },

    # Level 2: Intermediate Level with More Obstacles
    {
        "terrain": [
            [3, 3, -1, 1, 0],
            [3, -1, -1, 2, 0],
            [5, 4, -1, 2, 1],
            [6, -1, 4, -1, 1],
            [5, 5, 4, 3, 1],
        ],
        "origin": (0, 0),
        "drain": (4, 4),
        "target_score": 50,       # Higher score requirement
        "optimal_path_length": 9  # More steps required due to obstacles
    },

    # Level 3: Advanced Level with Tighter Constraints
    {
        "terrain": [
            [3, -1, 3, -1, 2],
            [4, 4, -1, 2, 1],
            [5, -1, -1, -1, 1],
            [6, 5, 4, -1, 1],
            [6, -1, 3, 2, 0],
        ],
        "origin": (0, 0),
        "drain": (4, 4),
        "target_score": 60,       # Higher score requirement
        "optimal_path_length": 10 # Longest optimal path due to obstacles
    },

    # Level 4: Complex Level with High Heights and Many Obstacles
    {
        "terrain": [
            [4, -1, 4, -1, 3],
            [5, 6, -1, 4, -1],
            [6, -1, -1, -1, 2],
            [6, 5, -1, 5, 2],
            [6, 6, 5, 3, 1],
        ],
        "origin": (0, 0),
        "drain": (4, 4),
        "target_score": 70,       # Highest score requirement
        "optimal_path_length": 12 # Longest optimal path
    }
]

# Screen settings
screen_width, screen_height = 600, 650  # Extra height for the Run button

# Cell settings
cell_size = 120
maxHeight = 10  # Maximum terrain height

# Colors
stack_colors = [
    "#e0f7fa", "#b2ebf2", "#80deea", "#4dd0e1", "#26c6da",
    "#00bcd4", "#00acc1", "#0097a7", "#00838f", "#006064"
]
water_color = "#1976d2"
empty_cell_color = (240, 228, 203)  # Bisque color in RGB

# Origin and Drain Colors
origin_color = (0, 255, 0)  # Green for the origin
drain_color = (255, 0, 0)   # Red for the drain
