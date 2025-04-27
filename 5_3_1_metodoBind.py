import tkinter as tk

def clic(evento):
    print("Clic detectado en posición:", evento.x, evento.y)

ventana = tk.Tk()
ventana.title("Ejemplo de bind")
ventana.bind("<Button-1>", clic)
ventana.mainloop()