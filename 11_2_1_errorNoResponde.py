import tkinter as tk
import threading
import time

def tarea_larga():
    for i in range(5):
        print(f"Proceso en ejecución: {i}")
        time.sleep(1)
    print("Proceso completado")

def ejecutar_tarea():
    hilo = threading.Thread(target=tarea_larga)
    hilo.start()

ventana = tk.Tk()
ventana.title("Evitar bloqueo de la ventana")

boton = tk.Button(ventana, text="Iniciar tarea", command=ejecutar_tarea)
boton.pack(pady=10)

ventana.mainloop()