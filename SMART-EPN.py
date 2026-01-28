import random
import webbrowser
from os import system
import time

nombres = []
cedulas = []
cupones = []
cuponGlobal=""

def menuOpciones():
    print("---- SMARTEPN ----")
    print("1. Registrar estudiante")
    print("2. Mostrar datos del estudiante")
    print("3. Comprar productos")
    print("4. Mostrar factura")
    print("5. Salir")
    return int(input("Seleccione una opción: "))

def validarCantidad():
  while True:
    numProdcutos = int(input("Ingrese el número de productos a registrar: "))
    if numProdcutos > 0:
        return numProdcutos
    print("El número de productos es incorrecto")
    

def apiWhatsApp(numero,mensaje):
    url = f'https://api.whatsapp.com/send?phone=593{numero}&text={mensaje}'
    webbrowser.open(url)


def registrarEstudiante():
    global cuponGlobal
    nombre = input("Nombre del estudiante: ")
    cedula = input("Cédula del estudiante: ")
    celular = input("Celular del estudiante: ")
    codigo = random.randrange(1000, 9999)
    
    nombres.append(nombre)
    cedulas.append(cedula)
    cupones.append(f"EPN-{codigo}")
    cuponGlobal=f"EPN-{codigo}"
    print(f"Estudiante {nombre} registrado con éxito.")
    mensaje = f"Bienvenido a SmartEPN - su cupón de descuento es EPN-{codigo} y tendrá un 50% de descuento en sus compras."
    print("Procesando los datos")
    print("Por favor espere....")
    time.sleep(3)
    apiWhatsApp(celular,mensaje)
    print("Mnesaje enviado con éxito")


def mostrarEstudiante(cedula):
    global cuponGlobal
    for i in range(len(cedulas)):
        if cedulas[i] == cedula:
            print("Registro encontrado:")
            print(f"Nombre del estudiante: {nombres[i]}")
            print(f"Cédula del estudiante: {cedulas[i]}")
            print(f"Cupón de descuento: {cupones[i]}")
            cuponGlobal=f"EPN-{cupones[i]}"
            return 
    print("No se encontró un estudiante con ese nombre.")


def ingresarProducto(numProdcutos,cuponEstudiante):
    sumatoria= promo = 0 
    for i in range(numProdcutos):
        precio = float(input(f'Ingrese el precio del producto {i+1}: '))
        sumatoria += precio
        promo+=1
    
    print('¿Quiere agregar cupón de descuento?')
    verificar = input("Ingrese si o no: ").lower()
    if verificar == "si":
        cupon = input("Ingrese el código: ")
        if cupon == cuponEstudiante:
            sumatoria = sumatoria * 0.5
        else:
            promo=0
            print("Cupón incorrecto. No se aplica descuento.")
    else:
        promo=0
    print("Productos registrados con éxito")
    return sumatoria,promo


def imprimirFactura(promo,sumatoria,numProdcutos):
    if (promo >= 1):
        print("---------- DESCUENTO ----------------")
        print("* Detalle del cupón de descuento")
        print(f"* Nombre del cupón de descuento es {cuponGlobal}")
        print(f'* Número de productos con descuento son: {promo}')
        print(f'* Precio final a pagar es: ${sumatoria}')
    else:
        print(f'* Número de productos son: {numProdcutos}')
        print(f'* Precio final a pagar es: ${sumatoria}')


def main():
    global cuponGlobal
    opcion = menuOpciones()
    while opcion !=5 :
        if opcion==1:
            system("cls")
            registrarEstudiante()
        elif opcion==2:
            system("cls")
            cedulaBuscar = input("Ingrese la cédula del estudiante a buscar: ")
            mostrarEstudiante(cedulaBuscar)
        elif opcion ==3:
            system("cls")
            numProdcutos = validarCantidad()
            sumatoria,promo= ingresarProducto(numProdcutos,cuponGlobal)
        elif opcion ==4:
            system("cls")
            imprimirFactura(promo,sumatoria,numProdcutos)
        opcion = menuOpciones()

    print("Muchas gracias")

main()