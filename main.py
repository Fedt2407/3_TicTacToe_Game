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

game_is_over = False

def print_grid():
    grid = f"\n {moves['A1']} | {moves['A2']} | {moves['A3']} \n-----------\n {moves['B1']} | {moves['B2']} | {moves['B3']} \n-----------\n {moves['C1']} | {moves['C2']} | {moves['C3']} \n"
    print(grid)

print(f"\nWelcome to Tic Tac Toe!")
print_grid()

def game_initialization():
    global player_1, player_2
    player_1 = input("Player 1, do you want to be X or O?: ").upper()
    if player_1 == "X":
        player_2 = "O"
    elif player_1 == "O":
        player_2 = "X"
    else:
        print("Invalid input. Please choose between X and O.")
        game_initialization()
    valid_move()

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
    for move in player1_moves:
        if 'A' in move and 'B' in move and 'C' in move:
            print("Player 1 wins!")
            return True
        elif '1' in move and '2' in move and '3' in move:
            print("Player 1 wins!")
            return True
        elif 'A1' in player1_moves and 'B2' in player1_moves and 'C3' in player1_moves:
            print("Player 1 wins!")
            return True
        elif 'A3' in player1_moves and 'B2' in player1_moves and 'C1' in player1_moves:
            print("Player 1 wins!")
            return True
    for move in player2_moves:
        if 'A' in move and 'B' in move and 'C' in move:
            print("Player 2 wins!")
            return True
        elif '1' in move and '2' in move and '3' in move:
            print("Player 2 wins!")
            return True
        elif 'A1' in player2_moves and 'B2' in player2_moves and 'C3' in player2_moves:
            print("Player 2 wins!")
            return True
        elif 'A3' in player2_moves and 'B2' in player2_moves and 'C1' in player2_moves:
            print("Player 2 wins!")
            return True

def check_drawn(player1_moves, player2_moves):
    global moves
    global game_is_over
    if len(player1_moves) + len(player2_moves) == 9:
        print("It's a draw!")
        continue_playing = input("Do you want to play again? (Y/N): ").upper()
        if continue_playing == 'Y':
            moves = {
                'A1': ' ', 'A2': ' ', 'A3': ' ',
                'B1': ' ', 'B2': ' ', 'B3': ' ',
                'C1': ' ', 'C2': ' ', 'C3': ' '
            }
            print_grid()
            game_initialization()

game_initialization()

while not game_is_over:
    check_victory(player1_moves, player2_moves)
    check_drawn(player1_moves, player2_moves)
    valid_move()