#!/usr/bin/env python
#
# A Game of Thrones House Selector app
# By: Kristian Bjoerke

__version__ = "0.9.1"

from kivy.app import App
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
    pass
        
class FourthScreen(Screen):
    pass

class MyScreenManager(ScreenManager):
    b1 = BoxLayout(orientation='vertical')
    b2 = BoxLayout(orientation='vertical')
    
    number_of_players = NumericProperty()
    houses = ListProperty(['House Stark',
        'House Lannister',
        'House Baratheon',
        'House Greyjoy',
        'House Tyrell',
        'House Martel'])
    names_list = ListProperty(['first',
        'second',
        'third',
        'fourth',
        'fifth',
        'sixth'])
    player_names = ListProperty()

    def select_number_of_players(self, np):
        self.number_of_players = np
        name = str(time.time())
        s = ThirdScreen(name=name)

        header_label = Label(text='Enter names of players:',
                font_size=30)

        self.b1.add_widget(header_label)

        for i in range(1, np+1):
            self.add_player(i)

        button = Button(text='Select houses', 
                font_size=20,
                on_release=self.select_houses)
        self.b1.add_widget(button)

        s.add_widget(self.b1)
        self.add_widget(s)
        self.current = name
    
    def add_player(self, i):
        height = self.height
        height_per_player = height/self.number_of_players

        hb = BoxLayout(orientation='horizontal')
        l = Label(text='Player '+str(i)+': ',
                font_size=20)
        t = TextInput(id=str(i),
                font_size=40)

        t.bind(text=self.update_player)

        hb.add_widget(l)
        hb.add_widget(t)
        self.b1.add_widget(hb)
    
    def update_player(self, textinput_instance, text):
        self.names_list[int(textinput_instance.id)-1] = text

    def select_houses(self, *args):
        self.player_names = self.names_list[0:self.number_of_players]
        
        name = str(time.time())
        s = FourthScreen(name=name)

        random.shuffle(self.player_names)

        for i in range(0, self.number_of_players):
            self.house_player(i)

        button = Button(text='Exit', 
                font_size=20,
                on_release=self.exit_selector)
        self.b2.add_widget(button)

        s.add_widget(self.b2) 
        self.add_widget(s)
        self.current = name

    def house_player(self, i):
        hb = BoxLayout(orientation='horizontal')
        l = Label(text=self.houses[i]+': '+self.player_names[i],
                font_size=40)
        hb.add_widget(l)
        self.b2.add_widget(hb)

    def exit_selector(self, *args):
        self.current='first'

        self.b1 = BoxLayout(orientation='vertical')
        self.b2 = BoxLayout(orientation='vertical')


root_widget = Builder.load_string('''
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
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
''')

class ScreenManagerApp(App):
    def build(self):
        return root_widget

ScreenManagerApp().run()
