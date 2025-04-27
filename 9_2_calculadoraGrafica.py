import tkinter as tk
from tkinter import messagebox

def agregar_caracter(caracter):
    entrada.insert(tk.END, caracter)

def borrar_todo():
    entrada.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except Exception as e:
        messagebox.showerror("Error", "Entrada inválida")

ventana = tk.Tk()
ventana.title("Calculadora")

entrada = tk.Entry(ventana, font=("Arial", 18), justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (texto, fila, columna) in botones:
    boton = tk.Button(
    ventana,
    text=texto,
    font=("Arial", 14),
    command=lambda t=texto: agregar_caracter(t) if t != '=' else calcular()
)
    boton.grid(row=fila, column=columna, padx=5, pady=5, sticky="nsew")

    borrar = tk.Button(ventana, text="C", font=("Arial", 14), command=borrar_todo)
    borrar.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

ventana.mainloop()