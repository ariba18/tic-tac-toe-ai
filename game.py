"""
Tic-Tac-Toe with an unbeatable AI using the Minimax algorithm.
Human is 'X', AI is 'O'. AI will never lose.
"""

# The board is a list of 9 elements, index 0-8, representing:
#  0 | 1 | 2
#  ---------
#  3 | 4 | 5
#  ---------
#  6 | 7 | 8
board = [" " for _ in range(9)]

HUMAN = "X"
AI = "O"

WIN_COMBOS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6)              # diagonals
]


def print_board():
    print()
    for row in range(3):
        cells = board[row*3 : row*3 + 3]
        print(" " + " | ".join(cells))
        if row < 2:
            print("---+---+---")
    print()


def check_winner(b, player):
    return any(all(b[i] == player for i in combo) for combo in WIN_COMBOS)


def is_full(b):
    return " " not in b


def get_empty_cells(b):
    return [i for i, cell in enumerate(b) if cell == " "]


def minimax(b, is_maximizing):
    # Base cases: someone already won, or it's a draw
    if check_winner(b, AI):
        return 1
    if check_winner(b, HUMAN):
        return -1
    if is_full(b):
        return 0

    if is_maximizing:  # AI's turn: trying to maximize score
        best_score = float("-inf")
        for cell in get_empty_cells(b):
            b[cell] = AI
            score = minimax(b, False)
            b[cell] = " "  # undo the move (backtrack)
            best_score = max(best_score, score)
        return best_score
    else:  # Human's turn: trying to minimize AI's score
        best_score = float("inf")
        for cell in get_empty_cells(b):
            b[cell] = HUMAN
            score = minimax(b, True)
            b[cell] = " "
            best_score = min(best_score, score)
        return best_score


def best_ai_move():
    best_score = float("-inf")
    move = None
    for cell in get_empty_cells(board):
        board[cell] = AI
        score = minimax(board, False)
        board[cell] = " "
        if score > best_score:
            best_score = score
            move = cell
    return move


def human_move():
    while True:
        try:
            choice = int(input("Your move (1-9): ")) - 1
        except ValueError:
            print("Please enter a number between 1 and 9.")
            continue
        if choice not in range(9) or board[choice] != " ":
            print("That cell is invalid or already taken. Try again.")
            continue
        return choice


def play():
    print("Welcome to Tic-Tac-Toe! You are X, the AI is O.")
    print("Cell positions:\n 1 | 2 | 3\n 4 | 5 | 6\n 7 | 8 | 9")
    print_board()

    current = HUMAN
    while True:
        if current == HUMAN:
            move = human_move()
            board[move] = HUMAN
        else:
            print("AI is thinking...")
            move = best_ai_move()
            board[move] = AI

        print_board()

        if check_winner(board, current):
            print(f"{current} wins!" if current == HUMAN else "AI wins! Better luck next time.")
            break
        if is_full(board):
            print("It's a draw!")
            break

        current = AI if current == HUMAN else HUMAN


if __name__ == "__main__":
    play()