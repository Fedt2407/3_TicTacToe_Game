moves = {
    'A1': ' ', 'A2': ' ', 'A3': ' ',
    'B1': ' ', 'B2': ' ', 'B3': ' ',
    'C1': ' ', 'C2': ' ', 'C3': ' '
}

active_player = 1
player_symbols = {1: '', 2: ''}
player_moves = {1: [], 2: []}
game_is_on = True

def print_grid():
    grid = f"\n {moves['A1']} | {moves['A2']} | {moves['A3']} \n-----------\n {moves['B1']} | {moves['B2']} | {moves['B3']} \n-----------\n {moves['C1']} | {moves['C2']} | {moves['C3']} \n"
    print(grid)

def game_initialization():
    global active_player
    active_player = 1
    for key in moves:
        moves[key] = ' '
    player_moves[1].clear()
    player_moves[2].clear()
    print_grid()
    set_player_symbols()

def set_player_symbols():
    global player_symbols
    player_1_symbol = input("Player 1, do you want to be X or O?: ").upper()
    if player_1_symbol in ["X", "O"]:
        player_symbols[1] = player_1_symbol
        player_symbols[2] = "O" if player_1_symbol == "X" else "X"
    else:
        print("Invalid input. Please choose between X and O.")
        set_player_symbols()

def valid_move():
    global active_player
    move = input(f"Player {active_player}, please enter a move: ").upper()
    if move in moves and moves[move] == ' ':
        moves[move] = player_symbols[active_player]
        player_moves[active_player].append(move)
        print_grid()
        if check_victory(player_moves[active_player]):
            print(f"Player {active_player} wins!")
            game_restart()
        elif check_draw():
            print("It's a draw!")
            game_restart()
        else:
            active_player = 2 if active_player == 1 else 1
    elif move in moves and moves[move] != ' ':
        print("Invalid move. That space is already taken.")
    else:
        print("Invalid coordinates. Please enter a valid move.\nValid moves are: A1, A2, A3, B1, B2, B3, C1, C2, C3.")
    if game_is_on:
        valid_move()

def check_victory(player_moves):
    winning_combinations = [
        ['A1', 'A2', 'A3'], ['B1', 'B2', 'B3'], ['C1', 'C2', 'C3'],
        ['A1', 'B1', 'C1'], ['A2', 'B2', 'C2'], ['A3', 'B3', 'C3'],
        ['A1', 'B2', 'C3'], ['A3', 'B2', 'C1']
    ]
    return any(all(move in player_moves for move in combo) for combo in winning_combinations)

def check_draw():
    return len(player_moves[1]) + len(player_moves[2]) == 9

def game_restart():
    global game_is_on
    continue_playing = input("Do you want to play again? (Y/N): ").upper()
    if continue_playing == 'Y':
        game_initialization()
    else:
        game_is_on = False

print(f"\nWelcome to Tic Tac Toe!")
game_initialization()

while game_is_on:
    valid_move()
