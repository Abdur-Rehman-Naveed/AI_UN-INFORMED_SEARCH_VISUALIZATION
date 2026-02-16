import matplotlib.pyplot as plt
import time
import numpy as np
from matplotlib.colors import ListedColormap
from collections import deque

Rows=10
Cols=10
Delay=0.1

Directions=[
   (-1, 0),   # Up
   (0, 1),    # Right
   (1, 1),    # Bottom-Right
   (1, 0),    # Bottom
   (0, -1),   # Left
   (-1, -1)   # Top-Left
]

def update_screen(grid,start,goal,visited,selected,path):
    display=np.copy(grid)

    for r, c in visited:
        display[r][c] = 2  # visited

    for r, c in selected:
        display[r][c] = 3  # selected

    for r, c in path:
        display[r][c] = 4  # path

    display[start] = 5   
    display[goal] = 6    

    plt.clf()
    plt.title("UNINFORMED SEARCH VISUALIZER",fontsize=15)
    colors_map = ListedColormap([
        "white",   # 0 empty
        "black",   # 1 (unused)
        "yellow",  # 2 explored
        "blue",    # 3 frontier
        "purple",  # 4 final path
        "green",   # 5 start
        "red"      # 6 goal
    ])

    plt.imshow(display, cmap=colors_map)

    # setting the axis marks and grid lines 
    plt.xticks(np.arange(-.5, Cols, 1), [])
    plt.yticks(np.arange(-.5, Rows, 1), [])
    plt.grid(color='gray', linestyle='-', linewidth=0.5)

    plt.pause(Delay)

#check validity of the move
def valid(r, c):
    return 0 <= r < Rows and 0 <= c < Cols

# to rebuild shortest path
def reconstruct(parent, goal):
    path = []
    while goal in parent:
        path.append(goal)
        goal = parent[goal]
    return path[::-1]


#bfs uninformed search algorithm

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

        update_screen(grid, start, goal, explored, list(queue), [])

    return []

def main():
    grid= np.zeros((Rows,Cols))
    start=(0,0)
    goal=(Rows-1,Cols-1)
    plt.figure(figsize=(6,6))

    path=bfs(grid,start,goal)
    update_screen(grid,start,goal,[],[],path)
    plt.show()

if __name__ == "__main__" :
    main()