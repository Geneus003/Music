import pygame, time, sys, os, vlc
from threading import Thread
from mutagen.mp3 import MP3
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton)
from PyQt5.QtGui import (QPixmap, QFont, QIcon)
from PyQt5.QtCore import (Qt, QSize)

pygame.init()

app = QApplication(sys.argv)
root = QWidget()


class MusicList():

    def __init__(self):

        self.all_music_dir = '/home/geneus/Music/Allmusic'
        self.all_music = os.listdir(self.all_music_dir)

        self.x_music_list = 10
        self.y_music_list = 10

        self.all_music_list_list = []

        for i in range(len(self.all_music)):
            self.all_music[i] = self.all_music[i][:int(len(self.all_music[i]) - 4)]
            self.all_music_list_list.append(QLabel(self.all_music[i], root))
            self.all_music_list_list[i].move(self.x_music_list, self.y_music_list)
            self.all_music_list_list[i].show()

            self.y_music_list += 20


music_list_var = MusicList()
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


def main_window(music_list_var):
    global my_input, st_sto

    root.resize(1280, 720)
    root.move(400, 200)
    root.show()

    my_input = input()

    now_music = Thread(target=playMusic)
    now_music.start()


main_window(music_list_var)

a = False

sys.exit(app.exec_())
