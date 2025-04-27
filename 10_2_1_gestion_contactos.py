import tkinter as tk
from tkinter import messagebox
import sqlite3

conexion = sqlite3.connect("contactosV2.db")
cursor = conexion.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS contactos (
        id INTEGER PRIMARY KEY, 
        nombre TEXT NOT NULL, 
        telefono TEXT NOT NULL,
        ciudad TEXT NO NULL)
""")
conexion.commit()

def ejecutar_sql(query, parametros=(), actualizar=False):
    cursor.execute(query, parametros)
    if actualizar:
        conexion.commit()
        actualizar_lista()

def agregar_contacto():
    nombre_contacto = entrada_nombre.get()
    telefono_contacto = entrada_telefono.get()
    ciudad_contacto = entrada_ciudad.get()
    
    if nombre_contacto and telefono_contacto and ciudad_contacto:
        ejecutar_sql("INSERT INTO contactos (nombre, telefono, ciudad) VALUES (?, ?, ?)", 
            (nombre_contacto, telefono_contacto, ciudad_contacto), True)
        entrada_nombre.delete(0, tk.END)
        entrada_telefono.delete(0, tk.END)
        entrada_ciudad.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Completa todos los campos.")

def eliminar_contacto():
    try:
        contacto_seleccionado = lista_contactos.get(lista_contactos.curselection())
        id_contacto = contacto_seleccionado.split(" ")[0]
        ejecutar_sql("DELETE FROM contactos WHERE id = ?", (id_contacto,), True)
    except:
        messagebox.showwarning("Advertencia", "Selecciona un contacto para eliminar.")

def actualizar_lista():
    lista_contactos.delete(0, tk.END)
    for id_contacto, nombre, telefono, ciudad in cursor.execute("SELECT * FROM contactos"):
        lista_contactos.insert(tk.END, f"{id_contacto} {nombre} - {telefono} - {ciudad}")

def mostrar_contacto():
    lista_contactos.delete(0, tk.END)
    for id_contacto, nombre, telefono, ciudad in cursor.execute("SELECT * FROM contactos"):
        lista_contactos.insert(tk.END, f"{id_contacto} {nombre} - {telefono} - {ciudad}")

ventana = tk.Tk()
ventana.title("Gestión de contactos")

tk.Label(ventana, text="Nombre").pack()
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

tk.Label(ventana, text="Teléfono").pack()
entrada_telefono = tk.Entry(ventana)
entrada_telefono.pack()

tk.Label(ventana, text="Ciudad").pack()
entrada_ciudad = tk.Entry(ventana)
entrada_ciudad.pack()

tk.Button(ventana, text="Agregar contacto", command=agregar_contacto).pack(pady=5)
tk.Button(ventana, text="Eliminar contacto", command=eliminar_contacto).pack(pady=5)
tk.Button(ventana, text="mostrar contacto", command=mostrar_contacto).pack(pady=5)

lista_contactos = tk.Listbox(ventana, width=50)
lista_contactos.pack(padx=10, pady=10)

actualizar_lista()
ventana.mainloop()
conexion.close()