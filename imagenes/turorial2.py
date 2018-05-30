# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/
 
# Imprime 'Hola' 10 veces
for i in range(10):
    print("Hola")
     
# Imprime 'Hola' 5 veces y 'Allí' una
for i in range(5):
    print("Hola")
print("Allí")
  
# Imprime 'Hola' 'Allí' 5 veces
for i in range(5):
    print("Hola")
    print("Allí")
  
# Imprime los números del 0 al 9
for i in range(10):
    print(i)
     
# Dos formas de imprimir los números del 1 al 10
for i in range(1, 11):
    print(i)
     
for i in range(10):
    print(i + 1)
     
# Dos formas de imprimir los números del 2 al 10
for i in range(2, 12, 2):
    print(i)
     
for i in range(5):
    print((i + 1) * 2)
     
# Cuenta atrás desde 10 hasta 1 (el cero no)
for i in range(10, 0, -1):
    print(i)
     
# Imprime números desde una lista
for i in [2, 6, 4, 2, 4, 6, 7, 4]:
    print(i)
     
# ¿Qué es lo que imprime éste código? ¿Por qué?
for i in range(3):
    print("a")
    for j in range(3):
        print("b")
 
# ¿Cuál es el valor de a?
a = 0
for i in range(10):
    a = a + 1
print(a)
 
# ¿Cuál es el valor de a?
a = 0
for i in range(10):
    a = a + 1
for j in range(10):
    a = a + 1
print(a)
 
# ¿Cuál es el valor de a?
a = 0
for i in range(10):
    a = a + 1
    for j in range(10):
        a = a + 1
print(a)     
 
# ¿Cuál es el valor de la suma?
sum = 0
for i in range(1, 101):
    sum = sum + i   