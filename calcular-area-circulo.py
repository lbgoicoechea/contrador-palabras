import math

# Paso 1: Solicitar al usuario que ingrese el radio del circulo.


radio = float(input("Por favor, ingrese el radio del circulo:   "))

# Paso 2: Calcular el área del circulo utilizando la formula area = pi *radio^2

area = math.pi * (radio**2)

# Paso 3: Mostrar al usuario el area calculada

print("El área del circulo con radio", radio, "es: ", area)

