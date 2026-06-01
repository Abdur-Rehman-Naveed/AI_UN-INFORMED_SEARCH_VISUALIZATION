import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from collections import deque
import heapq
import sys

Rows = 10  
Cols = 10
Delay = 0.05 

Directions = [
    (-1, 0),  # Up
    (0, 1),   # Right
    (1, 0),   # Down
    (1, 1),   # Bottom-Right
    (0, -1),  # Left
    (-1, -1)  # Top-Left
    
]

def update_screen(grid, start, goal, visited, selected, path, title="Search Visualizer"):
    display = np.copy(grid)

    # 2: Visited (Closed Set)
    for r, c in visited:
        display[r][c] = 1 

    # 3: Frontier (Open Set / Selected)
    for r, c in selected:
        display[r][c] = 2

    # 4: Final Path
    for r, c in path:
        display[r][c] = 3 

    display[start] = 4   
    display[goal] = 5   

    plt.clf()
    plt.title(title, fontsize=15)
    
    colors_map = ListedColormap([
        "white",   # 0: Empty
        "yellow",  # 1: Visited/Explored
        "cyan",    # 2: Frontier/Selected
        "purple",  # 3: Path
        "green",   # 4: Start
        "red"      # 5: Goal
    ])

    if not path:
        display[0][0] = display[0][0] 

    plt.imshow(display, cmap=colors_map, vmin=0, vmax=6)

    plt.xticks(np.arange(-.5, Cols, 1), [])
    plt.yticks(np.arange(-.5, Rows, 1), [])
    plt.grid(color='gray', linestyle='-', linewidth=0.5)

    plt.pause(Delay)

def valid(r, c):
    return 0 <= r < Rows and 0 <= c < Cols

def reconstruct(parent, current):
    path = []
    while current in parent:
        path.append(current)
        current = parent[current]
    path.append(current)
    return path[::-1]

# UNINFORMED SEARCH ALGORITHMS

def bfs(grid, start, goal):
    queue = deque([start])
    visited = set([start])
    parent = {}
    explored = []

    while queue:
        current = queue.popleft()
        explored.append(current)

        if current == goal:
            return reconstruct(parent, goal)

        for move in Directions:
            new_row, new_col = current[0] + move[0], current[1] + move[1]
            if valid(new_row, new_col) and (new_row, new_col) not in visited:
                queue.append((new_row, new_col))
                visited.add((new_row, new_col))
                parent[(new_row, new_col)] = current

        update_screen(grid, start, goal, explored, list(queue), [], "Breadth-First Search (BFS)")

    return []

def dfs(grid, start, goal):
    stack = [start]
    visited = set()
    parent = {}
    explored = []

    while stack:
        current = stack.pop()
        
        if current not in visited:
            visited.add(current)
            explored.append(current)

            if current == goal:
                return reconstruct(parent, goal)

            # Reversed directions usually helps DFS look more natural in grid
            for move in reversed(Directions):
                new_row, new_col = current[0] + move[0], current[1] + move[1]
                if valid(new_row, new_col) and (new_row, new_col) not in visited:
                    stack.append((new_row, new_col))
                    parent[(new_row, new_col)] = current

        update_screen(grid, start, goal, explored, stack, [], "Depth-First Search (DFS)")

    return []

def ucs(grid, start, goal):
    pq = []
    heapq.heappush(pq, (0, start))
    visited = set()
    parent = {}
    cost = {start: 0}
    explored = []

    while pq:
        current_cost, current = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)
        explored.append(current)

        if current == goal:
            return reconstruct(parent, goal)

        for move in Directions:
            new_row, new_col = current[0] + move[0], current[1] + move[1]
            if valid(new_row, new_col):
                new_cost = current_cost + 1 # Uniform cost of 1
                if (new_row, new_col) not in cost or new_cost < cost.get((new_row, new_col), float('inf')):
                    cost[(new_row, new_col)] = new_cost
                    parent[(new_row, new_col)] = current
                    heapq.heappush(pq, (new_cost, (new_row, new_col)))

        # Extract nodes from priority queue
        frontier_nodes = [node[1] for node in pq]
        update_screen(grid, start, goal, explored, frontier_nodes, [], "Uniform Cost Search (UCS)")

    return []

def dls(grid, current, goal, limit, parent, explored, start):
    if current == goal:
        return True
    if limit <= 0:
        return False

    explored.append(current)
    update_screen(grid, start, goal, explored, [], [], f"DLS (Depth Limit: {limit})")

    for move in Directions:
        new_row, new_col = current[0] + move[0], current[1] + move[1]
        if valid(new_row, new_col) and (new_row, new_col) not in parent:
            parent[(new_row, new_col)] = current
            if dls(grid, (new_row, new_col), goal, limit-1, parent, explored, start):
                return True
    return False

def iddfs(grid, start, goal):
    max_depth = Rows * Cols
    for depth in range(1, max_depth):
        parent = {}
        explored = []
        # Reset parent for start node
        if dls(grid, start, goal, depth, parent, explored, start):
            return reconstruct(parent, goal)
    return []

def bidirectional(grid, start, goal):
    q_start = deque([start])
    q_goal = deque([goal])

    visited_start = {start: None}
    visited_goal = {goal: None}

    explored = []

    while q_start and q_goal:
        if q_start:
            s = q_start.popleft()
            explored.append(s)
            
            for move in Directions:
                new_row, new_col = s[0] + move[0], s[1] + move[1]
                nxt = (new_row, new_col)
                if valid(new_row, new_col) and nxt not in visited_start:
                    visited_start[nxt] = s
                    q_start.append(nxt)
                    if nxt in visited_goal:
                        return build_path_bidirectional(visited_start, visited_goal, nxt)

        # Expand from Goal
        if q_goal:
            g = q_goal.popleft()
            explored.append(g)

            for move in Directions:
                new_row, new_col = g[0] + move[0], g[1] + move[1]
                nxt = (new_row, new_col)
                if valid(new_row, new_col) and nxt not in visited_goal:
                    visited_goal[nxt] = g
                    q_goal.append(nxt)
                    if nxt in visited_start:
                        return build_path_bidirectional(visited_start, visited_goal, nxt)

        update_screen(grid, start, goal, explored, list(q_start)+list(q_goal), [], "Bidirectional Search")

    return []

def build_path_bidirectional(vs, vg, meet):
    # Path from start to meet
    path_start = []
    curr = meet
    while curr:
        path_start.append(curr)
        curr = vs[curr]
    path_start.reverse()

    # Path from meet to goal
    path_goal = []
    curr = vg[meet] # Start from parent of meet
    while curr:
        path_goal.append(curr)
        curr = vg[curr]

    return path_start + path_goal


def main_menu():
    grid = np.zeros((Rows, Cols))
    start = (0, 0)
    goal = (Rows-1, Cols-1)
    
    # Enabling interactive mode for smoother animation
    plt.ion() 

    while True:
        print("\n" + "="*30)
        print(" UNINFORMED SEARCH VISUALIZER")
        print("="*30)
        print("1. Breadth-First Search (BFS)")
        print("2. Depth-First Search (DFS)")
        print("3. Uniform Cost Search (UCS)")
        print("4. Iterative Deepening (IDDFS)")
        print("5. Bidirectional Search")
        print("6. Exit")
        print("-" * 30)

        choice = input("Select Algorithm (1-6): ")
        path = []
        
        # Reset Plot
        plt.close('all')
        plt.figure(figsize=(6, 6))

        if choice == '1':
            path = bfs(grid, start, goal)
        elif choice == '2':
            path = dfs(grid, start, goal)
        elif choice == '3':
            path = ucs(grid, start, goal)
        elif choice == '4':
            path = iddfs(grid, start, goal)
        elif choice == '5':
            path = bidirectional(grid, start, goal)
        elif choice == '6':
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid selection. Try again.")
            continue

        # Show Final Path
        if path:
            print(f"Path Found! Length: {len(path)}")
            update_screen(grid, start, goal, [], [], path, "Path Found!")
        else:
            print("No path found.")
        
        # Keep window open until user closes it or presses a key
        print("Check the visualization window.")
        plt.show(block=True)
        
if __name__ == "__main__":
    main_menu()