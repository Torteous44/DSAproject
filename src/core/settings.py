import os

# gets the base directory. it by default goes into core/ so we take two steps back into dsaproject/
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# Paths for assets
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
IMAGE_DIR = os.path.join(ASSETS_DIR, 'images')
SOUND_DIR = os.path.join(ASSETS_DIR, 'sounds')

# Image paths
faucet_image_path = os.path.join(IMAGE_DIR, 'faucet.png')
drain_image_path = os.path.join(IMAGE_DIR, 'drain.png')

# Sound paths
click_sound_path = os.path.join(SOUND_DIR, 'click_sound.mp3')
water_flow_sound_path = os.path.join(SOUND_DIR, 'water.mp3')


levels = [
    # Level 1
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
        "target_score": 40,       
        "optimal_path_length": 7  
        
    },

    # Level 2
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

    # Level 3
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

    # Level 4
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
        "target_score": 70,       
        "optimal_path_length": 12 
    }
]

# Screen settings
screen_width, screen_height = 600, 650 

# Cell settings
cell_size = 120
maxHeight = 10  # Maximum terrain height

# Colors (ligher to darker/ lower to higher)
stack_colors = [
    "#F5DEB3",  
    "#DEB887",  
    "#D2B48C",  
    "#BC8F8F",  
    "#F4A460",  
    "#DAA520",  
    "#CD853F",  
    "#D2691E", 
    "#8B4513",  
    "#A0522D",  
]


empty_cell_color = (240, 228, 203) 

