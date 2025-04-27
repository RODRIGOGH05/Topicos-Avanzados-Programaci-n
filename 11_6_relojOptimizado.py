import tkinter as tk
import time
import threading

reloj_activo = False

def iniciar_reloj():
    global reloj_activo
    if not reloj_activo:
        reloj_activo = True
        hilo = threading.Thread(target=actualizar_reloj, daemon=True)
        hilo.start()

def detener_reloj():
    global reloj_activo
    reloj_activo = False

def actualizar_reloj():
    while reloj_activo:
        etiqueta.config(text=time.strftime("%H:%M:%S"))
        time.sleep(1)

ventana = tk.Tk()
ventana.title("Reloj optimizado con hilos")

etiqueta = tk.Label(ventana, font=("Arial", 36), text="00:00:00")
etiqueta.pack(padx=10, pady=20)

boton_iniciar = tk.Button(ventana, text="Iniciar", command=iniciar_reloj)
boton_iniciar.pack(side="left", padx=10, pady=10)

boton_detener = tk.Button(ventana, text="Detener", command=detener_reloj)
boton_detener.pack(side="right", padx=10, pady=10)

ventana.mainloop()