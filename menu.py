# menu.py
import pygame
from settings import levels, screen_width, screen_height
from score_manager import load_scores, reset_scores 

pygame.init()

# Screen setup for the menu
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Menu")

# Fonts 
title_font = pygame.font.Font(None, 50)
option_font = pygame.font.Font(None, 40)
info_font = pygame.font.Font(None, 20)
button_font = pygame.font.Font(None, 50)
exit_font = pygame.font.Font(None, 15)


# ___________INTRO SCREEN STUFF____________

def draw_intro():
    """Draw the introductory screen."""
    screen.fill((30, 30, 30))  # Background color for the intro screen

    # Title
    title_text = title_font.render("Welcome to WaterRouter", True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(screen_width // 2, 100))
    screen.blit(title_text, title_rect)

    # Introductory text
    intro_lines = [
        "Guide the water from the faucet to the drain.",
        "Adjust the terrain to ensure the water flows smoothly.",
        "Earn points by creating the optimal path.",
        "Avoid unnecessary modifications to maximize your score!"
    ]
    y_offset = 180
    for line in intro_lines:
        line_surface = info_font.render(line, True, (200, 200, 200))
        line_rect = line_surface.get_rect(center=(screen_width // 2, y_offset))
        screen.blit(line_surface, line_rect)
        y_offset += 30

    # Play button
    play_button_rect = pygame.Rect(screen_width // 2 - 100, screen_height // 2 + 50, 200, 50)
    pygame.draw.rect(screen, (50, 150, 50), play_button_rect)
    play_text = button_font.render("Play Game", True, (255, 255, 255))
    play_text_rect = play_text.get_rect(center=play_button_rect.center)
    screen.blit(play_text, play_text_rect)

    pygame.display.flip()  # Update the display
    return play_button_rect

def intro_screen():
    """Handle the intro screen loop."""
    running = True
    while running:
        play_button_rect = draw_intro()  # Draw the intro screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the Play Game button was clicked
                x, y = pygame.mouse.get_pos()
                if play_button_rect.collidepoint(x, y):
                    return  # Transition to the main menu

#____________MENU SCREEN STUFF_____________

def draw_menu(selected_level=None):
    screen.fill((50, 50, 50))  # Background color for the menu

    # Title
    title_text = title_font.render("Select Level", True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(screen_width // 2, 50))
    screen.blit(title_text, title_rect)

    # Level options
    scores = load_scores()  # Load existing scores if available
    y_offset = 150
    level_rects = []  # List to store the clickable rectangles for each level

    for i, level in enumerate(levels):
        level_text = f"Level {i + 1} - Target Score: {level['target_score']}"
        score_text = f"Best Score: {scores.get(str(i), 'Not Played')}"
        color = (255, 255, 255) if selected_level == i else (180, 180, 180)

        # Render level option
        level_surface = option_font.render(level_text, True, color)
        level_rect = level_surface.get_rect(center=(screen_width // 2, y_offset))
        screen.blit(level_surface, level_rect)

        # Render best score for level
        score_surface = info_font.render(score_text, True, color)
        score_rect = score_surface.get_rect(center=(screen_width // 2, y_offset + 30))
        screen.blit(score_surface, score_rect)

        # Add the level_rect to the list for click detection
        level_rects.append(level_rect)

        y_offset += 80  # Vertical spacing between levels

    # Reset Scores button
    reset_button_rect = pygame.Rect(20, screen_height - 50, 100, 30)  # Smaller button in bottom-left corner
    pygame.draw.rect(screen, (180, 50, 50), reset_button_rect)
    reset_text = exit_font.render("Reset Scores", True, (255, 255, 255))
    reset_text_rect = reset_text.get_rect(center=reset_button_rect.center)
    screen.blit(reset_text, reset_text_rect)

    pygame.display.flip()
    return level_rects, reset_button_rect  # Return level option rects and reset button rect

def menu():
    """Handle the menu screen loop."""
    selected_level = None
    running = True

    while running:
        level_rects, reset_button_rect = draw_menu(selected_level)  # Draw menu and get clickable areas

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                # Check if Reset Scores button is clicked
                if reset_button_rect.collidepoint(x, y):
                    reset_scores()
                    print("Scores have been reset!")

                # Check if a level was clicked
                for i, rect in enumerate(level_rects):
                    if rect.collidepoint(x, y):
                        return i  # Return the index of the clicked level

    pygame.quit()
    return None