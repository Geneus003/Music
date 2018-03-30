import pygame, time, sys, os
from threading import Thread
from mutagen.mp3 import MP3
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton)
from PyQt5.QtGui import (QPixmap, QFont, QIcon)
from PyQt5.QtCore import (Qt, QSize)

pygame.init()

app = QApplication(sys.argv)
root = QWidget()


class MainScreen():

    def __init__(self):

        self.a = 3


main_screen_var = MainScreen()
global a
a = True


def playMusic():
    while a == True:
        music_road = "Allmusic/"
        music_road += my_input
        music_road += ".mp3"
        pygame.mixer.music.load(music_road)
        b = MP3(music_road)
        pygame.mixer.music.play()
        time.sleep(10)
        pygame.mixer.music.pause()
        time.sleep(3)
        pygame.mixer.music.unpause()
        time.sleep(int(b))
        pygame.mixer.music.stop()
        break


def main_window(main_screen_var):
    global my_input

    root.resize(1280, 720)
    root.move(400, 200)
    root.show()

    all_music_dir = '/home/geneus/Music/Allmusic'

    all_music = os.listdir(all_music_dir)

    for i in range(len(all_music)):
        print(all_music[i])

    my_input = input()

    now_music = Thread(target=playMusic)
    now_music.start()


main_window(main_screen_var)

a = False

sys.exit(app.exec_())
