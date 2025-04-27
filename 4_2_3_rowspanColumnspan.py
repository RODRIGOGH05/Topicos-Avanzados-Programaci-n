import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo de rowspan y columnspan")

# Permitir que las filas y columnas se expandan
ventana.grid_rowconfigure(0, weight=1)
ventana.grid_rowconfigure(1, weight=1)
ventana.grid_rowconfigure(2, weight=1)
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)

# Etiqueta «Grande» ocupa 2 filas y 2 columnas
tk.Label(ventana, text="Grande", bg="red").grid(row=0, column=0, rowspan=2, columnspan=2, sticky="nsew")

# Etiqueta «Pequeño» en fila 2 y columna 1
tk.Label(ventana, text="Pequeño", bg="blue").grid(row=2, column=1, sticky="nsew")

ventana.mainloop()