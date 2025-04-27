import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo Combinado")
ventana.geometry("400x300")

# pack
tk.Label(ventana, text="Arriba", bg="red").pack(side="top", fill="x")

# grid
tk.Label(ventana, text="(0, 0)", bg="red").grid(row=0, column=0)
tk.Label(ventana, text="(0, 1)", bg="green").grid(row=0, column=1)
tk.Label(ventana, text="(1, 0)", bg="blue").grid(row=1, column=0)
tk.Label(ventana, text="(1, 1)", bg="yellow").grid(row=1, column=1)

# place
tk.Label(ventana, text="Centro", bg="yellow").place(relx=0.5, rely=0.5, anchor="center")

ventana.mainloop()