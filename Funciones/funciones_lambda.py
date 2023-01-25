# su uso es sencillo y rapido
# retorno inmediato


# FUncion Lambda
multiplicar_por_dos = lambda num : num * 2

print(multiplicar_por_dos(8))

numeros = [1,2,543,2,2,42,1,2]

numeros_pares = filter(lambda numero : numero % 2 == 0, numeros)
print(list(numeros_pares))