from tkinter import filedialog
import tkinter as tk

def abrir_archivo():
    archivo = filedialog.askopenfilename(
        title="Seleccionar archivo",
        filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
    )
    if archivo:
        print(f"Archivo seleccionado: {archivo}")

ventana = tk.Tk()
ventana.title("Abrir archivo")

boton = tk.Button(ventana, text="Abrir archivo", command=abrir_archivo)
boton.pack(pady=10)

ventana.mainloop()