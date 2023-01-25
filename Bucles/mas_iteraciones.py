deportes = ['futbol', 'tenis', 'handball', 'basket', 'autos']
cadena = "Hello Federico"

#Con el contiune salteo cuando coicide con esa iteracion
for deporte in deportes:
    if deporte == "basket":
        continue
    print(f'Me gusta jugar al {deporte}')
print('-----------------')

#Evitar que el bucle siga ejectuandose
for deporte in deportes:
    print(f'Me gusta jugar al {deporte}')
    if deporte == "tenis":
        break
    
print('-----------------')


# recorrer cadena de texto

for letra in cadena:
    print(letra)
print('-----------------')


numeritos = [2,4,6,8]
# for en una sola linea de codigo
numeros_duplicados = [x*2 for x in numeritos]
print(numeros_duplicados)
print('-----------------')
