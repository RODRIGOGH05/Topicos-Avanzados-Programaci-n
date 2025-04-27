from tkinter import ttk
import tkinter as tk

ventana = tk.Tk()
ventana.title("Aplicación de Temas")

# Mostrar temas disponibles
style = ttk.Style()
print("Temas disponibles:", style.theme_names())

# Aplicar un tema
style.theme_use("clam")

etiqueta = ttk.Label(
    ventana,
    text="Tema aplicado: clam",
    font=("Arial", 12)
)
etiqueta.pack(pady=10)

boton = ttk.Button(
    ventana,
    text="Botón con tema"
)
boton.pack(pady=10)

ventana.mainloop()