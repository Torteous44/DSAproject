### **WaterRouter: README**

Welcome to **WaterRouter**, a terrain-modifying puzzle game where you guide water from a faucet to a drain while optimizing terrain for maximum points. 

---

## Table of Contents
- [Features](#Features)
- [Installation and Setup](#installation_and_setup)
- [Game Controls](#game_controls)
- [File Breakdown](#file_breakdown)
- [Complexity Analysis](#complexity_analysis)

---

### **Features**
1. Modify terrain heights using stacks.
2. Simulate water flow in pseudo-3D.
3. Multiple levels of increasing difficulty.
4. Scoring system based on path length and terrain modifications.
5. Persistent high scores with a reset option.
6. Intro screen, instructions, and menu.

---

### **Installation and Setup**

#### **1. Clone the Repository**
Open a terminal or command prompt and run the following command to clone the repository:
```bash
git clone https://github.com/<your-github-username>/WaterRouter.git
cd WaterRouter
```

#### **2. Install Dependencies**
Ensure you have `pygame` installed. Run:
```bash
pip install pygame
```

#### **3. Run the Game**
Launch the game by running:
```bash
python main.py
```

---

### **Game Controls**

#### **Intro Screen**
- Click **Play Game** to start.

#### **Menu Screen**
- Click a level to begin.
- Click **Reset Scores** (bottom-left) to reset all high scores.
- Press **Q** to quit the game.

#### **Gameplay**
- **Left-click:** Increase terrain height.
- **Right-click:** Decrease terrain height.
- **Run Button:** Simulate water flow.
- Press **Esc** to return to the menu.

---

### **File Breakdown**
These are the most important files used for our game:

1) **"assets" File**:
**The "assests" file contains all the different assets we used in our game**,
- *"images" File*: Contains the images used for the drain and water faucet.
- *"sounds" File*: Contains the sound assets used to generate the different sounds in the levels.
2) **"src" File**:
**The "src" file contains the main "core" file that determines the main functionality of the game, the "utils" file that handles the score calculation and display of the scores.**
  
    *"core" File*:
  - audio.py: Contains the functions for playing the audio.
  - display.py: Handles how the game is displayed to the player.
  - gameplay.py: Handles how a specific level is played.
  - menu.py: Generates the menu screen.
  - settings.py: Handles the level settings.
  - simulation.py: Contains the Depth First Search algorithm for the water logic.
  - terrain.py: Handles the generation of stacks and matrix that determines the terrain of the level.

    *"utils" File*:
  - end_of_level.py: Handles the end of level display when the player completes the level.
  - score_manager.py: Calculates the score of the player and sorts them using the merge sort algorithm.
3) **tests.py**:
**This file is used to store code and features to be tested for our game.**

---

## Complexity Analysis

This project implements various algorithms, including **DFS** for water flow simulation and **Merge Sort** for score management. Below is the complexity analysis for these algorithms in the context of our game's terrain generation and levels.

### **DFS Algorithm:**

The DFS (Depth First Search) algorithm is used to simulate water flow through the terrain. The terrain is represented as a 3D grid of stacks, with each stack having a height. The algorithm explores all possible directions (up, down, left, right, and diagonals) to find a path from the origin to the drain.

**Time Complexity**
1. **Best Case**: \(O(V)\)
   - **Scenario**: The path from the origin to the drain is direct (no height mismatches).
   - The algorithm finds the solution with minimal exploration.

2. **Average Case**: \(O(V + E)\)
   - **Scenario**: The path involves several turns, and some backtracking is required.
   - DFS explores parts of the terrain but prunes unnecessary branches.

3. **Worst Case**: \(O(V + E)\)
   - **Scenario**: The terrain has no direct path, requiring the algorithm to explore nearly the entire grid.
   - The algorithm explores most paths due to backtracking.

**Where:**
- V = Number of cells in the grid (rows × columns).
- E = Edges connecting the cells (up to 8 edges per cell for diagonals.

**Merge Sort Algorithm:**

The Merge Sort algorithm is used to sort scores in descending order. It works by recursively dividing the input array into halves, sorting each half, and merging them back together.

**Time Complexity**
1. **Best Case**: \(O(n(log n)\)
   - **Scenario**: Scores are already sorted in descending order.
   - Even in the best case, merge sort divides the array and performs comparisons during merging.

2. **Average Case**: \(O(n(log n)\)
   - **Scenario**: Scores are in random order.
   - The algorithm performs consistent comparisons and merges at all levels of recursion.

3. **Worst Case**: \(O(n(log n)\)
   - **Scenario**: Scores are sorted in ascending order (reverse of desired order).
   - Merge Sort's performance remains unaffected by the input's order.

**Where:**
- n = Number of scores to be sorted.


### **Comparison of Algorithms**

| Algorithm       | Best Case       | Average Case    | Worst Case      | Use Case                     |
|------------------|-----------------|-----------------|-----------------|------------------------------|
| **DFS**         | \(O(V)\)        | \(O(V + E)\)    | \(O(V + E)\)    | Water flow simulation        |
| **Merge Sort**  | \(O(n(log n)\) | \(O(n(log n)\) | \(O(n(log n)\) | Sorting scores in descending |

---



  
  
  


