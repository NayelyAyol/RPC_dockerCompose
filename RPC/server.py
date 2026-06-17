# Importa la clase que permite crear un servidor XML-RPC
from xmlrpc.server import SimpleXMLRPCServer




# Lista donde se guardan las películas
# Se almacenan en memoria mientras el servidor esté activo
peliculas = [


    {
        "id":1,
        "nombre":"Matrix",
        "genero":"Accion"
    }

]







# Función para listar todas las películas
# Será llamada remotamente por el cliente
def listar_peliculas():



    # Verifica si no existen películas
    if len(peliculas) == 0:


        return "No existen peliculas"





    # Guarda el resultado final
    resultado = ""




    # Recorre cada película
    for p in peliculas:



        # Agrega información al texto
        resultado += (

            f"ID: {p['id']} "
            f"Nombre: {p['nombre']} "
            f"Genero: {p['genero']}\n"

        )




    # Devuelve todas las películas
    return resultado







# Función para crear una película
# Recibe nombre y género desde el cliente
def crear_pelicula(nombre,genero):



    # Genera un nuevo ID
    nuevo_id = len(peliculas)+1





    # Crea la película
    pelicula = {


        "id": nuevo_id,

        "nombre": nombre,

        "genero": genero

    }





    # Guarda la película en la lista
    peliculas.append(pelicula)




    return "Película creada correctamente"









# Función para buscar una película
# Recibe el ID desde el cliente
def buscar_pelicula(id):



    # Recorre todas las películas
    for p in peliculas:



        # Busca coincidencia de ID
        if p["id"] == id:



            # Devuelve los datos encontrados
            return (

                f"ID: {p['id']} "
                f"Nombre: {p['nombre']} "
                f"Genero: {p['genero']}"

            )




    # Si no encuentra la película
    return "Película no encontrada"









# Función para actualizar una película
def actualizar_pelicula(id,nombre,genero):



    # Recorre las películas
    for p in peliculas:



        # Busca el ID indicado
        if p["id"] == id:



            # Actualiza datos
            p["nombre"] = nombre

            p["genero"] = genero




            return "Película actualizada"





    return "Película no encontrada"









# Función para eliminar película
def eliminar_pelicula(id):



    # Recorre películas
    for p in peliculas:



        # Busca coincidencia
        if p["id"] == id:



            # Elimina película
            peliculas.remove(p)



            return "Película eliminada"





    return "Película no encontrada"










# Crea servidor XML-RPC
#
# 0.0.0.0 permite recibir conexiones externas
#
# 9000 es el puerto donde escucha
server = SimpleXMLRPCServer(
    ("0.0.0.0",9000)
)

# Publica funciones para que el cliente pueda usarlas

server.register_function(
    crear_pelicula,
    "crear_pelicula"
)

server.register_function(
    buscar_pelicula,
    "buscar_pelicula"
)

server.register_function(
    listar_peliculas,
    "listar_peliculas"
)

server.register_function(
    actualizar_pelicula,
    "actualizar_pelicula"
)

server.register_function(
    eliminar_pelicula,
    "eliminar_pelicula"
)

# Mensaje cuando inicia
print("Servidor RPC activo puerto 9000")

# Mantiene el servidor esperando solicitudes
server.serve_forever()