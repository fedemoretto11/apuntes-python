# Parametro args
# COn el astierisco, y siempre al final

def suma(nombre, *numeros):
    return f"{nombre}, la suma de tus numeros es {sum(numeros)}"


resultado = suma("Fede",2,3,5,1,12)
print(resultado)
    