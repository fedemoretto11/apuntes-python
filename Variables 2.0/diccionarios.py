#crendo diccionario con funcion, solo asi se puede crear diccionarios vacios

diccionario = dict(nombre ="Federico", apellido="Moretto")
print(diccionario)
print("--------------")

#Creando diccionarios con frontKeys, crea las claves con valores in definir
diccion = dict.fromkeys(["Federico", "Moretto"])
print(diccion)
print("--------------")
#Si pongo un segundo valor fuera de la lista va a ser el valor predeterminado en el diccionario
dicci = dict.fromkeys(["Federico", "Moretto"], "Capo")
print(dicci)
print("--------------")


#las listas no pueden ser claves
tupla_dicc = {("federico","moretto"): "diccionario con tupla de clave"}
print(tupla_dicc)
print("--------------")
# lista_dicc = {["federico","moretto"]: "diccionario con tupla de clave"}
# print(lista_dicc)
# print("Tira error porque no permite con listas")
# print("--------------")

# Los conjuntos si pero con frozen set
conj = {frozenset(["Fede", "More"]): "diccionario creado con conjunto como clave"}
print(conj)
print("--------------")