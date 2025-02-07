# Operaciones con Cadenas            
# Crea dos variables de cadena llamadas cadena1 y cadena2. 
cadena1 = "Jheyson"
cadena2 = "Galvis"
# Concatena las dos cadenas y guarda el resultado en una
# variable nueva 
cadena3 = cadena1 + " " + cadena2 
# Imprime la longitud de la cadena resultante
print(len(cadena3))
print(f"El profe es {cadena3}")
# Reto Impriman la longitud de la cadena Talento_Tech es MINTIC

# Formato de cadenas       
# Crea una variable con tu nombre
nombre = "Jheyson"
apellido = "Galvis"
# Utiliza el formato de cadena para imprimir un mensaje
# de bienvenida personalizado
print(f"Hola, mi nombre es {nombre} y mi apellido es {apellido}")

"""
nombre = "Kenay"
print(f"Mi perro se llama {nombre}")
"""

# Subcadenas y Métodos
# Crea una cadena larga y utiliza el método split() para
# dividirla en subcadenas en una lista de palabras.

cadena_larga = "Estoy aprendiendo a programar en Python"
lista_de_palabras = cadena_larga.split()
print

cadena_larga = "Estoy aprendiendo a programar en Python"  
cantidad_de_caracteres = len(cadena_larga)
print(cantidad_de_caracteres)

cadena_larga = "Estoy aprendiendo a programar en Python"
print("Número de palabras:", len(cadena_larga.split()))
print("Número de caracteres", len(cadena_larga))

# Métodos de Mayúsculas y Minúsculas 
# Crea una cadena en minúscula y conviertela a mayúsculas
# usando los métodos upper() y lower()

texto = "Hola, mundo"  
texto_minuscula = texto.lower()
texto_mayuscula = texto.upper()
print(texto_minuscula)
print(texto_mayuscula)  

# Operaciones Aritméticas
# Crea dos variables a y b, con valores numéricos
a = 29
b = 2025
# Realiza operaciones aritméticas básicas
# (suma, resta, multiplicación, división, exponente)
# con esta variable se imprimen los resultados.

print(a + b) # Suma
print(a - b) # Resta
print(a * b) # Multiplicación
print(a / b) # División
print(a ** b) # Exponente

# División y Módulo
# Divide dos números enteros y guarda el resultado en una variable llamada resultado

a = 5
b = 2
resultado = a / b
print(f"El resultado de la división es {resultado}")

# Ejercicio imprimir una multiplicación con base en el ejercicio anterior

a = 5
b = 2
resultado = a * b
print(f"El resultado de la multiplicación es {resultado}")

#Presicion de flotantes

#Crea una variabl c con un valor flotante

c = 3.14159 

#Realiza operaciones aritméticas que involucren flotantes y enteros
suma = c + a
resta = c - a
multiplicacion = c * a
division = c / a

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)

# Como se manejann las operaciones mixtas
a = 10 
b = 3.15
resultado = a * b

print(f"El resultado de la multiplicación es {resultado}")
print(type(resultado))  