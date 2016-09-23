# By: Kristian Bjoerke

from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

import time
import random

class FirstScreen(Screen):
    pass

class SecondScreen(Screen):
    pass

class ColourScreen(Screen):
    colour = ListProperty([1, 0, 0, 1])

class MyScreenManager(ScreenManager):
    def new_colour_screen(self):
        name = str(time.time())
        s = ColourScreen(name=name,
                colour=[random.random() for _ in range(3)] + [1])
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
            text: 'Choose number of players'
            font_size: 30
        BoxLayout:
            Button:
                text: '3'
                font_size: 30
                on_release: app.root.current = 'first'
            Button:
                text: '5'
                font_size: 30
                on_release: app.root.new_colour_screen()
        BoxLayout:
            Button:
                text: '4'
                font_size: 30
                on_release: app.root.current = 'first'
            Button:
                text: '6'
                font_size: 30
                on_release: app.root.new_colour_screen()
<ThirdScreen>:
    name: 'second'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Choose number of players'
            font_size: 30
        BoxLayout:
            Button:
                text: '3'
                font_size: 30
                on_release: app.root.current = 'first'
            Button:
                text: '5'
                font_size: 30
                on_release: app.root.new_colour_screen()
        BoxLayout:
            Button:
                text: '4'
                font_size: 30
                on_release: app.root.current = 'first'
            Button:
                text: '6'
                font_size: 30
                on_release: app.root.new_colour_screen()
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
