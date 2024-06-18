
from datetime import datetime
from collections import deque
from bisect import insort
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
    

print("--------------------------")
print("Modulo de Gestion de proyectos")
print("--------------------------")
print("\n1-crear\n2-modificar\n3-consultar\n4-eliminar\n5-Salir")


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
    def __init__(self, id, nombre, empresa_cliente, descripcion, fecha_inicio, fecha_vencimiento, estado_actual, porcentaje, prioridad, duracion =0):
        self.id = id
        self.nombre = nombre
        self.empresa_cliente = empresa_cliente
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_vencimiento = fecha_vencimiento
        self.estado_actual = estado_actual
        self.porcentaje = porcentaje
        self.prioridad = prioridad
        self.duracion = duracion  
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
            
    def buscar_tarea_por_nombre(self, nombre):
        tareas_encontradas = [tarea for tarea in self.tareas if tarea.nombre == nombre]
        return tareas_encontradas

    def eliminar_tarea(self, id):
        self.tareas = [tarea for tarea in self.tareas if tarea.id != id]

    def buscar_tarea(self, criterio):
        return [tarea for tarea in self.tareas if criterio(tarea)]

    def actualizar_tarea(self, id, **kwargs):
        for tarea in self.tareas:
            if tarea.id == id:
                for key, value in kwargs.items():
                    setattr(tarea, key, value)
                break

    # Métodos para la pila de tareas prioritarias
    def agregar_prioridad(self, id_tarea, prioridad):
        tarea_prioritaria = next((tarea for tarea in self.lista_tareas if tarea.id == id_tarea), None)
        if tarea_prioritaria:
            self.pila_prioridades = [tarea for tarea in self.pila_prioridades if tarea.id != id_tarea]
            tarea_prioritaria.prioridad = prioridad
            
            indice_a_insertar = next((indice for indice, tarea in enumerate(self.pila_prioridades) if tarea.prioridad < prioridad), len(self.pila_prioridades))
            
            self.pila_prioridades.insert(indice_a_insertar, tarea_prioritaria)
            print(f"Tarea prioritaria agregada exitosamente. ID: {id_tarea}, Prioridad: {prioridad}")
        else:
            print("Tarea no encontrada.")

    def eliminar_prioridad(self):
        if self.pila_prioridades:
            return self.pila_prioridades.pop()


    def consultar_prioridad(self):
        return self.pila_prioridades[-1]
    
    def calcular_tiempo_total_prioridades(self):
        tiempo_total = sum((tarea.fecha_vencimiento - tarea.fecha_inicio).total_seconds() / 3600 for tarea in self.pila_prioridades)
        return tiempo_total


    # Métodos para la cola de vencimientos
    def agregar_vencimiento(self, tarea):
        # Convert deque to list for sorting
        vencimientos_list = list(self.cola_vencimientos)
        
        # Insert task in sorted order based on due date
        insort(vencimientos_list, (tarea.fecha_vencimiento, tarea))
        
        # Convert back to deque
        self.cola_vencimientos = deque(vencimientos_list)

    def eliminar_vencimiento(self):
        return self.cola_vencimientos.popleft()

    def consultar_proxima_vencer(self):
        return self.cola_vencimientos[0]
    
    def calcular_tiempo_total_vencimiento(self):
        tiempo_total_segundos = sum((tarea.fecha_vencimiento - datetime.now()).total_seconds() for _, tarea in self.cola_vencimientos)
        tiempo_total_dias = tiempo_total_segundos / 86400
        return tiempo_total_dias
    
    def consultar_tareas_por_estado(self, estado_actual):
        tareas_filtradas = [tarea for tarea in self.tareas if tarea.estado_actual == estado_actual]
        print(f"Tareas con estado '{estado_actual}':")
        for tarea in tareas_filtradas:
            print(f"ID: {tarea.id}, Nombre: {tarea.nombre}")
    
    def filtrar_tareas_por_fecha(self, fecha_inicio=None, fecha_fin=None):
        tareas_filtradas = [tarea for tarea in self.tareas if (
            (not fecha_inicio or tarea.fecha_inicio >= fecha_inicio) and
            (not fecha_fin or tarea.fecha_vencimiento <= fecha_fin)
        )]
        print("Tareas filtradas por fecha:")
        for tarea in tareas_filtradas:
            print(f"ID: {tarea.id}, Nombre: {tarea.nombre}, Fecha Inicio: {tarea.fecha_inicio.strftime('%d/%m/%Y')}, Fecha Vencimiento: {tarea.fecha_vencimiento.strftime('%d/%m/%Y')}")

def menu():
    print("-----------------------------------------")
    print("Modulo de gestion de tareas y prioridades")
    print("-----------------------------------------")
    print("1. Crear tarea")
    print("1.1 Crear subtarea para una tarea existente")
    print("2. Insertar tarea en posición específica")
    print("3. Eliminar tarea")
    print("4. Buscar tarea")
    print("5. Actualizar tarea")
    print("6. Agregar prioridad")
    print("7. Eliminar prioridad")
    print("8. Consultar prioridad")
    print("9. Mostrar tiempo total de las tares prioritarias")
    print("10. Agregar vencimiento")
    print("11. Eliminar vencimiento")
    print("12. Consultar próxima a vencer")
    print("13. Mostrar tiempo total de vencimientos")
    print("---------------------")
    print("Modulo de Reportes")
    print("---------------------")
    print("14. Consulta de Tareas por Estado")
    print("15. Filtrado por Fecha")
    print("16. Salir")

def main():
    tarea_principal = Tarea(0, "Proyecto Principal", "Empresa X", "Descripción del proyecto", datetime.now(), datetime.now(), "En progreso", 0, prioridad = 1)
    
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
            
            nueva_tarea = Tarea(id, nombre, empresa_cliente, descripcion, fecha_inicio, fecha_vencimiento, estado_actual, porcentaje, prioridad =1)
            tarea_principal.agregar_tarea(nueva_tarea)
            print("Tarea agregada exitosamente.")
            print([t.nombre for t in tarea_principal.tareas])
        
        elif opcion == '1.1':
            nombre_tarea_principal = input("Ingrese el nombre de la tarea principal:")
            tareas_principales = tarea_principal.buscar_tarea_por_nombre(nombre_tarea_principal) 
            if tareas_principales:
                tarea_a_modificar = tareas_principales[0]
                id_subtarea = input("Ingrese el ID de la subtarea: ")
                nombre_subtarea = input("Ingrese el nombre de la subtarea: ")
                empresa_cliente_subtarea = input("Ingrese la empresa cliente de la subtarea: ")
                descripcion_subtarea = input("Ingrese la descripción de la subtarea: ")
                fecha_inicio_subtarea = datetime.strptime(input("Ingrese la fecha de inicio de la subtarea (dd/mm/yyyy): "), "%d/%m/%Y")
                fecha_vencimiento_subtarea = datetime.strptime(input("Ingrese la fecha de vencimiento de la subtarea (dd/mm/yyyy): "), "%d/%m/%Y")
                estado_actual_subtarea = input("Ingrese el estado actual de la subtarea: ")
                porcentaje_subtarea = float(input("Ingrese el porcentaje completado de la subtarea: "))
                nueva_subtarea = Tarea(id_subtarea, nombre_subtarea, empresa_cliente_subtarea, descripcion_subtarea, fecha_inicio_subtarea, fecha_vencimiento_subtarea, estado_actual_subtarea, porcentaje_subtarea, prioridad =1)
                tarea_a_modificar.agregar_subtarea(nueva_subtarea)
                print("Subtarea agregada exitosamente.")
                print([subtarea.nombre for subtarea in tarea_a_modificar.subtareas])
            else:
                print("Tarea principal no encontrada.")

        
        elif opcion == '2':
            id = input("Ingrese el ID de la tarea: ")
            nombre = input("Ingrese el nombre de la tarea: ")
            empresa_cliente = input("Ingrese la empresa cliente: ")
            descripcion = input("Ingrese la descripción de la tarea: ")
            fecha_inicio = datetime.strptime(input("Ingrese la fecha de inicio (dd/mm/yyyy): "), "%d/%m/%Y")
            fecha_vencimiento = datetime.strptime(input("Ingrese la fecha de vencimiento (dd/mm/yyyy): "), "%d/%m/%Y")
            estado_actual = input("Ingrese el estado actual de la tarea: ")
            porcentaje = float(input("Ingrese el porcentaje completado: "))
            posicion = int(input("Ingrese la posición donde desea insertar la tarea: "))
            
            nueva_tarea = Tarea(id, nombre, empresa_cliente, descripcion, fecha_inicio, fecha_vencimiento, estado_actual, porcentaje, prioridad =1)
            tarea_principal.agregar_tarea(nueva_tarea, posicion)
            print("Tarea insertada exitosamente en la posición especificada.")
            print([t.nombre for t in tarea_principal.tareas])
            
        elif opcion == '3':
            id = input("Ingrese el ID de la tarea a eliminar: ")
            tarea_principal.eliminar_tarea(id)
            for tarea in tarea_principal.tareas:
                print(tarea.nombre)
                
        elif opcion == '4':
            nombre = input("Ingrese el nombre de la tarea a buscar: ")
            tareas_encontradas = tarea_principal.buscar_tarea(lambda x: x.nombre == nombre)
            for t in tareas_encontradas:
                print(f"Tarea encontrada: {t.nombre}")
                print(f"ID: {t.id}")
                print(f"Empresa Cliente: {t.empresa_cliente}")
                print(f"Descripción: {t.descripcion}")
                print(f"Fecha Inicio: {t.fecha_inicio.strftime('%d/%m/%Y')}")
                print(f"Fecha Vencimiento: {t.fecha_vencimiento.strftime('%d/%m/%Y')}")
                print(f"Estado Actual: {t.estado_actual}")
                print(f"Porcentaje Completado: {t.porcentaje}%")

            
        elif opcion == '5':
            id = input("Ingrese el ID de la tarea a actualizar: ")
            print("Ingrese los nuevos datos de la tarea (deje en blanco si no desea cambiarlos):")
            nombre = input("Nuevo nombre: ")
            empresa_cliente = input("Nueva empresa cliente: ")
            descripcion = input("Nueva descripción: ")
            fecha_inicio = input("Nueva fecha de inicio (dd/mm/yyyy): ")
            fecha_vencimiento = input("Nueva fecha de vencimiento (dd/mm/yyyy): ")
            estado_actual = input("Nuevo estado actual: ")
            porcentaje = input("Nuevo porcentaje completado: ")
            
            kwargs = {}
            
            if nombre:
                kwargs['nombre'] = nombre
                
            if empresa_cliente:
                kwargs['empresa_cliente'] = empresa_cliente
                
            if descripcion:
                kwargs['descripcion'] = descripcion
            
            if fecha_inicio:
                kwargs['fecha_inicio'] = datetime.strptime(fecha_inicio, "%d/%m/%Y")
                
            if fecha_vencimiento:
                kwargs['fecha_vencimiento'] = datetime.strptime(fecha_vencimiento, "%d/%m/%Y")
                
            if estado_actual:
                kwargs['estado_actual'] = estado_actual
                
            if porcentaje:
                kwargs['porcentaje'] = float(porcentaje)
                
            tarea_principal.actualizar_tarea(id, **kwargs)
            print("Tarea actualizada exitosamente.")
            
            tarea_actualizada = next((t for t in tarea_principal.tareas if t.id == id), None)
            if tarea_actualizada:
                print(f"Tarea actualizada: {tarea_actualizada.nombre}")
                print(f"ID: {tarea_actualizada.id}")
                print(f"Empresa Cliente: {tarea_actualizada.empresa_cliente}")
                print(f"Descripción: {tarea_actualizada.descripcion}")
                print(f"Fecha Inicio: {tarea_actualizada.fecha_inicio.strftime('%d/%m/%Y')}")
                print(f"Fecha Vencimiento: {tarea_actualizada.fecha_vencimiento.strftime('%d/%m/%Y')}")
                print(f"Estado Actual: {tarea_actualizada.estado_actual}")
                print(f"Porcentaje Completado: {tarea_actualizada.porcentaje}%")
            
            else:
                print("No se encontró la tarea con el ID proporcionado.")

                
        elif opcion == '6':
            id = input("Ingrese el ID de la tarea prioritaria a agregar: ")
            prioridad = int(input("Ingrese el número de prioridad de la tarea (1 es la más alta): "))
            tarea_prioritaria = next((t for t in tarea_principal.tareas if t.id == id), None)
            if tarea_prioritaria:
                tarea_principal.pila_prioridades = [tarea for tarea in tarea_principal.pila_prioridades if tarea.id != id]
                tarea_prioritaria.prioridad = prioridad
                
                indice_a_insertar = next((indice for indice, tarea in enumerate(tarea_principal.pila_prioridades) if tarea.prioridad <= prioridad), len(tarea_principal.pila_prioridades))
                
                tarea_principal.pila_prioridades.insert(indice_a_insertar, tarea_prioritaria)
                print("Tarea prioritaria agregada exitosamente.")
                print("Pila de tareas prioritarias:")
                for tarea in reversed(tarea_principal.pila_prioridades):
                    print(f"ID: {tarea.id}, Prioridad: {tarea.prioridad}")
            else:
                print("No se encontró la tarea con el ID proporcionado.")
      
        elif opcion == '7':
            tarea_eliminada = tarea_principal.eliminar_prioridad()
            if tarea_eliminada:
                print(f"Tarea prioritaria eliminada: {tarea_eliminada.nombre}")
            else:
                print("No hay tareas prioritarias para eliminar.")
        
        elif opcion == '8':
            tarea_prioritaria = tarea_principal.consultar_prioridad()
            print(f"Tarea prioritaria actual: {tarea_prioritaria.nombre}")
            
        elif opcion == '9':
            tiempo_total = tarea_principal.calcular_tiempo_total_prioridades()
            print(f"Tiempo total de las tareas prioritarias: {tiempo_total:.2f} horas")
            
        elif opcion == '10':
            id = input("Ingrese el ID de la tarea próxima a vencer a agregar: ")
            tarea_proxima_vencer = next((t for t in tarea_principal.tareas if t.id == id), None)
            
            if tarea_proxima_vencer:
                tarea_principal.agregar_vencimiento(tarea_proxima_vencer)
                print("Tarea próxima a vencer agregada exitosamente.")
                
            print("Tareas próximas a vencer:")
            for _, tarea in tarea_principal.cola_vencimientos:
                print(f"ID: {tarea.id}, Fecha de Vencimiento: {tarea.fecha_vencimiento}")
                
        elif opcion == '11':
            if tarea_principal.cola_vencimientos:
                tarea_eliminada = tarea_principal.eliminar_vencimiento()[1]
                print(f"Tarea próxima a vencer eliminada: {tarea_eliminada.nombre}")
            else:
                print("No hay tareas próximas a vencer para eliminar.")
            
        elif opcion == '12':
            tarea_proxima_vencer = tarea_principal.consultar_proxima_vencer()[1]
            print(f"Tarea próxima a vencer actual: {tarea_proxima_vencer.nombre}")
            
        elif opcion == '13':
            tiempo_total_vencimiento_dias = tarea_principal.calcular_tiempo_total_vencimiento()
            print(f"Tiempo total restante para las tareas próximas a vencer: {tiempo_total_vencimiento_dias:.2f} días")
            
        elif opcion == '14':
            estado_actual = input("Ingrese el estado de las tareas a consultar (pendiente, en progreso, completada): ")
            tarea_principal.consultar_tareas_por_estado(estado_actual)
            
        elif opcion == '15':
            try:
                fecha_inicio_str = input("Ingrese la fecha de inicio (dd/mm/aaaa) (opcional): ")
                fecha_inicio = datetime.strptime(fecha_inicio_str, "%d/%m/%Y") if fecha_inicio_str else None

                fecha_fin_str = input("Ingrese la fecha de fin (dd/mm/aaaa) (opcional): ")
                fecha_fin = datetime.strptime(fecha_fin_str, "%d/%m/%Y") if fecha_fin_str else None

                tarea_principal.filtrar_tareas_por_fecha(fecha_inicio, fecha_fin)
            except ValueError:
                print("Formato de fecha no válido.")
                
        elif opcion == '16':
            break

if __name__ == "__main__":
    main()



