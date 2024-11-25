import pygame
from src.core.settings import levels, cell_size, screen_width, screen_height
from src.core.display import draw_grid
from src.core.audio import play_click_sound, play_water_flow_sound
from src.core.terrain import initialize_terrain, handle_click
from src.core.simulation import run_simulation
from src.utils.score_manager import GameScore, save_score
from src.utils.end_of_level import end_of_level

def play_level(level_index):
    """Play a specific level and return the final score."""
    level_data = levels[level_index]
    terrain = initialize_terrain(level_data["terrain"])
    target_score = level_data["target_score"]
    origin, drain = level_data["origin"], level_data["drain"]
    optimal_path_length = level_data["optimal_path_length"]  

    # init score tracker w/ optimal path length
    score_tracker = GameScore(optimal_path_length)
    running = True

    #define run button area
    run_button_rect = pygame.Rect(screen_width // 2 - 50, screen_height - 40, 100, 30)

    while running:
        # render grid
        draw_grid(terrain, origin, drain)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                # Check if the Run button is clicked
                if run_button_rect.collidepoint(x, y):
                    play_water_flow_sound()  # Play sound for water flow
                    path_length = run_simulation(terrain, origin, drain, score_tracker)

                    if path_length is not None:
                        score_tracker.set_path_length(path_length)  # set path length only if valid
                        final_score = score_tracker.final_score()
                        save_score(level_index, final_score)  # save the score for the level

                        if final_score >= target_score:
                            print("Level Completed!")
                            choice = end_of_level(level_index, final_score)  # display end-of-level screen
                            if choice == "retry":
                                return "retry"  
                            elif choice == "menu":
                                return "menu"  
                            
                        else:
                            print("Score too low. Resetting terrain and score.")
                            terrain = initialize_terrain(level_data["terrain"]) 
                            score_tracker = GameScore(optimal_path_length)
                    else:
                        print("Path did not reach drain, try again.")


                elif y < screen_height - 50:  # click within grid area
                    row, col = y // cell_size, x // cell_size
                    if 0 <= row < len(terrain) and 0 <= col < len(terrain[0]):
                        handle_click(row, col, terrain, score_tracker)  # adjust terrain, score track
                        play_click_sound()  

        pygame.display.flip()  

    return "menu"  
