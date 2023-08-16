from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.audio import SoundLoader
from threading import Timer
from kivy.core.window import Window
import easygui
from mutagen.mp3 import MP3

Window.size = (400, 400)

class PlayerExample(BoxLayout):
    slider = ObjectProperty(None)
    filename = ObjectProperty(None)
    play = ObjectProperty(None)
    pause = ObjectProperty(None)
    stop = ObjectProperty(None)
    time = ObjectProperty(None)
    all_time = ObjectProperty(None)
    music_file = None
    sound = None
    timer = None
    seconds = 0

    def load_music(self):
        if self.timer != None:
            self.timer.cansel()
        self.music_file = easygui.fileopenbox(filetypes=["*.mp3"])
        if self.sound != None:
            self.stop_music()