import tkinter as tk

def mostrar_seleccion():
    seleccion = lista.curselection()
    if seleccion:
        print("Selección:", lista.get(seleccion[0]))

ventana = tk.Tk()
ventana.title("Ejemplo de Listbox")

lista = tk.Listbox(ventana)
lista.pack(pady=10)

elementos = ["Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4", "Elemento 5"]
for elem in elementos:
    lista.insert(tk.END, elem)

boton = tk.Button(ventana, text="Mostrar Selección", command=mostrar_seleccion)
boton.pack()

ventana.mainloop()