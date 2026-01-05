''' Hangeman game '''

import random

movies = [
    'avesham',
    'padakalam',
    'kalki'
]
temp = ''
ch = random.choice(movies)
print(ch)
chance = 6
temp = ['_']*len(ch)
for i in range(len(ch)):
    print(temp[i],end='')
while chance > 0 and '_' in temp:
    l = input("\nEnter the letter: ")
    if l in ch:
        for i in range(len(ch)):
            if ch[i] == l:
                temp[i] = l
        print(temp)
    else:
        chance = chance-1
        print(f'You guessed wrong! {chance} left')
if '_' not in temp:
    print('You guessed correctly!')
if chance == 0:
    print(f"No chances left! The movie is {ch}")