from tkinter import messagebox
import tkinter as tk

def mostrar_advertencia():
    messagebox.showerror("Error", "Ha ocurrido un error.")

ventana = tk.Tk()
ventana.title("Mostrar error")

boton_warning = tk.Button(ventana, text="Mostrar error", command=mostrar_advertencia)
boton_warning.pack(pady=10)

ventana.mainloop()