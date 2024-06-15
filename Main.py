
#Clase Proyecto

class Proyecto:

    lista_proyectos = []
    
    #Propiedades del proyecto
    def __init__(self, id, nombre, descripcion, fechaInicio, fechaVencimiento, estadoActual, empresa, gerente, equipo):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fechaInicio = fechaInicio
        self.fechaVencimiento = fechaVencimiento
        self.estadoActual = estadoActual
        self.empresa = empresa 
        self.gerente = gerente
        self.equipo = equipo
        Proyecto.lista_proyectos.append([self.id, self.nombre, self.descripcion, self.fechaInicio, self.fechaVencimiento, self.estadoActual, self.empresa, self.gerente, self.equipo])

    def consultar():
        return Proyecto.lista_proyectos


print("Gestion de Proyectos y tareas\n1-crear\n2-modificar\n3-consultar\n4-eliminar\n5-listar\n6-Salir")

opcion = int(input("Ingrese una opcion: "))
contador = 0



while opcion < 6:

    if opcion == 1:
        #Tomando las variables para crear el nuevo proyecto

        id = contador
        nombre = str(input("Ingrese el nombre del proyecto: "))
        descripcion = str(input("Ingrese la descripcion del proyecto: "))
        fechaInicio = str(input("Ingrese la fecha de inicio del proyecto: "))
        fechaVencimiento = str(input("Ingrese la fecha de vencimiento del proyecto: "))
        estadoActual = str(input("Ingrese el estado actual del proyecto: "))
        empresa = str(input("Ingrese la empresa del proyecto: "))
        gerente = str(input("Ingrese el gerente del proyecto: "))
        equipo = str(input("Ingrese el equipo del proyecto: "))

        #Creando el nuevo objeto Proyecto
        nuevoProyecto = Proyecto(id, nombre, descripcion, fechaInicio, fechaVencimiento, estadoActual, empresa, gerente, equipo)
        print("Su Proyecto ha sido creado Exitosamente")

        contador += 1

    elif opcion == 2:
        result = Proyecto.consultar()
        print(result)

    opcion = int(input("Ingrese una opcion: "))

