from tkinter import messagebox
import tkinter as tk

def confirmar_accion():
    respuesta = messagebox.askyesno("Confirmación", "¿Deseas continuar?")
    if respuesta:
        print("Acción confirmada.")
    else:
        print("Acción cancelada.")

ventana = tk.Tk()
ventana.title("Confirmaciones")

boton_confirmar = tk.Button(ventana, text="Confirmar Acción", command=confirmar_accion)
boton_confirmar.pack(pady=10)

ventana.mainloop()