from src.core.menu import intro_screen, menu
from src.core.gameplay import play_level



def main():
    """Main function to control the game loop."""
    intro_screen()  

    while True:
        selected_level = menu()  # level selection menu
        if selected_level is None:
            break  # exit 

        while True:
            
            print(f"Starting Level {selected_level + 1}...")

            result = play_level(selected_level)  

            if result == "retry":
                continue 
            elif result == "menu":
                break  

    print("Thanks for playing!") 


if __name__ == "__main__":
    main()
