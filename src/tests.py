""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# OTHER ALGORITHMS NOT IN USE:
# DO NOT IMPLEMENT, WILL BREAK GAME
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def greedy_cpu(matrix, origin, drain):
    """
    Simulates a CPU player finding a path from origin to drain using a greedy algorithm.
    - origin: Tuple (row, col) of the starting position.
    - drain: Tuple (row, col) of the target position.

    Returns:
    - A list of positions (row, col) representing the path, or None if no path exists.
    """
    rows, cols = len(matrix), len(matrix[0])  # Get the dimensions of the grid.
    
    # Define possible movement directions: up, down, left, right.
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Start the CPU player at the origin position.
    current = origin
    path = []          # To store the path taken by the CPU.
    visited = set()    # To keep track of already visited positions.

    # Loop until the CPU reaches the target (drain).
    while current != drain:
        path.append(current)      # Add the current position to the path.
        visited.add(current)      # Mark the current position as visited.

        next_step = None  # Initialize the next move to None.

        # Evaluate all possible moves from the current position.
        for dr, dc in directions:
            new_row, new_col = current[0] + dr, current[1] + dc  # Calculate the new position.

            # Check if the new position is within the grid boundaries.
            if 0 <= new_row < rows and 0 <= new_col < cols:
                # Skip positions that are already visited.
                if (new_row, new_col) not in visited:
                    
                    # If no next step is chosen yet, or this move brings the CPU closer to the drain:
                    if not next_step or (
                        abs(new_row - drain[0]) + abs(new_col - drain[1])
                        < abs(next_step[0] - drain[0]) + abs(next_step[1] - drain[1])
                    ):
                        next_step = (new_row, new_col)  # Update the next step.

        # If no valid move exists, return None (the CPU is stuck).
        if next_step is None:
            return None

        # Move the CPU to the next chosen position.
        current = next_step

    # Once the drain is reached, add it to the path and return the complete path.
    path.append(drain)
    return path

""" Explination of Distance Calculation:
The abs() function is used in this context to calculate the absolute difference between the current position and the drain's coordinates along the rows and columns.
This gives the "Manhattan Distance" between the two points without explicitly referring to it as such.

The distance is calculated as:
distance=∣new_row−drain[0]∣+∣new_col−drain[1]∣
This measures how far the new position is from the drain in terms of row and column steps.

Purpose in the greedy algorithm:
-The greedy algorithm chooses the next step based on which potential move brings the current position closer to the drain.
-By using abs(), you get the magnitude of the difference, ignoring whether the movement is in the positive or negative direction,
since we are only interested in how "close" the points are, not the direction.
-Without abs(), negative differences (like -1 or -2) could interfere with the comparison logic since negative numbers are 
smaller in mathematical terms but irrelevant here.
"""

# Updated water logic for dfs to include obstacles:
def water_path_dfs(matrix: List[List[Stack]], origin: Tuple[int, int], drain: Tuple[int, int]) -> List[Tuple[int, int]]:
    """Simulate water flow from origin to drain using DFS, considering obstacles. Returns path if reachable, else empty list."""
    rows, cols = len(matrix), len(matrix[0])
    path = []
    visited = set()
    stack = [(origin[0], origin[1])]  # Start at origin

    # Define movement directions (up, down, left, right, and diagonals)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    while stack:
        row, col = stack.pop()
        if (row, col) in visited:
            continue

        visited.add((row, col))
        path.append((row, col))

        if (row, col) == drain:
            return path

        # Check if the current cell is an obstacle
        if matrix[row][col] == -1:
            continue  # Skip this cell as it's an obstacle

        current_stack = matrix[row][col]
      
        current_height = current_stack.pop() if not current_stack.is_empty() else 0  # 0 represents no height left in the stack

        for dr, dc in directions:
            newRow, newCol = row + dr, col + dc
            if 0 <= newRow < rows and 0 <= newCol < cols:  # Ensure within bounds
                # Skip the neighbor if it's an obstacle
                if matrix[newRow][newCol] == -1:
                    continue  # Skip obstacle cells
                
                
                if (newRow, newCol) not in visited:
                    neighbor_stack = matrix[newRow][newCol]
                    
                    if not neighbor_stack.is_empty() or current_height >= 0:  
                        stack.append((newRow, newCol))

    return []

# Adjusted terrain generation code to also include the obstacle:
import pygame
from src.core.settings import cell_size, maxHeight, stack_colors, empty_cell_color
from src.score_manager import GameScore
from display import hex_to_rgb

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
    rows, cols = len(level_terrain), len(level_terrain[0])
    terrain = [[None if random.random() > obstacle_probability else Stack() for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            if terrain[i][j] is not None:  # If not an obstacle
                height = level_terrain[i][j]
                for h in range(1, height + 1):
                    terrain[i][j].push(h)
    return terrain

def get_matrix_snapshot(terrain):
    """Return a 2D matrix of the current heights of each stack and obstacle in the terrain."""
    return [[-1 if cell is None else cell.peek() for cell in row] for row in terrain]

def handle_click(row, col, terrain, score_tracker: GameScore):
    """Handle a left or right mouse click to modify terrain."""
    stack = terrain[row][col]

    if stack is None: # Check if the clicked cell is an obstacle
        print(f"Cannot modify obstacle at ({row}, {col}).")
        return  # No modification if it's an obstacle
        
    top_value = stack.peek()

    # Detect left and right mouse clicks
    mouse_buttons = pygame.mouse.get_pressed()

    if mouse_buttons[0]:  # Left click: Increase height
        if top_value < maxHeight:
            stack.push(top_value + 1)
            score_tracker.add_modification()  # Deduct points for modifying terrain
            print(f"Increased height at ({row}, {col}) to {top_value + 1}")
    elif mouse_buttons[2]:  # Right click: Decrease height
        if top_value > 0:
            stack.pop()
            score_tracker.add_modification()  # Deduct points for modifying terrain
            print(f"Decreased height at ({row}, {col}) to {stack.peek()}")

    # Update color after modification
    color = hex_to_rgb(stack_colors[min(stack.peek(), len(stack_colors) - 1)]) if stack.peek() > 0 else empty_cell_color
    terrain[row][col].color = color 

#HINT SYSTEM: CURRENTLY IN DEVELOPMENT:
from collections import deque

def bfs_shortest_path(matrix, origin, drain):
    """Find the shortest path from origin to drain using BFS."""
    rows, cols = len(matrix), len(matrix[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(origin, [])])  # Store current position and path
    visited = set()

    while queue:
        (row, col), path = queue.popleft()

        if (row, col) in visited:
            continue

        visited.add((row, col))
        new_path = path + [(row, col)]

        if (row, col) == drain:
            return new_path

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols:
                if (new_row, new_col) not in visited and matrix[new_row][new_col] != -1:  # Skip obstacles
                    queue.append(((new_row, new_col), new_path))

    return []  

#For gameplay.py:
    def provide_hint(matrix, origin, drain, score_tracker):
    """Provide a hint to the player by showing the next step in the shortest path."""
    shortest_path = bfs_shortest_path(matrix, origin, drain)

    if not shortest_path:
        print("No valid path exists.")
        return None  # No hint possible

    # Deduct points for using the hint
    score_tracker.deduct_hint_points()

    # Return the next step in the shortest path (excluding the origin)
    if len(shortest_path) > 1:
        next_step = shortest_path[1]
        print(f"Hint: The next step is {next_step}.")
        return next_step
    else:
        print("You are already at the drain!")
        return None
        
#For display.py:
def show_hint(terrain, hint_cell):
    """Highlight the hint cell on the grid."""
    row, col = hint_cell
    hint_color = (255, 215, 0)  # Gold for the hint cell

    pygame.draw.rect(
        terrain.surface,
        hint_color,
        pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size),
    )
    pygame.display.update()

#For score_manager.py:
class GameScore:
    def __init__(self):
        self.score = 100  # Starting score

    def deduct_hint_points(self):
        """Deduct points for using a hint."""
        deduction = 10  # Adjust as needed
        self.score = max(0, self.score - deduction)
        print(f"Hint used! {deduction} points deducted. Remaining score: {self.score}")



