from game2dboard import Board
import random
import heapq

# board dimensions
rows = 5
cols = 5
maxHeight = 10


empty_cell_color = "bisque"
stack_colors = ["#e0f7fa", "#b2ebf2", "#80deea", "#4dd0e1", "#26c6da", "#00bcd4", "#00acc1", "#0097a7", "#00838f", "#006064"]
water_color = "#1976d2" 


b = Board(rows, cols)
b.cell_size = 120
b.cell_color = empty_cell_color
b.title = "Guide the Water!"
b.on_mouse_click = None  # disable click for now until we define the game logic


matrix = [[random.randint(1, maxHeight) for _ in range(cols)] for _ in range(rows)]

# Function to update the board based on matrix values
def updateBoard():
    for i in range(rows):
        for j in range(cols):
            height = matrix[i][j]
            if height > 0:
                # Set cell color based on height
                b[i][j] = height
                b.cell_color[i][j] = stack_colors[min(height - 1, len(stack_colors) - 1)]
            else:
                # Empty cell (no stack)
                b[i][j] = 0
                b.cell_color[i][j] = empty_cell_color

#Dijkstra’s 
def findOptimalPath(start, target):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left
    pq = []  # P - queue for cells, sorted by descending stack height
    visited = set()
    heapq.heappush(pq, (-matrix[start[0]][start[1]], start))  # Push starting cell with negated height for max-heap

    path = {}
    path[start] = None  # Start node has no previous cell

    while pq:
        current_height, (r, c) = heapq.heappop(pq)
        current_height = -current_height  # Convert back to positive height

        if (r, c) == target:
            break

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                next_height = matrix[nr][nc]
                if next_height <= current_height:  # move if next cell is at a lower or equal height
                    visited.add((nr, nc))
                    path[(nr, nc)] = (r, c)  # Track the path
                    heapq.heappush(pq, (-next_height, (nr, nc)))

    # backtrack to construct the optimal path
    optimal_path = []
    step = target
    while step:
        optimal_path.append(step)
        step = path[step]
    optimal_path.reverse()

    return optimal_path

# function to visualize the water path on the board
def showWaterPath(path):
    for r, c in path:
        b[r][c] = "w"
        b.cell_color[r][c] = water_color
        b.pause(0.1)  # Brief pause to simulate animation

#  start and target positions (can be dynamically updated)
start_position = (0, 0)
target_position = (rows - 1, cols - 1)


update_board()
b.show()

# Find and display the optimal path
optimal_path = find_optimal_path(start_position, target_position)
show_water_path(optimal_path)
