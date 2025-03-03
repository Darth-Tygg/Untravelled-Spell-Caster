# KivyMD training video: https://www.youtube.com/watch?v=LRXo0juuTrw&list=PLhTjy8cBISEpobkPwLm71p5YNBzPH9m9V&index=24
# https://www.youtube.com/watch?v=jtunAA7V96g
# RGB color values: https://www.w3schools.com/colors/colors_rgb.asp
# Font Styles: https://raw.githubusercontent.com/HeaTTheatR/KivyMD-data/master/gallery/kivymddoc/md-label-font-style.gif
# This Program helps calculate the casting difficulty and cost of spells and has a dice roller
# https://wiki.untraveled.games/
# All spells have a base cost of 2
# Range , Area of effect , Casting Speed , Duration


from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
import helpers
from kivymd.uix.list import ThreeLineListItem, MDList
from kivy.uix.scrollview import ScrollView
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.core.window import Window
import pyinputplus as py
import tkinter as tk
from tkinter import *


Window.size = (300, 500)

navigation_helper = """
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: 'Untraveled'
                        halign: 'center'
                        left_action_items: [["menu", lambda x: nav_drawer.set_state()]]                        
                    Widget:                        
                    MDLabel:
                        text: ''
                        halign: 'center'
                    ScrollView:
                        MDList:
                            id: container

                    MDBottomNavigation:
                        panel_color: app.theme_cls.primary_color
                        text_color_active: get_color_from_hex("F5F5F5")
                        MDBottomNavigationItem:
                            name: "Screen 1"
                            text: "Placeholder"
                            halign: "center"
                            icon: "language-python"
        MDNavigationDrawer:
            id: nav_drawer

"""

spell_range_helper = """
MDTextField:
    hint_text: "Enter range"
    pos_hint: {'center_x': 0.4, 'center_y': 0.7}
    size_hint_x: None
    width: 100
"""

spell_aoe_helper = """
MDTextField:
    hint_text: "Enter area of effect"
    pos_hint: {'center_x': 0.4, 'center_y': 0.6}
    size_hint_x: None
    width: 100
"""

cast_speed_helper = """
MDTextField:
    hint_text: "Enter cast speed"
    pos_hint: {'center_x': 0.4, 'center_y': 0.5}
    size_hint_x: None
    width: 100
"""

expiration_helper = """
MDTextField:
    hint_text: "Enter expiration"
    pos_hint: {'center_x': 0.4, 'center_y': 0.4}
    size_hint_x: None
    width: 100
"""


class Untraveled(MDApp):
    def build(self):
        screen = Builder.load_string(navigation_helper)
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Dark"
        button = MDRectangleFlatButton(text='Click Here', pos_hint={'center_x': 0.4, 'center_y': 0.2},
                                       size_hint_x=None, width=300, on_release=self.show_data)
        self.spell_range = Builder.load_string(spell_range_helper)
        screen.add_widget(self.spell_range)
        self.spell_aoe = Builder.load_string(spell_aoe_helper)
        screen.add_widget(self.spell_aoe)
        self.cast_speed = Builder.load_string(cast_speed_helper)
        screen.add_widget(self.cast_speed)
        self.expiration = Builder.load_string(expiration_helper)
        screen.add_widget(self.expiration)
        screen.add_widget(button)
        return screen

    def show_data(self, obj):
        s_range = {"touch": 0, "short": 1, "medium": 2, "long": 3, "extreme": 4}
        spell_area = {"small": 0, "large": 2, "huge": 6, "gargantuan": 12, "colossal": 20}
        casting_speed = {"short action": 4, "long action": 0, "2 rounds": -3, "3 rounds": -5, "4 rounds": -6,
                         "minute": -8,
                         "5 minutes": -18, "15 minutes": -23, "hour": -30}
        spell_expiration = {"round": 1, "minute": 2, "hour": 5, "day": 10, "week": 20, "month": 30, "year": 50}
        r = int(s_range.get(self.spell_range))
        a = int(spell_area.get(self.spell_aoe))
        c = int(casting_speed.get(self.cast_speed))
        e = int(spell_expiration.get(self.expiration))
        total = 2 + r + a + c + e
        close_button = MDFlatButton(text='Close', on_release=self.close_dialog)
        dialog = MDDialog(title='Casting difficulty and cost', int=total,
                          size_hint=(0.7, 1), buttons=[close_button])
        dialog.open()

    def navigation_draw(self, obj):
        print("Navigation")

    def close_dialog(self, obj):
        self.dialog.dismiss()


Untraveled().run()
