from tkinter import filedialog
import tkinter as tk

def seleccionar_directorio():
    directorio = filedialog.askdirectory(title="Seleccionar Directorio")
    if directorio:
        print(f"Directorio seleccionado: {directorio}")

ventana = tk.Tk()
ventana.title("Seleccionar directorio")

boton_directorio = tk.Button(ventana, text="Seleccionar Directorio", command=seleccionar_directorio)
boton_directorio.pack(pady=10)

ventana.mainloop()
