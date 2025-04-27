from tkinter import messagebox
import tkinter as tk

def mostrar_info():
    messagebox.showinfo("Información", "Esta es una notificación informativa.")

ventana = tk.Tk()
ventana.title("Mostrar mensajes informativos")

boton_info = tk.Button(ventana, text="Mostrar Información", command=mostrar_info)
boton_info.pack(pady=10)

ventana.mainloop()