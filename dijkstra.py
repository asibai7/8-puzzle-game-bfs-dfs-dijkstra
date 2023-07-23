import heapq
import time 

#Time function for start time
starTime = time.time()
#Class Puzzle for the State 
class Puzzle:
    # Initializes a new puzzle object with the given state, actual cost, previous puzzle object, 
    # and the move that led to the current state
    def __init__(self, state, cost=0, prev=None, move=0):
        self.state = state
        self.actual_cost = cost
        self.prev = prev
        self.move = move
    # Defines less than operation for puzzle objects based on their actual cost
    def __lt__(self, other):
        return self.actual_cost < other.actual_cost
    # Defines equality operation for puzzle objects based on their state
    def __eq__(self, other):
        return self.state == other.state
    # Defines hash function for puzzle objects based on their state
    def __hash__(self):
        return hash(str(self.state))
    # Returns the index of the blank tile (0) in the puzzle state
    def get_blank_index(self):
        return self.state.index(0)
    #Returns a list of neighbor puzzle objects that can be obtained by moving the blank tile up, down, left, or right
    def get_neighbors(self):
        neighbors = []
        index = self.get_blank_index()
        row, col = index // 3, index % 3 
        if row > 0:
            new_state = self.state.copy()
            new_state[index], new_state[index-3] = new_state[index-3], new_state[index]
            neighbors.append(Puzzle(new_state, self.actual_cost+new_state[index], self, new_state[index]))
        if row < 2:
            new_state = self.state.copy()
            new_state[index], new_state[index+3] = new_state[index+3], new_state[index]
            neighbors.append(Puzzle(new_state, self.actual_cost+new_state[index], self, new_state[index]))
        if col > 0:
            new_state = self.state.copy()
            new_state[index], new_state[index-1] = new_state[index-1], new_state[index]
            neighbors.append(Puzzle(new_state, self.actual_cost+new_state[index], self, new_state[index]))
        if col < 2:
            new_state = self.state.copy()
            new_state[index], new_state[index+1] = new_state[index+1], new_state[index]
            neighbors.append(Puzzle(new_state, self.actual_cost+new_state[index], self, new_state[index]))
        
        return neighbors
input_file = "input1.txt"
output_file = 'output.txt'
# Function for reading the input file with the initial puzzle
def read_puzzle_from_file(input_file):
    with open(input_file, 'r') as file:
        puzzle = [int(num) for num in file.read().split()]
        return puzzle
#funtion for writing the goal state 
def write_puzzle_to_file(output_file, puzzle):
    with open(output_file, 'w') as file:
        for i in range(3):
            for j in range(3):
                file.write(str(puzzle[i*3+j]))
            file.write('\n')
#Checks for inversions in the initial to see if the puzzle is solvable 
def is_solvable(state):
    flat_list = [elem for row in state for elem in row]
    flat_list = [flat_list[i] for i in [0, 1, 2, 5, 8, 7, 6, 3, 4]]
    inversions = 0
    for i in range(len(flat_list)):
        for j in range(i+1, len(flat_list)):
            if flat_list[j] and flat_list[i] and flat_list[i] > flat_list[j]:
                inversions += 1
    blank_row = len(state) - 1 - state.index([])
    return (inversions % 2 == 0) == (blank_row % 2 == 1)
#This function implements Dijkstra's Algorithm to find the shortest path to the goal state.
def solve_puzzle(puzzle):
  
    initial_puzzle = Puzzle(puzzle)
    heap = [initial_puzzle]
    visited = set()
    
    while heap:
        current_puzzle = heapq.heappop(heap)
        
        if current_puzzle.state == [1,2,3,8,0,4,7,6,5]:
            moves = []
            total_cost = current_puzzle.actual_cost
            while current_puzzle.prev:
                moves.append(current_puzzle.move)
                current_puzzle = current_puzzle.prev
            return (total_cost, moves[::-1])
        
            # Write the goal state to file
            #write_puzzle_to_file(output_file, current_puzzle.state)
            #return (total_cost, moves[::-1])
    
        visited.add(current_puzzle)
        neighbors = current_puzzle.get_neighbors()
        
        for neighbor in neighbors:
            if neighbor not in visited:
                heapq.heappush(heap, neighbor)
    return None

#Example usage
initial_state = read_puzzle_from_file(input_file)
result = solve_puzzle(initial_state)
if result is not None:
    total_cost, moves = result
    final_state = Puzzle([1, 2, 3, 8, 0, 4, 7, 6, 5]).state
    write_puzzle_to_file(output_file, final_state)
else:
    print("No solution found.")
print(result)
endTime = time.time()
print(endTime - starTime)
