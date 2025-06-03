"""
/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 */
"""

# Listas
my_list = ["Enrique","Natalia","Kevin","Laura"]
print(my_list)
my_list.append("Castor") #inserccion
print(my_list)
my_list.remove("Enrique")
print(my_list)
print(my_list[1]) # Acceso
my_list[1]= "Xayah" #Actualizacion
print(my_list)
my_list.sort() #Ordenacion
print(my_list)

#Tuplas
my_tuple = ("Enrique","Almanza", "Kikeflow", 27)
print(my_tuple[1]) #Acceso
print(my_tuple)

#Sets
my_sets = {"Enrique","Almanza", "Kikeflow", 27}
my_sets.add("kike10a2013@gmail.com") #Insercion
my_sets.remove("Enrique") #Eliminacion
print(my_sets)

#Diccionario
my_dict = {
    "name":"Enrique",
    "surname":"Almanza", 
    "alias":"Kikeflow",
    "age": "27"
}
my_dict["email"] = "kike10a2013@gmail.com" #Insercion
print(my_dict["name"]) #Acceso
my_dict["age"] = "28" #Actualizacion
print(my_dict)

#Ejercicio

def my_agenda():

    agenda = {}

    def insert_contact():
        phone = input("Introduce el telefono del contacto: ")
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
            agenda[name]= phone
        else:
            print(
                "Debes inreducir un numero de telefono un maximo de 12 digitos.")

    while True:

       print("")
       print("1. Buscar contacto")
       print("2. Insertar contacto")
       print("3. Actualizar contacto")
       print("4. Eliminar contacto")
       print("5. Salir")

       opcion = input("\nSelecciona una opcion: ")

       match opcion:
           case "1":
               name = input("Introduce el nombre del contacto a buscar: ")
               if name in agenda:
                   print(f"El numero de telefono de {name} es {agenda[name]}.")
               else:
                   print(f"El contacto {name} no esta en la agenda.")
           case "2":
               name = input("Introduce el nombre del contacto: ")
               insert_contact()           
           case "3":
               name = input("Introduce el nombre del contacto a actualizar: ")
               if name in agenda:
                   insert_contact()
               else:
                   print(f"el contacto {name} no esta en la agenda")
           case "4":
               name = input("Introduce el nombre del contacto a eliminar: ")
               if name in agenda:
                   del agenda[name]
               else:
                   print(f"el contacto {name} no esta en la agenda")
           case "5":
               print("Saliendo de la agenda")
               break
           case _:
                print("Opcion invalidad. Elige una opcion del 1 al 5")
    

my_agenda()


