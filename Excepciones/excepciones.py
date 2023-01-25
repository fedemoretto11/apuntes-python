#Creando funcion que suma numeros
def suma():
    # Creando un bucle
    while True:
        #Pidiendo numeros
        a = input("Diga el numero 1: ")
        b = input("Diga el numero 2: ")
        # intentdo converir a enteros y sumarlos
        try: 
            resultado = int(a) + int(b)
        # Si lanzo excepcion pedir datos denuevo
        except Exception as e:
            print("Te pedi un numero gato de la gorra")
            print(f"El error fue {e}")
        # si todo salio bien termina bucle
        else:
            break
        finally:
            print("Manejo de excepciones finalizado, rara vez utilizada")
    # Mostrando el resultado    
    return resultado

print(suma())