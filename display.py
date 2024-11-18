import pygame
from settings import cell_size, stack_colors, empty_cell_color, origin_color, drain_color, screen_width, screen_height

# Initialize the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Guide the Water")

def hex_to_rgb(hex_color):
    """Utility function to convert hex color to RGB"""
    return tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))

def darken_color(color, factor):
    """Adjusts a color's brightness by the given factor.

    factor > 1: Lighten the color.
    0 < factor < 1: Darken the color.
    """
    return tuple(
        min(255, max(0, int(c * factor))) for c in color
    )

def draw_stack_3d(i, j, height, base_color):
    """Draw a single stack in pseudo-3D with lighter brown tones."""
    x = j * cell_size
    y = i * cell_size

    for h in range(height):
        offset = h * 4  # Adjust for the height effect
        # Use a smaller decrement to keep colors lighter
        factor = max(0.8, 1 - h * 0.05)  # Ensure factor doesn't go below 0.8
        layer_color = darken_color(base_color, factor)
        pygame.draw.rect(
            screen,
            layer_color,
            (x + offset, y - offset, cell_size - 2 * offset, cell_size - 2 * offset),
        )

def draw_grid(matrix, origin, drain, water_path=[]):
    screen.fill((240, 240, 240))  # Fill background with a neutral color

    for i, row in enumerate(matrix):
        for j, stack in enumerate(row):
            height = stack.peek()
            if height > 0:
                base_color = hex_to_rgb(stack_colors[min(height - 1, len(stack_colors) - 1)])
                draw_stack_3d(i, j, height, base_color)  # Draw stacks
            else:
                pygame.draw.rect(
                    screen, empty_cell_color, (j * cell_size, i * cell_size, cell_size, cell_size)
                )

    # Draw faucet and drain
    draw_faucet_and_drain(origin, drain, matrix)  # Pass the matrix argument here

    # Draw Run button
    pygame.draw.rect(screen, (50, 50, 50), (screen_width // 2 - 50, screen_height - 40, 100, 30))
    font = pygame.font.Font(None, 24)
    text = font.render("Run", True, (255, 255, 255))
    screen.blit(text, (screen_width // 2 - 25, screen_height - 35))

    pygame.display.flip()  # Update the screen




def draw_water_layer(r, c, layer, base_height, color):
    """Draw a single water layer dynamically adjusted to terrain height."""
    offset = (base_height + layer) * 4  # Offset increases with terrain and water layer height
    pygame.draw.rect(
        screen,
        color,
        (
            c * cell_size + offset,
            r * cell_size - offset,
            cell_size - 2 * offset,
            cell_size - 2 * offset,
        ),
    )

def show_water_path(path, matrix):
    """Animate water flowing dynamically over terrain in pseudo-3D."""
    water_base_color = (28, 107, 160)  # Base water color (a nice blue)

    for r, c in path:
        stack_height = matrix[r][c].peek()  # Get the current height of the terrain
        for layer in range(3):  # Render 3 layers for the water
            water_color = tuple(
                max(0, min(255, int(water_base_color[i] * (1 - layer * 0.1)))) for i in range(3)
            )  # Slightly darken each layer
            draw_water_layer(r, c, layer, stack_height, water_color)

        # Update the display for the current cell
        pygame.display.update()
        pygame.time.delay(150)  # Delay for animation



# Load faucet and drain images
faucet_image = pygame.image.load("assets/faucet.png")
faucet_image = pygame.transform.scale(faucet_image, (cell_size // 3, cell_size // 3))  # Scale to one-third of the grid cell

drain_image = pygame.image.load("assets/drain.png")
drain_image = pygame.transform.scale(drain_image, (cell_size // 3, cell_size // 3))  # Scale to one-third of the grid cell

def draw_faucet_and_drain(origin, drain, matrix):
    """Draw the faucet and drain on the grid and outline the top block of their stacks."""
    # Outline colors
    faucet_outline_color = (0, 0, 255)  # Bright blue for faucet
    drain_outline_color = (255, 0, 0)  # Bright red for drain


    # Get stack heights for the faucet and drain
    faucet_height = matrix[origin[0]][origin[1]].peek()
    drain_height = matrix[drain[0]][drain[1]].peek()

    # Calculate pseudo-3D offsets
    faucet_offset = faucet_height * 4
    drain_offset = drain_height * 4

    # Draw outlines around the top block
    pygame.draw.rect(
        screen,
        faucet_outline_color,
        (
            origin[1] * cell_size + faucet_offset,
            origin[0] * cell_size - faucet_offset,
            cell_size - 2 * faucet_offset,
            cell_size - 2 * faucet_offset,
        ),
        2,  # Outline thickness
    )
    pygame.draw.rect(
        screen,
        drain_outline_color,
        (
            drain[1] * cell_size + drain_offset,
            drain[0] * cell_size - drain_offset,
            cell_size - 2 * drain_offset,
            cell_size - 2 * drain_offset,
        ),
        2,  # Outline thickness
    )

    # Calculate image placement to align with the center of the topmost block
    faucet_x = origin[1] * cell_size + (cell_size // 2) - (faucet_image.get_width() // 2)
    faucet_y = origin[0] * cell_size - faucet_offset + (cell_size // 2) - (faucet_image.get_height() // 2)

    drain_x = drain[1] * cell_size + (cell_size // 2) - (drain_image.get_width() // 2)
    drain_y = drain[0] * cell_size - drain_offset + (cell_size // 2) - (drain_image.get_height() // 2)

    # Draw the faucet image
    screen.blit(faucet_image, (faucet_x, faucet_y))

    # Draw the drain image
    screen.blit(drain_image, (drain_x, drain_y))
