#!/usr/bin/env python

# By: Kristian Bjoerke
__version__ = '1.0'

from random import shuffle

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, BooleanProperty, NumericProperty,\
        ListProperty

from time import time
from os.path import dirname, join
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.animation import Animation

class GOT_HouseSelectorScreen(ScreenManager):
    fullscreen = BooleanProperty(False)

    def add_widget(self, *args):
        if 'content' in self.ids:
            return self.ids.content.add_widget(*args)
        return super(ShowcaseScreen, self).add_widget(*args)



class GOT_HouseSelectorApp(App):

    number_of_players = StringProperty('')


    index = NumericProperty(-1)
    current_title = StringProperty()
    time = NumericProperty(0)
    show_sourcecode = BooleanProperty(False)
    sourcecode = StringProperty()
    screen_names = ListProperty([])
    hierarchy = ListProperty([])


    def _set_player_number(self, n_players):
        
        self.manager.number_of_players = n_players
        self.manager.current = 'players'


    def build(self):
        self.title = 'hello world'
        Clock.schedule_interval(self._update_clock, 1 / 60.)
        self.screens = {}
        self.available_screens = sorted([
             'Buttons', 'ScreenManager'])
#            'Buttons', 'ToggleButton', 'Sliders', 'ProgressBar', 'Switches',
#            'CheckBoxes', 'TextInputs', 'Accordions', 'FileChoosers',
#            'Carousel', 'Bubbles', 'CodeInput', 'DropDown', 'Spinner',
#            'Scatter', 'Splitter', 'TabbedPanel + Layouts', 'RstDocument',
#            'Popups', 'ScreenManager'])
        self.screen_names = self.available_screens
        curdir = dirname(__file__)
        self.available_screens = [join(curdir, 'data', 'screens',
            '{}.kv'.format(fn)) for fn in self.available_screens]
        self.go_next_screen()

    def go_next_screen(self):
        self.index = (self.index + 1) % len(self.available_screens)
        screen = self.load_screen(self.index)
        sm = self.root.ids.sm
        sm.switch_to(screen, direction='left')
        self.current_title = screen.name
        self.update_sourcecode()

    def load_screen(self, index):
        if index in self.screens:
            return self.screens[index]
        screen = Builder.load_file(self.available_screens[index].lower())
        self.screens[index] = screen
        return screen

    def _update_clock(self, dt):
        self.time = time()
    

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
    GOT_HouseSelectorApp().run()
