from tabulate import tabulate

def mostrarMenu(menu):
    print(tabulate(menu , headers="firstrow", tablefmt="outline"))

def generarID(lista):
    return len(lista) + 1

def insertarDatosPrueba(equipos, jugadores, partidos):
    # equipos
    equipos.append({"id": 1, "nombre": "Tiburones", "ciudad": "Getafe", "activo": True})
    equipos.append({"id": 2, "nombre": "Leones de Montepinar", "ciudad": "Madrid", "activo": True})
    equipos.append({"id": 3, "nombre": "Españoles de cornella", "ciudad": "Barcelona", "activo": True})
    equipos.append({"id": 4, "nombre": "La Avanzada", "ciudad": "Fuenlaabrada", "activo": True})

    # jugadores
    jugadores.append({"id": 1, "nombre": "Laura", "posicion": "Delantera", "equipo_id": 1, "activo": True})
    jugadores.append({"id": 2, "nombre": "Kylian Mbappe", "posicion": "Delantero", "equipo_id": 2, "activo": True})
    jugadores.append({"id": 3, "nombre": "Sergio Ramos", "posicion": "Defensa", "equipo_id": 3, "activo": True})

    
    # partidos
    partidos.append({
        "id": 1, "jornada": 3,
        "local_id": 1, "visitante_id": 2,
        "fecha": "2025-11-22", "hora": "18:30",
        "jugado": False, "resultado": None  # (golesLocal, golesvisitante)
    })
    

    partidos.append({
        "id": 2,
        "jornada": 2,
        "local_id": 2,  # leones de montepinar
        "visitante_id": 3,  # españoles de cornella
        "fecha": "2025-11-29",
        "hora": "20:00",
        "jugado": True,
        "resultado": (2, 2)  # empate
    })

    partidos.append({
        "id": 3,
        "jornada": 3,
        "local_id": 3,  # españoles de cornella
        "visitante_id": 4,  # la avanzada
        "fecha": "2025-12-02",
        "hora": "19:00",
        "jugado": True,
        "resultado": (1, 3)  # gana la avanzada
    })

    print("Datos de prueba insertados correctamente \n\n")
