# Importa la clase que permite crear un servidor XML-RPC
from xmlrpc.server import SimpleXMLRPCServer



# Lista donde se almacenan las películas en memoria
# Cada película es un diccionario
peliculas = [

    {
        "id":1,
        "nombre":"Matrix",
        "genero":"Accion"
    }

]


# Función que devuelve todas las películas registradas
# Esta función será llamada desde el cliente
def listar_peliculas():


    # Verifica si la lista está vacía
    if len(peliculas) == 0:


        # Envía mensaje al cliente
        return "No existen peliculas"


    # Variable donde se almacenará el resultado
    resultado = ""


    # Recorre cada película de la lista
    for p in peliculas:

        # Agrega los datos de cada película al texto final
        resultado += (

            f"ID: {p['id']} "
            f"Nombre: {p['nombre']} "
            f"Genero: {p['genero']}\n"

        )

    # Devuelve la lista completa
    return resultado



# Función para crear una película
# Recibe nombre y género desde el cliente
def crear_pelicula(nombre,genero):

    # Genera un nuevo ID
    # Usa el tamaño actual de la lista + 1
    nuevo_id = len(peliculas)+1


    # Crea un diccionario con los datos recibidos
    pelicula = {


        "id": nuevo_id,

        "nombre": nombre,

        "genero": genero

    }




    # Guarda la nueva película dentro de la lista
    peliculas.append(pelicula)



    # Devuelve respuesta al cliente
    return "Película creada correctamente"







# Función para actualizar una película
# Recibe ID, nuevo nombre y nuevo género
def actualizar_pelicula(id,nombre,genero):


    # Recorre todas las películas
    for p in peliculas:



        # Busca la película con el ID recibido
        if p["id"] == id:



            # Cambia el nombre anterior
            p["nombre"] = nombre



            # Cambia el género anterior
            p["genero"] = genero



            # Confirma actualización
            return "Película actualizada"




    # Si no encontró el ID
    return "Película no encontrada"







# Función para eliminar una película
def eliminar_pelicula(id):


    # Recorre las películas
    for p in peliculas:



        # Busca coincidencia por ID
        if p["id"] == id:



            # Elimina la película encontrada
            peliculas.remove(p)



            # Envía respuesta
            return "Película eliminada"




    # Si no existe
    return "Película no encontrada"







# Crea el servidor XML-RPC
# 0.0.0.0 permite recibir conexiones externas
# 9000 es el puerto del servidor
server = SimpleXMLRPCServer(
    ("0.0.0.0",9000)
)






# Publica la función listar_peliculas
# Ahora puede ser llamada desde el cliente
server.register_function(
    listar_peliculas,
    "listar_peliculas"
)





# Publica crear_pelicula
server.register_function(
    crear_pelicula,
    "crear_pelicula"
)





# Publica actualizar_pelicula
server.register_function(
    actualizar_pelicula,
    "actualizar_pelicula"
)





# Publica eliminar_pelicula
server.register_function(
    eliminar_pelicula,
    "eliminar_pelicula"
)





# Mensaje cuando el servidor inicia
print("Servidor RPC activo puerto 9000")





# Mantiene el servidor escuchando peticiones
# Nunca termina hasta detener el contenedor
server.serve_forever()