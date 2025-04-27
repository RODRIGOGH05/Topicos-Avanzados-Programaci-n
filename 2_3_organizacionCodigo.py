import tkinter as tk

class AplicacionEjemplo(tk.Tk):
  def __init__(self):
    super().__init__()

    self.title("Aplicación con Clases")

    self.geometry("300x200")
    self.crear_widgets()

  def crear_widgets(self):
    self.boton = tk.Button(self, text="Saludar", command=self.mostrar_mensaje)
    self.boton.pack()

  def mostrar_mensaje(self):
    print("¡Hola desde Tkinter!")

# Crear y ejecutar la aplicación
app = AplicacionEjemplo()
app.mainloop()