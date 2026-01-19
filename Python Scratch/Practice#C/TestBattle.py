import random

# Create empty 10x10 board
def create_board():
    return [["." for _ in range(10)] for _ in range(10)]

# Print board with optional hiding of ships
def print_board(board, hide_ships=True):
    print("  " + " ".join([chr(c) for c in range(65, 75)]))
    for i, row in enumerate(board):
        display_row = []
        for cell in row:
            if hide_ships and cell == "S":
                display_row.append(".")
            else:
                display_row.append(cell)
        print(f"{i+1:2} {' '.join(display_row)}")
    print()

# Check if ship placement is valid
def valid_placement(board, start_row, start_col, size, orientation):
    if orientation not in ["H", "V"]:
        return False
    if orientation == "H":
        if start_col + size > 10:
            return False
        for c in range(start_col, start_col + size):
            if board[start_row][c] == "S":
                return False
    else:  # VERTICAL
        if start_row + size > 10:
            return False
        for r in range(start_row, start_row + size):
            if board[r][start_col] == "S":
                return False
    return True

# Place ship on board
def place_ship(board, start_row, start_col, size, orientation):
    coords = []
    if orientation == "H":
        for c in range(start_col, start_col + size):
            board[start_row][c] = "S"
            coords.append((start_row, c))
    else:
        for r in range(start_row, start_row + size):
            board[r][start_col] = "S"
            coords.append((r, start_col))
    return coords

# Random ship generation
def generate_ships(board):
    ships = []
    for _ in range(4):
        while True:
            size = random.randint(2,5)
            orientation = random.choice(["H", "V"])
            start_row = random.randint(0,9)
            start_col = random.randint(0,9)
            if valid_placement(board, start_row, start_col, size, orientation):
                coords = place_ship(board, start_row, start_col, size, orientation)
                ships.append(coords)
                break
    return ships

# Check if all ships are destroyed
def all_ships_sunk(ships):
    for ship in ships:
        if ship:  # ship still has coordinates
            return False
    return True

# Player turn
def player_turn(player_name, player_view, opponent_board, opponent_ships):
    print(f"{player_name}'s turn")
    print_board(player_view)
    while True:
        try:
            move = input("Select cell (e.g., A5): ").upper()
            col = ord(move[0]) - 65
            row = int(move[1:]) - 1
            if row < 0 or row > 9 or col < 0 or col > 9:
                print("Invalid coordinates. Try again.")
                continue
            if player_view[row][col] != ".":
                print("Already selected. Try again.")
                continue

            if opponent_board[row][col] == "S":
                print("HIT!")
                player_view[row][col] = "X"
                # Remove hit coordinate from ship
                for ship in opponent_ships:
                    if (row, col) in ship:
                        ship.remove((row, col))
                        break
                if all_ships_sunk(opponent_ships):
                    return True  # Game over
                print_board(player_view)
                print("You get another turn!")
                continue
            else:
                print("MISS!")
                player_view[row][col] = "O"
                break
        except Exception as e:
            print("Invalid input. Format: A1, B5, etc.")
    return False

# Main game loop
def main():
    print("Welcome to Battleship!")
    player1_board = create_board()
    player2_board = create_board()
    player1_view = create_board()
    player2_view = create_board()

    print("Placing ships for Player 1...")
    player1_ships = generate_ships(player1_board)
    print("Placing ships for Player 2...")
    player2_ships = generate_ships(player2_board)

    turn = 1
    while True:
        if turn == 1:
            game_over = player_turn("Player 1", player1_view, player2_board, player2_ships)
            if game_over:
                print("Player 1 Wins!")
                break
            turn = 2
        else:
            game_over = player_turn("Player 2", player2_view, player1_board, player1_ships)
            if game_over:
                print("Player 2 Wins!")
                break
            turn = 1

if __name__ == "__main__":
    main()
