

### **Data Structures**

#### **1. Stacks**  
- **Purpose:** Represents the height of terrain blocks in the game.  
- **Implementation:** 
  - Each grid cell is a stack.
  - The stack is implemented using a linked list, where each `Node` stores the height level of the terrain.  
- **Key Operations:**  
  - **Push:** Adds height to the terrain when increasing block height.  
  - **Pop:** Decreases height when reducing block height.  
  - **Peek:** Retrieves the current height of a terrain cell without modifying it.  
- **Files:** `terrain.py`  

#### **2. Nodes**  
- **Purpose:** Building blocks of the linked list-based stack, where each node represents a single terrain height level.  
- **Implementation:** Each node contains a `value` (height) and a reference to the next node in the stack.  
- **Files:** `terrain.py`  

#### **3. 2D Matrix (Grid)**  
- **Purpose:** Represents the terrain as a grid, where each cell contains a stack.  
- **Usage:**  
  - Traversed for rendering the terrain in pseudo-3D.  
  - Used for water flow simulation.  
- **Files:** `terrain.py`, `simulation.py`, `display.py`  

#### **4. Sets**  
- **Purpose:** Tracks visited cells during the simulation of water flow to prevent revisiting.  
- **Benefit:** Efficient for membership checks, making traversal algorithms like DFS more optimal.  
- **Files:** `simulation.py`  

#### **5. Dictionaries**  
- **Purpose:** Stores and retrieves scores for each level using level indices as keys.  
- **Usage:**  
  - Retrieve the best score for a level.  
  - Update and save scores.  
- **Files:** `score_manager.py`  

---

### **Algorithms**

#### **1. Depth-First Search (DFS)**  
- **Purpose:** Simulates water flow from the faucet to the drain.  
- **Implementation:**  
  - Explores all possible paths from the origin to the drain by traversing neighboring cells.  
  - Stops when the drain is reached or all options are exhausted.  
- **Files:** `simulation.py`  

#### **2. Stack Operations**  
- **Purpose:** Modify the height of terrain blocks.  
- **Implementation:**  
  - **Push:** Adds a new height level when increasing the terrain height.  
  - **Pop:** Removes the top height level when decreasing terrain height.  
  - **Peek:** Retrieves the current height level of a terrain block.  
- **Files:** `terrain.py`  

#### **3. Grid Traversal**  
- **Purpose:** Iterates through the grid to render or update terrain state.  
- **Implementation:** Nested loops iterate over rows and columns of the 2D matrix.  
- **Files:** `terrain.py`, `display.py`  

#### **4. File I/O**  
- **Purpose:** Manages score persistence by reading and writing to a JSON file.  
- **Usage:**  
  - Loads saved scores when the game starts.  
  - Updates scores if a new high score is achieved.  
- **Files:** `score_manager.py`  

---

### **Summary**

#### **Data Structures:**
- Stacks (linked list implementation).
- Nodes (linked list elements).
- 2D Matrix (Grid).
- Sets.
- Dictionaries.

#### **Algorithms:**
- Depth-First Search (DFS).
- Stack Operations.
- Grid Traversal.
- File I/O for score management. 
