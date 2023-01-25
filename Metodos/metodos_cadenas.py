cadena1 = 'Hola soy Fede'
cadena2 = 'Bienvenido'
cadena_numero = 11

dir = dir(cadena1) # Nos muestra los metodos que podemos utilizar para ese parametro particular, es una funcion

upper = cadena1.upper() # todo a mayusuculas
lower = cadena1.lower() # todo a minusculas
capitalize = cadena1.capitalize() # primer letra a mayusculas (solo la primer letra, el resto lo pasa a minuscula)

find = cadena1.find("e") # busca cadena dentro de la cadena y retorna el valor donde inicia y devuelve -1 en caso de que no lo encuentre 
index = cadena1.index("e") # busca cadena en cadena pero si no encuentra tira una excepcion (especie de error)

is_numeric = cadena1.isnumeric() # devuelve true si es numerico, false si no lo es, si es un numero en cadena(num = "123") devuelve true
is_alpha = cadena1.isalpha() # devuelve true si es alfanumerico, false si no lo es (solo valido caracteres de la A hasta la Z, espacio da falso)

count = cadena1.count("e") # devuelve la cantidad de veces que coincide, si no esta devuelve 0 
len = len(cadena1) #contamos cuantos caracteres tiene una cadena

ends_with = cadena1.endswith("e") # devuelve true si termina con la cadena, falso si no lo hace
starts_with = cadena1.startswith("H") # devuelve true si empieza con la cadena, falso si no lo hace

replace = cadena1.replace("Hola","holanda papa")   # Reemplaza pedazo de cadena por una cadena dada. Dos parametros, el primero es el antiguo, y el segundo es el nuevo. Si encuentra el valor lo reemplaza, pero si no lo encuentra (...)
split =  cadena1.split(" ") # Separa cadena con la cadena que pasamos, el valor que le pasamos es por lo que queremos dividir


print(split)
 
