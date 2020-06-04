import csv
import datetime
# Librería para Validador de expresiones regulares
import re
#Libreria para manejar Sistema Operativo
import os
# Se importa las clases de clasePIA
from clasePIA import Contacto
# Se importa una clase que permite extraer elementos de un objeto
from operator import attrgetter

# Función para mostrar los elementos que tiene la lisa de ejemplo.
def CuantosElementosHay():
    txt = "El número de elementos de la colección es {}"
    print(txt.format(len(Contactos)))

def BuscarTelefono(telabuscar):
    coincidencia=False
    for contacto in Contactos:
        if (contacto.TELEFONO==telabuscar):
            coincidencia=True
            break
    return coincidencia

def BuscarContacto(nickBuscar):
    contador=-1
    indice_retorno=-1
    for contacto in Contactos:
        contador+=1
        if (contacto.NICKNAME==nickBuscar):
            indice_retorno=contador
            break
    return indice_retorno

# Se declara una variable de paso, que permitirá preguntar y validar información.
captura=""
# Función que valida un dato, y si es correcto, lo coloca en captura.
def ValidarDatos(_patron,_pregunta="Dame un dato: "):
    # Se especifica que captura es global.
    global captura
    while True:
        _fxvalor = input(_pregunta)
        coincide = re.search(_patron, _fxvalor)
        if (coincide):
            captura= _fxvalor
            break
        else:
            print("El dato no es correcto. Intenta de nuevo.")

# Función que convierte una expresión YYYY-MM-DD a datetime
def strtodate(expFecha):
        anio=int(expFecha[0:4])
        mes=int(expFecha[5:7])
        dia=int(expFecha[-2:])
        return datetime.date(anio,mes,dia)

Contactos = []
with open('contactos_movil.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='|')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
        else:
            NickN=str(row[0])
            Name=str(row[1])
            Email=str(row[2])
            Cell=str(row[3])
            FechNac= strtodate(row[4])
            Gasto= row[5]
            Contactos.append(Contacto(NickN,Name,Email,Cell,FechNac,Gasto))
        line_count += 1
    print(f'Processed {line_count} lines.')
# Se declara una lista que almacenará objetos. Inicia vacia
CuantosElementosHay()

# Se agregan objetos a la lista.
Contactos.append(Contacto("RS002","RAUL SALOMON","raul.salomon@unal.edu.mx",1234567890,strtodate("2001/09/11"),1500.00))
Contactos.append(Contacto("SS003","SABRINA SPELLMAN","sabrina.spellman@unal.edu.mx",9999999999,strtodate("1999/11/10"),1200.20))
CuantosElementosHay()

input("")
#Menu
# Se define una función utilizando la expresión lambda, que es equivalente a: os.system('cls')
LimpiarPantalla = lambda: os.system('cls')
LimpiarPantalla()
# Validador de expresiones regulares
# _txt es el texto a vlidar.
# _regex es el patrón de expresión regular a validar.
def RegEx(_txt,_regex):
    coincidencia=re.match(_regex, _txt)
    return bool(coincidencia)

def principal():
    while (True):
        LimpiarPantalla()
        print("LISTA DE COTACTOS")
        print(" ")
        print("[1] Agregar un contacto.")
        print("[2] Buscar un contacto.")
        print("[3] Eliminar un contacto.")
        print("[4] Mostrar contactos.")
        print("[0] Salir.")
        opcion_elegida = input("¿Qué deseas hacer?  > ")
        if RegEx(opcion_elegida,"^[123450]{1}$"):
            if opcion_elegida=="0":
                #Ordenamiento
                Contactos.sort(key=attrgetter('NICKNAME'),reverse=False)
                #Backup
                ruta_archivo=os.path.abspath(os.getcwd())
                archivo_respaldo=ruta_archivo+"\\contactos_movil.bak"
                archivo_normal=ruta_archivo+"\\contactos_movil.csv"

                print(archivo_respaldo)
                print(archivo_normal)

                # Si hay archivo de datos.
                if os.path.exists(archivo_normal):
                    # verifica si hay respaldo, y lo elimina
                    if os.path.exists(archivo_respaldo):
                        os.remove(archivo_respaldo)
                    # Pasa el archivo normal, para que sea archivo de respaldo
                    os.rename(archivo_normal,archivo_respaldo)

                # Genera el archivo CSV.
                f = open(archivo_normal,"w+")
                # Escribir el encabezado.
                f.write("NICKNAME | NOMBRE | CORREO | TELEFONO | FECHANACIMIENTO | GASTO\n")
                # Cierro el archivo.
                f.close()
                #Salir del programa

                f = open(archivo_respaldo,"w+")
                # Escribo los encabezados de mi CSV
                f.write("NICKNAME | NOMBRE | CORREO | TELEFONO | FECHANACIMIENTO | GASTO\n")
                # Escribimos en el CSV, a partir de la lista de objetos.
                for elemento in Contactos:
                    f.write(f'{elemento.NICKNAME}|{elemento.NOMBRE}|{elemento.CORREO}|{elemento.TELEFONO}|{elemento.FECHANACIMIENTO}|{elemento.GASTO}\n')

                # Cierro el archivo
                f.close()
                print("GRACIAS POR UTILIZAR EL PROGRAMA")
                break

            if opcion_elegida=="1":
                print("Seleccionaste la Opcion Agregar Contacto")

                # Nombre, de 1 a 20 letras mayúsculas, o espacio.
                ValidarDatos("^([a-zA-Z])\w{4,15}", "Nickname: ")
                NEWnickname=captura

                ValidarDatos("^([A-Z ]){9,24}$", "Nombre: ")
                NEWnombre=captura

                ValidarDatos("^[a-z0-9_.-]+@[a-z]+\.[a-z.]", "Correo: ")
                NEWcorreo=captura

                ValidarDatos("^[0-9]{2} ([0-9]{4})-([0-9]{4})$", "Telefono: ")
                NEWtelefono=captura

                ValidarDatos("^[0-9]{4}/[0-9]{2}/[0-9]{2}$","Fecha de Nacimiento: ")
                NEWfecha=captura

                ValidarDatos("[0-9]+\.[0-9]{2}$","Gastos: $")
                NEWgastos=captura

                Contactos.append(Contacto(NEWnickname,NEWnombre,NEWcorreo,NEWtelefono,NEWfecha,NEWgastos))

            if opcion_elegida=="2":
                print("Seleccionaste la Opcion Buscar Contacto")
                ValidarDatos("^([a-zA-Z])\w{4,15}", "Ingresa NickName a Buscar: ")
                NickName=captura

                indice_obtenido=BuscarContacto(NickName)
                if indice_obtenido==-1:
                    print("No se encontró el objeto")
                else:
                    print(f"\nNombre: {Contactos[indice_obtenido].NOMBRE}")
                    print(f"Telefono: {Contactos[indice_obtenido].TELEFONO}")
                    print(f"Correo: {Contactos[indice_obtenido].CORREO}")
                    print(f"Fecha de Nacimiento: {Contactos[indice_obtenido].FECHANACIMIENTO}")
                    print(f"Gastos: ${Contactos[indice_obtenido].GASTO}")
                    

            if opcion_elegida=="3":
                print("Eliminar Contacto")
                ValidarDatos("^([a-zA-Z])\w{4,15}", "Ingresa NickName a Buscar: ")
                NickName=captura

                indice_obtenido=BuscarContacto(NickName)
                if indice_obtenido==-1:
                    print("No se encontró el objeto")
                else:
                    print(f"\nEliminando a: {Contactos[indice_obtenido].NOMBRE}")
                    Contactos.pop(indice_obtenido)
            if opcion_elegida=="4":
                print("Mostrando Contactos")
                # Ordenamiento.
                Contactos.sort(key=attrgetter('NICKNAME'),reverse=False)
                # Barrido secuencial.
                for contacto in Contactos:
                    print("------------------------------------------")
                    print(f"Nickname: {contacto.NICKNAME}")
                    print(f"Nombre: {contacto.NOMBRE}")
                    print(f"Email: {contacto.CORREO}")
                    print(f"Telefono: {contacto.TELEFONO}")
                    print(f"Fecha de Nacimiento: {contacto.FECHANACIMIENTO}")
                    print(f"Gastos: ${contacto.GASTO}")

            input("Pulsa enter para contunuar...")
        else:
            print("Esa respuesta no es válida.")
            input("Pulsa enter para contunuar...")

principal()