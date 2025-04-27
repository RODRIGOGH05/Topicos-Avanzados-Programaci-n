
import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo de place")

tk.Label(ventana, text="Etiqueta 1", bg="red").place(x=50, y=50)
tk.Label(ventana, text="Etiqueta 2", bg="green").place(x=100, y=100)

ventana.mainloop()