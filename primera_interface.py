from tkinter import *

def mensaje():
   print("este mensaje es de boton")

ventana = Tk()
ventana.title("hola mundo")
ventana.geometry("400x200")

lbl= Label(ventana,text="Este es un label")
lbl.pack()

btn = Button(ventana,text="Presionar",command = mensaje)
btn.config(fg="red", bg="yellow")
btn.pack()
ventana.mainloop()

