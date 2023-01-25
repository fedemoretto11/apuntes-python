def saludar(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adj = "doña"
    elif (sexo == 'hombre'):
        adj = 'don'
    else:
        adj = 'love'    
    print(f"Hola {adj} {nombre} , todo bien??")
    
    
saludar('Federico', 'hombre')
saludar("Mery", "mujER")
print("---------------")


def crear_contraseña_random(num):
    chars = "abcdefghij"
    numero_string = str(num)
    num = int(numero_string[0])
    c1 = num - 2
    c2 = num
    c3 = num - 4
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*5}"
    return contraseña,num


password, numero = crear_contraseña_random(143) # Se agregaron retornos multiples

frase = f"tu nueva contraseña es: {password}"
frase2 = f"tu primer numero fue: {numero}"

print(frase)
print(frase2)
print("---------------")
    
    
