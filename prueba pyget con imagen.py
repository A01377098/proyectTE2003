#Archivo completo 4/6/2021

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import pygame
from glob import glob
import time
import os
import serial
from concurrent.futures import ProcessPoolExecutor #Multi-core processing 

#Estados de las señales
global running
running = True

#Creacion de la raíz
root = Tk()
root.title("Música")
root.geometry("500x400")

#Inicialización de la musica 
pygame.mixer.init()
global paused
paused = False

# Crear una lista de las canciones que hay en la raspberry
contenido = os.listdir('/home/pi/proyectTE2003/')
lista_Canciones = []

for archivo in contenido :
    if archivo.endswith(".mp3"):
        lista_Canciones.append(archivo)
    elif archivo.endswith(".wav"):
        lista_Canciones.append(archivo)

def add_song():
    #song =filedialog.askopenfilename(initialdir="audio/", title="Escoge una cancion", filetypes=(("mp3 FIles", ".mp3"), ))
    path = os.getcwd() + "/"
    for cancion in lista_Canciones:
        song = path + cancion
        song_box.insert(END, song)
#     song1=song.replace("D:/A_TEC CEM/IRS/4to Semestre/Programacion/Pygame/audio/", " ") 
#     song1=song1.replace(".mp3", " ")
    
<<<<<<< HEAD
#Recibe las señales del control mientras el mainloop de la raíz se va a ejecutar
def serial_signals():

    global state

    ser = serial.Serial('/dev/ttyACM0', 9600, timeout = 1)
    ser.flush()
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
                     
            if (line == "0xFF22DD"):
                
                if  state == "reproducir":
                    state = "pausar"
                    pausa(False)


                elif state == "pausar":
                    state = "reproducir"
                    play()

                        
            elif (line == "0xFF02FD"):
                state = "anterior"
                previous_song()
                
                    
            elif (line == "0xFFC23D"):
                state = "siguiente"
                next_song()

                    
            elif (line == "0xFF906F"):
                state = "subir_volumen"

                    
            elif (line == "0xFFA857"):
                state = "bajar_volumen"
    
=======
>>>>>>> 8141e82fb578081f4052ac9965843f88b7b22f2b
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

    if next_one[0]+1 > song_box.size():
        
        next_one = next_one[0]
    else:
        next_one = next_one[0]+1

    if (song_box.get(next_one) == ''):
        
        song = song_box.get(0)
        next_one = (0,)
    else:
        song = song_box.get(next_one)

    print(type(next_one))
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(-1)
    
    song_box.selection_clear(0, END)
    song_box.activate(next_one)
    song_box.selection_set(next_one, last = next_one)
    
def previous_song():
    next_one = song_box.curselection()

    if next_one[0] == 0:
        next_one = next_one[0]-1

    elif next_one[0]-1 < 0:
        
        next_one = next_one[0]
        song = song_box.get(next_one)

    else:
        next_one = next_one[0]-1
        song = song_box.get(next_one)

    if song_box.get(next_one) == '':
        print(song_box.size())
        song = song_box.get(song_box.size()-1)
        next_one = (song_box.size()-1,)

    

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

back= Button(controls_frame, image=back_image, borderwidth=0, command=previous_song)
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

#Recibe las señales del control mientras el mainloop de la raíz se va a ejecutar
ser = serial.Serial('/dev/ttyACM0', 9600, timeout = 1)
ser.flush()
contador_veces=0
while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        print(line)     
        if (line == "0xFF22DD"):
             if contador_veces%2 == 0: 
                estado = "pausar"
                 pausa(False)
                 pausa()

              else:
                   estado = "reproducir"
                   play()


          elif (line == "0xFF02FD"):
               estado = "anterior"
               previous_song()


          elif (line == "0xFFC23D"):
                estado = "siguiente"
                next_song()


          elif (line == "0xFF906F"):
                estado = "subir_volumen"


          elif (line == "0xFFA857"):
                estado = "bajar_volumen"
#executor = ProcessPoolExecutor()
#executor.map(root.mainloop(), serial_signals())
root.mainloop()
#root.destroy()
