
from typing import List, Tuple
from src.core.display import show_water_path
from collections import deque
from src.core.terrain import get_matrix_snapshot  



def water_path_dfs(matrix: List[List[int]], origin: Tuple[int, int], drain: Tuple[int, int]) -> List[Tuple[int, int]]:
    """Simulate water flow from origin to drain using DFS. Returns path if reachable, else empty list."""
    # Time Complexity: O(V + E), where V is the number of cells (rows * cols) and E is the number of edges between cells.
    # Each cell is visited once, and up to 8 neighbors are checked for each cell.
    rows, cols = len(matrix), len(matrix[0])
    path = []
    visited = set()
    stack = [(origin[0], origin[1])]

    #  movement directions (up, down, left, right, and diagonals)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    while stack:
        row, col = stack.pop()
        if (row, col) in visited:
            continue
        visited.add((row, col))
        path.append((row, col))

        if (row, col) == drain:
            print(path)
            return path

        for dr, dc in directions:
            newRow, newCol = row + dr, col + dc
            if 0 <= newRow < rows and 0 <= newCol < cols:
                if (newRow, newCol) not in visited and matrix[newRow][newCol] <= matrix[row][col]:
                    stack.append((newRow, newCol))

    return []  

def run_simulation(terrain, origin: Tuple[int, int], drain: Tuple[int, int], score_tracker) -> int:
    """Run the water path simulation and return path length if completed, else None."""
    # Time Complexity: O(V + E), where V and E are determined by the terrain matrix's size and connectivity.
    # `get_matrix_snapshot` is assumed to be O(rows * cols), and `show_water_path` has a time complexity dependent on the length of the path.
    matrix = get_matrix_snapshot(terrain)  # 2D list of heights

    path = water_path_dfs(matrix, origin, drain)

    if path and path[-1] == drain:  # if path reaches the drain
        show_water_path(path, terrain)  # visualize the path with terrain 
        return len(path)  # return path length
    else:
        print("Water did not reach the drain. Adjust the terrain and try again.")
        return None  # return none (if never reaches the drain)
