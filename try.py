import pyglet
pyglet.lib.load_library('avbin')
pyglet.have_avbin=True

music = pyglet.resource.media('Allmusic/Megastar.mp3')
music.play()

pyglet.app.run()
