from random import choice

name = input("Enter your name: ")
print(f"Hello, {name}")

with open('rating.txt') as database:
    for line in database:
        if name in line:
            name, score = line.split()
            score = int(score)
            break
        else:
            score = 0
            continue

game_options = input()
if game_options:
    variants = game_options.split(',')
else:
    variants = ['rock', 'paper', 'scissors']
print("Okay, let's start")

while True:
    user = input()
    if user == '!exit':
        print('Bye!')
        break
    elif user == '!rating':
        print(f'Your rating: {score}')
        continue
    elif user not in variants:
        print('Invalid input')
        continue
    else:
        option = choice(variants)

        user_index = variants.index(user)
        for_compare = variants[user_index + 1:] + variants[:user_index]

        if option == user:
            print(f"There is a draw ({option})")
            score += 50
        elif option in for_compare[:len(for_compare) // 2]:
            print(f"Sorry, but the computer chose {option}")
        else:
            print(f"Well done. The computer chose {option} and failed")
            score += 100
