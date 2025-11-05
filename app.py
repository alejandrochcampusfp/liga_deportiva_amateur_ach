# LLAMADA A LAS OTRAS CLASES CON SUS FUNCIONES
import funcionesgenerales
import funcionesEquipos
import funcionesJugadores
import funcionesCalendario
import funcionesRanking

# LISTAS
equipos = []
jugadores = []
partidos = []

# MENUS
menuPrincipal = [
    ["MENU PRINCIPAL"],
    ["1. Menu gestion Equipos"],
    ["2. Menu gestion Jugadores"],
    ["3. Menu Calendario y Partidos"],
    ["4. Resultados y Clasificación"],
    ["5. Insertar datos de prueba"],
    ["6. Salir"]
]


menuGestionEquipos = [
    ["MENU GESTION EQUIPOS"],
    ["1. Crear equipo"],
    ["2. Listar equipos"],
    ["3. Buscar por id"],
    ["4. Actualizar datos"],
    ["5. Eliminar equipo"],
    ["6. Volver al menú principal"]
]

menuGestionJugadores = [
    ["MENU GESTION JUGADORES"],
    ["1. Alta de jugador"],
    ["2. Listar jugadores"],
    ["3. Buscar por id"],
    ["4. Actualizar jugador"],
    ["5. Eliminar jugador"],
    ["6. Volver al menú principal"]
]

menuCalendarioyPartidos = [
    ["MENU CALENDARIO Y PARTIDOS"],
    ["1. Crear partido"],
    ["2. Listar partidos"],
    ["3. Reprogramar partido"],
    ["4. Eliminar partido"],
    ["5. Volver al menú principal"]
]

menuResultados = [
    ["MENU RESULTADOS Y CLASIFICACION"],
    ["1. Registrar resultado"],
    ["2. Ver clasificación"],
    ["3. Estadísticas por equipo"],
    ["4. Volver al menú principal"]
]

# MENU PRINCIPAL CON TODAS LAS OPCIONES
opcion = ""
while opcion != "6":
    funcionesgenerales.mostrarMenu(menuPrincipal)
    opcion = input("Elige una opción: ")

    match opcion:
        
        # EQUIPOS
        case "1":
            opcionEquipos = ""
            while opcionEquipos != "6":
                funcionesgenerales.mostrarMenu(menuGestionEquipos)
                opcionEquipos = input("Elige una opción: ")
                match opcionEquipos:
                    case "1":
                        funcionesEquipos.crearEquipo(equipos)
                    case "2":
                        funcionesEquipos.listarEquipos(equipos)
                    case "3":
                        funcionesEquipos.buscarEquipo(equipos)

                    case "4":
                        funcionesEquipos.actualizarEquipo(equipos)
                    case "5":
                        funcionesEquipos.eliminarEquipo(equipos)
                    case "6":
                        print("Volviendo al menú principal...\n ")
                    case _:
                        print("Opción no válida ")

        # JUGADORES
        case "2":
            opcionJugadores = ""
            while opcionJugadores != "6":
                funcionesgenerales.mostrarMenu(menuGestionJugadores)
                opcionJugadores = input("Elige una opción: ")
                match opcionJugadores:
                    case "1":
                        funcionesJugadores.crearJugador(jugadores, equipos)
                    case "2":
                        funcionesJugadores.listarJugadores(jugadores, equipos)
                    case "3":
                        funcionesJugadores.buscarJugador(jugadores, equipos)
                    case "4":
                        funcionesJugadores.actualizarJugador(jugadores)
                    case "5":
                        funcionesJugadores.eliminarJugador(jugadores)
                    case "6":
                        print("Volviendo al menú principal...\n ")
                    case _:
                        print("Opción no válida ")

        # CALENDARIO
        case "3":    
            opcionPartidos = ""
            while opcionPartidos != "5":
                funcionesgenerales.mostrarMenu(menuCalendarioyPartidos)
                opcionPartidos = input("Elige una opción: ")
                match opcionPartidos:
                    case "1":
                        funcionesCalendario.crearPartido(partidos, equipos)
                    case "2":
                        funcionesCalendario.listarPartidos(partidos, equipos)
                    case "3":
                        funcionesCalendario.reprogramarPartido(partidos)
                    case "4":
                        funcionesCalendario.eliminarPartido(partidos)
                    case "5":
                        print("Volviendo al menú principal...\n ")
                    case _:
                        print("Opción no válida ")

        
        # RANKING
        case "4":
            opcionRanking = ""
            while opcionRanking != "4":
                funcionesgenerales.mostrarMenu(menuResultados)
                opcionRanking = input("Elige una opción: ")
                match opcionRanking:
                    case "1":
                        funcionesRanking.registrarResultado(partidos)
                    case "2":
                        funcionesRanking.mostrarClasificacion(partidos, equipos)
                    case "3":
                        funcionesRanking.mostrarEstadisticasEquipo(partidos, equipos)
                    case "4":
                        print("Volviendo al menú principal...\n ")
                    case _:
                        print("Opción no válida ")
        
        # DATOS DE PRUEBA
        case "5":
            funcionesgenerales.insertarDatosPrueba(equipos, jugadores, partidos)

        # SALIR
        case "6":
            print("Saliendo del programa... ")

        case _:
            print("Opción no válida ")
