import matplotlib as plt
import time
import numpy as np


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



def main():
    grid= np.zeros((Rows,Cols))
    print(grid)
    print("hello")

if __name__ == "__main__" :
    main()