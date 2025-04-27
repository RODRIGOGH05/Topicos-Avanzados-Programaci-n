import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def cargar_imagen():
    ruta = filedialog.askopenfilename(filetypes=[("Imágenes", "*.png;*.jpg;*.jpeg;*.bmp")])

    if ruta:
        imagen = Image.open(ruta)
        imagen.thumbnail((400, 400), Image.LANCZOS)
        imagen_tk = ImageTk.PhotoImage(imagen)
        etiqueta_imagen.config(image=imagen_tk)
        etiqueta_imagen.image = imagen_tk

ventana = tk.Tk()
ventana.title("Visor de imágenes")

tk.Button(ventana, text="Cargar imagen", command=cargar_imagen).pack(pady=10)
etiqueta_imagen = tk.Label(ventana)
etiqueta_imagen.pack(pady=10)

ventana.mainloop()