import tkinter as tk
from tkinter import ttk

def mostrar_opcion(evento):
    print("Opción seleccionada:", combobox.get())

ventana = tk.Tk()
ventana.title("Ejemplo de Combobox")

combobox = ttk.Combobox(ventana, values=["Opción 1", "Opción 2", "Opción 3"])
combobox.pack(pady=10)
combobox.bind("Caja", mostrar_opcion)

ventana.mainloop()