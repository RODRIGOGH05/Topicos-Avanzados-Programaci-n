import tkinter as tk

def cargar_elementos():
    for i in range(100000):
        lista.insert(tk.END, f"Elemento {i}")
        
        if i % 100 == 0:
            ventana.update_idletasks()

ventana = tk.Tk()
ventana.title("Carga incremental")

lista = tk.Listbox(ventana)
lista.pack(padx=5, pady=10)

boton = tk.Button(ventana, text="Cargar datos", command=cargar_elementos)
boton.pack(pady=10)

ventana.mainloop()