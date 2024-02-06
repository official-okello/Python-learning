import random

picks = ['r','p','s']
counter = 0

class Play():
    def __init__(self, computer):
        self.computer = computer
    def draw(self, computer, player):
        if computer == player:
            return True
    def win(self, computer, player):
        if computer == 'r' and player == 'p' or computer == 'p' and player == 's' or computer == 's' and player == 'r':
            return True
    def loss(self, computer, player):
        if computer == 'r' and player == 's' or computer == 'p' and player == 'r' or computer == 's' and player == 'p':
            return True
    def valid_pick(self, player):
        if player in picks:
            return True

while True:
    computer = random.choice(picks)
    if counter > 3:
        break
    else:
        player = input('Rock(r), Paper(p), Scissors(s)?: ').lower()
        game = Play(player)
        if game.valid_pick(player):
            if game.draw(computer, player):
                print('It is a draw!')
                quit_play = input('Quit?(Y or N):').lower()
                if quit_play == 'y':
                    break
                else:
                    continue
            elif game.win(computer, player):
                print('Congratulations, you win!')
                quit_play = input('Quit?(Y or N):').lower()
                if quit_play == 'y':
                    break
                else:
                    continue
            elif game.loss(computer, player):
                print('Try again')
                counter += 1
        else:
            print('Invalid choice! Try again...')