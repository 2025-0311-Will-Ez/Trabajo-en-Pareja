# Programa sencillo para crear, leer y actualizar archivos de texto

import os

archivo_actual = None

while True:
    print("\n=== Menu ===")
    print("1.Crear archivo")
    print("2.Guardar registro")
    print("3.Leer archivo")
    print("4.Actualizar nombre")
    print("5.Salir")

#Esta opción es para elegir el nombre del archivo, no para escribir disparates.
    opcion = input("Elige una opción:")

    if opcion == "1":
        archivo_actual = input("Nombre del archivo (con.text):")
        if os.path.exists(archivo_actual):
            print("Archivo ya existe.")
        else:
            with open(archivo_actual, "w")as f:
                print("Archivo creado correctamente.")

#Esta opción es para guardar el registro. Aqui pondras: Nombre, Matrícula,  Correo y Teléfono.
    elif opcion == "2":
        if archivo_actual:
            nombre = input("Nombre:")
            matricula = input("Matrícula:")
            correo = input("Correo:")
            telefono = input("Teléfono.")
            with open(archivo_actual, "a")as f:
                f.write(f"Nombre: {nombre}\n")
                f.write(f"Matrícula: {matricula}\n")
                f.write(f"Correo: {correo}\n")
                f.write(f"Telefono: {telefono}\n\n")
            print("Registro guardado.")
        else:
            print("Primero crea un archivo.")
        
#Esta opción te va a mostrar lo que pusiste en la opción 2 (nombre, matrícula, correo, teléfono), así que no esperes gran cosa. Exactamente te va a mostrar el último registro guardado.
    elif opcion == "3":
            if archivo_actual and os.path.exists(archivo_actual):
                print("\n --- Contenido del archivo --- ")
                with open(archivo_actual, "r") as f:
                    print(f.read())

            else:
                print("Primero crea un archivo.")
        
    elif opcion == "3":
            if archivo_actual and os.path.exists(archivo_actual):
                print("\n --- Contenido del archivo --- ")
                with open (archivo_actual, "r") as f:
                    print(f.read())
            else:
                print("Primero crea un archivo.")

#Esta opción te va a permitir actualizar el nombre del último registro guardado.
    elif opcion == "4":
            if archivo_actual and os.path.exists(archivo_actual):
                nombre_buscar = input("Nombre a actualizar:")
                nombre_nuevo = input("Nuevo nombre:")
                with open(archivo_actual, "r") as f:
                    lineas = f.readlines()
                for i in range(len(lineas)):
                    if lineas [i].startswith("NOMBRE:") and lineas [i][8:].strip() == nombre_buscar:
                        lineas [i] = f"NOMBRE: {nombre_nuevo}\n"
                    with open(archivo_actual, "w") as f:
                        f.writelines (lineas)
                    print("Nombre actualizado.")
            else:
                    print("Primero crear un archivo.")

#Y por último, gracias a Dios. 5 para cerrar.
    elif opcion == "5":
        print("Cerrando programa...")
        break
    else:
        print("Opción no válida, intente de nuevo.")
