
import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo de Padding")

tk.Label(ventana, text="Sin Padding", bg="red").grid(row=0, column=0)
tk.Label(ventana, text="Con Padding", bg="green").grid(row=1, column=0, padx=20, pady=10)

ventana.mainloop()