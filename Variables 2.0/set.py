conjunto = set(['federico', 'moretto']) # requiere que se pase una lista

# meter un conjunto dentro de otro, hay que utilizar frozenset
conjunto1 = frozenset(["dato1", "dato2"])
conjunto2 = {conjunto1, "dato3"}

print(conjunto2)
print("-----")

# teoria de conjuntos

con1 = {1,3,5,7}
con2 = {1,3,7}

#para chequear si es un subconjunto
resultado = con2.issubset(con1)
resultado2 = con2 <= con1
print(resultado)
print(resultado2)
print("-----")

#para chequear si es un superconjunto
resultado3 = con2.issuperset(con1)
resultado4 = con2 > con1
print(resultado3)
print(resultado4)
print("-----")

#verificar si hay algun numero comun

resultado5 = con2.isdisjoint(con1) # va a ser true cuando ningun numero es igual
print(resultado5)
print("-----")