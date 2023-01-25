# todo lo siguiente funciona tanto en listas como en tuplas y sets (para esto ultimo un caso particaular aclarado mas abajo)

animales = ["gato", "perro", "oveja", "vaca"]
numeros = [1,5,8,2]
# Para recorrer e imprimir
for animal in animales:
    print(f'ahora la variable animal es: {animal}')
print("--------------")
    
# Para recorrer, multiplicar e imprimir
for numero in numeros:
    resultado = numero * 2
    print(f'ahora la variable animal es: {resultado}')
print("--------------")
    
# para iterar mas de una lista al mismo tiempo, tienen que tener el mismo tamaño
for numero,animal in zip(numeros, animales):
    print(f'recorriendo lista 1: {animal}')
    print(f'recorriendo lista 2: {numero}')
print("--------------")
    
    
    
for nume in range(30):
    print(nume)
print("--------------")

#forma no optima de recorrer una lista con su indice NO FUNCIONA EN SETS
print("Forma no optima de recorrer una lista con su indice")
for num in range(len(numeros)):
    print(numeros[num])
print("--------------")

#forma optima de recorrer una lista con su indice
print("Forma optima de recorrer una lista con su indice")
for num in enumerate(numeros):
    indice = num[0]
    valor = num[0]
    print(f'el indice es: {indice} y el valor es: {valor}')
print("--------------")


#usando el for/else
for num in numeros:
    print(f'ejecutando el ultimo bucle, valor actual: {num}')
else:
    print("bucle finalizado")
print("--------------")


