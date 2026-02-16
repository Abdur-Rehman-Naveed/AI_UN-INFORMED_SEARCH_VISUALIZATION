import matplotlib.pyplot as plt
import time
import numpy as np
from matplotlib.colors import ListedColormap


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


def main():
    grid= np.zeros((Rows,Cols))
    start=(0,0)
    goal=(Rows-1,Cols-1)
    plt.figure(figsize=(6,6))
    update_screen(grid,start,goal,[],[],[])
    plt.show()

if __name__ == "__main__" :
    main()