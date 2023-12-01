import pygame as p


class Sound:

    def __init__(self):
        p.mixer.init()

    def play_sound(self, file_path):
        p.mixer.music.load(file_path)
        p.mixer.music.play()



