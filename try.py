import pyglet
from PyQt5.QtCore import Qt

print(pyqt.version , qt.version)

music = pyglet.resource.media('Allmusic/Megastar.mp3')
music.play()

pyglet.app.run()