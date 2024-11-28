# score_manager.py

import json
import os
from src.core.settings import levels


SCORES_FILE = "scores.json"

class GameScore:
    def __init__(self, optimal_path_length):
        self.score = 100  # starting score
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

import json
import os
from src.core.settings import levels

# Path to the scores file
SCORES_FILE = "scores.json"

class GameScore:
    def __init__(self, optimal_path_length):
        self.score = 100  # Starting score
        self.modifications = 0
        self.path_length = 0
        self.optimal_path_length = optimal_path_length

    def add_modification(self):
        """Increment modifications and deduct points."""
        # Time Complexity: O(1)
        # This method only increments modifications and deducts points in constant time.
        self.modifications += 1
        self.score -= 5  # deduction for modification
        print(f"Modification made. Current score: {self.score}")

    def set_path_length(self, length):
        """Set the path length and calculate any penalty based on the optimal path."""
        # Time Complexity: O(1)
        # This method computes the penalty for extra steps by a simple arithmetic comparison and update, all of which are constant time operations.
        self.path_length = length
        if length > self.optimal_path_length: # when length exceeds optimal length
            extra_steps = length - self.optimal_path_length
            self.score -= extra_steps * 2  # then educt points for extra steps
            print(f"Path length set to {length}. Extra steps penalty applied. Current score: {self.score}")
        else:
            print(f"Path length set to {length}. No penalty applied as path is within optimal length.")

    def final_score(self):
        """Return the final score, ensuring it doesn’t go below zero."""
        # Time Complexity: O(1)
        # This method simply returns the final score in constant time after ensuring it doesn't go below zero.
        return max(self.score, 0)

# Score Management Functions

def load_scores():
    """Load scores from a file and ensure all levels have valid lists."""
    # Time Complexity: O(L), where L is the number of levels.
    # The function iterates over all levels to ensure each level has valid score entries. It loads the entire score data from the file and performs a check on each level.
    if os.path.exists(SCORES_FILE):
        with open(SCORES_FILE, "r") as file:
            try:
                scores = json.load(file)
                # init as lists
                for i in range(len(levels)):
                    level_key = str(i)
                    if not isinstance(scores.get(level_key), list):
                        scores[level_key] = []  # reset invalid 
            except json.JSONDecodeError:
                print("Error decoding scores file. Resetting to defaults.")
                scores = {str(i): [] for i in range(len(levels))}
    else:
        scores = {str(i): [] for i in range(len(levels))}  # init w/ empty lists
    
    return scores



def reset_scores():
    """Reset all scores to the original state."""
    # Time Complexity: O(L), where L is the number of levels.
    # This function initializes a new score structure for all levels and writes it back to the file, iterating over all levels in the process.
    initial_scores = {str(i): [] for i in range(len(levels))}
    with open(SCORES_FILE, "w") as file:
        json.dump(initial_scores, file)
    print("All scores have been reset to their original state.")


def get_player_rank(level_index, score):
    """Calculate the rank of the player's score for a specific level."""
    # Time Complexity: O(S), where S is the number of scores for the given level.
    # This function iterates through the scores list of a particular level to calculate the rank of the player's score.
    scores = load_scores()
    level_key = str(level_index)

    if level_key in scores:
        all_scores = scores[level_key]
        rank = 1
        for s in all_scores:
            if score < s:
                rank += 1
        return rank, len(all_scores)  #  rank, total players
    return 1, 1  # default 

def merge_sort_descending(array):
    """Sorts an array in descending order using merge sort."""
    # Time Complexity: O(N log N), where N is the size of the array.
    # Merge Sort is a divide-and-conquer sorting algorithm that splits the array into smaller parts, sorts them, and merges them back. The time complexity is logarithmic with respect to the size of the array.
    if len(array) <= 1:
        return array  


    mid = len(array) // 2
    left_half = merge_sort_descending(array[:mid])
    right_half = merge_sort_descending(array[mid:])


    return merge_descending(left_half, right_half)

def merge_descending(left, right):
    """Merge two sorted arrays in descending order."""
    # Time Complexity: O(N), where N is the total number of elements in the two arrays.
    # This function iterates through both sorted arrays and merges them into a single sorted array. The operation takes linear time with respect to the total number of elements.
    result = []
    while left and right:
        if left[0] >= right[0]:  # compare elements for descending order
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result.extend(left)
    result.extend(right)

    return result


def save_score(level_index, score):
    """Save the player's score for a specific level."""
    # Time Complexity: O(S log S), where S is the number of scores for the level.
    # This function loads the scores, appends the new score, sorts the scores list using merge sort (O(S log S) time), and writes the updated scores back to the file.
    scores = load_scores()  

    level_key = str(level_index) 
    if level_key not in scores or not isinstance(scores[level_key], list):
        print(f"Fixing invalid score entry for level {level_index}.")
        scores[level_key] = []  #level key =list

    # add new score then sort
    scores[level_key].append(score)

    scores[level_key] = merge_sort_descending(scores[level_key])  

    # save back to the file
    with open(SCORES_FILE, "w") as file:
        json.dump(scores, file)
    print(f"Saved score {score} for Level {level_index + 1}")

def validate_scores(scores):
    """Ensure all scores in the file are lists."""
    # Time Complexity: O(L), where L is the number of levels.
    # This function iterates through all levels and ensures that the scores for each level are stored as lists, correcting any invalid entries.
    for i in range(len(levels)):
        level_key = str(i)
        if not isinstance(scores.get(level_key), list):
            scores[level_key] = [] 
    return scores
