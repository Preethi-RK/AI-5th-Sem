

#Hill Climbing Algorithm to solve N Queens problem
import random

# Function to calculate the number of conflicts in the current configuration
def calculate_conflicts(board):
    n = len(board)
    conflicts = 0

    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j]:
                conflicts += 1  # Same column
            elif abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1  # Same diagonal

    return conflicts

# Function to generate a random configuration of queens (if needed)
def random_board(n):
    return [random.randint(0, n - 1) for _ in range(n)]

# Hill climbing algorithm to solve the N-Queens problem
def hill_climbing(n, current_board):
    current_conflicts = calculate_conflicts(current_board)
    iteration = 0

    # Repeat until we reach a solution or cannot improve
    while current_conflicts != 0:
        iteration += 1
        print(f"Iteration {iteration}, Conflicts: {current_conflicts}")
        print_board(current_board)

        neighbors = []

        # Generate neighbors by moving each queen to a different row in its column
        for i in range(n):
            for row in range(n):
                if row != current_board[i]:
                    new_board = current_board[:]
                    new_board[i] = row
                    neighbors.append(new_board)

        # Find the neighbor with the least conflicts
        best_neighbor = None
        best_conflicts = current_conflicts

        for neighbor in neighbors:
            neighbor_conflicts = calculate_conflicts(neighbor)
            if neighbor_conflicts < best_conflicts:
                best_conflicts = neighbor_conflicts
                best_neighbor = neighbor

        # If no better neighbor is found, we are stuck, return current board
        if best_conflicts >= current_conflicts:
            print("Stuck in local optimum.")
            return current_board

        # Otherwise, move to the best neighbor
        current_board = best_neighbor
        current_conflicts = best_conflicts

    print(f"Final Iteration {iteration + 1}, Conflicts: {current_conflicts}")
    print_board(current_board)  # Final solution
    return current_board

# Function to print the board in a readable format
def print_board(board):
    n = len(board)
    for i in range(n):
        row = ['Q' if col == board[i] else '.' for col in range(n)]
        print(' '.join(row))
    print()

# Function to get user input for the initial configuration of the queens
def get_user_input(n):
    while True:
        try:
            input_str = input("Enter the list of column positions (space-separated): ")
            board = [int(x) for x in input_str.split()]

            if len(board) != n:
                continue

            if any(x < 0 or x >= n for x in board):
                continue

            if len(set(board)) != n:
                continue

            return board

        except (ValueError):
            continue

# Main function to handle user input and run the algorithm
def main():
    while True:
        try:
            n = int(input("Enter the size of the board (N): "))
            if n <= 0:
                continue
            else:
                break
        except ValueError:
            continue

    initial_board = get_user_input(n)

    max_restarts = 10
    restart_count = 0

    while restart_count < max_restarts:
        solution = hill_climbing(n, initial_board)

        if calculate_conflicts(solution) == 0:
            return
        else:
            restart_count += 1
            initial_board = random_board(n)  # Restart with a random configuration

    print("\nFailed to find a solution after several attempts.")

# Run the program
if __name__ == "__main__":
    main()
