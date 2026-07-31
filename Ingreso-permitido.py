#Paso 1: Solicitar al usuario que ingrese la edad del cliente

edad = int(input("por favor, ingresa tu edad:   "))

#Paso 2: Verificar si la edad ingresada cumple con el requisito para ingresar

permitido = True if edad >= 18 else False #ternario


#Paso 3: Mostrar al usuario si su cliente puede o no ingresar a la discoteca.

if permitido:
    print("¡Puedes ingresar a la discoteca!")
else:
    print("Lo sentimos mucho, no se puede ingresar a la discoteca siendo menor de edad")