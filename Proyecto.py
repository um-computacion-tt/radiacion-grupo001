import tkinter as tk 
from tkinter import ttk 
from tkinter import *

import serial
PuertoSerie= serial.Serial("COM6", 9600)



def analisis():
    numimg=0
    sArduino = PuertoSerie.readline()
    while sArduino != "b'0.00\r\n'":
        sArduino = PuertoSerie.readline()
        caja_exp_sol=ttk.Label(text= sArduino[:-2])
        caja_exp_sol.place(x=140, y=40, width=60)
        break
    uv=float(sArduino[:-2])
    if uv <= 2:
        background = Label(ventana, image=imagen1).place(x=0, y=130)
        etiqueta_exposicion.config(text="La exposición es baja",foreground="#00CC00")
    elif 3<=uv and 5>=uv:
        etiqueta_exposicion.config(text="La exposición es moderada",foreground="#FFC107")
        background = Label(ventana, image=imagen2).place(x=0, y=130)
    elif 6<=uv and 7>=uv:
        etiqueta_exposicion.config(text="La exposición es alta",foreground="#FF6F00")
        background = Label(ventana, image=imagen2).place(x=0, y=130)
    elif 8<=uv and 10>=uv:
        etiqueta_exposicion.config(text="La exposición es muy alta",foreground="#E53935")
        background = Label(ventana, image=imagen3).place(x=0, y=130)
    elif uv>10:
        etiqueta_exposicion.config(text="La exposición es extramadamente alta",foreground="#9C27B0")
        background = Label(ventana, image=imagen3).place(x=0, y=130)


ventana = tk.Tk()
ventana.title("Exposición al Sol")
ventana.geometry("600x554")



etiqueta_indicacion=ttk.Label(text="Presione analizar: ")
etiqueta_indicacion.place(x=20,y=10)


etiqueta_exp_sol=ttk.Label(text="Radiación UV: ")
etiqueta_exp_sol.place(x=20,y=40)



boton_analizar = ttk.Button(text="Analizar", command=analisis)
boton_analizar.place(x=20, y=40)



etiqueta_exposicion=ttk.Label(text="La exposición es:")
etiqueta_exposicion.place(x=20, y=100)

imagen1 = PhotoImage(file="Escala1.png")
imagen2 = PhotoImage(file="Escala2.png")
imagen3 = PhotoImage(file="Escala3.png")


ventana.mainloop()
