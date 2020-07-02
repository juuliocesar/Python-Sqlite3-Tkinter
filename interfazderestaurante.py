import sqlite3
from tkinter import *


root = Tk()
root.title("Barriga llena")
root.resizable(0,0)
root.config(bd=25, relief="sunken")

Label(root, text="   Barriga llena, corazón   ", fg="darkblue", font=(
    "Times New Roman",28,"bold italic")).pack()

Label(root, text="Menú del día", fg="green", font=(
    "Times New Roman",24,"bold italic")).pack()

# Separación de títulos y categorias
Label(root, text="").pack()

conexion = sqlite3.connect("restaurante.db")
cursor = conexion.cursor()

# Buscar las categorías y platos de la bd
categorias = cursor.execute("SELECT * FROM CATEGORIA").fetchall()

for i in categorias:
    Label(root,text=i[1],fg="black", font=(
        "Times New Roman",20,"bold italic")).pack()

    platos = cursor.execute(f"SELECT * FROM PLATO WHERE CATEGORIA_ID = {i[0]} ").fetchall()

    for i in platos:
        Label(root, text=i[1],fg="gray", font=("Verdana",15,"italic")).pack()

    # Separación entre categorias
    Label(root, text="").pack()    


conexion.close()


# Precio del menú
Label(root, text="$65 (IVA incl.)", fg="darkgreen", font=(
    "Times New Roman",20,"bold italic")).pack(side="right")



root.mainloop()




