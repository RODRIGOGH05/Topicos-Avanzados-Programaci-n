import tkinter as tk

def mostrar_estado():
  print("Estado:", var.get())

ventana = tk.Tk()
ventana.title("Ejemplo de Checkbutton")

var = tk.IntVar()
check = tk.Checkbutton(ventana, text="Opción 1", variable=var, command=mostrar_estado)
check.pack(pady=10)

ventana.mainloop()