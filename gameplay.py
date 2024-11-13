# gameplay.py
import pygame
from settings import levels, cell_size, screen_width, screen_height
from display import draw_grid
from audio import play_click_sound, play_water_flow_sound
from terrain import initialize_terrain, handle_click, get_matrix_snapshot  # Import get_matrix_snapshot
from simulation import run_simulation
from score_manager import GameScore

def play_level(level_index):
    """Play a specific level and return the final score."""
    level_data = levels[level_index]
    terrain = initialize_terrain(level_data["terrain"])
    target_score = level_data["target_score"]
    origin, drain = level_data["origin"], level_data["drain"]
    optimal_path_length = level_data["optimal_path_length"]  # Get the optimal path length for the level

    # Initialize the score tracker with the optimal path length
    score_tracker = GameScore(optimal_path_length)
    running = True

    # Define the Run button area
    run_button_rect = pygame.Rect(screen_width // 2 - 50, screen_height - 40, 100, 30)

    while running:
        # Render the grid with terrain, obstacles, origin, and drain
        draw_grid(terrain, origin, drain)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Exit the level if the window is closed
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                # Check if the Run button is clicked
                if run_button_rect.collidepoint(x, y):
                    play_water_flow_sound()  # Play sound for water flow
                    path_length = run_simulation(terrain, origin, drain, score_tracker)
                    
                    if path_length is not None:
                        score_tracker.set_path_length(path_length)  # Set path length only if valid

                        final_score = score_tracker.final_score()
                        if final_score >= target_score:
                            print("Level Completed!")
                            return final_score  # Return the score at the end of the level
                    else:
                        print("Path did not reach drain, try again.")

                elif y < screen_height - 50:  # Ensure click is within grid area
                    row, col = y // cell_size, x // cell_size
                    if 0 <= row < len(terrain) and 0 <= col < len(terrain[0]):
                        handle_click(row, col, terrain, score_tracker)  # Adjust terrain and update score
                        play_click_sound()  # Play click sound for terrain modification

        pygame.display.flip()  # Update the display

    return 0  # Return zero if the game was exited
