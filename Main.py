
from datetime import datetime
from collections import deque
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


class Tarea:
    def __init__(self, id, nombre, empresa_cliente, descripcion, fecha_inicio, fecha_vencimiento, estado_actual, porcentaje):
        self.id = id
        self.nombre = nombre
        self.empresa_cliente = empresa_cliente
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_vencimiento = fecha_vencimiento
        self.estado_actual = estado_actual
        self.porcentaje = porcentaje
        self.tareas = []
        self.subtareas = []
        self.pila_prioridades = []
        self.cola_vencimientos = deque()

    def agregar_subtarea(self, subtarea):
        self.subtareas.append(subtarea)

    def agregar_tarea(self, tarea, posicion=None):
        if posicion is None:
            self.tareas.append(tarea)
        else:
            self.tareas.insert(posicion, tarea)

    def eliminar_tarea(self, id):
        self.subtareas = [tarea for tarea in self.subtareas if tarea.id != id]

    def buscar_tarea(self, criterio):
        return [tarea for tarea in self.subtareas if criterio(tarea)]

    def actualizar_tarea(self, id, **kwargs):
        for tarea in self.subtareas:
            if tarea.id == id:
                for key, value in kwargs.items():
                    setattr(tarea, key, value)
                break

    # Métodos para la pila de tareas prioritarias
    def agregar_prioridad(self, tarea):
        self.pila_prioridades.append(tarea)

    def eliminar_prioridad(self):
        if self.pila_prioridades:
            return self.pila_prioridades.pop()


    def consultar_prioridad(self):
        return self.pila_prioridades[-1]

    # Métodos para la cola de vencimientos
    def agregar_vencimiento(self, tarea):
        self.cola_vencimientos.append(tarea)

    def eliminar_vencimiento(self):
        return self.cola_vencimientos.popleft()

    def consultar_proxima_vencer(self):
        return self.cola_vencimientos[0]

def menu():
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Buscar tarea")
    print("4. Actualizar tarea")
    print("5. Agregar prioridad")
    print("6. Eliminar prioridad")
    print("7. Consultar prioridad")
    print("8. Agregar vencimiento")
    print("9. Eliminar vencimiento")
    print("10. Consultar próxima a vencer")
    print("11. Salir")

def main():
    tarea_principal = Tarea(0, "Proyecto Principal", "Empresa X", "Descripción del proyecto", datetime.now(), datetime.now(), "En progreso", 0)
    
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            id = input("Ingrese el ID de la tarea: ")
            nombre = input("Ingrese el nombre de la tarea: ")
            empresa_cliente = input("Ingrese la empresa cliente: ")
            descripcion = input("Ingrese la descripción de la tarea: ")
            fecha_inicio = datetime.strptime(input("Ingrese la fecha de inicio (dd/mm/yyyy): "), "%d/%m/%Y")
            fecha_vencimiento = datetime.strptime(input("Ingrese la fecha de vencimiento (dd/mm/yyyy): "), "%d/%m/%Y")
            estado_actual = input("Ingrese el estado actual de la tarea: ")
            porcentaje = float(input("Ingrese el porcentaje completado: "))
            
            nueva_tarea = Tarea(id, nombre, empresa_cliente, descripcion, fecha_inicio, fecha_vencimiento, estado_actual, porcentaje)
            tarea_principal.agregar_tarea(nueva_tarea)
            print("Tarea agregada exitosamente.")
            
        elif opcion == '2':
            id = input("Ingrese el ID de la tarea a eliminar: ")
            tarea_principal.eliminar_tarea(id)
            print("Tarea eliminada exitosamente.")
            
        elif opcion == '3':
            nombre = input("Ingrese el nombre de la tarea a buscar: ")
            tareas_encontradas = tarea_principal.buscar_tarea(lambda x: x.nombre == nombre)
            for t in tareas_encontradas:
                print(f"Tarea encontrada: {t.nombre}")
                
        elif opcion == '4':
            id = input("Ingrese el ID de la tarea a actualizar: ")
            estado_actual = input("Ingrese el nuevo estado actual de la tarea: ")
            porcentaje = float(input("Ingrese el nuevo porcentaje completado: "))
            
            tarea_principal.actualizar_tarea(id, estado_actual=estado_actual, porcentaje=porcentaje)
            print("Tarea actualizada exitosamente.")
            
        elif opcion == '5':
            id = input("Ingrese el ID de la tarea prioritaria a agregar: ")
            tarea_prioritaria = next((t for t in tarea_principal.subtareas if t.id == id), None)
            
            if tarea_prioritaria:
                tarea_principal.agregar_prioridad(tarea_prioritaria)
                print("Tarea prioritaria agregada exitosamente.")
                
        elif opcion == '6':
            tarea_eliminada = tarea_principal.eliminar_prioridad()
            if tarea_eliminada:
                print(f"Tarea prioritaria eliminada: {tarea_eliminada.nombre}")
            else:
                print("No hay tareas prioritarias para eliminar.")

            
        elif opcion == '7':
            tarea_prioritaria = tarea_principal.consultar_prioridad()
            print(f"Tarea prioritaria actual: {tarea_prioritaria.nombre}")
            
        elif opcion == '8':
            id = input("Ingrese el ID de la tarea próxima a vencer a agregar: ")
            tarea_proxima_vencer = next((t for t in tarea_principal.subtareas if t.id == id), None)
            
            if tarea_proxima_vencer:
                tarea_principal.agregar_vencimiento(tarea_proxima_vencer)
                print("Tarea próxima a vencer agregada exitosamente.")
                
        elif opcion == '9':
            tarea_eliminada = tarea_principal.eliminar_vencimiento()
            print(f"Tarea próxima a vencer eliminada: {tarea_eliminada.nombre}")
            
        elif opcion == '10':
            tarea_proxima_vencer = tarea_principal.consultar_proxima_vencer()
            print(f"Tarea próxima a vencer actual: {tarea_proxima_vencer.nombre}")
            
        elif opcion == '11':
            break

if __name__ == "__main__":
    main()
    
    
