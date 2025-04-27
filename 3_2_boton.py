import tkinter as tk

def accion():
  print("¡Botón presionado!")

ventana = tk.Tk()
ventana.title("Ejemplo de Button")

boton = tk.Button(ventana, text="Haz clic aquí", command=accion, bg="green", fg="white")
boton.pack(pady=10)

ventana.mainloop()