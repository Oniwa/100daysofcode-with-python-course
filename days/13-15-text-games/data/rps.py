import random


class Roll:
    def __init__(self):
        self.throw = None
        self. possible_throws = ['Rock', 'Paper', 'Scissors']
        self.win_table = {'Rock': {'Paper': False, 'Scissors': True,
                                   'Rock': None},
                          'Paper': {'Paper': None, 'Scissors': False,
                                    'Rock': True},
                          'Scissors': {'Paper': True, 'Scissors': None,
                                       'Rock': False}}

    def can_defeat(self, throw):
        return self.win_table[self.throw][throw]

    def random_throw(self):
        self.throw = random.choice(self.possible_throws)

    def get_roll(self):
        valid = False
        while not valid:
            roll = input("Enter 'r' for Rock, 'p' for Paper, or 's' for "
                         "Scissors: ")
            if roll.lower() == 'r':
                self.throw = 'Rock'
                valid = True
            elif roll.lower() == 'p':
                self.throw = 'Paper'
                valid = True
            elif roll.lower() == 's':
                self.throw = 'Scissors'
                valid = True
            else:
                print('Please enter a valid choice.')


class Player:
    def __init__(self):
        self.name = None
        self.record = {'Wins': 0, 'Losses': 0, 'Ties': 0}

    def get_name(self):
        self.name = input('Please enter your name: ')

    def update_record(self, outcome):
        if outcome is None:
            self.record['Ties'] += 1
        elif outcome:
            self.record['Wins'] += 1
        else:
            self.record['Losses'] += 1


def header():
    print('Get ready to play Rock, Paper, Scissors!  First player to two wins '
          'is the winner!')


def main():
    header()

    p1 = Player()
    p2 = Player()

    p1.get_name()
    p2.name = 'Computer'

    game_loop(p1, p2)


def game_loop(player1, player2):
    count = 1
    p2_roll = Roll()
    p1_roll = Roll()

    p1_wins = 0
    p2_wins = 0

    while p1_wins < 3 and p2_wins < 3:
        p2_roll.random_throw()
        p1_roll.get_roll()

        outcome = p1_roll.can_defeat(p2_roll.throw)
        player1.update_record(outcome)

        if outcome is None:
            print(f'Round {count} is a Tie!')
            player2.update_record(None)
        elif outcome:
            print(f'Round {count} goes to {player1.name}!')
            p1_wins += 1
            player2.update_record(False)
        else:
            print(f'Round {count} goes to {player2.name}!')
            p2_wins += 1
            player2.update_record(True)

        count += 1

    if player1.record['Wins'] > player2.record['Wins']:
        print(f'{player1.name} wins with a record of {player1.record["Wins"]}-'
              f'{player1.record["Losses"]}-{player1.record["Ties"]}')
    else:
        print(f'{player2.name} wins with a record of {player2.record["Wins"]}-'
              f'{player2.record["Losses"]}-{player2.record["Ties"]}')


if __name__ == "__main__":
    main()
