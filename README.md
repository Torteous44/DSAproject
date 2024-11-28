### **WaterRouter: README**

Welcome to **WaterRouter**, a terrain-modifying puzzle game where you guide water from a faucet to a drain while optimizing terrain for maximum points. 

---

### Contents
- [Features](#Features)
- [Installation and Setup](#Installation-and-Setup)
- [Game Controls](#Game-Controls)
- [File Breakdown](#File-Breakdown)
- [Complexity Analysis](#Complexity-Analysis)

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

Below is an overview of the key files and their respective roles in the game:

#### 1. **assets Directory**  
Contains all the media resources used in the game:
- **"images" Folder**: Stores the images for the game, including the drain and water faucet visuals.
- **"sounds" Folder**: Holds sound files for in-game audio effects.

#### 2. **src Directory**  
This folder contains the core game logic and utilities.

**Core Files:**
- **audio.py**: Manages the playback of sound effects during gameplay.
- **display.py**: Handles the graphical rendering of the game, including the grid and visual elements.
- **gameplay.py**: Contains the logic for playing a specific level, including terrain manipulation and water flow simulation.
- **menu.py**: Responsible for generating and managing the main menu screen.
- **settings.py**: Defines the game settings such as screen size, level configurations, and terrain layout.
- **simulation.py**: Implements the **Depth First Search (DFS)** algorithm to simulate water flow across the grid.
- **terrain.py**: Handles the generation of the terrain matrix, including stack heights that define the landscape for each level.

**Utility Files:**
- **end_of_level.py**: Manages the end-of-level screen and displays the results when a player completes a level.
- **score_manager.py**: Calculates and updates the player’s score, and sorts scores using the **Merge Sort** algorithm.

#### 3. **tests.py**  
This file contains various code snippets and functions designed for testing different features and mechanics of the game.

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
   - DFS explores parts of the terrain but eliminates unnecessary branches.

3. **Worst Case**: \(O(V + E)\)
   - **Scenario**: The terrain has no direct path, requiring the algorithm to explore nearly the entire grid.
   - The algorithm explores most paths due to backtracking.

**Where:**
- V = Number of cells in the grid (rows × columns).
- E = Edges connecting the cells (up to 8 edges per cell for diagonals).

### **Merge Sort Algorithm:**

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

### *Note*:

Additional documentation of the complexity analysis for all the other functions used are commented above the function themselves.




  
  
  


