from tkinter import messagebox
import tkinter as tk

def mostrar_advertencia():
    messagebox.showwarning("Advertencia", "Esta es una advertencia.")

ventana = tk.Tk()
ventana.title("Mostrar advertencia")

boton_warning = tk.Button(ventana, text="Mostrar advertencia", command=mostrar_advertencia)
boton_warning.pack(pady=10)

ventana.mainloop()