
import random

words = ["love", "family", "home", "smile"]

class Game:
    def __init__(self) -> None:
        self._word = Word()
        self._play_game = True
        self._player = Player()
        self._parachute = Parachute()
    
    def start_jumper(self):
        while self._play_game:
            self._do_output()
            self._get_input()
            self._do_update()
        

    def _do_output(self):
        self._word._get_word()

    def _get_input(self):
        ask_player = input("\nGuess a letter [a-z]: ")
        print(ask_player.lower())
        self._player.set_input(ask_player)
    
    def _do_update(self):
        self._word._check_word(self._player.get_input())
        self._parachute.body(self._word._get_wrong_guesses)

class Word:
    def __init__(self) -> None:
        self._secret = random.choice(words)
        self._right_guesses = ['_' for letter in self._secret] #['_'] * len(self._secret)
        self._wrong_guesses = []

    def _get_word(self):
        display = ' '.join(self._right_guesses)
        return print(display)
    
    def _check_word(self, letter):
        letter = str(letter)
        if letter in self._secret:
            index = 0
            for i in self._secret:
                if i == letter:
                    self._right_guesses[index] = letter
                index += 1
        #print(self._right_guesses)
        else:
            if letter not in self._wrong_guesses:
                self._wrong_guesses.append(letter)
                #return(len(self._wrong_guesses))
        print(self._wrong_guesses)
    
    def _get_wrong_guesses(self):
        return len(self._wrong_guesses)

class Player:
    def __init__(self) -> None:
        self._player_input = None
    
    def get_input(self):
        return self._player_input
    
    def set_input(self, letter):
        self._player_input = letter
        print(self._player_input + " set")

class Parachute:
    def __init__(self) -> None:
        self._x = 9
    
    def body(self, x):
        if x == 0:
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
            print('/___\\')
            print('\\   /')
            print(' \\ /')
            print('  O')
            print(' /|\\')
            print(' / \\')
            print()
            print('^^^^^')
        elif x == 2:
            print(' ___')
            print('\\   /')
            print(' \\ /')
            print('  O')
            print(' /|\\')
            print(' / \\')
            print()
            print('^^^^^')
        elif x == 3:
            print('\\   /')
            print(' \\ /')
            print('  O')
            print(' /|\\')
            print(' / \\')
            print()
            print('^^^^^')
        elif x == 4:
            print('    /')
            print(' \\ /')
            print('  O')
            print(' /|\\')
            print(' / \\')
            print()
            print('^^^^^')
        elif x == 5:
            print(' \\ /')
            print('  O')
            print(' /|\\')
            print(' / \\')
            print()
            print('^^^^^')
        elif x == 6:
            print('   /')
            print('  O')
            print(' /|\\')
            print(' / \\')
            print()
            print('^^^^^')
        elif x == 7:
            print('  x')
            print(' /|\\')
            print(' / \\')
            print()
            print('^^^^^')

p = Game()
#p._do_output()
#p._get_input()
#p._do_update()
p.start_jumper()