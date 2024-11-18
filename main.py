from src.core.menu import intro_screen, menu
from src.core.gameplay import play_level



def main():
    """Main function to control the game loop."""
    intro_screen()  # Display the intro screen

    while True:
        selected_level = menu()  # Display the level selection menu
        if selected_level is None:
            break  # Exit if the player quits from the menu

        while True:
            print(f"Starting Level {selected_level + 1}...")
            result = play_level(selected_level)  # Play the selected level

            if result == "retry":
                continue  # Retry the same level
            elif result == "menu":
                break  # Return to the menu

    print("Thanks for playing!")  # Exit message


if __name__ == "__main__":
    main()
