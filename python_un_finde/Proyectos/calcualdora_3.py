def Solicitar_numero(texto):
    leido = False
    while not leido:
        try:
            numero = int(input(texto))
        except ValueError:
            print("Error, tenes que ingresar un numero")
        else:
            leido = True
    return numero


def Sumar():
        num1 = Solicitar_numero("Ingrese el primer numero para sumar: ")
        num2 = Solicitar_numero("Ingrese el segundo numero numero para sumar: ")
        print(f"La suma es: {num1 + num2}")
        
def Restar():
        num1 = Solicitar_numero("Ingrese el primer numero para restar: ")
        num2 = Solicitar_numero("Ingrese el segundo numero numero para restar: ")
        print(f"La resta es: {num1 - num2}")
        
def Multiplicar():
        num1 = Solicitar_numero("Ingrese el primer numero para multiplicar: ")
        num2 = Solicitar_numero("Ingrese el segundo numero numero para multiplicar: ")
        print(f"La multiplicacion es: {num1 * num2}")
        
def Dividir():
        num1 = Solicitar_numero("Ingrese el numero para dividir: ")
        num2 = Solicitar_numero("Ingrese el divisor: ")
        try:
            resultado = num1 / num2
        except ZeroDivisionError:
            print("ERROR Bobolon, el divisor no puede ser 0")
        else:
            print(f"El resultado de la division es {resultado}")
            
            
def Mostrar_menu():
    print("*****CALCULATOR*****")
    print("")
    print("MENU")
    print("\t1) Suma\n \t2) Resta\n \t3) Multiplicacion\n \t4) Division\n \t5) Menu\n \t6) Salir\n")
    print("")
    print("********************")
    
def Saludo_salida():
        print("")
        print("********************")
        print("")
        print("Gracias por usar CALCULATOR")
        print("")
        print("********************")    
    
    
        
def Calculador():
    fin = False
    Mostrar_menu()
    while not(fin):
        option = input("Ingrese una opcion numerica: ")
        if option == "1":
            Sumar()
        elif option == "2":
            Restar()
        elif option == "3":
            Multiplicar()
        elif option == "4":
            Dividir()
        elif option == "5":
            Mostrar_menu()
        elif option == "6":
            Saludo_salida()
            fin = True            
        else:
            print("Ingrese una opcion correcta")   
                       
            
Calculador()