archivo_sin_leer = open("Archivos\\texto.txt",encoding="UTF-8")

# archivo = archivo_sin_leer.read() # Leer archivo completo
# linea = archivo_sin_leer.readline() # Lee una sola linea (entre parentesis pongo la cantidad limite de caracteres)
linea = archivo_sin_leer.readlines() # Leer todas las lineas (las devuelve com lista) //  el problema es que en caso de archivos grandes puede consumir mucha RAM
print(linea)
archivo_sin_leer.close() # Esto es para cerrar el archivo