"""
EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */
"""
#simple

def fun():
    print("soy una funcion")

fun()

#con un argumento

def sum(a,b):
    print(a + b)

sum(2,5)

#con argumento predeterminado
def default_arg_greet(name="Python"):
    print(f"hola, {name}")

default_arg_greet()

#con retorno

def nya(uwu):
    if uwu >=18:
        resultado = uwu**2
        return resultado
    else:
        print("no uwu")
    
nya(15)

#con argumentos y retorno
def return_args_greet(greet, name):
    return f"{greet}, {name}"

print(return_args_greet("hi","Enrique"))

#con retorno de varios valores

def multiple_return_greet():
    return "hola", "Python"

greet, name = multiple_return_greet()
print(name)
print(greet)

#con un numero variable de argumentos

def variable_arg_greet(*names):
    for name in names:
        print(f"hola, {name}")

variable_arg_greet("Python", "Enrique", "Almanza","kikeflow")

#con un numero variable de argumentos con pablara clave

def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"hola, {value} ({key})")

variable_key_arg_greet(
    language="python",
    name="Enrique",
    alias="kikeflow",
    age=36
)

#funciones dentro de funciones
def outer_function():
    def inner_function():
        print("funcion interna: hola python")
    inner_function()

outer_function()

#funciones del lenguaje(built-in)

print(len("Kikeflow"))
print(type(36))

#variables locales y globales

global_variable = "Python"

print(global_variable)

def hello_python():
    local_var ="hola"
    print(f"{local_var}, {global_variable}")

hello_python()

def funcion(nya, uwu):
    return len(nya+uwu)

print(funcion("Enrique","Kikeflow"))

def list_number(nya, uwu):
    count = 0
    for number in range(1, 101):
        if number %3==0 and number%5==0:
            print(nya+uwu)
        elif number % 5 == 0:
            print(uwu)
        elif number %3==0:
            print(nya)
        else:
            print(number)
            count += 1
    return count
        
print(list_number("Enrique", "Kikeflow"))

def print_numbers(text_1, text_2)-> int:
    count=0
    for number in range(1,101):
        if number %3==0 and number%5==0:
            print(text_1 + text_2)
        elif number%5 == 0:
            print(text_2)
        elif number %3 == 0:
            print(text_1)
        else:
            print(number)
            count += 1
    return count

            
print(print_numbers("UWU", "NYA"))



