import math

# Tic-Tac-Toe Board
board = [" " for _ in range(9)]

def print_board():
    """Prints the Tic-Tac-Toe board."""
    print("\n")
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("-" * 9)
    print("\n")

def check_winner(player):
    """Checks if the given player ('X' or 'O') has won."""
    win_conditions = [(0,1,2), (3,4,5), (6,7,8),  # Rows
                      (0,3,6), (1,4,7), (2,5,8),  # Columns
                      (0,4,8), (2,4,6)]           # Diagonals
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

def is_draw():
    """Checks if the board is full, resulting in a draw."""
    return " " not in board

def minimax(is_maximizing):
    """Minimax algorithm to calculate the best AI move."""
    if check_winner('O'):
        return 1
    if check_winner('X'):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = 'O'
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = 'X'
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

def ai_move():
    """Finds the best move for AI using Minimax."""
    best_score = -math.inf
    best_move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = 'O'
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = 'O'

def player_move():
    """Allows the player to input their move."""
    while True:
        try:
            move = int(input("Enter your move (A number between 1 and 9 inclusive): ")) - 1
            if board[move] == " ":
                board[move] = 'X'
                break
            else:
                print("⚠️ Invalid move! Spot already taken.")
        except (ValueError, IndexError):
            print("⚠️ Enter a valid number between 1 and 9.")

def main():
    print("🎮 Tic-Tac-Toe: You are 'X', AI is 'O' 🎮")
    print_board()

    while True:
        player_move()
        print_board()
        if check_winner('X'):
            print("🎉 You win! Congrats!")
            break
        if is_draw():
            print("🤝 It's a draw!")
            break

        print("AI is making a move...")
        ai_move()
        print_board()

        if check_winner('O'):
            print("💀 AI wins! Better luck next time.")
            break
        if is_draw():
            print("🤝 It's a draw!")
            break

if __name__ == "__main__":
    main()
