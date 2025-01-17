moves = {
    'A1': ' ', 'A2': ' ', 'A3': ' ',
    'B1': ' ', 'B2': ' ', 'B3': ' ',
    'C1': ' ', 'C2': ' ', 'C3': ' '
}

active_player = 1
player_1 = ''
player_2 = ''
player1_moves = []
player2_moves = []

game_is_on = True

def print_grid():
    grid = f"\n {moves['A1']} | {moves['A2']} | {moves['A3']} \n-----------\n {moves['B1']} | {moves['B2']} | {moves['B3']} \n-----------\n {moves['C1']} | {moves['C2']} | {moves['C3']} \n"
    print(grid)

print(f"\nWelcome to Tic Tac Toe!")

def game_initialization():
    global player_1, player_2, moves, player1_moves, player2_moves
    moves = {
            'A1': ' ', 'A2': ' ', 'A3': ' ',
            'B1': ' ', 'B2': ' ', 'B3': ' ',
            'C1': ' ', 'C2': ' ', 'C3': ' '
        }
    player1_moves = []
    player2_moves = []
    print_grid()
    player_1 = input("Player 1, do you want to be X or O?: ").upper()
    if player_1 == "X":
        player_2 = "O"
        valid_move()
    elif player_1 == "O":
        player_2 = "X"
        valid_move()
    else:
        print("Invalid input. Please choose between X and O.")
        game_initialization()

def valid_move():
    global active_player
    move = input(f"Player {active_player}, please enter a move: ").upper()
    if move in moves and moves[move] == ' ':
        if active_player == 1:
            moves[move] = player_1
            player1_moves.append(move)
            active_player = 2
        else:
            moves[move] = player_2
            player2_moves.append(move)
            active_player = 1
        print_grid()
    elif moves[move] != ' ':
        print("Invalid move. That space is already taken.")
    else:
        print("Invalid coordinates. Please enter a valid move.\nValid moves are: A1, A2, A3, B1, B2, B3, C1, C2, C3.")
        valid_move()


def check_victory(player1_moves, player2_moves):
    winning_combinations = [
        ['A1', 'A2', 'A3'], ['B1', 'B2', 'B3'], ['C1', 'C2', 'C3'],
        ['A1', 'B1', 'C1'], ['A2', 'B2', 'C2'], ['A3', 'B3', 'C3'],
        ['A1', 'B2', 'C3'], ['A3', 'B2', 'C1']
    ]
    for combination in winning_combinations:
        if all(move in player1_moves for move in combination):
            print("Player 1 wins!")
            game_restart()
        elif all(move in player2_moves for move in combination):
            print("Player 2 wins!")
            game_restart()

def check_drawn(player1_moves, player2_moves):
    if len(player1_moves) + len(player2_moves) == 9:
        print("It's a draw!")
        game_restart()

def game_restart():
    global game_is_on, active_player
    continue_playing = input("Do you want to play again? (Y/N): ").upper()
    if continue_playing == 'Y':
        active_player = 1
        game_initialization()
    else:
        game_is_on = False

game_initialization()

while game_is_on:
    check_victory(player1_moves, player2_moves)
    check_drawn(player1_moves, player2_moves)
    if not game_is_on:
        break
    valid_move()