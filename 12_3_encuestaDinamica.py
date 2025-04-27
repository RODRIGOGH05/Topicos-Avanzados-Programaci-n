import tkinter as tk
import csv

preguntas = [
    {"pregunta": "¿Color favorito?", "opciones": ["Rojo", "Verde", "Azul", "Amarillo"]},
    {"pregunta": "¿Estación favorita?", "opciones": ["Primavera", "Verano", "Otoño", "Invierno"]},
    {"pregunta": "¿Animal favorito?", "opciones": ["Perro", "Gato", "Ave", "Otro"]},
]

def iniciar_encuesta():
    ventana = tk.Tk()
    ventana.title("Encuesta")
    
    indice = 0
    respuestas = []
    opcion = tk.StringVar()
    opcion.set(None)

    def mostrar_pregunta():
        for widget in ventana.winfo_children():
            widget.destroy()

        if indice < len(preguntas):
            tk.Label(ventana, text=preguntas[indice]["pregunta"], font=("Arial", 14)).pack(pady=10)
            opcion.set(None)
            
            for op in preguntas[indice]["opciones"]:
                tk.Radiobutton(
                    ventana,
                    text=op,
                    variable=opcion,
                    value=op,
                    indicatoron=1).pack(anchor="w")
            
            tk.Button(ventana, text="Siguiente", command=guardar_respuesta).pack(pady=10)
        else:
            guardar_respuestas()

    def guardar_respuesta():
        nonlocal indice
        if opcion.get() and opcion.get() != "None":
            respuestas.append(opcion.get())
            indice += 1
            mostrar_pregunta()

    def guardar_respuestas():
        with open("resultados_encuesta.csv", "w", newline="", encoding="utf-8") as archivo:
            csv.writer(archivo).writerows([["Pregunta", "Respuesta"]] + 
                                [[preg["pregunta"], resp] for preg, resp in zip(preguntas, respuestas)])

        for widget in ventana.winfo_children():
            widget.destroy()
        tk.Label(ventana, text="Respuestas guardadas", font=("Arial", 12)).pack(pady=10)

    mostrar_pregunta()
    ventana.mainloop()

iniciar_encuesta()