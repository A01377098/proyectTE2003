#Archivo completo 4/6/2021

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import pygame
from glob import glob
import time
import os

root = Tk()
root.title("Música")
root.geometry("500x400")

#Inicialización de la musica 
pygame.mixer.init()
global paused
paused = False

# Crear una lista de las canciones que hay en la raspberry
contenido = os.listdir('C:\\Users\\Omar Sorchini\\Desktop\\TEC\\Eva\\proyectTE2003')
lista_Canciones = []

for archivo in contenido :
    if archivo.endswith(".mp3"):
        lista_Canciones.append(archivo)
    elif archivo.endswith(".wav"):
        lista_Canciones.append(archivo)

def add_song():
    #song =filedialog.askopenfilename(initialdir="audio/", title="Escoge una cancion", filetypes=(("mp3 FIles", ".mp3"), ))
    path = os.getcwd() + "/proyectTE2003/"
    for cancion in lista_Canciones:
        song = path + cancion
        song_box.insert(END, song)
    #song_name=song.split('/')[-1].split('.')[0]
#     song1=song.replace("D:/A_TEC CEM/IRS/4to Semestre/Programacion/Pygame/audio/", " ") 
#     song1=song1.replace(".mp3", " ")
    
    
    
def play():
    song = song_box.get(ACTIVE)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(-1)
    
def stop():
    pygame.mixer.music.stop()

def pausa(is_pausedo):
    global paused
    paused = is_pausedo
    if is_pausedo:
        pygame.mixer.music.unpause()
        paused=False
    else:
        pygame.mixer.music.pause()
        paused=True

def next_song():
    next_one = song_box.curselection()
    print(next_one)

    if next_one[0]+1 > song_box.size():
        
        next_one = next_one[0]
    else:
        next_one = next_one[0]+1

    if  (song_box.get(next_one) == ''):
        
        song = song_box.get(0)
        next_one = (0,)
    else:
        song = song_box.get(next_one)

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(-1)
    
    song_box.selection_clear(0, END)
    song_box.activate(next_one)
    song_box.selection_set(next_one, last = next_one)
    
def previous():
    next_one = song_box.curselection()

    if next_one[0]-1 < 0:
        
        next_one = next_one[0]
    else:
        next_one = next_one[0]-1

    song = song_box.get(next_one)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(-1)
    
    song_box.selection_clear(0, END)
    song_box.activate(next_one)
    song_box.selection_set(next_one, last = next_one)

imagenA = ImageTk.PhotoImage(Image.open("michael.gif"))
imagenB = ImageTk.PhotoImage(Image.open("play.png"))
imagenC = ImageTk.PhotoImage(Image.open("pausa.png"))
lista_Imagenes = [imagenA, imagenB, imagenC]

controls_frame_songs = Frame(root)
controls_frame_songs.pack()
label_image = Label(controls_frame_songs, image=imagenA, borderwidth=0)
#Lista de canciones
song_box = Listbox(controls_frame_songs, bg="black", fg="white", width=300, height= 18, selectbackground="gray", selectforeground="white")
label_image.grid(row=0, column=0)
song_box.grid(row = 0, column = 1)

#Botones de control
back_image= PhotoImage(file= "rewind.png")
play_image=PhotoImage(file= "play.png")
pause_image=PhotoImage(file= "pausa.png")
stop_image=PhotoImage(file= "stop.png")
forward_image=PhotoImage(file= "forward.png")

#Los botones se muestran en la ventana con un Frame
controls_frame = Frame(root)
controls_frame.pack()

back= Button(controls_frame, image=back_image, borderwidth=0, command=previous)
play=Button(controls_frame, image=play_image, borderwidth=0, command=play)
pauseButton=Button(controls_frame, image=pause_image, borderwidth=0, command=lambda: pausa(paused))
stop=Button(controls_frame, image=stop_image, borderwidth=0, command=stop)
forward=Button(controls_frame, image=forward_image, borderwidth=0, command=next_song)

back.grid(row=0, column=0 )
play.grid(row=0, column=1)
pauseButton.grid(row=0, column=2)
stop.grid(row=0, column=3)
forward.grid(row=0, column=4)

menuD=Menu(root)
root.config(menu=menuD)

add_song_menu = Menu(menuD)
menuD.add_cascade(label="Añade tus canciones", menu=add_song_menu)
add_song_menu.add_command(label= "Cargar canciones", command=add_song)

root.mainloop()
root.destroy()