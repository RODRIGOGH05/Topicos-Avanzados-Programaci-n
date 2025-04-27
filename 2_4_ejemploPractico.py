import tkinter as tk

# Función para mostrar el saludo
def saludar():
  nombre = entrada.get()
  etiqueta.config(text=f"¡Hola, {nombre}!")

# Ventana principal
ventana = tk.Tk()
ventana.title("Saludo Personalizado")
ventana.geometry("300x150")

# Widgets
etiqueta = tk.Label(ventana, text="Introduce tu nombre:")
etiqueta.pack(pady=5)

entrada = tk.Entry(ventana)
entrada.pack(pady=5)

boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack(pady=5)

# Bucle principal
ventana.mainloop()