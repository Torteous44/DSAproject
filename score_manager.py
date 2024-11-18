# score_manager.py

import json
import os
from settings import levels
# Define the path to the scores file
SCORES_FILE = "scores.json"

class GameScore:
    def __init__(self, optimal_path_length):
        self.score = 100  # Starting score, can be adjusted
        self.modifications = 0
        self.path_length = 0
        self.optimal_path_length = optimal_path_length

    def add_modification(self):
        """Increment modifications and deduct points."""
        self.modifications += 1
        self.score -= 5  # Deduct points for each modification
        print(f"Modification made. Current score: {self.score}")

    def set_path_length(self, length):
        """Set the path length and calculate any penalty based on the optimal path."""
        self.path_length = length
        if length > self.optimal_path_length:  # Only penalize if path exceeds optimal length
            extra_steps = length - self.optimal_path_length
            self.score -= extra_steps * 2  # Deduct points for extra steps
            print(f"Path length set to {length}. Extra steps penalty applied. Current score: {self.score}")
        else:
            print(f"Path length set to {length}. No penalty applied as path is within optimal length.")

    def final_score(self):
        """Return the final score, ensuring it doesn’t go below zero."""
        return max(self.score, 0)

# Score Management Functions

def load_scores():
    """Load scores from a file. Returns an empty dict if the file does not exist."""
    if os.path.exists(SCORES_FILE):
        with open(SCORES_FILE, "r") as file:
            return json.load(file)
    return {}

def save_score(level_index, score):
    """Save the best score for a specific level if it exceeds the existing best score."""
    scores = load_scores()  # Load current scores
    best_score = scores.get(str(level_index), 0)  # Default to 0 if no score exists

    # Ensure best_score is a valid integer or default to 0
    try:
        best_score = int(best_score)
    except ValueError:
        best_score = 0

    if score > best_score:
        scores[str(level_index)] = score  # Save as string for JSON compatibility
        with open(SCORES_FILE, "w") as file:
            json.dump(scores, file)
        print(f"New high score for Level {level_index + 1}: {score}")
    else:
        print(f"Score for Level {level_index + 1} not high enough to overwrite existing best: {best_score}")

def reset_scores():
    """Reset all scores to the original state."""
    initial_scores = {str(i): "Not Played" for i in range(len(levels))}
    with open(SCORES_FILE, "w") as file:
        json.dump(initial_scores, file)
    print("All scores have been reset to their original state.")