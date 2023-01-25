diccionario = {
    'nombre': 'Federico',
    'apellido': 'Moretto',
    'edad': 28
}

#muestra las claves
for key in diccionario:
    print(key)
print("----------------")
    
#itera las claves yu valores
for key in diccionario.items():
    print(key)
print("----------------")

for key in diccionario.items():
    clave = key[0]
    valor = key[1]
    print(f'la clave es: {clave} y el valor es: {valor}')
print("----------------")