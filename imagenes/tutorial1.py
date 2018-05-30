# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/
 
# Vídeo explicativo: http://youtu.be/pDpNSck2aXQ
 
 
# Variables usadas para el ejemplo de declaraciones ”if”
 
a = 4
b = 5
c = 6
 
# Comparaciones básicas
if a < b:
    print ("a es menor que b")
 
if a > b:
    print ("a es mayor que b")
 
if a <= b:
    print ("a es menor o igual a b")
 
if a >= b:
    print ("a es mayor o igual a b")
 
# OBSERVACIÓN: Es muy fácil confundir el uso de == y =.
# Utiliza == si estás preguntando si son iguales.
# Utiliza = si estás asignando un valor a una variable.
if a == b:
    print ("a es igual a b")
    
# Not equal 
if a != b:
    print ("a y b no son iguales")
     
# And
if a < b and a < c:
    print ("a es menor que b y c")
  
# Non-exclusive or   
if a < b or a < c:
    print ("a es menor que a o b (o ambos)")
 
     
# Tipos Booleanos de datos. Esto es correcto!
a = True
if a:
    print ("a es cierto")
     
if not(a):
    print ("a es falso")
 
a = True
b = False
 
if a and b:
    print ("a y b, ambos son ciertos")
     
a = 3
b = 3
c = a == b
print(c)
 
# Esto también es correcto y será cierto debido
# a que los valores no son cero:
if 1:
    print ("1")
if "A":
    print ("A")
 
# No se comportará como cierto ya que es cero.
if 0:
    print ("Cero")
     
# Comparar variables con valores múltiples.
# El primer if parece que funciona, pero siempre se comporta como cierto 
# aún cuando la variable 'a' no sea igual a 'b'.
# Esto se debe a que 'b' se considera cierta por sí misma.
a = "c"
if a == "B" or "b":
    print ("a es igual a b. A lo mejor.")
     
# Esta es la manera más adecuada para hacer un if.
if a == "B" or a == "b":
    print ("a es igual a b.")
 
# Ejemplo 1: Sentencia If 
temperatura = int(input("¿Cuál es la temperatura en grados Fahrenheit? "))
if temperatura > 90:
    print ("Hace calor fuera")
print ("Hecho")
 
# Ejemplo 2: Sentencia Else 
temperatura = int(input("¿Cuál es la temperatura en Fahrenheit? "))
if temperatura > 90:
    print ("Hace calor fuera")
else:
    print ("Hace fresco fuera")
print ("Hecho")
 
#Ejemplo 4: Sentencia  Else if
temperatura = int(input("¿Cuál es la temperatura en Fahrenheit? "))
if temperatura > 90:
    print ("Hace calor fuera")
elif temperatura < 30:
    print ("Hace fresco fuera")
else:
    print ("No hace calor fuera")
print ("Hecho")
 

 
# Comparaciones usando strings/cadenas de texto
nombre_usuario = input("¿Cuál es tu nombre? ")
if nombre_usuario == "Pablo":
    print ("Me gusta tu nombre.")
else:
    print ("Ok.") 