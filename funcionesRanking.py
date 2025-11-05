from tabulate import tabulate

# FUNCION para registrar el resultado de un partido
def registrarResultado(partidos):
    idPartido = int(input("Introduce el id del partido que quieres registrar: "))
    encontrado = False

    # recorremos la lista partidos partido por partido, y si el id del partido coincide 
    # con el que introduce el usuario comprobamos si se ha jugado o no se ha jugado
    for partido in partidos:
        if partido["id"] == idPartido:
            # si el partido no se ha jugado pedimos los datos 
            if partido["jugado"] == False:
                golesLocal = int(input("Introduce los goles del equipo local: "))
                golesVisitante = int(input("Introduce los goles del equipo visitante: "))

                # guardamos el resultado como una tupla (golesLocal, golesVisitante)
                partido["resultado"] = (golesLocal, golesVisitante)
                # marcamos el partido como jugado
                partido["jugado"] = True  
                print("Resultado registrado correctamente ")
            
            # si el partido se ha jugado mostramos un mensaje
            else:
                print("El partido ya tiene un resultado registrado ")
            encontrado = True

    # si no encuentra el partido mostramos un mensaje
    if encontrado == False:
        print("No se ha encontrado ningun partido con ese id ")


# FUNCION para mostrar la clasificacion de los equipos
def mostrarClasificacion(partidos, equipos):
    # lista donde se guardara la clasificacion completa con las estadisticas de cada equipo
    clasificacion = []

    # recorremos la lista de equipos
    for equipo in equipos:
        # solo contamos los equipos que esten activos
        if equipo["activo"] == True:
            # inicializamos los contadores del equipo
            pj = 0  
            g = 0   
            e = 0   
            p = 0   
            gf = 0  
            gc = 0  

            # Equipo", "PJ", "G", "E", "P", "GF", "GC", "DG", "PTS

            # recorremos la lista de partidos para calcular las estadisticas
            for partido in partidos:
                # solo contamos los partidos que ya se hayan jugado
                if partido["jugado"] == True:
                    # si el equipo fue el local
                    if partido["local_id"] == equipo["id"]:
                        # sumamosun partido jugado
                        pj = pj + 1 
                        # añadimos los goles a favor
                        gf = gf + partido["resultado"][0]
                        # añadimos los goles que recibe
                        gc = gc + partido["resultado"][1] 

                        # comprobamos el resultado del partido
                        # si el local mete mas goles gana
                        if partido["resultado"][0] > partido["resultado"][1]:
                            g = g + 1 
                        # si meten los mismos goles empatan
                        elif partido["resultado"][0] == partido["resultado"][1]:
                            e = e + 1
                        # si mete menos goles pierde
                        else:
                            p = p + 1

                    # si el equipo fue el visitante
                    elif partido["visitante_id"] == equipo["id"]:
                        # sumamos un partido jugado
                        pj = pj + 1 
                        # añadimos los goles en la segunda posicion
                        gf = gf + partido["resultado"][1] 
                        # los goles en contra van a la primera posicion porque son del local
                        gc = gc + partido["resultado"][0] 
                        # comprobamos el resultado del partido
                        # si el visitante mete mas goles gana
                        if partido["resultado"][1] > partido["resultado"][0]:
                            g = g + 1
                        # si meten los mismos goles empatan
                        elif partido["resultado"][1] == partido["resultado"][0]:
                            e = e + 1
                        # si el visitante mete menos goles pierde
                        else:
                            p = p + 1

            # la diferencia de goles es goles a favor menos en contra
            dg = gf - gc
            # los ganados valen 3 y los empates 1
            pts = g * 3 + e * 1

            # añadimos los datos del equipo como una fila a la clasificacion
            clasificacion.append([equipo["nombre"], pj, g, e, p, gf, gc, dg, pts])

    # definimos una funcion auxiliar para obtener los puntos de cada equipo y ordenar 
    # la lista de clasificacion, devuelve la columna de los puntos
    def obtener_puntos(fila):
        return fila[8] 

    # ordenamos la clasificacion por puntos, reverse true para que sea de mayor a menor
    clasificacion.sort(key=obtener_puntos, reverse=True)

    # si la clasificacion no esta vacia mostramos la tabla 
    if len(clasificacion) > 0:
        print(tabulate(clasificacion,
                        headers=["Equipo", "PJ", "G", "E", "P", "GF", "GC", "DG", "PTS"], tablefmt="grid"))
        
    # sino mostramos un mensaje
    else:
        print("No hay datos de la clasificacion ")


# FUNCION para mostrar las estadisticas de un equipo
def mostrarEstadisticasEquipo(partidos, equipos):
    idEquipo = int(input("Introduce el id del equipo para ver sus estadísticas: "))
    encontrado = False

    # recorremos la lista de equipos uno por uno y buscamos el equipo
    for equipo in equipos:
        if equipo["id"] == idEquipo:
            encontrado = True
            # inicializamos los contadores del equipo
            pj = 0
            gf = 0
            gc = 0
            pts = 0

            # recorremos la lista de partidos jugados
            for partido in partidos:
                # si el partido se ha jugado
                if partido["jugado"] == True:

                    # y si el equipo es local
                    if partido["local_id"] == idEquipo:
                        # sumamos un partido jugado
                        pj = pj + 1
                        # sumamos los goles a favor y los en contra
                        gf = gf + partido["resultado"][0]
                        gc = gc + partido["resultado"][1]

                        # si el local gana sumamos 3 puntos
                        if partido["resultado"][0] > partido["resultado"][1]:
                            pts = pts + 3
                        # si empata sumamos 1 punto, si pierde nada
                        elif partido["resultado"][0] == partido["resultado"][1]:
                            pts = pts + 1

                    # si el equipo es visitante
                    elif partido["visitante_id"] == idEquipo:
                        # sumamos un partido jugado
                        pj = pj + 1
                        # sumamos los goles a favor y los en contra pero en las posiciones contrarias al local
                        gf = gf + partido["resultado"][1]
                        gc = gc + partido["resultado"][0]

                        # si el visitante gana sumamos 3 puntos
                        if partido["resultado"][1] > partido["resultado"][0]:
                            pts = pts + 3
                        # si empata sumamos 1 y si pierde nada
                        elif partido["resultado"][1] == partido["resultado"][0]:
                            pts = pts + 1

            # mostramos los resultados en la tabla
            print(tabulate([[equipo["nombre"], pj, gf, gc, pts]],
                           headers=["Equipo", "PJ", "GF", "GC", "PTS"], tablefmt="grid"))

    # si no encuentra el equipo mostramos un mensaje
    if encontrado == False:
        print("No se ha encontrado ningun equipo con ese id ")
