import pygame
from src.utils.score_manager import load_scores
from src.core.settings import screen_width, screen_height

pygame.init()

# Screen setup for the end-of-level screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("End of Level")

# Fonts for text
title_font = pygame.font.Font(None, 60)
info_font = pygame.font.Font(None, 40)
button_font = pygame.font.Font(None, 30)

def draw_end_of_level_screen(level_index, final_score):
    """Display the end-of-level screen with leaderboard and options."""
    # Time Complexity: O(S), where S is the number of scores in the leaderboard for the level.
    # The function iterates through the leaderboard scores and renders them.
    # In the worst case, this function will process all scores for the level.
    screen.fill((30, 30, 30))  # Background color

    # Title
    title_text = title_font.render("Level Complete!", True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(screen_width // 2, 50))
    screen.blit(title_text, title_rect)

    # Final score
    final_score_text = f"Your Score: {final_score}"
    final_score_surface = info_font.render(final_score_text, True, (200, 200, 200))
    final_score_rect = final_score_surface.get_rect(center=(screen_width // 2, 120))
    screen.blit(final_score_surface, final_score_rect)

    # Leaderboard
    scores = load_scores().get(str(level_index), [])
    y_offset = 180

    if scores:
        leaderboard_title = info_font.render("Leaderboard:", True, (255, 255, 255))
        leaderboard_title_rect = leaderboard_title.get_rect(center=(screen_width // 2, y_offset))
        screen.blit(leaderboard_title, leaderboard_title_rect)

        y_offset += 40
        for rank, score in enumerate(scores, start=1):
            color = (255, 255, 0) if score == final_score else (200, 200, 200)
            score_text = f"{rank}. {score}"
            score_surface = info_font.render(score_text, True, color)
            score_rect = score_surface.get_rect(center=(screen_width // 2, y_offset))
            screen.blit(score_surface, score_rect)
            y_offset += 30
    else:
        no_scores_text = info_font.render("No scores yet!", True, (200, 200, 200))
        no_scores_rect = no_scores_text.get_rect(center=(screen_width // 2, y_offset))
        screen.blit(no_scores_text, no_scores_rect)

    # Buttons
    retry_button_rect = pygame.Rect(screen_width // 2 - 110, screen_height - 100, 100, 40)
    menu_button_rect = pygame.Rect(screen_width // 2 + 10, screen_height - 100, 100, 40)

    pygame.draw.rect(screen, (50, 150, 50), retry_button_rect)  # Retry button
    retry_text = button_font.render("Retry", True, (255, 255, 255))
    retry_text_rect = retry_text.get_rect(center=retry_button_rect.center)
    screen.blit(retry_text, retry_text_rect)

    pygame.draw.rect(screen, (150, 50, 50), menu_button_rect)  # Menu button
    menu_text = button_font.render("Menu", True, (255, 255, 255))
    menu_text_rect = menu_text.get_rect(center=menu_button_rect.center)
    screen.blit(menu_text, menu_text_rect)

    pygame.display.flip()
    return retry_button_rect, menu_button_rect

def end_of_level(level_index, final_score):
    """Handle the end-of-level screen logic."""
    # Time Complexity: O(1), as it processes each event in a loop, checking for button clicks (constant time operations).
    # The logic for handling button clicks is direct and doesn't scale with the number of elements.
    running = True
    while running:
        retry_button_rect, menu_button_rect = draw_end_of_level_screen(level_index, final_score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if retry_button_rect.collidepoint(x, y):
                    return "retry"
                elif menu_button_rect.collidepoint(x, y):
                    return "menu"
