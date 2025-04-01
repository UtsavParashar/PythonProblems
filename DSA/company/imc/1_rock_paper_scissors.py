import numpy as np

class RockPaperScissors:
    def __init__(self):
        self._computer_score = 0
        self._user_score = 0
        self.USER_WON = 'You won this round!'
        self.COMPUTER_WON = 'Computer won this round!'

    def _computer_value(self):
        return np.random.randint(1, 4)
    
    def _incrementer(self, player):
        if player == 'computer':
            self._computer_score += 1
        elif player == 'user':
            self._user_score += 1

    def _set_value(self, user_value):
        self._user_value = user_value


    def game_logic(self):
        self.computer_value = self._computer_value()
        print(f'You Entered - {self._user_value} and Computer Entered - {self.computer_value}')
        if self.computer_value == 1 and self._user_value == 3:
            print(self.COMPUTER_WON)
            self._incrementer('computer')
        elif self._user_value == 1 and self.computer_value == 3:
            print(self.USER_WON)
            self._incrementer('user')
        elif self.computer_value > self._user_value:
            print(self.COMPUTER_WON)
            self._incrementer('computer')
        elif self._user_value > self.computer_value:
            print(self.USER_WON)
            self._incrementer('user')
        elif self._user_value == self.computer_value:
            print("It's a tie, both of your score will be incremented")
            self._incrementer('computer')
            self._incrementer('user')

    def user_input(self):
        val = None
        while val != 0:
            val = input('Enter the value from 1-3 (1-Rock, 2-Paper, 3-Scissors), 0 to Exit: ')
            try:
                val = int(val)
            except:
                print('Enter a valid value from 1-3 (1-Rock, 2-Paper, 3-Scissors), 0 to Exit: ')
            
            if val != 0:
                rps._set_value(val)
                rps.game_logic()
            else: 
                if self._user_score > self._computer_score:
                    print('You won!')
                elif self._computer_score > self._user_score:
                    print('Computer won!')
                print(f'Final Score, You - {self._user_score}, Computer - {self._computer_score}')

                
            

if __name__ == '__main__':
    rps = RockPaperScissors()
    rps.user_input()


    
