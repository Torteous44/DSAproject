# main.py
import pygame
from menu import menu
from gameplay import play_level  # play_level handles gameplay logic for a single level
from score_manager import save_score

# Initialize pygame and set up the screen
pygame.init()

def main():
    """Main game loop for level selection and gameplay."""
    while True:
        # Show the menu and get the selected level index
        selected_level = menu()
        if selected_level is None:
            break  

        # Play the selected level and get the score at the end
        final_score = play_level(selected_level)

        # Save the score if it’s a new high score for the level
        save_score(selected_level, final_score)

    pygame.quit()


if __name__ == "__main__":
    main()
