import re

texto = '''Esta es la primer linea de texto capo,
Esta es la 2212312334. 
Y esta la 3ra pete'''


#esultado = re.findall(r"\S", texto)

#print(resultado)

# Armado de cadena que busque numero, seguido de punto y seguido espacio

resultado = re.findall(f"\d{4}", texto)
print(resultado)
