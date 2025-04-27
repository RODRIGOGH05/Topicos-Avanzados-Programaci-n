import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo de pack")

tk.Label(ventana, text="Arriba", bg="red").pack()
tk.Label(ventana, text="Centro", bg="green").pack()
tk.Label(ventana, text="Abajo", bg="blue").pack()

ventana.mainloop()