
#A* Search Algorithm- Misplace Tiles

import heapq

# A* search algorithm to solve the 8-puzzle problem
class Puzzle:
    def __init__(self, board, goal):
        self.board = board
        self.goal = goal
        self.n = len(board)

    def find_zero(self, state):
        # Find the index of the empty tile (0)
        for i in range(self.n):
            for j in range(self.n):
                if state[i][j] == 0:
                    return i, j

    def is_goal(self, state):
        return state == self.goal

    def possible_moves(self, state):
        # Generate all possible moves (up, down, left, right)
        moves = []
        i, j = self.find_zero(state)
        if i > 0:  # Up
            new_state = [row[:] for row in state]
            new_state[i][j], new_state[i-1][j] = new_state[i-1][j], new_state[i][j]
            moves.append(new_state)
        if i < self.n - 1:  # Down
            new_state = [row[:] for row in state]
            new_state[i][j], new_state[i+1][j] = new_state[i+1][j], new_state[i][j]
            moves.append(new_state)
        if j > 0:  # Left
            new_state = [row[:] for row in state]
            new_state[i][j], new_state[i][j-1] = new_state[i][j-1], new_state[i][j]
            moves.append(new_state)
        if j < self.n - 1:  # Right
            new_state = [row[:] for row in state]
            new_state[i][j], new_state[i][j+1] = new_state[i][j+1], new_state[i][j]
            moves.append(new_state)
        return moves

    def h(self, state):
        # Heuristic: Number of misplaced tiles
        misplaced = 0
        for i in range(self.n):
            for j in range(self.n):
                if state[i][j] != 0 and state[i][j] != self.goal[i][j]:
                    misplaced += 1
        return misplaced

    def astar(self):
        # A* search algorithm
        frontier = []
        heapq.heappush(frontier, (self.h(self.board), 0, self.board, []))  # (f(n), g(n), state, path)
        explored = set()

        while frontier:
            f, g, state, path = heapq.heappop(frontier)

            if self.is_goal(state):
                return path + [state]  # Return the solution path

            explored.add(str(state))

            for move in self.possible_moves(state):
                if str(move) not in explored:
                    heapq.heappush(frontier, (g + 1 + self.h(move), g + 1, move, path + [state]))

        return None

def print_puzzle(path):
    for step in path:
        for row in step:
            print(row)
        print()

# Initial state of the 8-puzzle
initial_state = [
    [2, 8, 3],
    [6, 4, 1],
    [7, 0, 5]
]

# Final state (goal state)
goal_state = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]

# Solve the puzzle
puzzle = Puzzle(initial_state, goal_state)
solution = puzzle.astar()

if solution:
    print("Solution found!")
    print_puzzle(solution)
    print(f"Number of steps to solution: {len(solution) - 1}")  # Exclude the initial state from the count
else:
    print("No solution found.")

print("Preethi Narasimhan - 1BM22CS207")
