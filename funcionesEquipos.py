from tabulate import tabulate
import funcionesgenerales

# FUNCION para crear un nuevo equipo
def crearEquipo(equipos):
    # el id del nuevo equipo lo generamos usando la longitud actual de la lista equipos + 1
    idEquipo = funcionesgenerales.generarID(equipos)
    
    # pedimos los datos al usuario
    nombreEquipo = input("Introduce el nombre del equipo: ")
    ciudadEquipo = input("Introduce la ciudad del equipo: ")
    # por defecto los equipos se crean activos
    activoEquipo = True  

    # creamos un diccionario con los datos del equipo
    equipo = {
        "id": idEquipo,
        "nombre": nombreEquipo,
        "ciudad": ciudadEquipo,
        "activo": activoEquipo
    }
    # añadimos el diccionario a la lista equipos
    equipos.append(equipo)
    print("se ha creado correctamente")


# FUNCION para listar los equipos activos
def listarEquipos(equipos):
    # nos creamos una lista para guardar los equipos activos    
    equiposActivos = []

     # recorremos todos los equipos uno por uno de la lista equipos
    for equipo in equipos:
        # si el equipo está activo lo añadimos a la lista
        if equipo["activo"] == True:
            equiposActivos.append([equipo["id"], equipo["nombre"], equipo["ciudad"]])

    # si hay equipos activos los mostramos en una tabla
    if len(equiposActivos) > 0:
        print(tabulate(equiposActivos, headers=["ID", "Nombre", "Ciudad"], tablefmt="grid"))
     # si no hay ninguno mostramos un mensaje
    else:
        print("No hay equipos activos para mostrar ")


# FUNCION que busca un equipo por id
def buscarEquipo(equipos):
    idBuscar = int(input("Introduce el id del equipo que quieres buscar: "))
    # inicializamos una variable booleana a false para que cuando encuentre 
    # el equipo se cambie a true y salga del bucle pra dejar de buscar
    encontrado = False  

    # recorremos cada equipo de la lista equipos uno por uno
    for equipo in equipos:
        # si el id que introduce el usaurio coincide con el de algun equipo lo muestra
        if equipo["id"] == idBuscar:
            print("Equipo encontrado: ")
            print(tabulate([[equipo["id"], equipo["nombre"], equipo["ciudad"], equipo["activo"]]],
                           headers=["ID", "Nombre", "Ciudad", "Activo"], tablefmt="grid"))
            encontrado = True

    # si no lo encuentra mostramos un mensaje al usuario
    if encontrado == False:
        print("No se ha encontrado ningun equipo con ese id ")


# FUNCION que actualiza los datos de un equipo
def actualizarEquipo(equipos):
    idActualizar = int(input("Introduce el id del equipo que quieres actualizar: "))
    encontrado = False

    # recorremos cada equipo de la lista equipos uno por uno
    for equipo in equipos:
        # si el id que introduce el usuario coincide con el de algun equipo, 
        # pedimos los nuevos datos del equipo
        if equipo["id"] == idActualizar:
            nuevoNombre = input("Introduce el nuevo nombre del equipo: ")
            nuevaCiudad = input("Introduce la nueva ciudad del equipo: ")
            equipo["nombre"] = nuevoNombre
            equipo["ciudad"] = nuevaCiudad
            print("Datos del equipo actualizados correctamente ")
            encontrado = True

    if encontrado == False:
        print("No se ha encontrado ningun equipo con ese id ")


# FUNCION que elimina (cambia el valor de activo a false) un equipo
def eliminarEquipo(equipos):
    idEliminar = int(input("Introduce el id del equipo que quieres eliminar: "))
    encontrado = False

     # recorremos cada equipo de la lista equipos uno por uno
    for equipo in equipos:
        # si el id que introduce el usuario coincide con el de algun equipo, 
        # cambiamos el valor de activo a false
        if equipo["id"] == idEliminar:
            equipo["activo"] = False
            print("EL equipo se ha eliminado ")
            encontrado = True

    if encontrado == False:
        print("No se ha encontrado ningun equipo con ese id ")
