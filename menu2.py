from  tkinter import *
from PIL import ImageTk, Image

top = Tk()


mb=  Menubutton ( top, text="Menú", relief=RAISED )
mb.grid()
mb.menu =  Menu ( mb, tearoff = 0 )
mb["menu"] =  mb.menu

reproduccionVar = IntVar()
temperaturaVar = IntVar()
otrosVar = IntVar()

imagenA = ImageTk.PhotoImage(Image.open("Imagenes/myimage.png"))
label_image = Label(image=imagenA)

mb.menu.add_checkbutton ( label="Reproductor de música",
                          variable=reproduccionVar )
mb.menu.add_checkbutton ( label="Temperatura",
                          variable=temperaturaVar )
mb.menu.add_checkbutton ( label="Otros",
                          variable=otrosVar )

label_image.grid(row=1, column=0, columnspan=3)
mb.grid(row=0, column=0, columnspan=3)
top.mainloop()