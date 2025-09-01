import tkinter as tk
from tkinter import messagebox

def mostrardatos():
    nombre = txtnombre.get().strip()
    apellido = txtapellido.get().strip()
    email = txtemail.get().strip()
    telefono = txttelefono.get().strip()
    
    if not nombre or not apellido or not email or not telefono:
        messagebox.showwarning("Campos vacíos", "Por favor, completa todos los campos.")
        return

      # Limpio el frame antes de mostrar nuevos datos
    for widget in info.winfo_children():
        widget.destroy()
    
     # Muestro los datos ingresados en el frame
    tk.Label(info, text=f"Nombre: {nombre}", font=("Arial", 12)).place(x=10, y=10)
    tk.Label(info, text=f"Apellido: {apellido}", font=("Arial", 12)).place(x=10, y=40)
    tk.Label(info, text=f"Email: {email}", font=("Arial", 12)).place(x=10, y=70)
    tk.Label(info, text=f"Teléfono: {telefono}", font=("Arial", 12)).place(x=10, y=100)
    
     # Limpio los campos de entrada
    txtnombre.delete(0, tk.END)
    txtapellido.delete(0, tk.END)
    txtemail.delete(0, tk.END)
    txttelefono.delete(0, tk.END)


def salir():
    ventana.destroy()

#Configuracion de la ventana
ventana = tk.Tk()

ancho = ventana.winfo_screenwidth()
alto = ventana.winfo_screenheight()
ventana.geometry(f"{ancho}x{alto}")

ventana.title("App con Place")
ventana.resizable(False, False)

# Permitir salir con la tecla ESC
ventana.bind("<Escape>", lambda e: salir())

# TÍTULO
inicio = tk.Label(ventana, text="Formulario de registro", font=("Bahnschrift SemiBold", 24))
inicio.place(x=50, y=20)

# ETIQUETAS 
lblnombre = tk.Label(ventana, text="Nombre:")
lblapellido = tk.Label(ventana, text="Apellido:")
lblemail = tk.Label(ventana, text="Email:")
lbltelefono = tk.Label(ventana, text="Teléfono:")

lblnombre.place(x=50, y=80)
lblapellido.place(x=50, y=120)
lblemail.place(x=50, y=160)
lbltelefono.place(x=50, y=200)

#  CAMPOS DE ENTRADA 
txtnombre = tk.Entry(ventana, width=30)
txtapellido = tk.Entry(ventana, width=30)
txtemail = tk.Entry(ventana, width=30)
txttelefono = tk.Entry(ventana, width=30)

txtnombre.place(x=150, y=80)
txtapellido.place(x=150, y=120)
txtemail.place(x=150, y=160)
txttelefono.place(x=150, y=200)

#Botones 
btnguardar = tk.Button(ventana, text="Guardar", command=mostrardatos, bg="lightblue")
btnguardar.place(x=150, y=240)

btnsalir = tk.Button(ventana, text="Salir", command=salir, bg="lightcoral")
btnsalir.place(x=230, y=240)

#Frame para mostrar informacion
info = tk.Frame(ventana, bd=2, relief="groove", width=400, height=150)
info.place(x=50, y=300)

ventana.mainloop()


 