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

levels = [
    # Level 1: Basic Level
    {
        "terrain": [
            [5, 6, 2, 1, 0],
            [6, 4, 6, 1, 0],
            [4, 6, 2, 7, 0],
            [5, 1, 3, 3, 1],
            [5, 4, 3, 9, 0],
        ],
        "origin": (0, 0),
        "drain": (4, 4),
        "target_score": 40,       # Minimum score to complete the level
        "optimal_path_length": 7  # Shortest possible path length
    },

    # Level 2:
    {
        "terrain": [
            [5, 6, 1, 1, 0],
            [4, 8, 1, 2, 0],
            [3, 7, 1, 2, 1],
            [4, 8, 5, 9, 1],
            [4, 4, 2, 5, 1],
        ],
        "origin": (0, 0),
        "drain": (4, 3),
        "target_score": 50,       
        "optimal_path_length": 9  
    },

    # Level 3:
    {
        "terrain": [
            [3, 9, 9, 10, 2],
            [4, 4, 7, 2, 5],
            [5, 8, 1, 8, 3],
            [6, 5, 4, 4, 1],
            [6, 1, 3, 2, 0],
        ],
        "origin": (0, 0),
        "drain": (0, 4),
        "target_score": 60,       
        "optimal_path_length": 10 
    },

    # Level 4: 
    {
        "terrain": [
            [4, 10, 8, 1, 2],
            [10, 6, 9, 1, 1],
            [6, 10, 9, 1, 2],
            [6, 8, 7, 7, 7],
            [6, 6, 5, 3, 1],
        ],
        "origin": (0, 0),
        "drain": (4, 4),
        "target_score": 70,       # Highest score requirement
        "optimal_path_length": 12 
    }
]

# Screen settings
screen_width, screen_height = 600, 650  # Extra height for the Run button

# Cell settings
cell_size = 120
maxHeight = 10  # Maximum terrain height

# Colors
stack_colors = [
    "#F5DEB3",  # Wheat (very light brown)
    "#DEB887",  # Burlywood
    "#D2B48C",  # Tan
    "#BC8F8F",  # Rosy Brown
    "#F4A460",  # Sandy Brown
    "#DAA520",  # Goldenrod
    "#CD853F",  # Peru
    "#D2691E",  # Chocolate
    "#8B4513",  # Saddle Brown
    "#A0522D",  # Sienna
]



empty_cell_color = (240, 228, 203)  # Bisque color in RGB

# Origin and Drain Colors
origin_color = (0, 255, 0)  # Green for the origin
drain_color = (255, 0, 0)   # Red for the drain
