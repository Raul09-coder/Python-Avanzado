import datetime
import csv
from operator import attrgetter

class Contacto :
    def __init__( self,NICKNAME,NOMBRE,CORREO,TELEFONO,FECHANACIMIENTO,GASTO):
        self.NICKNAME = NICKNAME
        self.NOMBRE = NOMBRE
        self.CORREO = CORREO
        self.TELEFONO = TELEFONO
        self.FECHANACIMIENTO = FECHANACIMIENTO
        self.GASTO = GASTO