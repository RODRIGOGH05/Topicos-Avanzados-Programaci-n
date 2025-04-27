import tkinter as tk

def mostrar_texto():
  print("Texto ingresado:", entrada.get())

ventana = tk.Tk()
ventana.title("Ejemplo de Entry")

entrada = tk.Entry(ventana, width=20)
entrada.pack(pady=5)

boton = tk.Button(ventana, text="Mostrar Texto", command=mostrar_texto)
boton.pack(pady=10)

ventana.mainloop()