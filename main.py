# By: Kristian Bjoerke

from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ListProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

import time
import random

class FirstScreen(Screen):
    pass

class SecondScreen(Screen):
    pass

class ThirdScreen(Screen):
    b = BoxLayout(orientation='vertical')
    number_of_players = NumericProperty()
    houses = ListProperty(['House Stark',
        'House Lannister',
        'House Baratheon',
        'House Greyjoy',
        'House Tyrell',
        'House Martel'])
    player_names = ListProperty(['first',
        'second',
        'third',
        'fourth',
        'fifth',
        'sixth'])

    def add_player(self, i):
        height = self.height
        height_per_player = height/self.number_of_players

        hb = BoxLayout(orientation='horizontal')
        l = Label(text='Player '+str(i)+': ',
                font_size=20)
        t = TextInput(font_size=40)

        hb.add_widget(l)
        hb.add_widget(t)
        self.b.add_widget(hb)

class ColourScreen(Screen):
    colour = ListProperty([1, 0, 0, 1])

class MyScreenManager(ScreenManager):
    def new_colour_screen(self):
        name = str(time.time())
        s = ColourScreen(name=name,
                colour=[random.random() for _ in range(3)] + [1])
        self.add_widget(s)
        self.current = name

    def select_number_of_players(self, np):
        name='player_screen'
        s = ThirdScreen(name=name,
                number_of_players=np)

        header_label = Label(text='Number of players: '+str(np),
                font_size=30)

        s.b.add_widget(header_label)

        for i in range(1, np+1):
            s.add_player(i)

        button = Button(text='Select houses', 
                font_size=20)
        s.b.add_widget(button)

        s.add_widget(s.b)
        self.add_widget(s)
        self.current = name
        


root_widget = Builder.load_string('''
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
#:import random random.random
MyScreenManager:
    transition: FadeTransition()
    FirstScreen:
    SecondScreen:

<FirstScreen>:
    name: 'first'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Game of Thrones Board Game House Selector'
            font_size: 30
        BoxLayout:
            Button:
                text: 'Start'
                font_size: 30
                on_release: app.root.current = 'second'
            Button:
                text: 'Info'
                font_size: 30
<SecondScreen>:
    name: 'second'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Number of players?'
            font_size: 30
        BoxLayout:
            Button:
                text: '3'
                font_size: 30
                on_release: app.root.select_number_of_players(3)
            Button:
                text: '5'
                font_size: 30
                on_release: app.root.select_number_of_players(5)
        BoxLayout:
            Button:
                text: '4'
                font_size: 30
                on_release: app.root.select_number_of_players(4)
            Button:
                text: '6'
                font_size: 30
                on_release: app.root.select_number_of_players(6)


<ColourScreen>:
    BoxLayout:
        orientation: 'vertical'
        colour: random(), random(), random(), 1
        Label:
            text: 'colour {:.2},{:.2},{:.2} screen'.format(*root.colour[:3])
            font_size: 30
        Widget:
            canvas:
                Color:
                    rgba: root.colour
                Ellipse:
                    pos: self.pos
                    size: self.size
        BoxLayout:
            Button:
                text: 'goto first screen'
                font_size: 30
                on_release: app.root.current = 'first'
            Button:
                text: 'get random colour screen'
                font_size: 30
                on_release: app.root.new_colour_screen()
''')

class ScreenManagerApp(App):
    def build(self):
        return root_widget

ScreenManagerApp().run()
