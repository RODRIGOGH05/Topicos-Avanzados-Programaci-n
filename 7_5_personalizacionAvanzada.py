from tkinter import ttk
import tkinter as tk

ventana = tk.Tk()
ventana.title("Estilización avanzada")

style = ttk.Style()
style.configure(
    "Custom.TButton",
    font=("Helvetica", 12),
    foreground="blue",
    background="white",
    padding=10
)

boton = ttk.Button(
    ventana,
    text="Botón personalizado",
    style="Custom.TButton"
)
boton.pack(pady=20)

ventana.mainloop()