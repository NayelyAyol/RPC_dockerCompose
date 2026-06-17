# Importa la librería XML-RPC
# Permite que el cliente se comunique con el servidor remoto
import xmlrpc.client

# Función que muestra el menú de opciones
def menu():

    # Título del menú
    print("\n===================")
    print(" MENU PELICULAS ")
    print("===================")

    # Opciones disponibles
    print("1. Crear")       # Registrar película
    print("2. Buscar")      # Buscar película por ID
    print("3. Listar")      # Mostrar todas las películas
    print("4. Actualizar")  # Modificar película
    print("5. Eliminar")    # Borrar película
    print("6. Salir")       # Finalizar programa

    # Retorna la opción ingresada por teclado
    return input("Seleccione: ")

# Función principal del cliente
def ejecutar_cliente():


    # Crea la conexión con el servidor XML-RPC
    #
    # "servidor" corresponde al nombre del servicio
    # definido en docker-compose
    #
    # 9000 es el puerto donde escucha el servidor
    cliente = xmlrpc.client.ServerProxy(
        "http://servidor:9000/"
    )

    # Mantiene el cliente activo
    # hasta que el usuario seleccione salir
    while True:
        # Muestra el menú
        opcion = menu()

        # Crear película
        if opcion == "1":

            # Solicita datos
            nombre = input("Nombre: ")

            genero = input("Genero: ")

            # Ejecuta la función remota
            # del servidor
            respuesta = cliente.crear_pelicula(
                nombre,
                genero
            )

            # Muestra respuesta
            print(respuesta)

        # Buscar película
        elif opcion == "2":

            # Solicita el ID de búsqueda
            id = int(input("ID de la pelicula: "))

            # Llama a la función remota buscar_pelicula()
            respuesta = cliente.buscar_pelicula(
                id
            )

            # Muestra resultado
            print(respuesta)

        # Listar películas
        elif opcion == "3":

            # Llama a la función remota
            # listar_peliculas()
            respuesta = cliente.listar_peliculas()

            # Imprime películas recibidas
            print(respuesta)

        # Actualizar película
        elif opcion == "4":

            # Solicita ID
            id = int(input("ID: "))

            # Solicita nuevos datos
            nombre = input("Nuevo nombre: ")

            genero = input("Nuevo genero: ")

            # Ejecuta actualización en servidor
            respuesta = cliente.actualizar_pelicula(
                id,
                nombre,
                genero
            )

            # Muestra resultado
            print(respuesta)

        # Eliminar película
        elif opcion == "5":

            # Solicita ID a eliminar
            id = int(input("ID: "))
            # Llama al método remoto
            respuesta = cliente.eliminar_pelicula(
                id
            )
            # Muestra respuesta
            print(respuesta)

        # Salir
        elif opcion == "6":
            print("Saliendo...")

            # Rompe el ciclo
            break

        # Opción incorrecta
        else:
            print("Opcion incorrecta")

# Ejecuta el cliente
# solamente si este archivo es ejecutado directamente
if __name__ == "__main__":


    ejecutar_cliente()