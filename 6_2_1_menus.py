import tkinter as tk

def nuevo_archivo():
    print("Nuevo archivo creado")

def guardar_archivo():
    print("Archivo guardado")

ventana = tk.Tk()
ventana.title("Ejemplo de menús")

menu_principal = tk.Menu(ventana)
ventana.config(menu=menu_principal)
menu_archivo = tk.Menu(menu_principal, tearoff=0)
menu_archivo.add_command(label = "Nuevo", command = nuevo_archivo)
menu_archivo.add_command(label="Abrir")
menu_archivo.add_command(label="Guardar", command= guardar_archivo)
#menu_archivo.add_separador()
menu_archivo.add_command(label="Salir", command=ventana.quit)
menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
ventana.mainloop()