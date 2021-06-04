# importing pyglet module
import pyglet
import os 
# width of window
width = 800
    
# height of window
height = 600
    
# caption i.e title of the window
title = "Auto D"

    
# creating a window
window = pyglet.window.Window(width, height, title)
text = "Bievenido"
label = pyglet.text.Label(text,
                          font_name ='Times New Roman',
                          font_size = 36,
                          x = window.width//2, y = window.height//2,
                          anchor_x ='center', anchor_y ='center')

def Leyendo_Canciones():
    ruta = r'/home/pi/Documents/Proyecto_Canciones_1'
    Lista_F = []
    contenido = os.listdir(ruta)
    
# video path
vidPath ="/home/pi/proyectTE2003/y2mate.com - Duncan Laurence  Arcade Lyrics ft FLETCHER_1080p.mp4"

# creating a media player object
player = pyglet.media.Player()

# creating a source object
source = pyglet.media.StreamingSource()

# load the media from the source
MediaLoad = pyglet.media.load(vidPath)

# add this media in the queue
player.queue(MediaLoad)

# play the video
player.play()

# on draw event
@window.event
def on_draw():
    
    # clea the window
    window.clear()
    label.draw()
    
    # if player sorce exist
    # and video format exist
    if player.source and player.source.video_format:
        
        # get the texture of video and
        # make surface to display on the screen
        player.get_texture().blit(0, 0)
        
        
# key press event   
@window.event
def on_key_press(symbol, modifier):
    
    # key "p" get press
    if symbol == pyglet.window.key.P:
        
        # printng the message
        print("Key : P is pressed")
        
        # pause the video
        player.pause()
        
        # printing message
        print("Video is paused")
        
        
    # key "r" get press
    if symbol == pyglet.window.key.R:
        
        # printng the message
        print("Key : R is pressed")
        
        # resume the video
        player.play()
        
        # printing message
        print("Video is resumed")

# run the pyglet application
pyglet.app.run()
