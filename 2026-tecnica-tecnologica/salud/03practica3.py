'''
Practica #3
Realiza un programa en Python que pregunte al usuario su nombre, edad y ciudad.
Luego el programa debe mostrar una pequeña presentación con esos datos en pantalla.
Finalmente, el programa debe mostrar el tipo de dato de cada variable usando type().
'''
#Crear variables y guardar datos que el usuario introduce
print("=====INTRODUCE TUS DATOS=====")
nombre1 = input("Introduce tu nombre: ")
edad1 = input("Introduce tu edad: ")
ciudad1 = input("Introduce tu ciudad: ")
#Ver los datos que el usuario ingreso
print("============================")
print("=====DATOS DEL USUARIO=====")
print("Su nombre es: ", nombre1)
print("Su edad es: ", edad1)
print("Su ciudad es: ", ciudad1)
#Ver los tipos de datos que el usuario ingreso
print("nombre1 es un tipo de dato: ",type(nombre1))
print("edad1 es un tipo de dato: ",type(edad1))
print("ciudad1 es un tipo de dato: ",type(ciudad1))
print("===========================")
#Para borrar la terminal usaremos el comando "clear"

