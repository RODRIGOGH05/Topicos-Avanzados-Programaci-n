import tkinter as tk

def registrar_tecla(evento):
    etiqueta_teclas.config(text=f"Tecla presionada: {evento.char}")

def registrar_clic(evento):
    etiqueta_clics.config(text=f"Clic en posición: ({evento.x}, {evento.y})")

ventana = tk.Tk()
ventana.title("Registro de Eventos")
ventana.geometry("400x200")

etiqueta_teclas = tk.Label(ventana, text="Presiona una tecla")
etiqueta_teclas.pack(pady=10)

etiqueta_clics = tk.Label(ventana, text="Haz clic en cualquier parte")
etiqueta_clics.pack(pady=10)

ventana.bind("<Key>", registrar_tecla)
ventana.bind("<Button-1>", registrar_clic)

ventana.mainloop()