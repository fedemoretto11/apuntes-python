# todo archivo.py es un modulo

# 3 tipos
#     a) de puthon (escritos en C)
#     b) de 3ros
#     c) propios


# Forma de llmar modulos (Importar) (solo pide el nombre, sin la extension)

# import modulo_saludar # Opcion 1
#import modulo_saludar as s_aludar # Opcion2 (se utiliza el "as" para crearlo de forma mas abreviada)
from modulo_saludar import saludar #Opcion 3 (para importar solo una funcion determinada y no todo el modulo)

#Opcion 1
# saludo2 = modulo_saludar.saludar("Federico") # Esto es un name-space, y siempore se llama con la funcion como metodo
# print(saludo2)

#Opcion 2
#saludo2 = s_aludar.saludar("Federico") # Esto es un name-space, y siempore se llama con la funcion como metodo
# print(saludo2)

# Opcion 3
saludo3 = saludar("Federico")
print(saludo3)


# Acceder al nombre de este modulo
print(__name__)

#Acceder al nombre del modulo llamado
# print(s_aludar.__name__)
