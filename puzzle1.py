import random

def display(x):
    if x == 0:
        print('')
        print(' ___')
        print('/___\\')
        print('\\   /')
        print(' \\ /')
        print('  O')
        print(' /|\\')
        print(' / \\')
        print()
        print('^^^^^')
    elif x == 1:
        print('')
        print(' ___\\')
        print('\\   /')
        print(' \\ /')
        print('  O')
        print(' /|\\')
        print(' / \\')
        print()
        print('^^^^^')
    elif x == 2:
        print('')
        print(' ___')
        print('\\   /')
        print(' \\ /')
        print('  O')
        print(' /|\\')
        print(' / \\')
        print()
        print('^^^^^')
    elif x == 3:
        print('')
        print('\\   /')
        print(' \\ /')
        print('  O')
        print(' /|\\')
        print(' / \\')
        print()
        print('^^^^^')
    elif x == 4:
        print('')
        print('    /')
        print(' \\ /')
        print('  O')
        print(' /|\\')
        print(' / \\')
        print()
        print('^^^^^')
    elif x == 5:
        print('')
        print(' \\ /')
        print('  O')
        print(' /|\\')
        print(' / \\')
        print()
        print('^^^^^')
    elif x == 6:
        print('')
        print('   /')
        print('  O')
        print(' /|\\')
        print(' / \\')
        print()
        print('^^^^^')
    elif x == 7:
        print('')
        print('  x')
        print(' /|\\')
        print(' / \\')
        print()
        print('^^^^^')
        #print("Game is over :(")

        

words = ["love", "family", "home", "smile"]

word = random.choice(words)

right_guesses = ['_'] * len(word)
wrong_guess = []

display(0)


print(word)
print(right_guesses)

def update():
    for i in right_guesses:
        print(i, end = '')

while True:
    
    guess = input("\nGuess a letter [a-z]: ")

    if guess.lower() in word:
        index = 0
        for i in word:
            if i == guess:
                right_guesses[index] = guess
                display(len(wrong_guess))
            index += 1
        update()
    else:
        if guess not in wrong_guess:
            wrong_guess.append(guess)
            if len(wrong_guess) >= 0:
                display(len(wrong_guess))
                if len(wrong_guess) == 7:
                    print("Game is over :(")
                    break

        else:
            print('You already guess that letter.')


    if '_' not in right_guesses:
        print("\ncorrect!")
        break # or self._play_game = True