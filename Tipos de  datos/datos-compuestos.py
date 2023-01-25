# Listas --> conjunto de datos // 1 tipo de matriz

lista  = ['Federico', 'Moretto', True, 1.78]
print(lista[0])



# Tuplas -->  conjunto de datos que NO se puede modificar

tupla = ('Federico', 'Moretto', False, 1.90)
print(tupla[2])



# Conjunto / SET 
# (no tienen orden fijo)
# (no se puede acceder por indice a los elementos) 
# (No permite repetir valores) 
# (Muy bueno para eliminar duplicados)

conjunto = {'Federico', 'Moretto', False, 1.90}



#Diccionario (dict)
diccionario = {
    'nombre': 'Federico',
    'apellido': 'Moretto',
    'edad': 28,
    'esta_emocionado' : True
    #'clave'/'key': valor,
}
print(diccionario['apellido'])