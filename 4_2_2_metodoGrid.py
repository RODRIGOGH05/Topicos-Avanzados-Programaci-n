import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo básico de grid")

# Colocar etiquetas en una cuadrícula de 2x2
tk.Label(ventana, text="(0, 0)", bg="red").grid(row=0, column=0)
tk.Label(ventana, text="(0, 1)", bg="green").grid(row=0, column=1)
tk.Label(ventana, text="(1, 0)", bg="blue").grid(row=1, column=0)
tk.Label(ventana, text="(1, 1)", bg="yellow").grid(row=1, column=1)

ventana.mainloop()