import tkinter as tk
import time

def mover_circulo():
    for _ in range(50):
        canvas.move(circulo, 5, 0)
        ventana.update()
        time.sleep(0.05)

ventana = tk.Tk()
ventana.title("Optimización de Canvas")

canvas = tk.Canvas(ventana, width=400, height=200, bg="white")
canvas.pack()

circulo = canvas.create_oval(50, 50, 100, 100, fill="blue")

boton = tk.Button(ventana, text="Mover círculo", command=mover_circulo)
boton.pack(pady=10)

ventana.mainloop()