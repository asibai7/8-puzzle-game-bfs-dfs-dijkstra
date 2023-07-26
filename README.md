# 8-puzzle-game-bfs-dfs-dijkstra

Wrote a program which solves the 8 puzzle game by 3 different algorithms: BFS, DFS, and Dijkstra.

Solving the 8 puzzle problem with BFS

1) Have python 3.5 or higher installed on your development environment of your choice 
2) Install numpy on your computer by using "pip install numpy" in your environment
3) Download the zipped file and extract the folder to a destination of your choice
4) Open the folder in your development environment and select main.py
5) I've included 3 test cases given in the Final Project PDF, so to change each initial state you can change line 147 to "test.txt", "test2.txt", and "test3.txt" for each case
6) Open a new terminal and run "python3 main.py" to see the cost and the steps it takes to get to the goal state

Solving the 8 puzzle problem with DFS

1. Open the dfs python file in addition to the input.txt file
2. Edit the input.txt file to include the initial state you want to test
3. Run the code using a python compiler where the command line will be python dfs.py for example
4. The code will then use the program to determine if your code is solvable or not
5. If it is solvable, it will also output the cost to find the goal state using DFS

Solving the 8 puzzle problem with Dijkstra's Algorithm 

1. Have Python 3.5 or above installed on your computer and viable IDE such as VScode
2. Save the code as a .py file
3. Create an input text file with the initial state of the program. The format should follow the below example:
1 3 4
8 0 2 
7 6 5
Ensure that the input text file is within the same directory as the program
4. Open a terminal and run the code by typing 'python dijsktra.py'. This will execute the program and generate an output file with the goal state based on the initial state
5. Open the text file to see the goal state of the puzzle
