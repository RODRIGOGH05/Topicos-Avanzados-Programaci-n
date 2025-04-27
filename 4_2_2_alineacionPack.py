import tkinter as tk

ventana = tk.Tk()
ventana.title("Configuración de pack")

tk.Label(ventana, text="Izquierda", bg="red").pack(side="left")
tk.Label(ventana, text="Derecha", bg="green").pack(side="right")
tk.Label(ventana, text="Centro", bg="blue").pack(side="top", fill="x")

ventana.mainloop()