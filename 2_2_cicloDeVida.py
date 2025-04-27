import tkinter as tk

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de Ciclo de Vida")
ventana.geometry("300x200")

# Añadir un botón
def accion():
  print("¡Botón presionado!")

boton = tk.Button(ventana, text="Presióname", command=accion)
boton.pack()

# Iniciar el loop principal
ventana.mainloop()