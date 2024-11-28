# terrain.py
import pygame
from src.core.settings import  maxHeight, stack_colors, empty_cell_color
from src.utils.score_manager import GameScore
from src.core.display import hex_to_rgb

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is None:
            return None
        else:
            value = self.top.value
            self.top = self.top.next
            return value

    def peek(self):
        return self.top.value if self.top is not None else 0

def initialize_terrain(level_terrain):
    """Initialize terrain with stacks based on level data."""
    # Time Complexity: O(R * C * H), where R is the number of rows, C is the number of columns,
    # and H is the maximum height of any stack in the terrain. The time complexity comes from iterating through
    # each cell in the terrain and pushing heights to the stack.
    rows, cols = len(level_terrain), len(level_terrain[0])
    terrain = [[Stack() for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            height = level_terrain[i][j]
            for h in range(1, height + 1):
                terrain[i][j].push(h)
    return terrain

def get_matrix_snapshot(terrain):
    """Return a 2D matrix of the current heights of each stack in the terrain."""
    # Time Complexity: O(R * C), where R is the number of rows and C is the number of columns.
    # We iterate through each cell in the terrain and call peek() on each stack (constant time for peek).
    return [[cell.peek() for cell in row] for row in terrain]

def handle_click(row, col, terrain, score_tracker: GameScore):
    """Handle a left or right mouse click to modify terrain."""
    # Time Complexity: O(1), as it involves a constant number of operations:
    #    - peeking at the top of a stack (O(1)),
    #    - pushing or popping a value from a stack (O(1)).
    stack = terrain[row][col]
    top_value = stack.peek()

    # detect clicks
    mouse_buttons = pygame.mouse.get_pressed()

    if mouse_buttons[0]:  # Left click: Increase height
        if top_value < maxHeight:
            stack.push(top_value + 1)
            score_tracker.add_modification()  # deduct points for modifying terrain
            print(f"Increased height at ({row}, {col}) to {top_value + 1}")
    elif mouse_buttons[2]:  # Right click: Decrease height
        if top_value > 0:
            stack.pop()
            score_tracker.add_modification()  # deduct points for modifying terrain
            print(f"Decreased height at ({row}, {col}) to {stack.peek()}")

    # update color
    color = hex_to_rgb(stack_colors[min(stack.peek(), len(stack_colors) - 1)]) if stack.peek() > 0 else empty_cell_color
    terrain[row][col].color = color  
