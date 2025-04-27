import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

conexion = sqlite3.connect("inventario.db")
cursor = conexion.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        cantidad INTEGER NOT NULL,
        precio REAL NOT NULL
    )
""")
conexion.commit()

def agregar_producto():
    try:
        cursor.execute("INSERT INTO productos (nombre, cantidad, precio) VALUES (?, ?, ?)",
                        (entrada_nombre.get(), int(entrada_cantidad.get()), float(entrada_precio.get())))
        conexion.commit()
        actualizar_tabla()
        for entrada in (entrada_nombre, entrada_cantidad, entrada_precio):
            entrada.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce valores válidos.")

def eliminar_producto():
    seleccionado = tabla.focus()
    if not seleccionado:
        messagebox.showwarning("Advertencia", "Selecciona un producto para eliminar.")
        return
    try:
        id_producto = tabla.item(seleccionado)["values"][0]
        cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
        conexion.commit()
        actualizar_tabla()
    except IndexError:
        messagebox.showwarning("Advertencia", "Error al obtener el producto seleccionado.")

def actualizar_tabla():
    for item in tabla.get_children():
        tabla.delete(item)
    cursor.execute("SELECT * FROM productos")
    for producto in cursor.fetchall():
        tabla.insert("", tk.END, values=producto)

ventana = tk.Tk()
ventana.title("Gestión de Inventario")

campos = ["Nombre del Producto", "Cantidad", "Precio"]
entradas = []
for campo in campos:
    tk.Label(ventana, text=campo).pack()
    entrada = tk.Entry(ventana)
    entrada.pack()
    entradas.append(entrada)

entrada_nombre, entrada_cantidad, entrada_precio = entradas

tk.Button(ventana, text="Agregar Producto", command=agregar_producto).pack(pady=5)
tk.Button(ventana, text="Eliminar Producto", command=eliminar_producto).pack(pady=5)

tabla = ttk.Treeview(ventana, columns=("ID", "Nombre", "Cantidad", "Precio"), show="headings")
for col in ("ID", "Nombre", "Cantidad", "Precio"):
    tabla.heading(col, text=col)
tabla.pack(padx=10, pady=10)

actualizar_tabla()
ventana.mainloop()
conexion.close()