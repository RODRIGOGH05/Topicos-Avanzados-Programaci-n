import tkinter as tk
import time

def actualizar_reloj():
    etiqueta.config(text=time.strftime("%H:%M:%S"))
    ventana.after(1000, actualizar_reloj)

ventana = tk.Tk()
ventana.title("Reloj en tiempo real")

etiqueta = tk.Label(ventana, font=("Arial", 24))
etiqueta.pack(pady=10)

actualizar_reloj()
ventana.mainloop()