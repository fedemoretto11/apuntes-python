def Sumar():
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        resultado = num1 + num2
        print(f"La suma es: {resultado}")
        
def Restar():
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        resultado = num1 - num2
        print(f"La resta es: {resultado}")
        
def Multiplicar():
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        resultado = num1 * num2
        print(f"La multiplicacion es: {resultado}")
        
def Dividir():
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        resultado = num1 / num2
        print(f"La division es: {resultado}")
        
def Calculador():
    fin = False
    print("*****CALCULATOR*****")
    print("Menu: 1) Suma 2) Resta 3) Multiplicacion 4) Division 5) Salir")
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
            print("Gracias por usar CALCULATOR")
            fin = True
        else:
            print("Ingrese una opcion correcta")   
                       
            
Calculador()