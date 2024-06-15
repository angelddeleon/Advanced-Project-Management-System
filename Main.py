
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

    #Devuelve la lista de los proyectos a hacer
    def consultar():
        return Proyecto.lista_proyectos

    #Elimina el proyecto deseado por su id
    def eliminarId(id):

            listaProyectos = Proyecto.lista_proyectos
            listaNueva = []

            for x in listaProyectos:
                if x[0] == id:
                    continue
                
                listaNueva += [x]

            Proyecto.lista_proyectos = listaNueva

    #Eliminar un proyecto por su nombre
    


print("Gestion de Proyectos y tareas\n1-crear\n2-modificar\n3-consultar\n4-eliminar\n5-listar\n6-Salir")


contador = 0
opcion = int(input("Ingrese una opcion: "))


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

        elif opcion == 3:
            result = Proyecto.consultar()
            print(result)

            print("Cual Proyecto desea Eliminar (Por id): ")

            proyectoId = int(input("Proyecto a eliminar"))



            Proyecto.eliminarId(proyectoId)



        opcion = int(input("Ingrese una opcion: "))


