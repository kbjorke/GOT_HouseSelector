# By: Kristian Bjoerke

from random import shuffle

houses = ['House Stark',
        'House Lannister',
        'House Baratheon',
        'House Greyjoy',
        'House Tyrell',
        'House Martel']

print 'A Game Of Thrones The Board Game'
print 'House selector:\n'

test_condition = False

while (not test_condition):
    number_of_players = int(raw_input('Enter number of players (3-6): '))
    
    test_condition = (number_of_players >= 3 and number_of_players <= 6)

    if not test_condition:
        print 'Number of players must be between 3 and 6!'

print ''

player_names = ['first',
        'second',
        'third',
        'fourth',
        'fifth',
        'sixth']

for i in range(number_of_players):
    name = raw_input('Enter name of %s player: ' % player_names[i])
    player_names[i] = name

player_names = player_names[0:number_of_players]

shuffle(player_names)

print ''

for i in range(number_of_players):
    print '%- 16s: %s' % (houses[i], player_names[i])

print ''





