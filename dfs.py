class Node:
    def __init__(self, state, parent=None, cost=0):
        self.state = state
        self.parent = parent
        self.children = []
        self.cost = cost

    def add_child(self, child):
        self.children.append(child)

    def is_goal(self):
        return self.state == [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

    def __str__(self):
        return str(self.state)

def count_inversions(state):
    flat_list = [elem for row in state for elem in row]
    flat_list = [flat_list[i] for i in [0, 1, 2, 5, 8, 7, 6, 3, 4]]
    inversions = 0
    for i in range(len(flat_list)):
        for j in range(i+1, len(flat_list)):
            if flat_list[j] and flat_list[i] and flat_list[i] > flat_list[j]:
                inversions += 1
    return inversions

def is_solvable(state):
    inversions = count_inversions(state)
    return inversions % 2 == 0

def get_children(node):
    children = []
    i, j = find_blank(node.state)
    for move in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        x, y = i + move[0], j + move[1]
        if 0 <= x < 3 and 0 <= y < 3:
            child_state = [row[:] for row in node.state]
            child_state[i][j], child_state[x][y] = child_state[x][y], child_state[i][j]
            child_node = Node(child_state, parent=node, cost=node.cost+1)
            children.append(child_node)
    return children

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def dfs(initial_state):
    initial_node = Node(initial_state)
    stack = [initial_node]
    visited = set()
    while stack:
        node = stack.pop()
        if node.is_goal():
            # Print the goal state
            print("Goal State:")
            for row in node.state:
                print(row)
            # Return the cost of reaching the goal state
            return "Cost of getting to Goal state is ${}".format(node.cost)
        visited.add(str(node))
        children = get_children(node)
        for child in children:
            if str(child) not in visited:
                node.add_child(child)
                stack.append(child)
    return "Goal state not reachable"

if __name__ == "__main__":
    initial_state = []
    with open('input.txt', 'r') as f:
        for line in f:
            row = [int(num) for num in line.strip().split()]
            initial_state.append(row)
    print("Initial State:")
    for row in initial_state:
        print(row)
    if is_solvable(initial_state):
        print("Number of inversions: ", count_inversions(initial_state))
        goal_node = dfs(initial_state)
        if goal_node:
            print(goal_node)
        else:
            print("Goal state not reachable")
    else:
        print("Number of inversions: ", count_inversions(initial_state))
        print("Initial state is unsolvable")