import tkinter as tk 
from tkinter import ttk 

import serial
PuertoSerie= serial.Serial("COM6", 9600)


def analisis():
    sArduino = PuertoSerie.readline()
    while sArduino != "b'0.00\r\n'":
        sArduino = PuertoSerie.readline()
        caja_exp_sol=ttk.Label(text= sArduino[:-2])
        caja_exp_sol.place(x=140, y=40, width=60)
        print(sArduino[:-2])
        break
    uv=float(sArduino[:-2])
    if uv <= 2:
        etiqueta_exposicion.config(text="La exposición es baja",foreground="#00CC00")
    elif 3<=uv and 5>=uv:
        etiqueta_exposicion.config(text="La exposición es moderada",foreground="#FFC107")
    elif 6<=uv and 7>=uv:
        etiqueta_exposicion.config(text="La exposición es alta",foreground="#FF6F00")
    elif 8<=uv and 10>=uv:
        etiqueta_exposicion.config(text="La exposición es muy alta",foreground="#E53935")
    elif uv>10:
        etiqueta_exposicion.config(text="La exposición es extramadamente alta",foreground="#9C27B0")

ventana = tk.Tk()
ventana.title("Exposición al Sol")
ventana.config(width=400,height=300)

etiqueta_indicacion=ttk.Label(text="Ingrese la radiación UV: ")
etiqueta_indicacion.place(x=20,y=10)

etiqueta_exp_sol=ttk.Label(text="Radiación UV: ")
etiqueta_exp_sol.place(x=20,y=40)



boton_analisar = ttk.Button(text="Analizar", command=analisis)
boton_analisar.place(x=20, y=40)

etiqueta_exposicion=ttk.Label(text="La exposición es:")
etiqueta_exposicion.place(x=20, y=120)


ventana.mainloop()
