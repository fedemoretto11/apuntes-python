class Direccion():
    def __init__(self):
        self.__Calle = ""
        self.__Piso = ""
        self.__Ciudad = ""
        self.__Codigo_postal = ""
    def Get_calle(self):
        return self.__Calle
    def Get_piso(self):
        return self.__Piso   
    def Get_ciudad(self):
        return self.__Ciudad   
    def Get_codigo_postal(self):
        return self.__Codigo_postal
    def Set_calle(self,calle):
        self.__Calle = calle
    def Set_piso(self,piso):
        self.__Piso = piso
    def Set_ciudad(self,ciudad):
        self.__Ciudad = ciudad
    def Set_codigo_postal(self,codigo_postal):
        self.__Codigo_postal = codigo_postal
        
class Persona():
    def __init__(self):
        self.__Nombre = ""
        self.__Apellido = ""
        self.__Nacimiento = ""
    def Get_nombre(self):
        return self.__Nombre
    def Get_apellido(self):
        return self.__Apellido
    def Get_nacimiento(self):
        return self.__Nacimiento
    def Set_nombre(self, nombre):
        self.__Nombre = nombre
    def Set_apellido(self, apellido):
        self.__Apellido = apellido
    def Set_nacimiento(self, Nacimiento):
        self.__Nacimiento = Nacimiento
    
class Telefono():
    def __init__(self):
        self.__Fijo = ""
        self.__Movil = ""
        self.__Trabajo = ""
    def Get_fijo(self):
        return self.__Fijo
    def Get_movil(self):
        return self.__Movil
    def Get_trabajo(self):
        return self.__Trabajo
    def Set_fijo(self,fijo):
        self.__Fijo = fijo
    def Set_movil(self,movil):
        self.__Movil = movil
    def Set_trabajo(self,trabajo):
        self.__Trabajo = trabajo
    
class Contacto(Direccion, Persona, Telefono):
    def __init__(self):
        self.__Email = ""
    def Get_email(self):
        return self.__Email
    def Set_email(self, email):
        self.__Email = email
    def Mostrar_contacto(self):
        print("----------Contacto----------")
        print(f"Nombre: {self.Get_nombre()}")
        print(f"Apellido: {self.Get_apellido()}")
        print(f"Fecha de Nacimiento: {self.Get_nacimiento()}")
        print(f"Direccion: {self.Get_calle()} {self.Get_piso()}")
        print(f"Ciuad: {self.Get_ciudad()} // C.P.: {self.Get_codigo_postal()}")
        print(f"Telefono fijo: {self.Get_fijo()}")
        print(f"Telefono Movil: {self.Get_movil()}")
        print(f"Telefono Laboral: {self.Get_trabajo()}")
        print(f"Email: {self.__Email}")
        print("----------------------------")
        

class Agenda():
    def __init__(self, path):
        self.__Lista_Contactos = []
        self.__Path = path
    def Cargar_contactos(self):
        try:
            fichero = open(self.__Path, "r")
        except:
            print("ERROR, el archivo solicitado no exite, pete")
        else:
            contactos = fichero.readlines()
            fichero.close()
            if (len(contactos)>0):
                for contacto in contactos:
                    datos = contacto.split("#")
                    if (len(datos)==11):
                        nuevo_contacto = Contacto()
                        nuevo_contacto.Set_nombre(datos[0])
                        nuevo_contacto.Set_apellido(datos[1])
                        nuevo_contacto.Set_nacimiento(datos[2])
                        nuevo_contacto.Set_movil(datos[3])
                        nuevo_contacto.Set_fijo(datos[4])
                        nuevo_contacto.Set_trabajo(datos[5])
                        nuevo_contacto.Set_calle(datos[6])
                        nuevo_contacto.Set_piso(datos[7])
                        nuevo_contacto.Set_ciudad(datos[8])
                        nuevo_contacto.Set_codigo_postal(datos[9])
                        nuevo_contacto.Set_email(datos[10])
                        self.__Lista_Contactos = self.__Lista_Contactos + [nuevo_contacto]
                print(f"Se han cargado un total de {len(self.__Lista_Contactos)} contactos")
    def Crear_nuevo_contacto(self, nuevo_contacto):
        self.__Lista_Contactos = self.__Lista_Contactos + [nuevo_contacto]
    def Guardar_contactos(self):
        try:
            fichero = open(self.__Path,"w")
        except:
            print("Error, no se puede guardar")
        else:
            for contacto in self.__Lista_Contactos:
                texto = contacto.Get_nombre() + "#"
                texto = texto + contacto.Get_apellido() + "#"
                texto = texto + contacto.Get_nacimiento() + "#"
                texto = texto + contacto.Get_movil() + "#"
                texto = texto + contacto.Get_fijo() + "#"
                texto = texto + contacto.Get_trabajo() + "#"
                texto = texto + contacto.Get_calle() + "#"
                texto = texto + contacto.Get_piso() + "#"
                texto = texto + contacto.Get_ciudad() + "#"
                texto = texto + contacto.Get_codigo_postal() + "#"
                texto = texto + contacto.Get_email() + "#"
                fichero.write(texto)
            fichero.close()
    def Mostrar_agenda(self):
        print("########## AGENDA ##########")
        print(f"Numero de contactos: {len(self.__Lista_Contactos)}")
        for contacto in self.__Lista_Contactos:
            contacto.Mostrar_contacto()
        print("############################")
    def Buscar_contacto_por_nombre(self,nombre):
        lista_encontrados = []
        for contacto in self.__Lista_Contactos:
            if contacto.Get_nombre() == nombre:
                lista_encontrados = lista_encontrados + [contacto]
        return lista_encontrados
    def Borrar_contacto_por_nombre(self,nombre):
        lista_final = []
        for contacto in self.__Lista_Contactos:
            if contacto.Get_nombre() != nombre:
                lista_final = lista_final + [contacto]
        print(f"Info: {len(self.__Lista_Contactos) - len(lista_final)} contactos han sido borrados")
        self.__Lista_Contactos = lista_final


def Obtener_opcion(texto):
    leido = False
    while not leido:
        try:
            numero = int(input(texto))
        except ValueError:
            print("ERROR. Ingrese un numero")
        else:
            leido = True
    return numero

def Mostrar_menu():
    print("*****Agenda*****")
    print("")
    print("MENU")
    print("\t1) Mostrar contactos\n \t2) Buscar contactos\n \t3) Crear nuevo contacto\n \t4) Borrar contacto\n \t5) Guardar contacto\n \t6) Salir\n")
    print("")
    print("********************")
    
def Buscar_contacto(agenda):
    print("Buscar contactos: 1) Nombre 2) Volver")
    finbuscar = False
    while not finbuscar:
        opc_buscar  = Obtener_opcion("Opcion: ")
        if opc_buscar == 1:
            encontrados = agenda.Buscar_contacto_por_nombre(input("Introduzca el nombre a buscar: "))
            if len(encontrados) > 0:
                print("Contacto encontrados")
                for item in encontrados:
                    item.Mostrar_contacto()
                print("####################")
            else:
                print("NO SE HAN ENCONTRADO CONTACTOS")
            finbuscar = True
        elif opc_buscar == 2:
            finbuscar = True
            
def Proceso_crear_contacto(agenda):
    nuevo_contacto = Contacto()
    nuevo_contacto.Set_nombre(input("Introduce el nombre del contacto: "))
    nuevo_contacto.Set_apellido(input("Introduce el apellido del contacto: "))
    nuevo_contacto.Set_nacimiento(input("Introduce la fecha de nacimiento del contacto: "))
    nuevo_contacto.Set_movil(input("Introduce telefono celular del contacto: "))
    nuevo_contacto.Set_fijo(input("Introduce telefono fijo del contacto: "))
    nuevo_contacto.Set_trabajo(input("Introduce telefono laboral del contacto: "))
    nuevo_contacto.Set_calle(input("Introduce la calle del contacto: "))
    nuevo_contacto.Set_piso(input("Introduce el numero de casa del contacto: "))
    nuevo_contacto.Set_ciudad(input("Introduce la ciudad del contacto: "))
    nuevo_contacto.Set_codigo_postal(input("Introduce el CP del contacto: "))
    nuevo_contacto.Set_email(input("Introduce el mail del contacto: "))
    agenda.Crear_nuevo_contacto(nuevo_contacto)
    
    
    
def Borrar_contacto(agenda):
    print("Buscar contactos a borrar: 1) Nombre 2) Volver")
    finbuscar = False
    while not finbuscar:
        opc_buscar  = Obtener_opcion("Opcion: ")
        if opc_buscar == 1:
            agenda.Borrar_contacto_por_nombre(input("Introduce el nombre a borrar: "))
            finbuscar = True
        elif opc_buscar == 2:
            finbuscar = True

def Main():
    agenda = Agenda("python_un_finde\\proyecto_final\\agenda.txt")
    agenda.Cargar_contactos()
    fin = False
    while not fin:
        Mostrar_menu()
        opc = Obtener_opcion("Opcion: ")
        if opc == 1:
            agenda.Mostrar_agenda()
        elif opc == 2:
            Buscar_contacto(agenda)
        elif opc == 3:
            Proceso_crear_contacto(agenda)
        elif opc == 4:
            Borrar_contacto(agenda)
        elif opc == 5:
            agenda.Guardar_contactos()
        elif opc == 6:
            print("Saliendo del sistema")
            fin = True
        else:
            print("Ingrese una opcion correcta")


Main()

