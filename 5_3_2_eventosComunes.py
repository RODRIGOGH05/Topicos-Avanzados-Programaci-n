import tkinter as tk

def tecla_presionada(evento):
    print(f"Tecla presionada: {evento.char}")

ventana = tk.Tk()
ventana.title("Ejemplo de Teclas")
ventana.bind("<Key>", tecla_presionada)
ventana.mainloop()