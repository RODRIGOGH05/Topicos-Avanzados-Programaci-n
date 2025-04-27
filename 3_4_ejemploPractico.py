import tkinter as tk

def enviar_datos():
  nombre = entrada_nombre.get()
  comentario = area_comentarios.get("1.0", tk.END)
  print(f"Nombre: {nombre}\nComentario: {comentario}")

ventana = tk.Tk()
ventana.title("Formulario de contacto")
ventana.geometry("400x300")

tk.Label(ventana, text="Nombre:", font=("Arial", 12)).pack(pady=5)
entrada_nombre = tk.Entry(ventana, width=30)
entrada_nombre.pack(pady=5)

tk.Label(ventana, text="Comentario:", font=("Arial", 12)).pack(pady=5)
area_comentarios = tk.Text(ventana, height=5, width=30)
area_comentarios.pack(pady=5)

tk.Button(ventana, text="Enviar", command=enviar_datos, bg="blue", fg="white").pack(pady=10)

ventana.mainloop()