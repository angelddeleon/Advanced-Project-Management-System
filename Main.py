
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

    #Modificar algun proyecto

    def modificarId(id):
            listaProyectos = Proyecto.lista_proyectos
            listaNueva = []

            #Recorre la lista de proyectos y sale un menu del cual debe de seleccionar lo que se quiere cambiar

            for x in listaProyectos:
                if x[0] == id:
                    print("Que desea modificar\n1-nombre\n2-descripcion\n3-fechaInicio\n4-fechaVencimiento\n5-estadoActual\n6-empresa\n7-gerente\n8-equipo\n9-Todos")

                    modificarOpcion = int(input("Marque su opcion: "))

                    if modificarOpcion == 1:
                        nombreModificado = str(input("Nuevo Nombre: "))
                        x[1] = nombreModificado

                    elif modificarOpcion == 2:
                        descripcionModificado = str(input("Nueva Descripcion: "))
                        x[2] = descripcionModificado

                    elif modificarOpcion == 3:
                        fechaInicioModificado = str(input("Nueva Fecha Inicio: "))
                        x[3] = fechaInicioModificado

                    elif modificarOpcion == 4:
                        fechaVencimientoModificado = str(input("Nuevo Nombre: "))
                        x[4] = fechaVencimientoModificado

                    elif modificarOpcion == 5:
                        estadoActualModificado = str(input("Nuevo Nombre: "))
                        x[5] = estadoActualModificado
                    
                    elif modificarOpcion == 6:
                        empresaModificado = str(input("Nuevo Nombre: "))
                        x[6] = empresaModificado
                    
                    elif modificarOpcion == 7:
                        gerenteModificado = str(input("Nuevo Nombre: "))
                        x[7] = gerenteModificado

                    elif modificarOpcion == 8:
                        equipoModificado = str(input("Nuevo Nombre: "))
                        x[8] = equipoModificado
                    
                    elif modificarOpcion == 9:
                        nombreModificado = str(input("Nuevo Nombre: "))
                        x[1] = nombreModificado
                        descripcionModificado = str(input("Nueva Descripcion: "))
                        x[2] = descripcionModificado
                        fechaInicioModificado = str(input("Nueva Fecha Inicio: "))
                        x[3] = fechaInicioModificado
                        fechaVencimientoModificado = str(input("Nuevo Nombre: "))
                        x[4] = fechaVencimientoModificado
                        estadoActualModificado = str(input("Nuevo Nombre: "))
                        x[5] = estadoActualModificado
                        empresaModificado = str(input("Nuevo Nombre: "))
                        x[6] = empresaModificado
                        gerenteModificado = str(input("Nuevo Nombre: "))
                        x[7] = gerenteModificado
                        equipoModificado = str(input("Nuevo Nombre: "))
                        x[8] = equipoModificado

                    else:
                        print("Ingrese una opcion valida")
                        
                
                listaNueva += [x]

            Proyecto.lista_proyectos = listaNueva
    


print("Gestion de Proyectos y tareas\n1-crear\n2-modificar\n3-consultar\n4-eliminar\n5-Salir")


contador = 1
opcion = int(input("Ingrese una opcion: "))


while opcion < 5:

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

            print("Que proyecto desea modificar(por id): ")

            proyectoId = int(input("Proyecto a modificar"))

            Proyecto.modificarId(proyectoId)

            print("Su proyecto ha sido Modificado")

        elif opcion == 3:
            result = Proyecto.consultar()
            print(result)

        elif opcion == 4:
            result = Proyecto.consultar()
            print(result)

            print("Cual Proyecto desea Eliminar (Por id): ")

            proyectoId = int(input("Proyecto a eliminar: "))



            Proyecto.eliminarId(proyectoId)

            



        opcion = int(input("Ingrese una opcion: "))


