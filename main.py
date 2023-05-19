"""
Universidad Nacional de San Juan
Facultad de Ciencias Exactas, Fisicas y Naturales

Asignatura: Programacion Orientada a Objetos

Autor: Federico Gabriel Sanchez
Legajo: EO14-53   Esp: TUPW

Unidad 2 - Ejercicio 1
"""

from clase_Email import Email
from clase_ManejadorEmail import ManejadorEmail

if __name__ == '__main__':
    
    nombre = input('Ingrese su nombre: ')
    id = input('Ingrese ID: ')
    dom = input('Ingrese dominio: ')
    tipoDom = input('Ingrese tipo de dominio: ')
    contraseña = input('Ingrese contraseña: ')

    mail = Email(id,dom,tipoDom,contraseña)

    print("Estimado",nombre,"te enviaremos tus mensajes a la dirección", mail.retornaEmail(),".")
    print("El mail es: ", mail.retornaEmail())
    print("El dominio es: ", mail.getDominio())

    mail.modificar_Contraseña()

    correo1 = "informatica.fcefn@gmail.com"

    mail2= mail.crearCuenta(correo1)
    lista = ManejadorEmail()
    lista.testEmail()

    inicio = 0
    dominio = input('Ingrese dominio: ')
    cantidad = lista.controlDom(dominio,inicio)

    print("La cantidad de dominios es igual a ",cantidad)