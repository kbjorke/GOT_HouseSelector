#!/usr/bin/env python

# By: Kristian Bjoerke
__version__ = '1.0'

from random import shuffle

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
#from kivy.uix.label import Label
#from kivy.uix.button import Button


class InitialScreen(FloatLayout):

    def __init__(self, **kwargs):
        super(InitialScreen, self).__init__(**kwargs)
        

class GOT_HouseSelector(App):

    def build(self):

        return InitialScreen()

"""
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
"""




if __name__ == '__main__':
    GOT_HouseSelector().run()
