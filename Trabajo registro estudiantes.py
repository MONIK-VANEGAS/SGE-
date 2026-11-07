estudiantes = []
contador_estudiantes = 0

bandera_salir = False

def mostrar_menu():
    """Muestra las opciones disponibles en el sistema."""
    print("\n===================================")
    print(" SISTEMA DE GESTIÓN DE ESTUDIANTES")
    print("===================================")
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante por ID")
    print("4. Salir")


def leer_entero(mensaje):
    """Solicita un número entero y valida que la entrada sea correcta."""
    while True:
        entrada = input(mensaje).strip()
        try:
            numero = int(entrada)
            return numero
        except ValueError:
            print("Entrada no válida. Debe ingresar un número entero.")


def mostrar_estudiante(estudiante):
    """Muestra los datos de un estudiante recibido como parámetro."""
    print("-----------------------------------")
    print("ID:", estudiante["id"])
    print("Nombre:", estudiante["nombre"])
    print("Edad:", estudiante["edad"])
    print("Carrera:", estudiante["carrera"])


def agregar_estudiante():
    """Solicita y registra los datos de un estudiante."""
    global contador_estudiantes

    print("\n--- Agregar estudiante ---")
    identificacion = leer_entero("Ingrese el ID del estudiante: ")

    for estudiante in estudiantes:
        if estudiante["id"] == identificacion:
            print("Ya existe un estudiante registrado con ese ID.")
            return

    nombre = input("Ingrese el nombre completo: ").strip()
    while nombre == "":
        print("El nombre no puede estar vacío.")
        nombre = input("Ingrese el nombre completo: ").strip()

    edad = leer_entero("Ingrese la edad: ")
    while edad <= 0:
        print("La edad debe ser mayor que cero.")
        edad = leer_entero("Ingrese la edad: ")

    carrera = input("Ingrese la carrera: ").strip()
    while carrera == "":
        print("La carrera no puede estar vacía.")
        carrera = input("Ingrese la carrera: ").strip()

    nuevo_estudiante = {
        "id": identificacion,
        "nombre": nombre,
        "edad": edad,
        "carrera": carrera
    }

    estudiantes.append(nuevo_estudiante)
    contador_estudiantes += 1

    print("Estudiante agregado correctamente.")


def mostrar_estudiantes():
    """Muestra todos los estudiantes registrados."""
    print("\n--- Lista de estudiantes ---")

    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
    else:

        for estudiante in estudiantes:
            mostrar_estudiante(estudiante)

        print("-----------------------------------")
        print("Total de estudiantes:", len(estudiantes))


def buscar_estudiante():
    """Busca un estudiante usando su ID."""
    print("\n--- Buscar estudiante ---")

    if contador_estudiantes == 0:
        print("No hay estudiantes registrados para buscar.")
        return

    identificacion = leer_entero("Ingrese el ID que desea buscar: ")
    encontrado = False

    for estudiante in estudiantes:
        if estudiante["id"] == identificacion:
            mostrar_estudiante(estudiante)
            encontrado = True
            break

    if encontrado:
        print("Búsqueda finalizada: estudiante encontrado.")
    else:
        print("No se encontró un estudiante con ese ID.")


def ejecutar_sistema():
    """Controla el menú principal hasta que se seleccione salir."""
    global bandera_salir

    while not bandera_salir:
        mostrar_menu()
        opcion = leer_entero("Seleccione una opción: ")

        if opcion == 1:
            agregar_estudiante()
        elif opcion == 2:
            mostrar_estudiantes()
        elif opcion == 3:
            buscar_estudiante()
        elif opcion == 4:
            bandera_salir = True
            print("Gracias por utilizar el sistema. ¡Hasta pronto!")
        else:
            print("Opción no válida. Seleccione una opción del 1 al 4.")


if __name__ == "__main__":
    ejecutar_sistema()