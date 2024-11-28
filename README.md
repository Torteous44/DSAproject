### **WaterRouter: README**

Welcome to **WaterRouter**, a terrain-modifying puzzle game where you guide water from a faucet to a drain while optimizing terrain for maximum points. 

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
**This file is used to store coded to be tested for our game.**
  
  
  


