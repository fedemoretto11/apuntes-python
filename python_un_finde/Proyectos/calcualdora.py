fin = False
print("*****CALCULATOR*****")
print("Menu: 1) Suma 2) Resta 3) Multiplicacion 4) Division 5) Salir")
while not(fin):
    option = input("Ingrese una opcion numerica: ")
    if option == "1":
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        print("La suma es: ", num1 + num2)
    elif option == "2":
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        print("La resta es: ", num1 - num2)
    elif option == "3":
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        print("La multiplicacion es: ", num1 * num2)
    elif option == "4":
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        print("La division es: ", num1 / num2)
    elif option == "5":
        print("Gracias por usar CALCULATOR")
        fin = True
    else:
        print("Ingrese una opcion correcta")              