# print("Bienvenido a esta hermosa seccion, decime tu nombre perrito malvado:")
# nombre = input()
# print(f"Pero que nombre de mierda que tenes {nombre}")
# edad = input("A ver papa, decime tu edad ahora: ")
# print(f"En serio tenes {edad} años? Estas hecho mierda")


# numero1 = int(input("A ver papu, decime un numero: "))
# numero2 = int(input("Ya que estas al pedo decime otro asi laburo un rato: "))
# suma = numero1 + numero2
# print(f"Genial perrito, la suma de tus numeros es {suma}")


# numero1 = float(input("A ver papu, decime un numero, pero si tenes huevos, que sea con coma: "))
# numero2 = float(input("Pillo eh, decime otro igual: "))
# suma = numero1 + numero2
# redondeado = round(suma,2)
# print(f"Genial perrito, la suma de tus numeros es {redondeado} , si me la banque y te lo redondee a 2 digitos")

# string = "esto es una cadena de texto.\nPero con salto de linea"
# print(string)


#   ____________________
#   LISTA == ARRAY EN JS

# lista_o_array = ["Federico", "Moretto", "Genio", 28, True]
# lista_nueva = ["Mery", "Diosa"]
# union = lista_o_array + lista_nueva
# print(lista_o_array)
# print(lista_o_array[2])
# print(lista_o_array[0])
# print(union)
# lista_o_array = lista_o_array + ["San Lorenzo"]
# print(lista_o_array)
# lista_o_array[2] = "Escrupulante"
# print(lista_o_array)
# del lista_o_array[4]
# print(lista_o_array)
# lista_op = ["Federico", "Moretto", "Genio",["San Lorenzo", "Capo"], 28, True]
# print(lista_op)
# print(lista_op[1])
# print(lista_op[3])

#   ______
#   TUPLAS

# primer_tupla = ("Federico", "Moretto", 28)

# print(primer_tupla)
# print(primer_tupla[2])

#   _______________________________
#   DICCIONARIOS como Objetos en JS

# meses_traducidos = {
#     "Enero": "January",
#     "Febrero": "Febraury",
#     "Marzo": "March",
#     "Abril": "April",
#     "Mayo": "May",
#     "Junio": "June",
#     "Julio": "July",
#     "Agosto": "August",
#     "Septiembre": "September",
#     "Octubre": "October",
#     "Noviembre": "November",
#     "Diciembre": "December"
# }

# print(meses_traducidos)
# print(meses_traducidos["Febrero"])
# print(meses_traducidos["Agosto"])

#   _________________
#   Strings - metodos

# string = "hola fede"
# print(string.capitalize())
# print(string.upper())
# print(string.lower())
# print(len(string))
# print(string.isalnum())
# print(string.isalpha())
# print(string.isdigit())
# print(string.islower())
# print(string.isupper())
# print(string.lstrip())
# print(string.rstrip())
# print(string.strip())
# print(min(string))
# print(max(string))
# print(string.replace("fede", "Federico"))

#   ____________
#   IF/ELIF/ELSE

# numero = int(input("Ingrese un numero del 1 al 10: "))
# if numero > 10:
#     print("Usted a ingresado un numero mayor que 10")
# print(f"El numero que Ud. ingreso es: {numero}")

# string = "Fede hizo un gol hoy"
# if "fefiño" in string:
#     print("¡Palabra Encontrada!")
# else:
#     print("Sorry men, no esta esa palabra")
    
    
# string = "Fede hizo un gol hoy"
# if string.startswith("h"):
#     print("Exito")
# else:
#     print("Sorry men, no empieza con esa letra")

# numero1 = int(input("Ingrese el primer numero: "))
# numero2 = int(input("Ingrese el segundo numero: "))

# if numero1 > numero2:
#     print(f"El primer numero ({numero1}) es mayor que el segundo numero ({numero2})")
# elif numero1 == numero2:
#     print(f"Ambos numeros son iguales, son el numero {numero1}")
# else:
#     print(f"El segudno numero ({numero2}) es mayor que el primer numero ({numero1})")

#   ______
#   BUCLES

# i = 0
# while i < 10:
#     print(i)
#     i += 1

#continuar = True
# while continuar == True:
#     valor = int(input("Introduzca un numero mayor a 100: "))
#     if valor > 100:
#         continuar = False
# print("Tu hermana, digo programa acabado")

# lista1 = [1,2,3,4,5,6,7,8,9]
# lista2 = ["Federico", "Maria", "Programacion"]
# for item in lista1:
#     print(item, end=" ")


# for item in lista2:
#     print(item, end=" ")

# for item in range(10):
#     print(item, end=" ")


# for item1 in range(3):
#     for item2 in range(5):
#         print(f"item 1 = {item1}, item2 = {item2}")
        
        
# item1  = 0
# while item1 < 3:
#     for item2 in range(5):
#         print(f"item1 = {item1}, item2 = {item2}")
#     item1 += 1


# i1 = 0
# while i1 < 3:
#     i2 = 0
#     while i2 < 5:
#         print(f"item 1 = {i1}, item2 = {i2}")
#         i2 += 1
#     i1 += 1


#   _________
#   FUNCIONES

# def Saludar():
#     print("Hola pipol")
# Saludar()

# def Mayor_que_cero(num):
#     if num > 0:
#         print("El numero es mayor que 0")
#     elif num == 0:
#         print("El numero es igual a 0")
#     else:
#         print("El numero es menor que 0")
# Mayor_que_cero(10)
# Mayor_que_cero(0)
# Mayor_que_cero(-3)

# def Sumar(num1,num2):
#     return num1 + num2
# num1 = int(input("Ingrese el primero numero: "))
# num2 = int(input("Ingrese el segundo numero: "))
# resultado = Sumar(num1,num2)
# print(resultado)

# def SumarRestar(num1,num2):
#     return num1 + num2, num1 - num2

# num1 = int(input("Ingrese el primero numero: "))
# num2 = int(input("Ingrese el segundo numero: "))
# resultado_suma, resultado_resta = SumarRestar(num1,num2)
# print(resultado_suma)
# print(resultado_resta)

# def Sumatoria(*valores):
#     total = 0
#     for valor in valores:
#         total += valor
#     return total

# resultado = Sumatoria(10,10,10,10,10)
# print(resultado)

# def SumarRestar(num1,num2):
#     return Sumar(num1,num2), Restar(num1,num2)

# def Sumar(num1,num2):
#     return num1 + num2
# def Restar(num1,num2):
#     return num1 - num2
# num1 = int(input("Ingrese el primero numero: "))
# num2 = int(input("Ingrese el segundo numero: "))
# resultado_suma, resultado_resta = SumarRestar(num1,num2)
# print(resultado_suma)
# print(resultado_resta)


#   ________________________________
#   PROGRAMACION ORIENTADA A OBJETOS

# class Punto:
#     def __init__(self,x,y):
#         self.X = x
#         self.Y = y
#     def Mostrar_punto(self):
#         print("El punto es (",self.X,",",self.Y,")")
        
# p1 = Punto(4,6)
# p2 = Punto(5,8)
# p3 = Punto(10,12)
# p4 = Punto(9,2)
# p1.Mostrar_punto()
# p2.Mostrar_punto()
# p3.Mostrar_punto()
# p4.Mostrar_punto()
    
# p4.X = 1
# p4.Mostrar_punto()

# p3 = Punto(10,12)
# p3.Mostrar_punto()
# p4 = Punto(9,2)
# p4.Mostrar_punto()
# p3 = p4
# p3.Mostrar_punto()

class Punto:
    def __init__(self,x,y):
        self.X = x
        self.Y = y
    def Mostrar_punto(self):
        print("El punto es (",self.X,",",self.Y,")")
        
        
class Triangulo:
    def __init__(self, v1,v2,v3):
        self.V1 = v1
        self.V2 = v2
        self.V3 = v3
    def Mostrar_vertices(self):
        self.V1.Mostrar_punto()
        self.V2.Mostrar_punto()
        self.V3.Mostrar_punto()
        
v1 = Punto(3,4)
v2 = Punto(6,8)
v3 = Punto(9,2)
triangulo = Triangulo(v1,v2,v3)
triangulo.Mostrar_vertices()
