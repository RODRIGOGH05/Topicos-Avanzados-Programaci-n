import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo de sticky")

# La etiqueta "Expandida" se estira en todas las direcciones
tk.Label(ventana, text="Expandida", bg="red").grid(row=0, column=0, sticky="nsew")

# La etiqueta "Centrada" se alinea en el centro de su celda
tk.Label(ventana, text="Centrada", bg="blue").grid(row=1, column=0, sticky="")

ventana.mainloop()