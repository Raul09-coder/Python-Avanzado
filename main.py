#Todos los programas se ejecutan como funciones de este progama.

#Estructura para importar una clase: from 'nombreprograma' import 'nombredelafunción'

#Estructura de llamado: nombrefuncióndelprograma()
from HolaMundo import main
from Funciones import norecibeargumentos
from Funciones import recibeargumentos
from Funciones import argumentosopcionales
from PreguntaValida import principal
from PreguntaDatos import mainPregunta
from UsoFormato import mainFormat
from Usoregex import mainRegex

main()
print("*"*25)
mainFormat()
print("*"*25)
norecibeargumentos()
print("*"*25)
#Enviar valores a una función que recibe argumentos
fname=input("Ingresa tu nombre: ")
lname=input("Ingresa tu apellido: ")
recibeargumentos(fname,lname)
print("*"*25)
city=input("Ingresa tu ciudad: ")
argumentosopcionales(city)
print("*"*25)
mainPregunta()
print("*"*25)
principal()
print("*"*25)
mainRegex()