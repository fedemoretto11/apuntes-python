import re

texto = '''Esta es la primer linea de texto capo,
Esta es la 2212312334. 
Y esta la 3ra pete'''


#esultado = re.findall(r"\S", texto)

#print(resultado)

# Armado de cadena que busque numero, seguido de punto y seguido espacio

# resultado = re.findall(f"\d{4}", texto)
# print(resultado)


texto = "Hola, mi numero de telefono es: 2268 510595 2268 518438"

pattern = r'\d{4}\s\d{6}'

reemplazo = re.sub(pattern,"(Numero oculto)", texto)
print(reemplazo)