frase = input("Ingrese una frase: ")
lista = frase.split(" ")
palabras = len(lista)
print('-------------------')
print(f'La persona dijo {palabras} palabras')
tiempo_frase = palabras / 2
print('-------------------')
# print(f'La persona dijo la frase en {tiempo_frase} segundos')
# print('-------------------')

if tiempo_frase < 60:
    print(f'La persona dijo la frase en {tiempo_frase} segundos')
else:
    print('Para flaco, no te pedi un testamento')
 
print('-------------------')

print(f'Dalto tardaria {palabras * 100 // 2 * 1.3 / 100} segundos en decir lo mismo')
print('-------------------')