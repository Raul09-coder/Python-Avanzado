# Pregunta y valida un dato.

# Módulo requerido para la validación de expresiones regulares
import re
# Módulo para trabajar con datos de tipo datetime
import datetime

# Se declara una variable global, que permitirá preguntar y validar información.
captura=""

# Función que valida un dato, y si es correcto, lo coloca en la variable captura, si no, se mantiene preguntando.
def askandcheck(_patron,_pregunta="Dame un dato: "):
    # Se especifica que la valiable 'captura' es global.
    global captura
    #Ciclo Infinito
    while True:
        _fxvalor = input(_pregunta)
        #asigna a la variable 'coincide' el valor recolectado de la funcion search evaluando que cumpla las condiciones asignadas al argumento '_patron' de '_fxvalor'
        coincide = re.search(_patron, _fxvalor)
        if (coincide):
            captura= _fxvalor
            break
        else:
            print("El dato no es correcto. Intenta de nuevo.")

# Función que convierte un valor en formato YYYY-MM-DD a datetime
def strtodate(_dtoconv):
    return datetime.datetime(int(_dtoconv[0:4]), int(_dtoconv[5:7]), int(_dtoconv[-2:]))


def principal():
    # Sólo acepta un código de 4 dígitos
    askandcheck("^[0-9]{4}$", "ID (4 dígitos): ")
    numeroID=captura
    # Nombre, de 1 a 20 sólo letras mayúsculas, o espacio.
    askandcheck("^([A-Z]){1,20}$", "Nombre: ")
    nombre=captura
    # S o N
    askandcheck("^[S|N]$", "Acepta (S/N): ")
    acepta=captura
    # Fecha estructurada año-mes-dia
    askandcheck("^(19|20)\d\d[-](0[1-9]|1[012])[-](0[1-9]|[12][0-9]|3[01])$", "Dame una fecha (YYYY-MM-DD): ")
    fecha=captura

    #Presneta los valores recolectados
    print("ID: ",numeroID)
    print("Nombre: ",nombre)
    print("Respuesta S/N: ",acepta)
    print("Fecha: ",fecha)