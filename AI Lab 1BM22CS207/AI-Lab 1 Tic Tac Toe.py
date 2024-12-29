import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def human_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                raise ValueError
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                return row, col
            else:
                print("Cell already taken, try again.")
        except ValueError:
            print("Invalid input, please enter a number between 1 and 9.")

def computer_move(board):
    # Check for a winning move
    for move in get_available_moves(board):
        board[move[0]][move[1]] = "O"
        if check_winner(board) == "O":
            return move
        board[move[0]][move[1]] = " "

    # Block human from winning
    for move in get_available_moves(board):
        board[move[0]][move[1]] = "X"
        if check_winner(board) == "X":
            board[move[0]][move[1]] = "O"
            return move
        board[move[0]][move[1]] = " "

    # Choose a random move (if no immediate win/block)
    return random.choice(get_available_moves(board))

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe! You are 'X' and the computer is 'O'.")

    while True:
        print_board(board)
        row, col = human_move(board)
        board[row][col] = "X"

        if check_winner(board) == "X":
            print_board(board)
            print("Congratulations! You win!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        print("Computer's turn:")
        row, col = computer_move(board)
        board[row][col] = "O"

        if check_winner(board) == "O":
            print_board(board)
            print("Computer wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
