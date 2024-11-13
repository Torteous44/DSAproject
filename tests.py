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
