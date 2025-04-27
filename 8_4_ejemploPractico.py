from tkinter import filedialog
import tkinter as tk

def abrir_archivo():
    archivo = filedialog.askopenfilename(
        title="Abrir archivo",
        filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
    )

    if archivo:
        with open(archivo, "r") as f:
            contenido = f.read()
            area_texto.delete("1.0", tk.END)
            area_texto.insert(tk.END, contenido)

def guardar_archivo():
    archivo = filedialog.asksaveasfilename(
        title="Guardar archivo",
        defaultextension=".txt",
        filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
    )

    if archivo:
        with open(archivo, "w") as f:
            contenido = area_texto.get("1.0", tk.END)
            f.write(contenido)

ventana = tk.Tk()
ventana.title("Editor de texto")

area_texto = tk.Text(ventana, wrap="word", width=50, height=20)
area_texto.pack(padx=5, pady=10)

boton_abrir = tk.Button(ventana, text="Abrir archivo", command=abrir_archivo)
boton_abrir.pack(side="left", padx=5, pady=10)

boton_guardar = tk.Button(ventana, text="Guardar archivo", command=guardar_archivo)
boton_guardar.pack(side="right", padx=5, pady=10)

ventana.mainloop()