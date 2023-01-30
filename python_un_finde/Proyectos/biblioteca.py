class Autor:
    def __init__(self, nombre, apellido):
        self.Nombre = nombre
        self.Apellido = apellido
    def Mostrar_autor(self):
        print(f"Autor: {self.Nombre} {self.Apellido}")
        
        
class Libro:
    def __init__(self, titulo,isbn):
        self.Titulo = titulo
        self.isbn = isbn
    def Añadir_autor(self,autor):
        self.Autor = autor
    def Mostrar_libro(self):
        print("-----Libro-----")
        print(f"Titulo: {self.Titulo}")
        print(f"ISBN: {self.isbn}")
        self.Autor.Mostrar_autor()
        print("---------------")
    def Obtener_titulo(self):
        return self.Titulo
  
    
class Biblioteca:
    def __init__(self):
        self.Lista_libros = []
    def Numero_libros(self):
        return len(self.Lista_libros)
    def Añadir_libro(self, libro):
        self.Lista_libros = self.Lista_libros + [libro]
    def Borrar_libro(self, titulo):
        encontrado = False
        posicion_a_borrar = -1
        for item in self.Lista_libros:
            posicion_a_borrar += 1
            if item.Obtener_titulo() == titulo:
                encontrado = True
                break
        if encontrado:
            del self.Lista_libros[posicion_a_borrar]
            print("Libro borrado correctamente")
        else:
            print("Libro no encontrado")
    def Mostrar_Biblioteca(self):
        print("##############################")
        for item in self.Lista_libros:
            item.Mostrar_libro()
        print("##############################")
        
        
def Mostrar_Menu():
    print("")
    print("")
    print("----------MENU DE LA BIBLIOTECA----------")
    print("1) Añadir Libro a la Biblioteca") 
    print("2) Mostrar la Biblioteca")
    print("3) Borrar libro de la Biblioteca")
    print("4) Mostrar el numero de libros que componen la Biblioteca")
    print("5) Salir")
    print("-----------------------------------------")
    print("")
    print("")          
    
    
def Añadir_libro_a_biblioteca(biblioteca):
    titulo = input("Introduzca el titulo del libro: ")
    isbn = input("Introduzca el ISBN del libro: ")
    autor_nombre = input("Introduzca el nombre del autor: ")
    autor_apellido = input("Introduzca el apellido del autor: ")
    autor = Autor(autor_nombre, autor_apellido)
    libro = Libro(titulo, isbn)
    libro.Añadir_autor(autor)
    biblioteca.Añadir_libro(libro)
    return biblioteca

def Mostrar_biblioteca(biblioteca):
    biblioteca.Mostrar_Biblioteca()

def Borrar_libro(bibilioteca):
    titulo = input("Ingrese el libro a borrar: ")
    bibilioteca.Borrar_libro(titulo)
    
def Numero_libros(bibilioteca):
    print(f"El numero de libros en la biblioteca es: {bibilioteca.Numero_libros()}")
    
fin = False
biblioteca = Biblioteca()

while not fin:
    Mostrar_Menu()
    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        biblioteca = Añadir_libro_a_biblioteca(biblioteca)
    elif opcion == "2":
        Mostrar_biblioteca(biblioteca)
    elif opcion == "3":
        Borrar_libro(biblioteca)
    elif opcion == "4":
        Numero_libros(biblioteca)
    elif opcion == "5":
        print("Saliendo, Gracias")
        fin = True
    else:
        print("Opcion incorrecta, ingrese nuevamente")