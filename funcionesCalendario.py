from tabulate import tabulate
import funcionesgenerales

# FUNCION para crear un partido nuevo
def crearPartido(partidos, equipos):
    # el id del nuevo partido lo generamos usando la longitud actual de la lista partidos + 1
    idPartido = funcionesgenerales.generarID(partidos)
    # pedimos al usuario que introduzca los demas datos
    jornada = int(input("Introduce el número de jornada: "))
    idLocal = int(input("Introduce el id del equipo local: "))
    idVisitante = int(input("Introduce el id del equipo visitante: "))

    # comprobamos que los equipos sean distintos y que esten activos
    if idLocal == idVisitante:
        print("Los equipos tienen que ser diferentes")
        return

    # inicializamos las variables de activo a false
    localActivo = False
    visitanteActivo = False

    # recorremos todos los equipos de la lista equipos uno por uno
    for equipo in equipos:
        # si el id coincide con idLocal y el equipo esta activo,
        #  cambiamos el valor de locaActivo a true
        if equipo["id"] == idLocal and equipo["activo"] == True:
            localActivo = True
        # si el id coincide con idVisitante y el equipo esta activo,
        #  cambiamos el valor de visitanteActivo a true
        if equipo["id"] == idVisitante and equipo["activo"] == True:
            visitanteActivo = True

    # si algun equipo no esta activo muestra el mensaje al usuario
    if localActivo == False or visitanteActivo == False:
        print("Uno o ambos equipos no están activos ")
    # si ambos equipos estan activos
    else:
        # pedimos la fecha y la hora de partido
        fecha = input("Introduce la fecha del partido (AAAA-MM-DD): ")
        hora = input("Introduce la hora del partido (HH:MM): ")

        # creamos el diccionario partido con los datos
        partido = {
            "id": idPartido,
            "jornada": jornada,
            "local_id": idLocal,
            "visitante_id": idVisitante,
            "fecha": fecha,
            "hora": hora,
            "jugado": False,
            "resultado": None
        }

        # añadimos el diccionario partido a la lista partidos
        partidos.append(partido)
        print("se ha creado correctamente")


# FUNCION para listar todos los partidos
def listarPartidos(partidos, equipos):
    # nos creamos una lista para guardar las filas que vamos a mostrar en la tabla
    listaPartidos = []

    # recorremos cada partido de la lista partidos uno por uno
    for partido in partidos:
        # inicializamos las variables
        nombreLocal = ""
        nombreVisitante = ""

        # recorremos la lista equipos para localizar nombres que coincidan con los ids del partido
        for equipo in equipos:
            # si coincide el id guarda el nombre del equipo local
            if equipo["id"] == partido["local_id"]:
                nombreLocal = equipo["nombre"]
            # si coincide el id guarda el nombre del equipo visitante
            if equipo["id"] == partido["visitante_id"]:
                nombreVisitante = equipo["nombre"]

        # añadimos a la lista una fila cn los datos que vamos a mostrar en la tabla
        listaPartidos.append([
            partido["id"], partido["jornada"], nombreLocal, nombreVisitante,
            partido["fecha"], partido["hora"], partido["jugado"]
        ])

    # si la lista no está vacia mostramos los datos
    if len(listaPartidos) > 0:
        print(tabulate(listaPartidos, headers=["ID", "Jornada", "Local", "Visitante", "Fecha", "Hora", "Jugado"], tablefmt="grid"))
    # si esta vacia muestra este mensaje
    else:
        print("no hay partidos para mostrar")


# FUNCION para cambiar la fecha y hora
def reprogramarPartido(partidos):
    # pedimos el id del partido que queremos cambiar
    idCambiar = int(input("Introduce el id del partido que quieres reprogramar: "))
    # inicializamos una variable booleana a false para que cuando encuentre el partido 
    # cambie su valor a true deje de buscar y salga del bucle 
    encontrado = False

    # recorremos cada partido de la lista partidos
    for partido in partidos:
        # si el id del partido coincide con el id que introduce el usuario
        if partido["id"] == idCambiar:
            # y si el partido no se ha jugado se puede reprogramar
            if partido["jugado"] == False:
                # pedimos la nueva fecha y la nueva hora al usuario
                nuevaFecha = input("Introduce la nueva fecha (AAAA-MM-DD): ")
                nuevaHora = input("Introduce la nueva hora (HH:MM): ")
                # cambiamos los valores en el diccionario
                partido["fecha"] = nuevaFecha
                partido["hora"] = nuevaHora
                print("El partido se ha reprogramado correctamente")
            # si el partido se ha jugado no se cambia
            else:
                print("El partido ya se ha jugado, no se puede reprogranar")
            # cambniamos el valor de la variable booleana a true para salir del bucle y que deje de buscar
            encontrado = True

    # si no encontramos el partido se muestra este mensaje al usuario
    if encontrado == False:
        print("No se ha encontrado ningun partido con ese id ")


# FUNCION para eliminar partidos
def eliminarPartido(partidos):
    idEliminar = int(input("Introduce el id del partido que quieres eliminar: "))
    # inicializamos una variable booleana a false para que cuando encuentre el partido 
    # cambie su valor a true deje de buscar y salga del bucle 
    encontrado = False

    # recorremos cada partido de la lista partidos
    for partido in partidos:
        # si el id del partido coincide con el id que introduce el usuario
        if partido["id"] == idEliminar:
            # y el partido no se ha jugado, lo eliminamos de la lista partidos
            if partido["jugado"] == False:
                partidos.remove(partido)
                print("El partido se ha eliminado correctamente")
            # si el partido se ha jugado no podemos eliminarlo de la lista
            else:
                print("El partido ya se ha jugado, no se puede reprogranar")
            # cambniamos el valor de la variable booleana a true para salir del bucle y que deje de buscar
            encontrado = True

    # si no encontramos el partido se muestra este mensaje al usuario
    if encontrado == False:
        print("No se ha encontrado ningun partido con ese id ")
