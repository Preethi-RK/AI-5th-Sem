import copy

# Define the goal state
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]  # 0 represents the empty space

# Function to calculate Manhattan distance
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                x, y = divmod(state[i][j] - 1, 3)  # Goal position
                distance += abs(x - i) + abs(y - j)
    return distance

# Check if the puzzle is solved
def is_goal(state):
    return state == goal_state

# Function to find the empty tile (0)
def find_empty(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Possible moves for the empty tile (up, down, left, right)
def get_neighbors(state):
    empty_x, empty_y = find_empty(state)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left
    neighbors = []
    
    for dx, dy in directions:
        new_x, new_y = empty_x + dx, empty_y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:  # Check boundaries
            new_state = copy.deepcopy(state)
            new_state[empty_x][empty_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[empty_x][empty_y]
            neighbors.append(new_state)
    
    return neighbors

# DFS algorithm to solve the puzzle
def dfs(state, visited):
    if is_goal(state):
        return [state]  # Return the path to solution
    
    visited.append(state)
    
    # Get neighbors sorted by Manhattan distance
    neighbors = get_neighbors(state)
    neighbors.sort(key=manhattan_distance)
    
    for neighbor in neighbors:
        if neighbor not in visited:
            path = dfs(neighbor, visited)
            if path:  # If a solution is found, return the path
                return [state] + path
    
    return None  # No solution found, backtrack

# Main function to run DFS on the 8-puzzle
def solve_puzzle(initial_state):
    visited = []
    path = dfs(initial_state, visited)
    if path:
        print("Solution found!")
        for step in path:
            for row in step:
                print(row)
            print()
    else:
        print("No solution found.")

# Initial state of the puzzle (can be changed)
initial_state = [[1, 2, 3],
                 [4, 0, 6],
                 [7, 5, 8]]

solve_puzzle(initial_state)
