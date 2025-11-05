from tabulate import tabulate
import funcionesgenerales

# FUNCION para crear un jugador nuevo
def crearJugador(jugadores, equipos):
    # el id lo generamos usando la longitud actual de la lista jugadores + 1
    idJugador = funcionesgenerales.generarID(jugadores)

    # pedimos los datos al usuario del jugador
    nombreJugador = input("Introduce el nombre del jugador: ")
    posicionJugador = input("Introduce la posición del jugador: ")
    idEquipoJugador = int(input("Introduce el id del equipo al que pertenece: "))

    # nos declaramos una variable booleana para que cuando lo encuentre cambie a true y deje de buscar
    equipoEncontrado = False

    # comprobamos si el equipo existe y si esta activo para poder crear el jugador
    for equipo in equipos:     
        if equipo["id"] == idEquipoJugador and equipo["activo"] == True:
            equipoEncontrado = True

    # sino no se puede crear
    if equipoEncontrado == False:
        print("El equipo no existe o no está activo, no se puede crear al jugador")
    
    # creamos un nuevo diccionario jugador
    else:
        jugador = {
            "id": idJugador,
            "nombre": nombreJugador,
            "posicion": posicionJugador,
            "equipo_id": idEquipoJugador,
            "activo": True
        }
        # añadimos el jugador a la lista jugadores
        jugadores.append(jugador)
        print("Se ha creado correctamente")


# FUNCION para listar los jugadores que estan activos
def listarJugadores(jugadores, equipos):
    # nos creamos una lista vacia para guardar los jugadores activos
    jugadoresActivos = []

    # recorremos cada jugador de la lista jugadores
    for jugador in jugadores:
        # si el jugador esta activo
        if jugador["activo"] == True:
            # buscamos el nombre del equipo del jugador
            nombreEquipo = ""
            # recorremos cada equipo de la lista equipo
            for equipo in equipos:
                # y si el id del equipo coincide con el id del equipo del jugador el nombre de la variable nombreEquipo 
                # va a ser el nombre del equipo
                if equipo["id"] == jugador["equipo_id"]:
                    nombreEquipo = equipo["nombre"]
            # añadimos a nuestra lista que nos hemos creado antes a los jugadores
            jugadoresActivos.append([jugador["id"], jugador["nombre"], jugador["posicion"], nombreEquipo])

    # si la lista no esta vacia mostramos los jugadores
    if len(jugadoresActivos) > 0:
        print(tabulate(jugadoresActivos, headers=["ID", "Nombre", "Posición", "Equipo"], tablefmt="grid"))
    # si está vacia mostramos un mensaje al usuario
    else:
        print("No hay jugadores activos para mostrar ")


# FUNCION para buscar un jugador por id
def buscarJugador(jugadores, equipos):
    idBuscar = int(input("Introduce el id del jugador a buscar: "))
    encontrado = False

    # recorremos la lista jugadores jugador por jugador, y si el id que introduce el 
    # usauario coincide con el de algun jugador lo muestra y deja de buscar 
    # cambiando el valor de encontrado a true
    for jugador in jugadores:
        if jugador["id"] == idBuscar:
            # buscamos el nombre del equipo del jugador
            nombreEquipo = ""
            for equipo in equipos:
                if equipo["id"] == jugador["equipo_id"]:
                    nombreEquipo = equipo["nombre"]

            print("Jugador encontrado:")
            print(tabulate([[jugador["id"], jugador["nombre"], jugador["posicion"], nombreEquipo, jugador["activo"]]],
                           headers=["ID", "Nombre", "Posición", "Equipo", "Activo"], tablefmt="grid"))
            
            encontrado = True

    # si no lo encuentra mostramos un mensaje
    if encontrado == False:
        print("No se ha encontrado ningun jugador con ese id ")


# FUNCION para actualizar los datos de un jugador
def actualizarJugador(jugadores):
    idActualizar = int(input("Introduce el id del jugador a actualizar: "))
    encontrado = False

    # recorremos la lista jugadores jugador por jugador, y si el id que introduce el 
    # usauario coincide con el de algun jugador pedimos los nuevos datos del jugador
    # y deja de buscar cambiando el valor de encontrado a true
    for jugador in jugadores:
        if jugador["id"] == idActualizar:
            nuevoNombre = input("Introduce el nuevo nombre: ")
            nuevaPosicion = input("Introduce la nueva posición: ")
            jugador["nombre"] = nuevoNombre
            jugador["posicion"] = nuevaPosicion
            print("Datos actualizados correctamente ")
            encontrado = True

    # si no lo encuentra mostramos un mensaje
    if encontrado == False:
        print("No se ha encontrado ningun jugador con ese id ")


# FUNCION para eliminar (cambiar a false el campo activo ) de un jugador
def eliminarJugador(jugadores):
    idEliminar = int(input("Introduce el id del jugador a eliminar: "))
    encontrado = False

    # recorremos la lista jugadores jugador por jugador, y si el id que introduce el 
    # usauario coincide con el de algun jugador el valor de activo cambia a false
    # y deja de buscar cambiando el valor de encontrado a true
    for jugador in jugadores:
        if jugador["id"] == idEliminar:
            jugador["activo"] = False
            print("El jugador se ha eliminado")
            encontrado = True

    # si no lo encuentra mostramos un mensaje
    if encontrado == False:
        print("No se ha encontrado ningun jugador con ese id ")