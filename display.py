# display.py
import pygame
from settings import cell_size, stack_colors, water_color, empty_cell_color, origin_color, drain_color, screen_width, screen_height

# Initialize the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Guide the Water")

# Utility function to convert hex colors to RGB
def hex_to_rgb(hex_color):
    return tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))

# Draw the grid with terrain and color coding
def draw_grid(matrix, origin, drain):
    screen.fill(empty_cell_color)  # Background for the grid

    # Iterate through each cell in the matrix and draw it
    for i, row in enumerate(matrix):
        for j, stack in enumerate(row):
            height = stack.peek()
            if height > 0:
                # Color cell based on height in stack_colors
                color = hex_to_rgb(stack_colors[min(height - 1, len(stack_colors) - 1)])
            else:
                color = empty_cell_color  # Color for empty cells

            # Draw cell with determined color
            pygame.draw.rect(screen, color, (j * cell_size, i * cell_size, cell_size, cell_size))

            # Display height value in the cell (optional, for debugging)
            if height > 0:
                font = pygame.font.Font(None, 36)
                text = font.render(str(height), True, (0, 0, 0))
                text_rect = text.get_rect(center=(j * cell_size + cell_size // 2, i * cell_size + cell_size // 2))
                screen.blit(text, text_rect)

            # Draw the origin and drain markers
            if (i, j) == origin:
                pygame.draw.circle(screen, origin_color, (j * cell_size + cell_size // 2, i * cell_size + cell_size // 2), 10)
            elif (i, j) == drain:
                pygame.draw.circle(screen, drain_color, (j * cell_size + cell_size // 2, i * cell_size + cell_size // 2), 10)

    # Draw the Run button
    pygame.draw.rect(screen, (50, 50, 50), (screen_width // 2 - 50, screen_height - 40, 100, 30))
    font = pygame.font.Font(None, 24)
    text = font.render("Run", True, (255, 255, 255))
    screen.blit(text, (screen_width // 2 - 25, screen_height - 35))

    pygame.display.flip()  # Update the display with the new grid

# Show water path on the board
def show_water_path(path):
    for r, c in path:
        # Set the cell to water color
        pygame.draw.rect(screen, hex_to_rgb(water_color), (c * cell_size, r * cell_size, cell_size, cell_size))
        # Optionally display "W" to signify water (for visual clarity)
        font = pygame.font.Font(None, 36)
        text = font.render("W", True, (255, 255, 255))
        text_rect = text.get_rect(center=(c * cell_size + cell_size // 2, r * cell_size + cell_size // 2))
        screen.blit(text, text_rect)
        pygame.display.update()
        pygame.time.delay(100)  # Delay for water flow animation
