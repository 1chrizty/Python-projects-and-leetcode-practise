''' turn based rpg game '''

# import random
# player = 100
# computer = 100
# while player >= 0 and computer >= 0:
#     a = random.randint(1,20)
#     print(f'player hit taken: {a}')
#     player -= a
#     print(f'player health {player}')
#     b = random.randint(1,20)
#     print(f'computer hit taken: {b}')
#     computer -= b
#     print(f'computer health {computer}')

# if player <= 0:
#     print('computer wins!!!')
# else:
#     print('user wins!!!!')


''' snake and ladder '''

import random

snakes = {13: 8, 37: 29, 56: 42, 73: 45, 99: 2}
ladders = {9: 26, 19: 38, 65: 95}

n = int(input("Enter number of players: "))
players = [0] * n

def move_player(pos):
    dice = random.randint(1, 6)
    print(f"Rolled a {dice}")
    if pos == 0 and dice != 6:
        return pos
    pos += dice
    if pos > 100:
        pos -= dice
    if pos in snakes:
        print(f"Snake from {pos} to {snakes[pos]}")
        pos = snakes[pos]
    elif pos in ladders:
        print(f"Ladder from {pos} to {ladders[pos]}")
        pos = ladders[pos]
    return pos

won = False
while not won:
    for i in range(n):
        input(f"\nPlayer {i + 1}'s turn. Press Enter to roll the dice.")
        players[i] = move_player(players[i])
        print(f"Player {i + 1} is now at position {players[i]}")
        if players[i] == 100:
            print(f"\nPlayer {i + 1} wins!")
            won = True
            break





''' Dice throw '''

# import random
# score1 = 0
# score2 = 0
# a = random.randint(1,6)
# print(f'player1 chance: {a}')
# for i in range(0,a):
#     b = random.randint(1,6)
#     print(f'rolled: {b}')
#     score1 += b
# print(f'sum: {score1}')
# c = random.randint(1,6)
# print(f'player2 chance: {c}')
# for i in range(0,c):
#     d = random.randint(1,6)
#     print(f'rolled: {d}')
#     score2 += d
# print(f'sum: {score2}')

# if score1 > score2:
#     print('player1 wins!!!!')
# elif score2 > score1:
#     print('player2 wins!!!!')
# else:
#     print('draw!!!')


''' with function '''
# def dice():
#     initial = random.randint(1,6)
#     score = 0
#     for i in range(initial):
#         b = random.randint(1,6)
#         score += b
#     return score
# player1 = dice()
# player2 = dice()

# if player1 > player2:
#     print(f'player1: {player1} wins over player2: {player2}')
# elif player2 > player1:
#     print(f'player2: {player2} wins over player1: {player1}')
# else:
#     print(f'player1: {player1} draw with player2: {player2}')

