from tkinter import filedialog
import tkinter as tk

def guardar_archivo():
    archivo = filedialog.asksaveasfilename(
        title="Guardar archivo",
        defaultextension=".txt",
        filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
    )
    
    if archivo:
        with open(archivo, "w") as f:
            f.write("Este es un archivo guardado desde Tkinter.")
        print(f"Archivo guardado: {archivo}")

ventana = tk.Tk()
ventana.title("Guardar archivo")

boton_guardar = tk.Button(ventana, text="Guardar Archivo", command=guardar_archivo)
boton_guardar.pack(pady=10)

ventana.mainloop()