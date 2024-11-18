### **WaterRouter: README**

Welcome to **WaterRouter**, a terrain-modifying puzzle game where you guide water from a faucet to a drain while optimizing terrain for maximum points. 

---

### **Features**
1. Modify terrain heights using stacks.
2. Simulate water flow in pseudo-3D.
3. Multiple levels of increasing difficulty.
4. Scoring system based on path length and terrain modifications.
5. Persistent high scores with a reset option.
6. Intro screen, instructions, and a visually appealing menu.

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

### **Project Structure**

#### **Core Scripts**
- **`main.py`**: Entry point; manages intro, menu, and gameplay flow.
- **`menu.py`**: Handles the intro screen and level selection menu.
- **`gameplay.py`**: Manages level-specific gameplay.
- **`settings.py`**: Stores configurations like terrain, levels, and visual settings.
- **`terrain.py`**: Implements the stack-based terrain system.
- **`simulation.py`**: Simulates water flow using Depth-First Search.
- **`display.py`**: Renders the grid, terrain, and water animations.
- **`score_manager.py`**: Handles scoring, saving, and resetting scores.

#### **Assets**
- **`assets/faucet.png`**: Faucet icon.
- **`assets/drain.png`**: Drain icon.
- **`sounds/click_sound.mp3`**: Click effect for terrain changes.
- **`sounds/water.mp3`**: Flow effect during water simulation.