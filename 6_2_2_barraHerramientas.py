import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Ejemplo de barra de herramientas")

toolbar = ttk.Frame(ventana, relief="raised", padding=2)
toolbar.pack(side="top", fill="x")

boton_nuevo = ttk.Button(toolbar, text="Nuevo", command=lambda: print("Nuevo"))
boton_nuevo.pack(side="left", padx=2)

boton_guardar = ttk.Button(toolbar, text="Guardar", command=lambda: print("Guardar"))
boton_guardar.pack(side="left", padx=2)

boton_guardar = ttk.Button(toolbar, text="ayuda", command=lambda: print("ayuda"))
boton_guardar.pack(side="left", padx=2)

ventana.mainloop()