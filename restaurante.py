#SISTEMA DE GESTIÓN DE PLATILLOS DE UN RESTAURANTE

import sqlite3

#PARTE1-----------------------------
def crear_bd():

    try:
        conexion = sqlite3.connect("restaurante.db")
        cursor = conexion.cursor()

        cursor.execute("""
        CREATE TABLE CATEGORIA(ID INTEGER PRIMARY KEY AUTOINCREMENT, 
        NOMBRE VARCHAR(100) UNIQUE NOT NULL)""")

        cursor.execute(""" CREATE TABLE PLATO(ID INTEGER PRIMARY KEY 
        AUTOINCREMENT, NOMBRE VARCHAR(100) UNIQUE NOT NULL,
        CATEGORIA_ID INTEGER NOT NULL,
        FOREIGN KEY(CATEGORIA_ID) REFERENCES CATEGORIA(ID))
    
        """)

        conexion.commit()
        conexion.close()
        print("Se ha creado correctamente")

    except:
        print("La base de datos con las tablas 'CATEGORÍA' Y 'PLATO' ya existe")

#PARTE 2 SE AGREGA CATEGORIA----------------------------------
def agregar_categoria():
    
    try:
        a = input("Inserte un nombre de categoria: ") 

        conexion = sqlite3.connect("restaurante.db")
        cursor = conexion.cursor()

        cursor.execute(f"INSERT INTO CATEGORIA VALUES(NULL,'{a}')")
    
        conexion.commit()
        conexion.close()
        print("Se ha agregado correctamente")
    
    except:
        print(f"Ya existe la categoria {a}") 


#PARTE TRES SE AGREGA PLATO------------------------------
def agregar_plato():

    try:
        conexion = sqlite3.connect("restaurante.db")
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM CATEGORIA")
        a = cursor.fetchall() #Nos devuelve una lista con el campo nombre
        if a == []:
            print("Aún no hay ninguna categoria disponible")
        else:
            print("LAS CATEGORIAS DISPONIBLES SON LAS SIGUIENTES: ")
            for i in a:
                print(f"-[{i[0]}]. {i[1]} ")

            seleccion = int(input("¿CUÁL CATEGORIA DESEA SELECCIONAR? \n >"))

            nombre = input("INGRESE EL NOMBRE DEL PLATO: \n >")

            cursor.execute(f"INSERT INTO PLATO VALUES(NULL,'{nombre}',{seleccion})")

            conexion.commit()
            conexion.close() 
            print(f"Se agrego el plato: {nombre} correctamente")
    
    except sqlite3.IntegrityError:
        print(f"El plato {nombre} ya esta agregado")

def vercategorias():
    
    try:
        conexion = sqlite3.connect("restaurante.db")
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM CATEGORIA")
    
        b = cursor.fetchall() #Nos devuelve una lista con el campo id y nombre de la tabla categoria

        if b == []:
            print("Aún no hay platillos en ninguna categoria")

        else:
            print("LAS CATEGORIAS DISPONIBLES SON LAS SIGUIENTES: ")
            for i in b:
                print(f"-[{i[0]}]. {i[1]} ")

            selecc = int(input("¿DE CUÁL CATEGORÍA DESEA VER LOS PLATILLOS?\n>")) 

            cursor.execute(f"SELECT NOMBRE FROM PLATO WHERE CATEGORIA_ID={selecc}")
            a = cursor.fetchall()

            for i in a:
                print(i[0])  

            conexion.commit()
            conexion.close() 
    except: 
        print("La opción ingresada no es válida")


def mostrar_menu():
    while True:
        try:
            print("---BIENVENIDO AL RESTAURANTE DE REASON---")
            print("-[1] Agregar una categoría")
            print("-[2] Agregar un platillo a una categoría")
            print("-[3] Ver platillos")
            print("-[4] Salir")

            opc = int(input("Ingrese el número de la operación que desea realizar: "))

            if opc == 1:
                agregar_categoria()

            elif opc==2:
                agregar_plato()
            
            elif opc==3:
                vercategorias()

            elif opc == 4:
                print("Gracias por su visita")
                break
            else:
                print("Ingreso una opción no válida")

        except:
            print("Ingreso una opción no válida")


crear_bd()
mostrar_menu()


