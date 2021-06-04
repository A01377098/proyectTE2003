from tkinter import *
from tkinter import filedialog
import pygame
from glob import glob

root = Tk()
root.title("Música")
root.geometry("500x400")

#Inicialización de la musica 
pygame.mixer.init()
global paused
paused = False

def add_song():
    song =filedialog.askopenfilename(initialdir="audio/", title="Escoge una cancion", filetypes=(("mp3 FIles", ".mp3"), ))
    #song_name=song.split('/')[-1].split('.')[0]
#     song1=song.replace("D:/A_TEC CEM/IRS/4to Semestre/Programacion/Pygame/audio/", " ") 
#     song1=song1.replace(".mp3", " ")
    song_box.insert(END, song)
    
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
    next_one = song_box.cursor.curselection()
    next_one = next_one[0]+1
    song = song_box.get(next_one)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(-1)
    
    song_box.selection_clear(0, END)
    song_box.active(next_one)
    song_box.selection_set(next_one, Last=None)
    
def previous():
    next_one = song_box.cursor.curselection()
    next_one = next_one[0]-1
    song = song_box.get(next_one)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(-1)
    
    song_box.selection_clear(0, END)
    song_box.active(next_one)
    song_box.selection_set(next_one, Last=None)
    
#Lista de canciones
song_box = Listbox(root, bg="black", fg="white", width=300, selectbackground="gray", selectforeground="white")
song_box.pack(pady=20)

#Botones de control
back_image= PhotoImage(file= "Musica/rewind.png")
play_image=PhotoImage(file= "Musica/play.png")
pause_image=PhotoImage(file= "Musica/pausa.png")
stop_image=PhotoImage(file= "Musica/stop.png")
forward_image=PhotoImage(file= "Musica/forward.png")

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
menuD.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label= "Añade cancion a la lista", command=add_song)

root.mainloop()
