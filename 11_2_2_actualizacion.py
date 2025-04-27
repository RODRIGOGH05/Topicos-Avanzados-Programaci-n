import time
import tkinter as tk

def actualizar_etiqueta():
    etiqueta.config(text="Actualizando...")
    ventana.update_idletasks()
    time.sleep(4)
    etiqueta.config(text="¡Actualizado!")

ventana = tk.Tk()
ventana.title("Actualización de Widgets")

etiqueta = tk.Label(ventana, text="Estado inicial")
etiqueta.pack(pady=10)

boton = tk.Button(ventana, text="Actualizar", command=actualizar_etiqueta)
boton.pack(pady=10)

ventana.mainloop()