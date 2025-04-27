import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo de Text")

area_texto = tk.Text(ventana, height=5, width=30)
area_texto.pack(pady=10)

ventana.mainloop()