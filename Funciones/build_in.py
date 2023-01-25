numeros = [4,7,4,1,3454,12]


# Alugnos ejemplos

numero_mas_alto = max(numeros) # Devuelve el numero mas alto
numero_mas_bajo = min(numeros) # Devuelve el numero mas bajo
numero_redondeado = round(12.234234,2) # Devuelve el numero redondeado con los decimales que indico en el 2do parametro
resultado_booleano = bool(0) # Devuelve true si pongo numeros != 0 y cadenas, cualquier cosa que no sea vacia
resultado_all = all([234, True, "verdadero"]) #parecido al anterior pero devuelve de tod (todos tienen que ser verdadero)
sum_total = sum(numeros) # suma todo los valores de un iterable






print("numero mas alto")
print(numero_mas_alto)
print("--------")
print("numero mas bajo")
print(numero_mas_bajo)
print("--------")
print("numero redondeado")
print(numero_redondeado)
print("--------")
print("Resultado booleano")
print(resultado_booleano)
print("--------")
print("Resultado all")
print(resultado_all)
print("--------")
print("Suma total de numeros")
print(sum_total)
print("--------")