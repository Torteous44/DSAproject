### `main.py`
- **Purpose**: Primary entry point for the game.
- **Functionality**: Manages the game loop, loads the menu, and initiates the gameplay for a selected level.
  - **Process**:
    - Calls `menu()` from `menu.py` to display the main menu and obtain the player’s level choice.
    - If a level is chosen, it starts gameplay by calling `play_level` from `gameplay.py`.
    - Once gameplay finishes, it displays the score or redirects back to the menu for another level.

### `menu.py`
- **Purpose**: Provides the main menu interface for level selection and viewing scores.
- **Functionality**:
  - Displays the title, list of levels, and best score for each level.
  - Detects mouse clicks on level options to initiate level selection.
  - Uses `load_scores` from `score_manager.py` to display previous high scores.
  - **Process**:
    - `draw_menu()` renders level options with best scores and clickable rectangles.
    - `menu()` listens for mouse events and returns the selected level index.

### `settings.py`
- **Purpose**: Stores core configurations and level data.
- **Functionality**:
  - Defines game constants, including screen dimensions, colors, and file paths.
  - Contains a list of level configurations, each with `terrain`, `origin`, `drain`, `target_score`, and `optimal_path_length`.
  - **Process**:
    - Other modules reference `settings.py` for configurations, ensuring consistency across the project.

### `display.py`
- **Purpose**: Handles all game visuals, including the terrain grid and water animation.
- **Functionality**:
  - `draw_grid()` renders the grid with terrain heights, origin, and drain markers.
  - `show_water_path()` animates water flow along a determined path from `simulation.py`.
  - **Process**:
    - Reads terrain data and modifies cell colors based on height or water flow, calling Pygame’s `draw.rect` and `update()` functions to reflect changes on the screen.

### `gameplay.py`
- **Purpose**: Manages gameplay interactions within a level.
- **Functionality**:
  - `play_level()` is the primary function for handling in-level gameplay.
  - Manages terrain modifications and scoring adjustments, and initiates the water flow simulation when the player chooses to “Run.”
  - **Process**:
    - Processes mouse events to increase or decrease cell height.
    - Calls `run_simulation()` from `simulation.py` when the player is ready to simulate water flow.
    - Tracks score adjustments based on moves and path length.

### `terrain.py`
- **Purpose**: Initializes and manages the terrain grid.
- **Functionality**:
  - Sets up each cell with stack heights using `Stack` objects, representing the height of terrain at each point.
  - Contains methods to adjust heights (increase/decrease) based on player clicks.
  - **Process**:
    - `initialize_terrain()` loads terrain data for the chosen level and sets initial heights.
    - `handle_click()` adjusts cell heights upon player input.
    - `get_matrix_snapshot()` creates a matrix of current heights for pathfinding.

### `simulation.py`
- **Purpose**: Runs the water flow simulation from origin to drain.
- **Functionality**:
  - `run_simulation()` animates water flow along a determined path.
  - `water_path_dfs()` uses depth-first search (DFS) to compute the shortest path, if possible, from origin to drain based on the current terrain.
  - **Process**:
    - Calculates water flow direction based on height comparisons between cells.
    - Animates the flow on screen, and checks if the path reaches the drain within the optimal path length.

### `score_manager.py`
- **Purpose**: Tracks and manages scoring for gameplay.
- **Functionality**:
  - `GameScore` class: Calculates score based on terrain modifications and path length.
  - `load_scores()` and `save_score()` functions handle score storage, saving high scores to `scores.json`.
  - **Process**:
    - `add_modification()` deducts points for height changes.
    - `set_path_length()` deducts points only if the player’s path exceeds the optimal path length.
    - `final_score()` returns the final score for a level, ensuring it remains non-negative.

### `audio.py`
- **Purpose**: Provides sound effects for in-game actions.
- **Functionality**:
  - `play_click_sound()` plays a sound when the player modifies terrain.
  - `play_water_flow_sound()` plays a sound when the water flow simulation begins.
  - **Process**:
    - Loads audio files specified in `settings.py` and plays them using Pygame’s mixer functionality, triggered by actions in `gameplay.py`.

### `waterLogic.py`
- **Purpose**: Defines water flow rules based on terrain heights.
- **Functionality**:
  - `waterPath()` determines viable paths based on cell heights, allowing water to flow from a higher to a lower cell.
  - **Process**:
    - Implements logic to check if water can move from the current cell to neighboring cells based on terrain height.
    - Returns a path or confirms that no path is possible based on the current terrain setup.
