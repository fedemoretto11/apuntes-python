# Pedir un numero y devolver los numeros primos desde el 0 hasta el ingresado por el usuario

def numeros_primos(num):
    for i in range(2, num - 1):
        if num % i == 0: return False
    return True

def primos_hasta(num):
    primos = []
    for i in range(3, num + 1):
        resultado = numeros_primos(i)
        if resultado == True: primos.append(i)
    return primos

resultado= primos_hasta(39)
print(resultado)