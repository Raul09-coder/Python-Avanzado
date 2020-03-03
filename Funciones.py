# Demostracion de los diferentes tipos de funciones
# Argumentos utilizados
#   No recibe argumentos
#   Recibe argumentos
#   Tiene argumentos opcionales
# Retorno de valores
#   No retorna valores
#   Retorna valores
# Se pueden dar combinaciones de ambos aspectos

# Para declarar funciones se utiliza la palabra reservada 'def'

# Estructura para declarar una funcion: def 'nombredefuncion'():

# Es impotante que las funciones contegan algun tipo de codigo. En caso contrario usar pass

# Si una variable se declara fuera de una función se dice que es global 
variableglobal="Soy global"

# S i se quiere usar la variable global dentro de una función, debe utilizar la palabra reservada 'global'

def pendiente():
    pass

def norecibeargumentos():
    global variableglobal
    variableglobalLocal=4
    print("No recibe argumentos")
    print(variableglobalLocal)
    print(variableglobal)

# Los argumentos se declaran dentro de parentesis en forma de lista separada por comas.

#Estructura para declarar una función con argumentos:
#def 'NombreFunción' ('Argumento1','Argumento2'):
def recibeargumentos(fname, lname):
    print(fname + " " + lname)
    print(variableglobal)

# Un argumento opcional se presenta cuando le asignas un valor al momento de su declaracion.
# Los argumentos opcionales siempre van al final de la lista de argumentos.
def argumentosopcionales(city, country = "Mexico"):
    print("I am from " + city + ", " + country)

# Si se especifica return, la funcion devuelve valores 

def elevoalcuadrado(x):
  return x * x

def main():
    print(elevoalcuadrado(4))