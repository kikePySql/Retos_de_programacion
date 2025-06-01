""""
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
"""
#Aritmeticos
sum = 3 + 5
rest = 5 - 4
multi = 5 * 5
div = 5 / 6
div_modulus = 6 % 12
exp = 3**2
floor_division = 12//4

#logicos
8 < 10 and 5 < 4
6 > 3 or 5 < 4
not(8 < 10 and 5 < 4)

#Comparison Operators
8 ==8
9 !=8
9 > 7
8 < 9
9 >= 8
10 <= 11

#Assignment Operators
x = 5
x += 3 #x = x + 3
x -= 4 #x = x - 4
x *= 5 #x = x * 5
x /= 3 #x = x / 3
x %= 3 #x = x % 3
x //= 3 #x = x//3
x **= 5 #x = x ** 5

#operadores de identidad
a=1
b=1
c=10
print(a is b)
print(a is not c)

#operadores de pertenencia
print("u" in "Enrique")
print("h" not in "Enrique")

#operadores de bit
a = 10
b = 3
print(10&3)
print(10|3)
print(10^3)
print(~10)
print(10>>2)
print(10<<2)

#Estructuras de control

number = int(input("Escribe un numero: "))
if number > 0:
    print("este numero es positivo")
elif number == 0:
    print("Es el 0")
else:
    print("este numero es negativo")

def clasification():
    for number in range(1,101):
        if number % 10 == 0:
            print("uwu")
        elif number % 5 == 0:
            print("nyaaa")
        else:
            print(number)

print(clasification())

def clasic():
    for index in range(10,56):
        if index % 2 == 0 and index!=16 and index % 3 !=0:
            print(index)

print(clasic())