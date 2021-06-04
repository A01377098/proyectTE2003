from tkinter import *
from PIL import ImageTk, Image
import os 
from pygame import mixer
from glob import glob
import serial

# ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
# ser.flush()

root = Tk()
root.title("AutoD")
titulo  = Label(root, text = "BIenvenido de nuevo")
#root.iconbitmap("D:\\A_TEC CEM\\IRS\\4to Semestre\\Programacion\\musica.mp4
titulo.grid(row=0, column=0, columnspan=3)
imagenA = ImageTk.PhotoImage(Image.open("Imagenes/myimage.png"))
imagenB = ImageTk.PhotoImage(Image.open("Imagenes/homero.png"))
imagenC = ImageTk.PhotoImage(Image.open("Imagenes/homer2.png"))
imagenD = ImageTk.PhotoImage(Image.open("Imagenes/stich.png"))
imagenE = ImageTk.PhotoImage(Image.open("Imagenes/conejo.png"))
lista_Imagenes = [imagenA, imagenB, imagenC, imagenD, imagenE]

status = Label(root, text="Canciones 1 of " + str(len(lista_Imagenes)), bd=1, relief=SUNKEN, anchor=E)

label_image = Label(image=imagenB)
label_image.grid(row=1, column=0, columnspan=3)
# Crear una lista de las canciones que hay en la raspberry
contenido = os.listdir('D:\\A_TEC CEM\\IRS\\4to Semestre\\Programacion')
lista_Canciones = []
#imagenA = ImageTk.PhotoImage(Image.open())
for archivo in contenido :
    if archivo.endswith(".mp3"):
        lista_Canciones.append(archivo)
    elif archivo.endswith(".wav"):
        lista_Canciones.append(archivo)
            
def forward(image_number):
    global button_forward
    global button_back
    global label_image
    
    label_image.grid_forget()
    label_image = Label(image=lista_Imagenes[image_number-1])
    button_forward = Button(root, text = ">>", command= lambda: forward(image_number +1))
    button_back = Button(root, text = "<<", command= lambda: back(image_number -1))
    
    if image_number == 5:
         button_forward = Button(root, text = ">>", state=DISABLED)
    button_back.grid(row=2, column=0)
    button_forward.grid(row=2, column =2)
    
    label_image.grid(row=1, column=0, columnspan=3)
    status = Label(root, text="Canciones "+ str(image_number) + " of " + str(len(lista_Imagenes)), bd=1, relief=SUNKEN, anchor=E)    
    status.grid(row=3, column=0, columnspan=3, sticky=W+E)
    
def back(image_number):
    global button_forward
    global button_back
    global label_image
    
    label_image.grid_forget()
    label_image = Label(image=lista_Imagenes[image_number-1])
    button_forward = Button(root, text = ">>", command= lambda: forward(image_number +1))
    button_back = Button(root, text = "<<", command= lambda: back(image_number -1))
    
    button_back.grid(row=2, column=0)
    button_forward.grid(row=2, column =2)
    
    label_image.grid(row=1, column=0, columnspan=3)
    status = Label(root, text="Canciones "+ str(image_number) + " of " + str(len(lista_Imagenes)), bd=1, relief=SUNKEN, anchor=E)    
    status.grid(row=3, column=0, columnspan=3, sticky=W+E)
    
def Reproductor(Lista):
    pass
#     opcion = ""
#     print("1")
#     contador = 0
#     while True:  
#         mixer.init()
#         i = contador
#         cancion = str(Lista[contador])
#         mixer.music.load(cancion)
#         mixer.music.set_volume(0.9)
#         mixer.music.play()
#         i = 0
#         while True:
#             long_string = Lista[contador]
#             if i == len(long_string)+1:
#                 i = 0
#             framebuffer[1] = long_string[i:i+16]
#             time.sleep(0.300)
#             i += 1
#             Ocupado = mixer.music.get_busy()
#             print("Esperando opcion")
#             if ser.in_waiting > 0:
#                 opcion = ser.readline().decode('utf-8').rstrip()
#             if opcion == "Pause":
#                 print("Pausa")
#                 opcion = ""
#                 mixer.music.pause()
#             elif opcion == "Play":
#                 print("Play")
#                 opcion = ""
#                 mixer.music.unpause()
#             elif opcion =="Sig":
#                 opcion = ""
#                 print("Sig")
#                 contador += 1
#                 if contador <= len(Lista)-1:
#                     mixer.music.stop()
#                     lcd.clear()
#                     break
#                 else:
#                     contador = 0
#                     mixer.music.stop()
#                     lcd.clear()
#                     break
#             elif opcion =="Ant":
#                 opcion = ""
#                 contador -=1
#                 print(contador)
#                 if contador >= 0:
#                     mixer.music.stop()
#                     break
#                 else:
#                     contador = len(Lista)-1
#                     mixer.music.stop()
#                     break
#             elif opcion == "Enter":
#                 mixer.music.stop()
#                 return
#             
#             elif Ocupado == False:
#                 contador += 1
#                 if contador <= len(Lista)-1:
#                     mixer.music.stop()
#                     lcd.clear()
#                     break
#                 else:
#                     contador = 0
#                     print("Fin")
#                     break
#                 


button_back = Button(root, text = "<<", command=back)
button_forward = Button(root, text = ">>", command= lambda: forward(2))

button_back.grid(row=2, column=0)
button_forward.grid(row=2, column =2)
buttoon_play_musica.grid(row=2, column=4)

status.grid(row=3, column=0, columnspan=3, sticky=W+E)
#


root.mainloop()