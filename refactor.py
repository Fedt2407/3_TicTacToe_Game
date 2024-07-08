# Description: Refactoring of the Tic Tac Toe game using functions and global variables.
moves = {f"{letter}{number}": ' ' for letter in "ABC" for number in range(1, 4)}
active_player = 1
symbols = ['X', 'O']
game_is_on = True

# Grid printing
def print_grid():
    print("\n " + "\n-----------\n ".join([" | ".join([moves[f"{letter}{number}"] for number in range(1, 4)]) for letter in "ABC"]) + "\n")

# Game initialization
def game_initialization():
    global active_player
    print("\nWelcome to Tic Tac Toe!")
    print_grid()
    choice = input("Player 1, do you want to be X or O?: ").upper()
    while choice not in symbols:
        print("Invalid input. Please choose between X and O.")
        choice = input("Player 1, do you want to be X or O?: ").upper()
    symbols[0], symbols[1] = (choice, 'O') if choice == 'X' else ('O', 'X')
    active_player = 1
    game_loop()

# Management of a valid move
def valid_move():
    move = input(f"Player {active_player}, please enter a move: ").upper()
    if move in moves and moves[move] == ' ':
        moves[move] = symbols[active_player - 1]
        print_grid()
        if check_victory():
            print(f"Player {active_player} wins!")
            game_restart()
        elif check_draw():
            print("It's a draw!")
            game_restart()
        else:
            switch_player()
    else:
        print("Invalid move. Please try again.")
        valid_move()

# Victory check
def check_victory():
    winning_combinations = [
        ['A1', 'A2', 'A3'], ['B1', 'B2', 'B3'], ['C1', 'C2', 'C3'],
        ['A1', 'B1', 'C1'], ['A2', 'B2', 'C2'], ['A3', 'B3', 'C3'],
        ['A1', 'B2', 'C3'], ['A3', 'B2', 'C1']
    ]
    for combination in winning_combinations:
        if all(moves[move] == symbols[active_player - 1] for move in combination):
            return True
    return False

# Draw check
def check_draw():
    return all(space != ' ' for space in moves.values())

# Change of active player
def switch_player():
    global active_player
    active_player = 2 if active_player == 1 else 1

# Game restart
def game_restart():
    global game_is_on
    if input("Do you want to play again? (Y/N): ").upper() == 'Y':
        moves.update({key: ' ' for key in moves})
        game_initialization()
    else:
        game_is_on = False

# Main game loop
def game_loop():
    while game_is_on:
        valid_move()

game_initialization()