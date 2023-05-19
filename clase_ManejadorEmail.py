"""
Unidad 2 - Ejercicio 1 - modulo 2: Manejador para Email
"""
import csv
from clase_Email import Email

class ManejadorEmail:

    def __init__(self):
        self.__listaEmail = []
    
    def agregarEmail(self, unEmail):
        self.__listaEmail.append(unEmail)
    
    def testEmail(self):
        archivo = open('BaseDatos.csv')
        reader = csv.reader(archivo, delimiter =',')

        for fila in reader:
            id = fila[0]
            dom = fila[1]
            tipoDom = fila[2]
            contraseña = fila[3]
            unEmail = Email(id,dom,tipoDom,contraseña)
            self.agregarEmail(unEmail)
        archivo.close()

    def contadorDominio(self,dominio,cantidad):
        i = 0
        for i in range(len(self.__listaEmail)):
            if(self.__listaEmail[i].getDominio() == dominio):
                cantidad = cantidad + 1
        return(cantidad)