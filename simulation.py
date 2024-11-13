# simulation.py
from typing import List, Tuple
from display import show_water_path
from collections import deque
from terrain import get_matrix_snapshot  # Ensure this function returns a 2D list of heights



def water_path_dfs(matrix: List[List[int]], origin: Tuple[int, int], drain: Tuple[int, int]) -> List[Tuple[int, int]]:
    """Simulate water flow from origin to drain using DFS. Returns path if reachable, else empty list."""
    rows, cols = len(matrix), len(matrix[0])
    path = []
    visited = set()
    stack = [(origin[0], origin[1])]

    # Define movement directions (up, down, left, right, and diagonals)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    while stack:
        row, col = stack.pop()
        if (row, col) in visited:
            continue
        visited.add((row, col))
        path.append((row, col))

        # Stop if we reach the drain
        if (row, col) == drain:
            return path

        # Explore neighbors
        for dr, dc in directions:
            newRow, newCol = row + dr, col + dc
            if 0 <= newRow < rows and 0 <= newCol < cols:
                if (newRow, newCol) not in visited and matrix[newRow][newCol] <= matrix[row][col]:
                    stack.append((newRow, newCol))

    return []  # Return empty list if no path is found

def run_simulation(terrain, origin: Tuple[int, int], drain: Tuple[int, int], score_tracker) -> int:
    """Run the water path simulation and return path length if completed, else None."""
    matrix = get_matrix_snapshot(terrain)  # Get a 2D list of heights

    path = water_path_dfs(matrix, origin, drain)

    if path and path[-1] == drain:  # Check if path reaches the drain
        show_water_path(path)  # Visualize the path
        return len(path)  # Return the path length if successful
    else:
        print("Water did not reach the drain. Adjust the terrain and try again.")
        return None  # Return None if path does not reach the drain
