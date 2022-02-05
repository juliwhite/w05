import random

words = ["love", "family", "home", "smile"]

class Game:
    def __init__(self) -> None:
        self._word = Word()
        self._play_game = True
        self._player = Player()
        self._server = Server()
        self.parachute = Parachute()

    def game(self):
        while self._play_game:
            self._output()
            self._player._get_guess_letter 
            #self._update()
    
    def _output(self):
        self._word = Word()
        self._word._get_display_dash
        self._word._get_display_dash
        self._player._get_guess_letter
        self._word._check_guess
        

    #def _get_player_input(self):
        #guess = self._s
        #self._player.ser

    #def _update(self):
        #pass





class Word:

    def __init__(self) -> None:
        self._word = random.choice(words)
        self._display_dash = ['_'] * len(self._word)
        self._right_guesses = ['_'] * len(self._word)
        self._wrong_guess = []
        
        self._guess = Player()
        self._body = Parachute()
    
    def _get_display_dash(self):
        dash = self._right_guesses
        return print(dash)
        
    
    def _get_right_guesses():
        pass

    def _get_wrong_guess():
        pass

    def _get_word(self):
        return self._right_guesses
    
    def update(self):
        for i in self._right_guesses:
            print(i, end = '')
    
    def _check_guess(self):
        if self._guess.lower() in self._word:
            index = 0
            for i in self._word:
                if i == self._guess:
                    self._right_guesses[index] = self._guess
                    self._body(len(self._wrong_guess))
                index += 1
            #update(self)
        else:
            if self._guess not in self._wrong_guess:
                self._wrong_guess.append(self._guess)
                if len(self._wrong_guess) >= 0:
                    self._body(len(self._wrong_guess))

            else:
                print('You already guess that letter.')



class Player:
    def __init__(self) -> None:
        self._guess_letter = random.choice(words)#input("Guess a letter [a-z]: ")
    
    def _get_guess_letter(self):
        return print("hello")
        #return self._get_guess_letter



class Parachute:
    def __init__(self) -> None:
        self._x = 0
    
    def body(self):
        if self._x == 0:
            print(' ___')
            print('/___\\')
            print('\\   /')
            print(' \\ /')
            print('  O')
            print(' /|\\')
            print(' / \\')
            print()
            print('^^^^^')
        elif self._x == 1:
            print('/___\\')
            print('\\   /')
            print(' \\ /')
            print('  O')
            print(' /|\\')
            print(' / \\')
            print()
            print('^^^^^')
        elif self._x == 2:
            print(' ___')
            print('\\   /')
            print(' \\ /')
            print('  O')
            print(' /|\\')
            print(' / \\')
            print()
            print('^^^^^')
        elif self._x == 3:
            print('\\   /')
            print(' \\ /')
            print('  O')
            print(' /|\\')
            print(' / \\')
            print()
            print('^^^^^')
        elif self._x == 4:
            print('    /')
            print(' \\ /')
            print('  O')
            print(' /|\\')
            print(' / \\')
            print()
            print('^^^^^')
        elif self._x == 5:
            print(' \\ /')
            print('  O')
            print(' /|\\')
            print(' / \\')
            print()
            print('^^^^^')
        elif self._x == 6:
            print('   /')
            print('  O')
            print(' /|\\')
            print(' / \\')
            print()
            print('^^^^^')
        elif self._x == 7:
            print('  x')
            print(' /|\\')
            print(' / \\')
            print()
            print('^^^^^')
        elif self._x == 8:
            print("Game is over :(")



class Server:
    pass

p = Game()
p.game()

