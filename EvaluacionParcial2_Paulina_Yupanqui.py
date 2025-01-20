fondo_cambio = 40000
descuentos = float
registro_dinero__ingresado = 0
precio_auto = 0
correo = ""

print("Bienvenido a arriendo de estacionamientos")
print("*****************************************")
print("Catálogo de tipo de vehículo")
print("Auto: $2.000\n  Camioneta: $3.000\n  Camión: $4.000\n  Motocicleta: $890")

while True:
    correo = str(input("Ingrese su correo electrónico: "))
    if len (correo) <8 or len (correo) >30:
        print("El nombre debe tener entre 8 y 30 carácteres")
        continue
    
    print("Menú de autos")
    print("*************")
    print("Los tipos de vehículos a disponibilidad son:\n [1]Auto: $2.000\n  [2]Camioneta: $3.000\n  [3]Camión: $4.000\n  [4]Motocicleta: $890")
    opc = ""
    while True:
        try:
            opc = int(input("Seleccione un número del tipo de vehículo que tenga ud: "))
            if opc == 1:
                precio_auto = 2000
                print("El tipo de vehículo seleccionado es: Auto, con un costo de $2.000")
            elif opc == 2:
                precio_auto = 3000
                print("El tipo de vehículo seleccionado es: Camioneta, con un costo de $3.000")
            elif opc == 3:
                precio_auto = 4000
                print("El tipo de vehículo seleccionado es: Camión, con un costo de $4.000")
            elif opc == 4:
                precio_auto = 890
                print("El tipo de vehículo seleccionado es: Motocicleta, con un costo de $890")
            else:
                print("Opción inválida, intente nuevamente")
                continue
            break
        except ValueError:
            print("Debe ingresar un número de 1 a 5")
    while True: 
        try: 
            registro_dinero__ingresado = int(input("Ingrese la cantidad de dinero con la que va a pagar: "))
            if registro_dinero__ingresado < 1 or registro_dinero__ingresado > 10000:
                print("La cantidad de dinero que ingrese no puede ser 0 ni mayor a $10.000")
                continue
            break
        except ValueError: 
            print("Debe ingresar un número")
    
    codigo = 0
    codigo = int(input("Si desea finalizar el proceso, ingrese el código secreto: "))
    if codigo == 3312:
        print("Su total es de: \n Gracias por hacer uso de nuestro servicio :)")
        break
    else:
        print("El código es incorrecto, por favor llame a un administrador")
               