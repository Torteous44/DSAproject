# main.py
import pygame
from menu import menu, intro_screen
from gameplay import play_level  
from score_manager import save_score


pygame.init()

def main():
    """Main game loop for level selection and gameplay."""

    intro_screen()
    while True:
        
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
