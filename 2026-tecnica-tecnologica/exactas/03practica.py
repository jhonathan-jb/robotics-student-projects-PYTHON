'''
Practica 3
1.Realizar un programa para 
pedir datos personales al usuario:
    Nombre
    Edad
    Ciudad
2. Luego se debe mostrar los datos de la persona
y ver el tipo de dato que es.
'''
nombre1 = input("Introduce tu nombre: ")
edad1 = input("Introduce tu edad: ")
ciudad1 = input("Introduce tu ciudad: ")
#ahora veremos los datos que dio el usuario
print("=================")
print("DATOS DEL USUARIO")
print("Su nombre es: ", nombre1)
print("Su edad es: ", edad1)
print("Su ciudad es: ", ciudad1)
print("=================")
print("TIPOS DE DATOS")
print("nombre1 es un tipo de dato",type(nombre1))
print("edad1 es un tipo de dato",type(edad1))
print("ciudad1 es un tipo de dato",type(ciudad1))
print("FIN TERMINASTE LA PRACTICA")
#El comando "clear" en la terminal sirve para borrar la terminal