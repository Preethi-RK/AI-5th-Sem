# Algorithm for Truth-Table Entailment Check

# Function: Define individual logical components of the Knowledge Base (KB)
def A_or_C(A, B, C):
    # Represents the logical expression A \/ C
    return A or C

def B_or_not_C(A, B, C):
    # Represents the logical expression B \/ ¬C
    return B or not C

# Function: Combine logical components to define the full KB
def KB(A, B, C):
    # KB = (A \/ C) ∧ (B \/ ¬C)
    return A_or_C(A, B, C) and B_or_not_C(A, B, C)

# Function: Define the Query (α)
def query(A, B, C):
    # Query = A \/ B
    return A or B

# Function: Print the truth table and check entailment
def print_truth_tables(symbols):
    import itertools

    print(f"{'A':<6}{'B':<6}{'C':<6}{'A∨C':<8}{'B∨¬C':<8}{'KB':<8}{'α (A∨B)':<8}")
    print("-" * 56)

    both_true = []  # Store rows where both KB and query are true
    kb_values = []  # Store KB values
    query_values = []  # Store Query values

    # Generate all possible truth assignments for the symbols
    for values in itertools.product([False, True], repeat=len(symbols)):
        assignment = dict(zip(symbols, values))

        # Extract current truth values for each symbol
        A_val = assignment['A']
        B_val = assignment['B']
        C_val = assignment['C']

        # Evaluate each part of the truth table
        A_or_C_val = A_or_C(A_val, B_val, C_val)
        B_or_not_C_val = B_or_not_C(A_val, B_val, C_val)
        KB_val = KB(A_val, B_val, C_val)
        query_val = query(A_val, B_val, C_val)

        # Append values for checking entailment later
        kb_values.append(KB_val)
        query_values.append(query_val)

        # Print each row of the truth table
        print(f"{str(A_val):<6}{str(B_val):<6}{str(C_val):<6}"
              f"{str(A_or_C_val):<8}{str(B_or_not_C_val):<8}"
              f"{str(KB_val):<8}{str(query_val):<8}")

        # Store rows where both KB and query are true
        if KB_val and query_val:
            both_true.append(assignment)

    # Check entailment: If all KB values imply corresponding Query values
    entails = all(kb <= q for kb, q in zip(kb_values, query_values))

    # Print rows where both KB and Query are true
    print("\nCombinations where both KB and α (A∨B) are true:")
    print(f"{'A':<6}{'B':<6}{'C':<6}")
    print("-" * 18)
    for assignment in both_true:
        print(f"{assignment['A']:<6}{assignment['B']:<6}{assignment['C']:<6}")

    # Print entailment result
    if entails:
        print("\nResult: The Knowledge Base (KB) entails the Query (α).")
    else:
        print("\nResult: The Knowledge Base (KB) does not entail the Query (α).")

# Main execution
if __name__ == "__main__":
    # Define symbols in the Knowledge Base
    symbols = ['A', 'B', 'C']

    # Print the truth table and check entailment
    print_truth_tables(symbols)
