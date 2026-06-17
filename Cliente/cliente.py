# Importa la librería XML-RPC para poder conectarse a un servidor remoto
import xmlrpc.client


# Función que muestra el menú de opciones al usuario
def menu():

    # Imprime el título del menú
    print("\n===================")
    print(" MENU PELICULAS ")
    print("===================")


    # Opciones disponibles del CRUD
    print("1. Crear")       # Registrar una película
    print("2. Listar")      # Mostrar películas existentes
    print("3. Actualizar")  # Modificar una película
    print("4. Eliminar")    # Borrar una película
    print("5. Salir")       # Cerrar el programa


    # Solicita al usuario una opción y la retorna
    return input("Seleccione: ")





# Función principal del cliente
def ejecutar_cliente():


    # Crea una conexión con el servidor XML-RPC
    # "servidor" es el nombre del contenedor en Docker
    # 9000 es el puerto donde escucha el servidor RPC
    cliente = xmlrpc.client.ServerProxy(
        "http://servidor:9000/"
    )



    # Mantiene el cliente funcionando hasta que el usuario salga
    while True:


        # Muestra el menú y guarda la opción seleccionada
        opcion = menu()



        # Si el usuario selecciona crear película
        if opcion == "1":


            # Solicita datos de la película
            nombre = input("Nombre: ")

            genero = input("Genero: ")



            # Llama la función remota del servidor
            # Envía nombre y género como parámetros
            respuesta = cliente.crear_pelicula(
                nombre,
                genero
            )



            # Muestra la respuesta enviada por el servidor
            print(respuesta)





        # Si el usuario selecciona listar películas
        elif opcion == "2":



            # Ejecuta la función listar_peliculas()
            # que existe en el servidor
            respuesta = cliente.listar_peliculas()



            # Imprime las películas recibidas
            print(respuesta)





        # Si el usuario selecciona actualizar
        elif opcion == "3":


            # Solicita el ID de la película a modificar
            # int convierte el texto ingresado a número
            id = int(input("ID: "))


            # Solicita nuevos datos
            nombre = input("Nuevo nombre: ")

            genero = input("Nuevo genero: ")



            # Envía los datos al servidor
            # para ejecutar actualizar_pelicula()
            respuesta = cliente.actualizar_pelicula(
                id,
                nombre,
                genero
            )



            # Muestra resultado
            print(respuesta)





        # Si el usuario selecciona eliminar
        elif opcion == "4":


            # Solicita el ID que se quiere eliminar
            id = int(input("ID: "))



            # Llama al servidor para eliminar
            respuesta = cliente.eliminar_pelicula(
                id
            )


            # Muestra resultado
            print(respuesta)





        # Salir del programa
        elif opcion == "5":


            print("Saliendo...")


            # Rompe el ciclo while
            break





        # Si escribe una opción diferente
        else:

            print("Opcion incorrecta")






# Verifica que este archivo sea ejecutado directamente
if __name__ == "__main__":


    # Inicia el cliente RPC
    ejecutar_cliente()