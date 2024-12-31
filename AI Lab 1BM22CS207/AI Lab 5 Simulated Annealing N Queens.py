
#Simulated Annealing to solve N Queens problem
import random
import math

def generateRandomBoard(n):
    """Generate a random board represented by a permutation of columns."""
    return random.sample(range(n), n)

def generateNeighbor(state):
    """Generate a neighbor by moving one queen to another row in its column."""
    newState = state[:]
    row = random.randint(0, len(state) - 1)
    newRow = random.randint(0, len(state) - 1)

    # Ensure the queen moves to a different row (no self-move)
    while newRow == newState[row]:
        newRow = random.randint(0, len(state) - 1)

    newState[row] = newRow
    return newState

def calculateEnergy(state):
    """Calculate the number of attacking pairs of queens."""
    conflicts = 0
    n = len(state)

    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j]:  # Same column
                conflicts += 1
            if abs(state[i] - state[j]) == abs(i - j):  # Same diagonal
                conflicts += 1
    return conflicts

def simulatedAnnealing(n, initialTemperature=1000, minimumTemperature=0.01, alpha=0.95, numberOfIterations=100):
    """Simulated Annealing algorithm to solve the N-Queens problem."""
    # Generate an initial random board
    currentState = generateRandomBoard(n)
    currentEnergy = calculateEnergy(currentState)
    T = initialTemperature

    print("Starting simulated annealing...")

    # Iterate while the temperature is above the minimum
    iteration = 0
    while T > minimumTemperature:
        iteration += 1
        print(f"\nIteration {iteration}, Temperature: {T:.4f}")
        print(f"Current state: {currentState}")
        print(f"Current energy (conflicts): {currentEnergy}")

        for _ in range(numberOfIterations):
            # Generate a random neighbor (new board configuration)
            nextState = generateNeighbor(currentState)
            nextEnergy = calculateEnergy(nextState)

            # If the next state is better or accepted by probability
            if nextEnergy < currentEnergy:
                currentState = nextState
                currentEnergy = nextEnergy
            else:
                deltaEnergy = nextEnergy - currentEnergy
                probability = math.exp(-deltaEnergy / T)
                if random.random() < probability:
                    currentState = nextState
                    currentEnergy = nextEnergy

        # Cool the temperature
        T *= alpha

        # If a solution with zero conflicts is found, return the solution
        if currentEnergy == 0:
            return currentState

    # Return the best state found if no perfect solution is found
    return currentState

# Function to handle user input for the board configuration
def getUserInput(n):
    """Get user input for the initial configuration of queens."""
    while True:
        try:
            # Ask the user for the queen positions
            user_input = input(f"Enter the initial positions of the queens (0 to {n-1} for {n} queens, separated by spaces): ")
            positions = list(map(int, user_input.split()))

            # Validate the input
            if len(positions) != n:
                print(f"Error: You must provide exactly {n} positions.")
                continue

            # Ensure no duplicates (no two queens in the same column)
            if len(set(positions)) != n:
                print("Error: Two queens cannot be placed in the same column.")
                continue

            # Ensure the positions are within the valid range (0 to n-1)
            if any(pos < 0 or pos >= n for pos in positions):
                print(f"Error: Queen positions must be between 0 and {n-1}.")
                continue

            return positions
        except ValueError:
            print("Error: Invalid input. Please enter integers separated by spaces.")


# Main function to get user input and run the algorithm
if __name__ == "__main__":
    n = int(input("Enter the number of queens (n): "))

    # Get user input for the initial positions of the queens
    initial_state = getUserInput(n)

    # Calculate energy for the initial state
    initial_energy = calculateEnergy(initial_state)
    print(f"Initial board configuration: {initial_state}")
    print(f"Initial energy (conflicts): {initial_energy}")

    # Run the simulated annealing algorithm
    solution = simulatedAnnealing(n)

    # Output the results
    if calculateEnergy(solution) == 0:
        print("\nSolution found!")
        print(solution)
    else:
        print("\nNo perfect solution found. Best found solution:")
        print(solution)
