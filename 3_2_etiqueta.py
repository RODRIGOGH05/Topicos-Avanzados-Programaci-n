import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo de Label")

etiqueta = tk.Label(ventana, text="¡Bienvenido a Tkinter!", font=("Times New Roman", 14), fg="white")
etiqueta.pack(pady=10)

ventana.mainloop()