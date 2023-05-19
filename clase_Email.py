"""
Unidad 2 - Ejercicio 1 - modulo 1: Clase Email
"""

class Email:
    __idCuenta = ""
    __dominio = ""
    __tipoDominio = ""
    __contraseña = ""

    def __init__(self, nombreCuenta, dominio, tipoDominio, contraseña):
        self.__idCuenta = nombreCuenta
        self.__dominio = dominio
        self.__tipoDominio = tipoDominio
        self.__contraseña = contraseña
    
    def getDominio(self):
        return self.__dominio
    
    def retornaEmail(self):
        return(self.__idCuenta+'@'+self.__dominio+'.'+self.__tipoDominio)
    
    def modificar_Contraseña(self):
        contraseña = input('Teclee su contraseña actual: ')

        if(contraseña == self.__contraseña):
            self.__contraseña = input('Ingrese su nueva contraseña: ')
            print("Contraseña modificada.")
        else:
            print("Contraseña incorrecta.")
        return
    
    def crearCuenta(self, nombreUsuario):
        x = nombreUsuario.split('@')
        y = x[1].split('.')
        id = x[0]
        dom = y[0]
        tipo = y[1]
        contraseña = "1234"

        direccionCorreo = Email(id,dom,tipo,contraseña)
        return(direccionCorreo)
    
    def mostrarDatos(self):
        print("Mail: ",self.__idCuenta+'@'+self.__dominio+'.'+self.__tipo)
        print("Contraseña: ",self.__contraseña)
        return

