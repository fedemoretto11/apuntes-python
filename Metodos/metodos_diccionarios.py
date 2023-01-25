diccionario = {
    'nombre': 'Federico',
    'apellido': 'Moretto',
    'edad': 28,
    'interesado_en_python': True
    }

diccionario2 = {
    'nombre': 'Maria',
    'apellido': 'Paulse',
    'edad': 22,
    'interesado_en_python': False
    }


keys = diccionario.keys() # Devuelve las claves y nos sirve para iterar
get = diccionario.get('nombre') # Devuelve el valor de la clave que pedimos, si no existe no lanza excepcion sino que indica NONE
diccionario2.clear() # ELimina todo los elementos del diccionario
diccionario.pop('nombre') # Elimina un elemento del diccionario, para elimnar mas elementos los spearo con ,
items = diccionario.items() # Devuelve un elemento dict_items iterable


print(items)