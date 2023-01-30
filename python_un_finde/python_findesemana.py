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

# class Punto:
#     def __init__(self,x,y):
#         self.X = x
#         self.Y = y
#     def Mostrar_punto(self):
#         print("El punto es (",self.X,",",self.Y,")")
        
        
# class Triangulo:
#     def __init__(self, v1,v2,v3):
#         self.V1 = v1
#         self.V2 = v2
#         self.V3 = v3
#     def Mostrar_vertices(self):
#         self.V1.Mostrar_punto()
#         self.V2.Mostrar_punto()
#         self.V3.Mostrar_punto()
        
# v1 = Punto(3,4)
# v2 = Punto(6,8)
# v3 = Punto(9,2)
# triangulo = Triangulo(v1,v2,v3)
# triangulo.Mostrar_vertices()


#   _________________________________________
#   PROGRAMACION ORIENTADA A OBJETOS AVANZADA

# class Punto_publico:
#     def __init__(self, x, y):
#         self.X = x
#         self.Y = y
    
# class Punto_privado:
#     def __init__(self, x, y):
#         self.__X = x
#         self.__Y = y
#     def Get_x(self):
#         return self.__X
#     def Get_y(self):
#         return self.__Y
#     def Set_x(self,x):
#         self.__X = x
#     def Set_y(self, y):
#         self.__Y = y
        
        
# publico = Punto_publico(4,6)
# privado = Punto_privado(7,3)
# print(f"Valores punto publico: {publico.X}, {publico.Y}")
# print(f"Valores punto privado: {privado.Get_x()}, {privado.Get_y()}")
# publico.X = 8
# privado.Set_x(9)
# print(f"Valores punto publico: {publico.X}, {publico.Y}")
# print(f"Valores punto privado: {privado.Get_x()}, {privado.Get_y()}")


# class Operar_valores:
#     def __init__(self, num1, num2):
#         self.__num1 = num1
#         self.__num2 = num2
#     def __Sumar(self):
#         return self.__num1 + self.__num2
#     def __Restar(self):
#         return self.__num1 - self.__num2
#     def Operar(self):
#         print(f"El resultado de la suma es {self.__Sumar()}")
#         print(f"El resultado de la resta es {self.__Restar()}")
        
        
# operar_valores = Operar_valores(10,5)
# operar_valores.Operar()
# print(f"El resultado de la suma es {operar_valores.__Sumar()}") # Sale el error por intentar acceder a metodos privados


# ________
# HERENCIA

# class Electrodomestico:
#     def __init__(self):
#         self.__Encendido = False
#         self.__Tension = 0
#     def Encender(self):
#         self.__Encendido = True
#     def Apagar(self):
#         self.__Encendido = False
#     def Encendido(self):
#         return self.__Encendido
#     def Set_tension(self, tension):
#         self.__Tension = tension
#     def Get_tension(self):
#         return self.__Tension
    
# class Lavadora(Electrodomestico):
#     def __init__(self):
#         self.__RPM = 0
#         self.__Kilos = 0
#     def Set_RPM(self, rpm):
#         self.__RPM = rpm
#     def Set_kilos(self, kgs):
#         self.__Kilos = kgs
#     def Mostrar_lavadora(self):
#         print("")
#         print("**********")
#         print("Lavadora:")
#         print(f"\tRPM: {self.__RPM}")
#         print(f"\tKilos: {self.__Kilos}")
#         print(f"\tTension: {self.Get_tension()}")
#         if self.Encendido():
#             print("\tLavadora Encendida")
#         else:
#             print("\tLavadora Apagada")
#         print("**********")
#         print("")
        
# class Microondas(Electrodomestico):
#     def __init__(self):
#         self.__Max_power = 0
#         self.__Grill = False
#     def Set_max_power(self, power):
#         self.__Max_power = power
#     def Set_grill(self, grill):
#         self.__Grill = grill
#     def Mostrar_microondas(self):
#         print("")
#         print("**********")
#         print("Microondas:")
#         print(f"\tPotencia Maxima: {self.__Max_power}")
#         if self.__Grill == True:
#             print(f"\tGrill: Si")
#         else:
#             print(f"\tGrill: No")
#         print(f"\tTension: {self.Get_tension()}")
#         if self.Encendido():
#             print("\tMicroondas Encendido")
#         else:
#             print("\tMicroondas Apagado")
#         print("**********")
#         print("")       
        
# lavadora = Lavadora()
# lavadora.Set_RPM(1200)
# lavadora.Set_kilos(12)
# lavadora.Set_tension(220)
# lavadora.Encender()

# microondas = Microondas()
# microondas.Set_max_power(0)
# microondas.Set_grill(True)
# microondas.Set_tension(220)
# microondas.Encender()

# lavadora.Mostrar_lavadora()
# microondas.Mostrar_microondas()
# lavadora.Apagar()
# lavadora.Mostrar_lavadora()
# microondas.Apagar()
# microondas.Mostrar_microondas()


# _________________
# HERENCIA MULTIPLE

# class Hotel():
#     def __init__(self):
#         self.__Rooms = 0
#         self.__Stars = 0
#     def Set_rooms(self, rooms):
#         self.__Rooms = rooms
#     def Set_Stars(self, stars):
#         self.__Stars = stars
#     def Mostrar_hotel(self):
#         print("---------------")
#         print("Hotel:")
#         print(f"Estrellas: {self.__Stars}")
#         print(f"Habitaciones: {self.__Rooms}")
#         print("---------------")
        
# class Restaurant():
#     def __init__(self):
#         self.__Tenedores = 0
#         self.__Apertura = 0
#     def Set_tenedores(self, tenedores):
#         self.__Tenedores = tenedores
#     def Set_Apertura(self,apertura):
#         self.__Apertura = apertura
#     def Mostrar_restaurant(self):
#         print("---------------")
#         print("Restaurant:")
#         print(f"Tenedores: {self.__Tenedores}")
#         print(f"Horario de apertura: {self.__Apertura}")
#         print("---------------")        
        
# class Negocio(Hotel, Restaurant):
#     def __init__(self):
#         self.__Nombre = ""
#         self.__Direccion = ""
#         self.__Telefono = ()
#     def Set_nombre(self, nombre):
#         self.__Nombre = nombre
#     def Set_direccion(self, direccion):
#         self.__Direccion = direccion
#     def Set_telefono(self, telefono):
#         self.__Telefono = telefono
#     def Mostrar_negocio(self):
#         print("*********************")
#         print("Negocio:")
#         print(f"Nombre: {self.__Nombre}")
#         print(f"Direccion: {self.__Direccion}")
#         print(f"Telefono: {self.__Telefono}")
#         self.Mostrar_hotel()
#         self.Mostrar_restaurant()
#         print("*********************")    
    
    
# negocio = Negocio()
# negocio.Set_Stars(4)
# negocio.Set_rooms(26)
# negocio.Set_tenedores(52)
# negocio.Set_Apertura(20)
# negocio.Set_nombre("El Palacete Feliz")
# negocio.Set_direccion("Avenida Hapinnes 69")
# negocio.Set_telefono("00224-2723-2934")
# negocio.Mostrar_negocio()


#   ________
#   FICHEROS

# archivo = open("python_un_finde\\prueba.txt","r", encoding="UTF-8")
# texto = archivo.read()
# print(texto)
# archivo.close()

# for linea in open("python_un_finde\\prueba.txt","r", encoding="UTF-8"):
#     print(linea)
 
    
# flectura = open("python_un_finde\\prueba.txt","r", encoding="UTF-8")
# texto = flectura.read()
# print("*****Texto original*****")
# print(texto)
# print("")
# flectura.close()

# f_escritura = open("python_un_finde\\prueba.txt","a", encoding="UTF-8")   
# f_escritura.write("Argentina campeon del mundo\n")
# f_escritura.close()
# print("*****Texto modificado*****")
# flectura = open("python_un_finde\\prueba.txt","r", encoding="UTF-8")
# texto = flectura.read()
# print(texto)
# print("")
# flectura.close()

# fcrear = open("creando_un_fichero.txt", "x")
# fcrear.write("Hola papa\n")
# fcrear.write("A ver si sale bien esto")
# fcrear.close()

# flectura = open("python_un_finde\\creando_un_fichero.txt","r", encoding="UTF-8")
# texto = flectura.read()
# print(texto)
# flectura.close()


# f_reescribir = open("python_un_finde\\creando_un_fichero.txt","w", encoding="UTF-8")
# f_reescribir.write("Esta linea deberia ser nueva\n")
# f_reescribir.write("Lo mismo que esta\n")
# f_reescribir.close()
# f_leer = open("python_un_finde\\creando_un_fichero.txt","r", encoding="UTF-8")
# texto = f_leer.read()
# print(texto)
# f_leer.close()


#   ___________
#   EXCEPCIONES

# try:
#     print(3/0)
# except ZeroDivisionError:
#     print("Error, NO SE PUEDE DIVIDIR POR CERO, SALAME")
# except:
#     print("La estas pifiando pa")
# else:
#     print("Bien papa, no son tan pajero como el de arriba")
# finally:
#     print("Programa terminado, bobolon")