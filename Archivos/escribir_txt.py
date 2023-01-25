with open("Archivos\\texto.txt","w", encoding="UTF-8") as archivo: #la "w" sobreesxcribe la "a" agrega
    #archivo.write("La tenes adentro") #Esto sirve para sobreescribirt el archivo
    archivo.writelines(["Hola pepito, todo bien??\n","Bien y vos??"]) #Tambien sobreescribe pero las lineas que le paso
    