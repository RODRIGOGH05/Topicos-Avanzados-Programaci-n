from tkinter import ttk
import tkinter as tk

ventana = tk.Tk()
ventana.title("Widgets modernos con ttk")

etiqueta = ttk.Label(ventana, text="Etiqueta con ttk", font=("Arial", 12))
etiqueta.pack(pady=10)

boton = ttk.Button(ventana, text="Botón moderno")
boton.pack(pady=10)

ventana.mainloop()