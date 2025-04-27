from tkinter import ttk
import tkinter as tk

def cambiar_tema():
    tema_seleccionado = combobox.get()
    style.theme_use(tema_seleccionado)

ventana = tk.Tk()
ventana.title("Selector de Tema")
ventana.geometry("300x200")

style = ttk.Style()

etiqueta = ttk.Label(
    ventana,
    text="Selecciona un tema:",
    font=("Arial", 12)
)
etiqueta.pack(pady=10)

combobox = ttk.Combobox(
    ventana,
    values=style.theme_names()
)
combobox.pack(pady=10)
combobox.current(0) # Seleccionar el primer tema por defecto
combobox.bind("<<comboboxselected>>", lambda e: cambiar_tema())

boton = ttk.Button(
    ventana,
    text="Aplicar Tema",
    command=cambiar_tema
)
boton.pack(pady=20)

ventana.mainloop()