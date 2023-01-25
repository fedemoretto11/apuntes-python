import pandas as pd

#Buscar archivo con pandas
# se usa df como varibale porque es un Data Frame
# Poneiendo "names= [lista]" modifica los encabezados de las columnas 
df = pd.read_csv("Archivos\\datos.csv",names=["name", "lastname", "age"]) 
df2 = pd.read_csv("Archivos\\datos.csv",names=["name", "lastname", "age"]) 

#print(df) # Asi obtengo todos los datos

#print(df["name"]) # Asi los datos de una columna en particular
nombres = df["name"]

# Slicing
# Sirve para recorrer colocando inicio y final (inicio incluido, final no)
cadena_simple = "0123456789"
#print(cadena_simple[2:6])

df_ordenado = df.sort_values("age") # se usa sort_values para ordenar por nombre de columna
#print(df_ordenado)

# Cocantenando los 2 data frames

df_concatenado = pd.concat([df,df2])
#print(df_concatenado)

#Accediendo a la primer fila
primer_fila = (df.head(1)) # Muestra la fila que le paso por parametro ( si le paso 3 me muestra la 3 primeras, osea desde el encaberzado hasta la fila que indico)

#Accediendo a la ultima fila
ultima_fila = (df.tail(1)) # Muestra la fila que le paso por parametro ( si le paso 3 me muestra la 3 ultimas, osea desde el final hasta la fila que indico)


# Accediendo a la cantidad de filas y columas
filas_y_columnas_totales = df.shape #primero filas y despues columnas, devuelve una tupla
filas_totales = filas_y_columnas_totales[0]
columnas_totales = filas_y_columnas_totales[1]
#print(filas_y_columnas_totales)

# Obteniendo data estadistca del fata frame
df_info = df.describe()
#print(df_info)

#Accediendo a un elemnto especifico con loc
elemento_especifico_loc = df.loc[1, "name"]
#print(elemento_especifico_loc)

#Accediendo a un elemnto especifico con iloc
elemento_especifico_iloc = df.iloc[1, 1]
#print(elemento_especifico_iloc)

#accediendo a todos las filas de una columa
nombres = df.iloc[:,1]
#print(nombres)

