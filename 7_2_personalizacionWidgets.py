import tkinter as tk

ventana = tk.Tk()
ventana.title("Estilización básica")

etiqueta = tk.Label(
    ventana,
    text="Etiqueta personalizada",
    bg="lightblue",
    fg="darkblue",
    font=("Helvetica", 14, "bold"),
    relief="solid"
)
etiqueta.pack(pady=10, padx=10)

boton = tk.Button(
    ventana,
    text="Botón estilizado",
    bg="green",
    fg="white",
    font=("Arial", 12, "italic"),
    relief="raised"
)
boton.pack(pady=10, padx=10)

ventana.mainloop()