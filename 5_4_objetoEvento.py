import tkinter as tk

def mostrar_detalles(evento):
    print(f"Evento en {evento.widget} - Coordenadas: ({evento.x}, {evento.y})")

ventana = tk.Tk()
ventana.title("Detalles del Evento")
ventana.bind("Evento", mostrar_detalles)
ventana.mainloop()