"""El codigo permite crear una ventana con un boton
Envia datos cada que se presiona el boton
se usará para escribir el bit hacia el PLC
Se utiliza la librería tkinter y functools"""
#Importar los módulos necesarios
import Scripts.Modbus_client as client
import tkinter as tk
from tkinter import ttk
from functools import partial
import time
#Funcion para escribir el bit en el PLC, simula un pulsador
def escribir(ip,addres):
    client.write_simple_coil(ip,addres,1)#Escribe 1 al bit
    time.sleep(0.8)#Espera 0.8segundos
    client.write_simple_coil(ip,addres,0)#Escribe 0 al bit
    return

#Funcion para crear la ventana con el boton
def single_button(ip="",addres = ""):
    root = tk.Tk()#Creacion del objecto que permite crear ventanas
    root.config(width=300, height=200) #Configura una ventana de 300x200px
    root.title("Escritura de single coil")#Coloca el título a la ventana
    boton = ttk.Button(text="Escritura de coil", command=partial(escribir,ip,addres))#crea un boton en la ventana
    boton.place(x=50, y=50) #Coloca el boton en la posicion (50,50)px
    root.mainloop()#Crea un lazo loop hasta que se cierre la ventana 