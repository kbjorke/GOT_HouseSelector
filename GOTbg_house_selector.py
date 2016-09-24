# By: Kristian Bjoerke

from random import shuffle


print 'A Game Of Thrones The Board Game'
print 'House selector:\n'

print 'Game versions availiable:'
print '1: Original Version'
print '2: A Feast For Crows\n'
print '3: Rumble in the South [4 player variant]'
print '4: Struggle in the North [4 player variant]'
print '5: Race to King\'s Landing [5 player variant]'
print '6: King in the North [5 player variant]\n'

game_version = int(raw_input('Enter game version number: '))

player_names = ['first',
        'second',
        'third',
        'fourth',
        'fifth',
        'sixth']

if game_version == 1:

    test_condition = False
    while (not test_condition):
        number_of_players = int(raw_input('Enter number of players (3-6): '))
    
        test_condition = (number_of_players >= 3 and number_of_players <= 6)

        if not test_condition:
            print 'Number of players must be between 3 and 6!'

        houses = ['House Stark',
                'House Lannister',
                'House Baratheon',
                'House Greyjoy',
                'House Tyrell',
                'House Martel']

elif game_version == 2:
        
    number_of_players = 4

    houses = ['House Stark',
            'House Arryn',
            'House Lannister',
            'House Baratheon']
        
elif game_version == 3:
        
    number_of_players = 4

    houses = ['House Lannister',
            'House Baratheon',
            'House Tyrell',
            'House Martell']

elif game_version == 4:
        
    number_of_players = 4

    houses = ['House Stark',
            'House Lannister',
            'House Baratheon',
            'House Greyjoy']

elif game_version == 5:
        
    number_of_players = 5

    houses = ['House Stark',
            'House Lannister',
            'House Greyjoy',
            'House Tyrell',
            'House Martell']

elif game_version == 6:
        
    number_of_players = 4

    houses = ['House Lannister',
            'House Baratheon',
            'House Greyjoy',
            'House Tyrell',
            'House Martell']


print ''

for i in range(number_of_players):
    name = raw_input('Enter name of %s player: ' % player_names[i])
    player_names[i] = name

player_names_cut = player_names[0:number_of_players]

shuffle(player_names_cut)

print ''

for i in range(number_of_players):
    print '%- 16s: %s' % (houses[i], player_names_cut[i])

print ''
