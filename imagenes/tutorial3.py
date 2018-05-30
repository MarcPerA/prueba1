# Sample Python/Pygame Programs

 
# Podemos emplear un bucle while allí donde, también, podríamos usar un bucle for:
i = 0
while i < 10:
    print(i)
    i = i + 1
 
# Es lo mismo que:
for i in range(10):
    print(i)
 
# Es posible simplificar el código:
# i=i+1
# Con lo siguiente:
# i += 1
# Esto lo podemos hacer también con la resta y la multiplicación.
i = 0
while i < 10:
    print(i)
    i += 1
 
# ¿Qué imprimiremos aquí?
i = 1
while i <= 2 ** 32:
    print(i)
    i *= 2
 
     
 
# Una tarea muy habitual, es iterar hasta que el usuario realiza una petición de salida.
 
salir = "n"
while salir == "n":
    salir = input ("¿Quieres salir? ")
 
     
# Existen diversas formas para salir de un bucle. Un operador booleano que dispare el evento es una
# forma de conseguirlo.
hecho = False
while not hecho:
    salir = input ("¿Quieres salir? ")
    if salir == "s":
        hecho = True;
         
    ataca = input ("¿El elfo atacó al dragón? ")
    if ataca == "s":
        print("Mala elección, estás muerto.")
        hecho = True;
     
valor = 0
incremento = 0.5
while valor < 0.999:
    valor += incremento
    incremento *= 0.5
    print(valor)
     
 
# -- Problemas habituales con los bucles while --
 
# El programador quiere hacer una cuenta atrás empezando en 10.
# ¿Qué es lo que está mal, y cómo lo podemos arreglar?
i = 10
while i == 0:
    print (i)
    i -= 1
     
# ¿Qué es lo que está mal en este bucle que intenta contar hasta 10? 
# ¿Qué sucederá cuando lo ejecutemos? 
i = 1
while i < 10:
    print (i)