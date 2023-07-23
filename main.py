import numpy as np
import time

# Used to calculate the total run time of the algorithm
startTime = time.time()

# Counts the number of inversions in a matrix
def count_inversions(state):
    flat_list = [elem for row in state for elem in row]
    flat_list = [flat_list[i] for i in [0, 1, 2, 5, 8, 7, 6, 3, 4]]
    inversions = 0
    for i in range(len(flat_list)):
        for j in range(i+1, len(flat_list)):
            if flat_list[j] and flat_list[i] and flat_list[i] > flat_list[j]:
                inversions += 1
    print(inversions)
    return inversions

# Function to see if the puzzle is solvable by having an even number of inversions
def isSolvable(puzzle):
 
    # Count inversions in given 8 puzzle
    inv_count = count_inversions(start)
 
    # return true if inversion count is even.
    return inv_count % 2 == 0

# Class for nodes
class Node:
    # Constructer method for the class Node. State represents the current state of the node, Parent represents the parent of the current state node, Action represents the move taken to reach the current node
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

# Class defintion for a queue based frontier used in tree and graph algorithms
class QueueFrontier:
    # Constructer method for the Queue Frontier which initializes a list
    def __init__(self):
        self.frontier = []
    # Takes in a node and appends it to the end of the stack
    def add(self, node):
        self.frontier.append(node)
    # Returns true if the state node matches any state in the frontier
    def contains_state(self, state):
        return any((node.state[0] == state[0]).all() for node in self.frontier)
    # Returns true if the frontier is an empty list
    def empty(self):
        return len(self.frontier) == 0
    # Returns and removes the first node in the frontier list, follows FIFO so it will remove the oldest node. If the frontier is empty it will raise an exception error
    def remove(self):
        if self.empty():
            raise Exception("Empty Frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

# Class definition for that defines functions for solving the 8 puzzle problem
class Puzzle:
    # Constructor method for the puzzle which intializes the start and goal state and sets the solution to none
    def __init__(self, start, startIndex, goal, goalIndex):
        self.start = [start, startIndex]
        self.goal = [goal, goalIndex]
        self.solution = None
    # Takes in a state and returns a tuple representing all the possible moves from that state. Also, creates a copy of the matrix and swaps two tiles and appends the resulting state to results, along with the move taken (up, down, left, right)
    def expand_node(self, state):
        cost = 0
        mat, (row, column) = state
        results = []
        if row > 0:
            mat1 = np.copy(mat)
            mat1[row][column] = mat[row - 1][column]
            mat1[row - 1][column] = 0
            results.append(('up', [mat1, (row - 1, column)]))
        if column > 0:
            mat1 = np.copy(mat)
            mat1[row][column] = mat[row][column - 1]
            mat1[row][column - 1] = 0
            results.append(('left', [mat1, (row, column - 1)]))
        if row < 2:
            mat1 = np.copy(mat)
            mat1[row][column] = mat[row + 1][column]
            mat1[row + 1][column] = 0
            results.append(('down', [mat1, (row + 1, column)]))
        if column < 2:
            mat1 = np.copy(mat)
            mat1[row][column] = mat[row][column + 1]
            mat1[row][column + 1] = 0
            results.append(('right', [mat1, (row, column + 1)]))
        return results
    # Puzzle method that prints out information about the puzzle game. It prints the starting and goal states of the puzzle as well as the states explored to reach the goal. It will also print the move taken at each step.
    def print(self):
        cost = 0
        solution = self.solution if self.solution is not None else None
        print("Start State:\n", self.start[0], "\n")
        print("Goal State:\n", self.goal[0], "\n")
        print("\nStates Explored: ", self.num_explored, "\n")
        print("Solution:\n ")
        for action, cell in zip(solution[0], solution[1]):
            cost += 1
            print("action: ", action, "\n", cell[0], "\n")
        print("Goal Reached!")
        print("Cost: $", cost)
    
    # Checks to see whether the given state is not already in the list of explored states
    def does_not_contain_state(self, state):
        for st in self.explored:
            if(st[0] == state[0]).all():
                return False
        return True
    
    # Solves the puzzle by using breadth first search
    # Intializes variables and nodes in which we will loop through until a solution is or is not found.
    # Within the loop we will remove a node from the frontier queue and increment the num_explored counter, and checks to see whether the removed node is the goal node.
    # If it is the goal node, then the method will construct a list contaning the action and cells that represent the solution path
    # The method will store the solution then return it
    def solve(self):
        self.num_explored = 0
        start = Node(state = self.start, parent = None, action = None)
        frontier = QueueFrontier()
        frontier.add(start)
        self.explored = []
        while True:
            if frontier.empty():
                raise Exception("No solution")
            node = frontier.remove()
            self.num_explored += 1
            if (node.state[0] == self.goal[0]).all():
                actions = []
                cells = []
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return
            self.explored.append(node.state)
            for action, state in self.expand_node(node.state):
                if not frontier.contains_state(state) and self.does_not_contain_state(state):
                    child = Node(state = state, parent = node, action = action)
                    frontier.add(child)

# Intializes the start and goal matrix
start = np.loadtxt("test3.txt", dtype = int)
goal = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])
#start = np.loadtxt("test.txt", dtype = int)
#goal = np.array([[1,2,3],[4,5,6],[7,8,0]])
#goal5 = np.array([[1,2,3],[8,0,4],[7,6,5]])
#goal = np.array([[1,2,3],[8,0,4],[7,6,5]])


# Intializes the goal and start index, you can change the index based on where the zero is in the matrix
startIndex = (1, 1)
goalIndex = (1, 1)

# If the start matrix inversions remainder is equal to zero and the goal matrix remainder is equal to zero then it should be solvable. same thing if the start matrix inversions remainder is 1 and goal matrix inversions remainder is 1
if (isSolvable(start)):
    print("Solvable")
    p = Puzzle(start, startIndex, goal, goalIndex)
    p.solve()
    p.print()
else:
    print("Not Solvable")
    
endTime = time.time()
print(endTime - startTime)

