# menu.py
import pygame
from settings import levels, screen_width, screen_height
from score_manager import load_scores  # Function to retrieve scores

pygame.init()

# Screen setup for the menu
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Menu")

# Font for text display
title_font = pygame.font.Font(None, 60)
option_font = pygame.font.Font(None, 40)
info_font = pygame.font.Font(None, 20)
exit_font = pygame.font.Font(None,15)

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

    # Instructions
    instructions = [
        "Left-click to increase height.",
        "Right-click to decrease height.",
        "Press 'Run' to start the water flow.",
        "Escape to return to the menu."
    ]
    y_offset += 20
    for line in instructions:
        instr_surface = info_font.render(line, True, (100, 200, 200))
        instr_rect = instr_surface.get_rect(center=(screen_width // 2, y_offset))
        screen.blit(instr_surface, instr_rect)
        y_offset += 30

    # Exit option
    exit_text = exit_font.render("Press Q to Quit", True, (200, 200, 200))
    exit_rect = exit_text.get_rect(center=(screen_width // 2, screen_height - 20))
    screen.blit(exit_text, exit_rect)

    pygame.display.flip()
    return level_rects  # Return the rectangles for each level option

def menu():
    selected_level = None
    running = True

    while running:
        level_rects = draw_menu(selected_level)  # Draw menu and get level option rects

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if a level was clicked
                x, y = pygame.mouse.get_pos()
                for i, rect in enumerate(level_rects):
                    if rect.collidepoint(x, y):
                        return i  # Return the index of the clicked level

    pygame.quit()
    return None
