# 🧩 PS 49 – Maze Escape Game

A console-based maze escape game developed using **Python 3**. The player navigates through a maze using **W, A, S, D** keys to reach the exit while avoiding walls and staying within the maze boundaries.

The project demonstrates the use of **2D Lists, Functions, Classes, Movement Logic, and Breadth-First Search (BFS)** to find the shortest path from the starting point to the exit.

## 📌 Project Information

- **Project Name:** Maze Escape Game
- **Problem Statement:** PS 49
- **Programming Language:** Python 3
- **Application Type:** Console-Based Game
- **Difficulty Level:** Beginner-Friendly
- **Core Concepts:** 2D Lists, Loops, Functions, Classes, Algorithms, BFS

## 🎯 Objectives

- Create a maze using a 2D list.
- Allow the player to move using keyboard commands.
- Prevent movement through walls and outside the maze.
- Count only valid player movements.
- Find the shortest path using the Breadth-First Search algorithm.
- Provide an interactive menu and automated test cases.

## 🎮 Game Preview

The maze uses the following symbols:

| Symbol | Meaning |
|---|---|
| `P` | Player / Starting Position |
| `#` | Wall |
| `.` | Empty Path |
| `E` | Exit |
| `*` | Shortest Path |

### Maze Layout

```text
P . . # #
# # . # #
# . . . #
# . # # #
# . . . E
```

The objective is to move the player from `P` to `E` without crossing any walls.

## 🕹️ Controls

| Key | Action |
|---|---|
| `W` | Move Up |
| `A` | Move Left |
| `S` | Move Down |
| `D` | Move Right |
| `Q` | Quit the current game and return to the menu |

Invalid keys are rejected, and movements blocked by walls or maze boundaries do not count toward the total moves.

## ✨ Features

- **Interactive Menu:** Play, view the shortest path, or quit.
- **Player Movement:** Move in four directions using W/A/S/D.
- **Collision Detection:** Prevents the player from crossing walls.
- **Boundary Checking:** Keeps the player inside the maze.
- **Move Counter:** Tracks valid movements only.
- **Shortest Path Finder:** Uses BFS to calculate the shortest route.
- **Route Visualization:** Displays the shortest path using `*` symbols.
- **Scripted Gameplay:** Run a predefined sequence of moves.
- **Automated Testing:** Checks expected game behavior using five test cases.

## 🧠 Concepts Used

### 1. Two-Dimensional Lists

The maze is represented as a list of lists, with each inner list representing a row.

```python
def build_maze():
    return [list(row) for row in MAZE_ROWS]
```

### 2. Functions

Functions such as `find_cell()`, `inside()`, and `attempt_move()` organize the code into reusable components.

### 3. Classes and Objects

The `Game` class maintains the player's position, maze, move count, and winning status.

### 4. Breadth-First Search (BFS)

BFS explores reachable cells level by level using a queue. It finds the shortest path in an unweighted maze where each movement has equal cost.

### 5. Testing

The program includes automated tests for normal movement, boundary conditions, invalid input, successful escape, and shortest-path calculation.

## ⚙️ Requirements

- Python 3.8 or later recommended
- A terminal or command prompt
- Any Python-compatible code editor, such as VS Code or IDLE

No external libraries are required. The project uses Python's built-in modules.

## 🚀 Installation and Execution

### Step 1: Save the Python File

Save your Python code as:

```text
maze_escape.py
```

### Step 2: Open the Terminal

Navigate to the directory containing `maze_escape.py`.

### Step 3: Run the Game

```bash
python maze_escape.py
```

### Step 4: Select a Menu Option

```text
=== MAZE ESCAPE GAME ===
1. Play
2. Shortest path (BFS)
3. Quit
Choose an option:
```

Enter `1` to play, `2` to view the shortest path, or `3` to quit.

## 🧪 Running the Test Cases

Run all automated test cases with:

```bash
python maze_escape.py --test
```

The program reports whether each test passes or fails.

### Run a Specific Sequence of Moves

```bash
python maze_escape.py --moves DDSSASSDDD
```

This executes a predefined sequence of movements without requiring interactive input.

### Expected Test Scenarios

1. **Normal Input:** The player moves right using `D`.
2. **Boundary Condition:** The player attempts to move up from `(0, 0)`.
3. **Invalid Input:** The player attempts an invalid key after moving.
4. **Successful Escape:** The player reaches the exit using a valid move sequence.
5. **Shortest Path:** BFS calculates and displays the shortest route.

## 📂 Project Structure

```text
Maze-Escape-Game/
│
├── maze_escape.py    # Main Python program
└── README.md         # Project documentation
```

## ⏱️ Algorithm and Complexity

Let `R` be the number of rows and `C` be the number of columns in the maze.

- **BFS Time Complexity:** `O(R × C)`
- **BFS Space Complexity:** `O(R × C)`

Each reachable cell is visited at most once, and each cell has at most four neighboring cells.

## 🔮 Future Improvements

- Add multiple maze levels and increasing difficulty.
- Allow custom maze sizes.
- Add a timer and high-score system.
- Introduce random maze generation.
- Add a graphical user interface using Tkinter or Pygame.
- Provide hints and automatic player navigation.

## 🎓 Learning Outcomes

By completing this project, students can learn how to:

- Work with 2D lists in Python.
- Apply conditional statements and loops.
- Create modular programs using functions and classes.
- Implement basic game movement and collision detection.
- Understand queue-based graph traversal.
- Apply BFS to solve shortest-path problems.
- Write automated tests to validate program behavior.

## 👨‍💻 Author

**Project:** PS 49 – Maze Escape Game  
**Language:** Python 3

---

*This project is designed as a beginner-friendly demonstration of Python programming and basic algorithmic problem-solving.*
