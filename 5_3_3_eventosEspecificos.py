import tkinter as tk

def saludo():
    print("¡Hola!")

ventana = tk.Tk()
ventana.title("Ejemplo de command")
boton = tk.Button(ventana, text="Saludar", command=saludo)
boton.pack()
ventana.mainloop()