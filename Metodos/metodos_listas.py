lista1 = ['Federico', 'Moretto', 28, True]
lista2 = [45, 22, 98, 44, True, False]


lista3 = list(['hola', 'chau', 23]) # Sirve para crear lista, su uso se da principalmente para crear listas vacias

len = len(lista1) # Devuelve la cantidad de elementos de la lista

lista1.append('ricotero') # Agrega un elemento a la lista al final
lista1.insert(2, "Hola beibi") # Agega un elemento a la lista en un indice especifico (primer parametro la posicion, segundo lo que quiero agregar)
lista1.extend(["pepe", False, 31]) # Agrega varios elementos a la lista, no puede pasar elementos unicos y dentro de corchetes

lista1.pop(0) # Elimina un elemento de la lista por el indice (poniendo -num elimina contando desde el ultimo)
lista1.remove('ricotero') # Remueve un elemento por su valor
lista1.clear() # Elimina todos los elementos de la lista 

lista2.sort() # Ordena la lista de menor a mayor, solo cuando NO hay string
lista2.sort(reverse = True) # Ordena la lista de mayor a menor, solo cuando NO hay string
lista2.reverse() # Invierte los elementos de una lista

print(lista1)
print(lista2)
