''' Tic Tac Toe '''
board = [' ' for i in range(9)]

def play():
    for i in range(3):
        if i < 2:
            print(f" {board[3*i]} | {board[3*i+1]} | {board[3*i+2]} ")
            print("___|___|___")
        else:
            print(f" {board[3*i]} | {board[3*i+1]} | {board[3*i+2]} ")
            print("   |   |   ")

def check(player):
    conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  
        (0, 4, 8), (2, 4, 6)              
    ]
    for a, b, c in conditions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def draw():
    return ' ' not in board

print("Welcome to the world of Tic Tac Toe Game\n" \
"Remember the cell to draw (X or O)\n" \
" 0 | 1 | 2 \n___|___|___\n 3 | 4 | 5 \n___|___|___\n 6 | 7 | 8\n   |   |")
while True:
    player = input('Choose (X or O): ').upper()
    if player not in ['X','O']:
        print('Wrong choice! Please choose X or O.')
    else:
        break

while True:
    print(f'Player {player} turn!')
    cell = int(input('Enter the cell to draw: '))
    if cell < 0 or cell > 8 or board[cell] != " ":
        print("Invalid move! Try again.")
        continue
    board[cell] = player
    play()
    if check(player):
        print(f"Player {player} wins!")
        break
    elif draw():
        play()
        print("Draw!")
        break
    if player == 'X':
        player = 'O'
    else:
        player = 'X'