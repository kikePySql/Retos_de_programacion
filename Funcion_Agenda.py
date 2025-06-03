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

       opcion = input("\nSelecciona una opcion")

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