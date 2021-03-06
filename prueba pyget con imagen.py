#Archivo completo 4/6/2021
#800 x 480 resolucion de pantalla raspberrypi

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import pygame
from glob import glob
import time
import os
import serial
#from concurrent.futures import ProcessPoolExecutor #Multi-core processing 

#Creacion de serial
ser = serial.Serial('/dev/ttyACM0', 9600, timeout = 0, writeTimeout=0)
#Estados de las señales
global state
state = ""
global contador_veces
contador_veces = 0

#Creacion de la raíz
root = Tk()
root.title("Música")
root.geometry("800x480")

#Actualizacion de string de temperatura
global valor
valor = StringVar()
valor.set("20")

#Actualizacion de variable temperatura
global temperatura_valor_signal
temperatura_valor_signal = 0.0
#Inicialización de la musica 
pygame.mixer.init()
global paused
paused = False

# Crear una lista de las canciones que hay en la raspberry
# Directorio de Omar: C:/Users/Omar Sorchini/Desktop/TEC/Eva/proyectTE2003
# Directorio de Raspberry: /home/pi/proyectTE2003

contenido = os.listdir('/home/pi/proyectTE2003')
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
        song_box.insert(END, cancion)
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

    if next_one[0]+1 > song_box.size():
        
        next_one = next_one[0]
    else:
        next_one = next_one[0]+1

    if (song_box.get(next_one) == ''):
        
        song = song_box.get(0)
        next_one = (0,)
    else:
        song = song_box.get(next_one)

    #print(type(next_one))
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
        #print(song_box.size())
        song = song_box.get(song_box.size()-1)
        next_one = (song_box.size()-1,)

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(-1)
    
    song_box.selection_clear(0, END)
    song_box.activate(next_one)
    song_box.selection_set(next_one, last = next_one)

def exit():
    
    pygame.quit()
    sys.exit()


#Actualizacion de linea de temperatua en le pantalla
def updateTemp(temperatura_valor_signal):
    valor.set("La temperatura actual es: " + str(temperatura_valor_signal) + "°")
    #temp_text.after(1, updateTemp)
    
#Recibe las señales del control mientras el mainloop de la raíz se va a ejecutar
def serial_signals():

    global state
    global contador_veces
    global temperatura_valor_signal

    if ser.in_waiting > 0:
        line = ser.readline().decode('latin1').rstrip()
        #if len(line) == 0:
            #break
                     
        if (line == "0xFF22DD"):
            contador_veces += 1
            if  contador_veces%2 == 0: #Se encuentra reproduciendo
                state = "pausar"
                pausa(False)
            elif contador_veces%2 != 0: #Indicativo que está en pausa
                state = "reproducir"
                play()
      
        elif (line == "0xFF02FD"):
            state = "anterior"
            previous_song()
                
                    
        elif (line == "0xFFC23D"):
            state = "siguiente"
            next_song()
            
        elif (line=="1"):
            add_song()
            
        else: 
             temperatura_valor_signal = line 
             updateTemp(temperatura_valor_signal)
             
    root.after(10, serial_signals)

imagenA = ImageTk.PhotoImage(Image.open("michael.gif"))
imagenB = ImageTk.PhotoImage(Image.open("play.png"))
imagenC = ImageTk.PhotoImage(Image.open("pausa.png"))
lista_Imagenes = [imagenA, imagenB, imagenC]

#Botones de control
back_image= PhotoImage(file= "rewind.png")
play_image=PhotoImage(file= "play.png")
pause_image=PhotoImage(file= "pausa.png")
stop_image=PhotoImage(file= "stop.png")
forward_image=PhotoImage(file= "forward.png")
delete_image=PhotoImage(file = "off.png")
temp_image = PhotoImage(file = "sunshine.png")

#Frame 1
control_temp_frame = Frame(root)
control_temp_frame.pack()
temp = Button(control_temp_frame, image= temp_image , borderwidth= 0)
temp_text = Label(control_temp_frame, textvariable = valor,borderwidth=0)
temp.grid(row = 0, column= 0)
temp_text.grid(row = 0, column= 1)

#Frame 2
controls_frame_songs = Frame(root)
controls_frame_songs.pack()
label_image = Label(controls_frame_songs, image=imagenA, borderwidth=0)
#Lista de canciones
song_box = Listbox(controls_frame_songs, bg="black", fg="white", width=170, height= 14, selectbackground="gray", selectforeground="white")
label_image.grid(row=0, column=0)
song_box.grid(row = 0, column = 1)

#Los botones se muestran en la ventana con un Frame
#Frame 3
controls_frame = Frame(root)
controls_frame.pack()

backButton= Button(controls_frame, image=back_image, borderwidth=0, command=previous_song)
playButton=Button(controls_frame, image=play_image, borderwidth=0, command=play)
pauseButton=Button(controls_frame, image=pause_image, borderwidth=0, command=lambda: pausa(paused))
stopButton=Button(controls_frame, image=stop_image, borderwidth=0, command=stop)
forwardButton=Button(controls_frame, image=forward_image, borderwidth=0, command=next_song)
exitButton = Button(controls_frame, image = delete_image, borderwidth=0, command= exit)

backButton.grid(row=0, column=0 )
playButton.grid(row=0, column=1)
pauseButton.grid(row=0, column=2)
stopButton.grid(row=0, column=3)
forwardButton.grid(row=0, column=4)
exitButton.grid(row=0, column=5)

menuD=Menu(root)
root.config(menu=menuD)

add_song_menu = Menu(menuD)
menuD.add_cascade(label="Añade tus canciones", menu=add_song_menu)
add_song_menu.add_command(label= "Cargar canciones", command=add_song)

#executor = ProcessPoolExecutor()
#executor.map(root.mainloop(), serial_signals())
root.after(1000, serial_signals)
root.after(1005, updateTemp)
root.mainloop()
#root.destroy()
