"""
PS 49 - Maze Escape Game
Language : Python 3
Concepts : 2D Lists, Algorithms (BFS), Movement

A console maze game. The maze is a 2D list (list of lists). The player moves
with W/A/S/D, walls and the maze border block movement (and are not counted),
and a Breadth-First Search finds the shortest path from start to exit.

Usage
-----
  python maze_escape.py                 interactive menu
  python maze_escape.py --moves DDSSASSDDD   run a scripted move string
  python maze_escape.py --test          run the 4 required test cases
"""

import io
import sys
from collections import deque
from contextlib import redirect_stdout

# ----------------------------------------------------------------------------
# Maze definition  (# wall, . path, P start, E exit)
# ----------------------------------------------------------------------------
MAZE_ROWS = [
    "P..##",
    "##.##",
    "#...#",
    "#.###",
    "#...E",
]

WALL, PATH, START, EXIT = "#", ".", "P", "E"

# key -> (row change, column change)
DIRECTIONS = {
    "W": (-1, 0),   # up
    "A": (0, -1),   # left
    "S": (1, 0),    # down
    "D": (0, 1),    # right
}


def build_maze():
    """Return the maze as a 2D list (list of lists of characters)."""
    return [list(row) for row in MAZE_ROWS]


def find_cell(maze, symbol):
    """Return (row, col) of the first cell equal to symbol, or None."""
    for r, row in enumerate(maze):
        for c, cell in enumerate(row):
            if cell == symbol:
                return (r, c)
    return None


def inside(maze, r, c):
    """True when (r, c) lies inside the maze."""
    return 0 <= r < len(maze) and 0 <= c < len(maze[0])


def print_maze(maze, player, path=None):
    """Print the maze with the player's current position marked as P.

    Cells listed in `path` (other than start/exit) are drawn as '*'.
    """
    on_path = set(path or [])
    for r, row in enumerate(maze):
        line = []
        for c, cell in enumerate(row):
            if (r, c) == player:
                line.append("P")
            elif cell == EXIT:
                line.append("E")
            elif (r, c) in on_path and cell != WALL:
                line.append("*")
            elif cell == START:
                line.append(PATH)          # start tile is just a path tile
            else:
                line.append(cell)
        print(" ".join(line))


# ----------------------------------------------------------------------------
# Movement
# ----------------------------------------------------------------------------
def attempt_move(maze, position, key):
    """Try to move one step.

    Returns (new_position, status) where status is one of
    'moved', 'wall', 'outside', 'invalid'.
    """
    if key not in DIRECTIONS:
        return position, "invalid"
    dr, dc = DIRECTIONS[key]
    nr, nc = position[0] + dr, position[1] + dc
    if not inside(maze, nr, nc):
        return position, "outside"
    if maze[nr][nc] == WALL:
        return position, "wall"
    return (nr, nc), "moved"


class Game:
    """Holds the state of one play-through."""

    def __init__(self):
        self.maze = build_maze()
        self.start = find_cell(self.maze, START)
        self.exit = find_cell(self.maze, EXIT)
        self.position = self.start
        self.moves = 0          # only valid moves are counted
        self.won = False

    def press(self, key):
        """Process one key press, print the result and the maze."""
        key = key.upper()
        self.position_before = self.position
        self.position, status = attempt_move(self.maze, self.position, key)
        r, c = self.position

        if status == "moved":
            self.moves += 1
            print(f"Player moved to (row {r}, col {c}) | Moves: {self.moves}")
        elif status == "outside":
            print(f"Cannot move outside the maze. Player stays at ({r}, {c}) "
                  f"| Moves: {self.moves}")
        elif status == "wall":
            print(f"Wall ahead. Move blocked. Player stays at ({r}, {c})")
        else:
            print(f"Invalid key '{key}'. Use W, A, S or D only.")

        print_maze(self.maze, self.position)

        if self.position == self.exit:
            self.won = True
            print(f"You escaped the maze! Total moves: {self.moves}")
        return status


# ----------------------------------------------------------------------------
# Breadth-First Search
# ----------------------------------------------------------------------------
def bfs_shortest_path(maze, start, goal):
    """Return the shortest path as a list of (row, col), or None."""
    queue = deque([start])
    parent = {start: None}                 # also acts as the visited set
    while queue:
        current = queue.popleft()
        if current == goal:
            break
        for dr, dc in DIRECTIONS.values():
            nr, nc = current[0] + dr, current[1] + dc
            nxt = (nr, nc)
            if inside(maze, nr, nc) and maze[nr][nc] != WALL and nxt not in parent:
                parent[nxt] = current
                queue.append(nxt)
    if goal not in parent:
        return None
    path, node = [], goal
    while node is not None:
        path.append(node)
        node = parent[node]
    return path[::-1]


def path_to_keys(path):
    """Convert a list of cells into a W/A/S/D key sequence."""
    reverse = {v: k for k, v in DIRECTIONS.items()}
    return [reverse[(b[0] - a[0], b[1] - a[1])] for a, b in zip(path, path[1:])]


def show_shortest_path():
    """Menu option 2: display the BFS shortest path from start to exit."""
    maze = build_maze()
    start, goal = find_cell(maze, START), find_cell(maze, EXIT)
    path = bfs_shortest_path(maze, start, goal)
    if path is None:
        print("No path exists from start to exit.")
        return
    print(f"Shortest path length: {len(path) - 1} steps")
    print("Route: " + " ".join(path_to_keys(path)))
    print("Cells: " + " -> ".join(f"({r},{c})" for r, c in path))
    print_maze(maze, start, path)


# ----------------------------------------------------------------------------
# Modes
# ----------------------------------------------------------------------------
def run_scripted(moves):
    """Play a whole string of keys, e.g. 'DDSSASSDDD'."""
    game = Game()
    print_maze(game.maze, game.position)
    for key in moves:
        if game.won:
            break
        game.press(key)
    print(f"Moves counted: {game.moves}")
    return game


def play_interactive():
    game = Game()
    print("\nMove with W (up), A (left), S (down), D (right). Q returns to the menu.")
    print_maze(game.maze, game.position)
    while not game.won:
        try:
            keys = input("Move: ").strip()
        except EOFError:
            return
        for key in keys:
            if key.upper() == "Q":
                return
            game.press(key)
            if game.won:
                break


def menu():
    while True:
        print("\n=== MAZE ESCAPE GAME ===")
        print("1. Play")
        print("2. Shortest path (BFS)")
        print("3. Quit")
        try:
            choice = input("Choose an option: ").strip()
        except EOFError:
            return
        if choice == "1":
            play_interactive()
        elif choice == "2":
            show_shortest_path()
        elif choice == "3":
            print("Goodbye!")
            return
        else:
            print("Invalid option. Enter 1, 2 or 3.")


# ----------------------------------------------------------------------------
# Test cases from the problem statement
# ----------------------------------------------------------------------------
def capture(func, *args):
    """Run func and return everything it printed, as a list of lines."""
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        func(*args)
    return [line.strip() for line in buffer.getvalue().splitlines()]


TEST_CASES = [
    ("Test Case 1: Normal Input (Move: D)",
     run_scripted, ("D",),
     ["Player moved to (row 0, col 1) | Moves: 1"]),
    ("Test Case 2: Boundary (Move: W at (0, 0))",
     run_scripted, ("W",),
     ["Cannot move outside the maze. Player stays at (0, 0) | Moves: 0"]),
    ("Test Case 3: Invalid Input (Moves: D, D, D, X)",
     run_scripted, ("DDDX",),
     ["Wall ahead. Move blocked. Player stays at (0, 2)",
      "Invalid key 'X'. Use W, A, S or D only.",
      "Moves counted: 2"]),
    ("Test Case 4a: Valid Scenario (D, D, S, S, A, S, S, D, D, D)",
     run_scripted, ("DDSSASSDDD",),
     ["You escaped the maze! Total moves: 10"]),
    ("Test Case 4b: Menu option 2 (Shortest path)",
     show_shortest_path, (),
     ["Shortest path length: 10 steps"]),
]


def run_tests():
    """Run every test case and report PASS/FAIL. Returns True if all pass."""
    all_ok = True
    for title, func, args, expected in TEST_CASES:
        lines = capture(func, *args)
        missing = [e for e in expected if e not in lines]
        ok = not missing
        all_ok = all_ok and ok
        print(f"[{'PASS' if ok else 'FAIL'}] {title}")
        for e in expected:
            print(f"        expected: {e}")
        for m in missing:
            print(f"        MISSING : {m}")
    print("\nAll test cases passed." if all_ok else "\nSome test cases failed.")
    return all_ok


def main():
    args = sys.argv[1:]
    if args and args[0] == "--test":
        sys.exit(0 if run_tests() else 1)
    if args and args[0] == "--moves":
        run_scripted(args[1] if len(args) > 1 else "")
        return
    menu()


if __name__ == "__main__":
    main()