# AI_UN-INFORMED_SEARCH_VISUALIZATION

An interactive Python tool that visualizes classic uninformed search algorithms on a 2D grid. Watch in real-time as different algorithms navigate from a start point to a goal, highlighting the exploration process, the frontier, and the final path.

🚀 Features

Real-time Visualization: Powered by "matplotlib", showing the algorithm's progress step-by-step.
Multiple Algorithms: Compare how different strategies explore the same space.
Interactive Menu: Easy-to-use terminal interface to select and run algorithms.
Dynamic Path Reconstruction: Highlights the most efficient path found once the goal is reached.

🧠 Algorithms Included

1. Breadth-First Search (BFS): Explores level by level; guaranteed to find the shortest path in an unweighted grid.
2. Depth-First Search (DFS): Explores as far as possible along each branch before backtracking.
3. Uniform Cost Search (UCS): Expands the cheapest node next (behaves like BFS here as edge weights are uniform).
4. Iterative Deepening DFS (IDDFS): Combines DFS's space-efficiency with BFS's completeness by gradually increasing depth limits.
5. Bidirectional Search: Runs two simultaneous searches—one from the start and one from the goal—meeting in the middle to reduce exploration time.


🛠️ Installation & Requirements

Ensure you have Python installed, along with the necessary libraries:

pip install matplotlib numpy


🎮 How to Run

1. Clone this repository or save the code to a file named "search_visualizer.py".
2. Run the script:

python search_visualizer.py


3. Follow the terminal prompts to select an algorithm (1-6).
4. A window will pop up showing the grid. "Yellow" represents explored nodes, "Cyan" is the current frontier, and "Purple" is the final path.


🎨 Visualization 

Color   Meaning 

White  | Unexplored / Empty Space
Green  | Start Point (0, 0) 
Red    | Goal Point (9, 9) 
Yellow | Explored Nodes (Visited) 
Cyan   | Frontier (Nodes queued for exploration) 
Purple | Final Calculated Path 


⚙️ Configuration

You can easily modify the grid size or the animation speed at the top of the script:

`Rows` / `Cols`: Change the dimensions of the grid (default is 10x10).
`Delay`: Adjust the time (in seconds) between visualization frames.
`Directions`: Currently set to allow **6-directional** movement (Up, Right, Down, Left, and two diagonals).

📝 License

This project is open-source and available under the MIT License. Feel free to use it for educational purposes!
