import json
import os

# Archivo donde los datos se guardaran
ARCHIVO = "estudiantes.json"

# Lista de estudiantes
estudiantes = []


def cargar_estudiantes():
    """
    Carga los estudiantes desde un archivo JSON si existe.
    """
    global estudiantes
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            estudiantes = json.load(f)
    else:
        estudiantes = []


def guardar_estudiantes():
    """
    aqui gyardara a los estudiantes en un archivo JSON.
    """
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(estudiantes, f, indent=4, ensure_ascii=False)


def agregar_estudiante():
    """
    Se agregara lista de los estudiantes.
    """
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))

    calificaciones = []
    for i in range(4):  # 4 materias
        materia = input(f"Ingrese el nombre de la materia {i+1}: ")
        nota = float(input(f"Ingrese la calificación de {materia}: "))
        calificaciones.append({"materia": materia, "nota": nota})

    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "calificaciones": calificaciones
    }
    estudiantes.append(estudiante)
    guardar_estudiantes()
    print(f"Estudiante {nombre} agregado y guardado.\n")


def eliminar_estudiante():
    """
    Elimina un estudiante de la lista por su nombre.
    """
    nombre = input("Ingrese el nombre del estudiante a eliminar: ")
    for estudiante in estudiantes:
        if estudiante["nombre"].lower() == nombre.lower():
            estudiantes.remove(estudiante)
            guardar_estudiantes()
            print(f"Estudiante {nombre} eliminado y cambios guardados.\n")
            return
    print(f"No se encontró al estudiante con nombre: {nombre}\n")


def promedio_estudiante():
    """
    Calcula el promedio de las calificaciones de un estudiante por nombre.
    """
    nombre = input("Ingrese el nombre del estudiante para calcular su promedio: ")
    for estudiante in estudiantes:
        if estudiante["nombre"].lower() == nombre.lower():
            notas = [c["nota"] for c in estudiante["calificaciones"]]
            promedio = sum(notas) / len(notas)
            print(f"El promedio de {nombre} es: {promedio:.2f}\n")
            return
    print(f"No se encontró al estudiante con nombre: {nombre}\n")


def mostrar_estudiantes():
    """
    Muestra la lista de todos los estudiantes.
    """
    if not estudiantes:
        print("No hay estudiantes registrados.\n")
        return

    print("Lista de estudiantes:")
    for est in estudiantes:
        print(f"- {est['nombre']} (Edad: {est['edad']})")
        for c in est["calificaciones"]:
            print(f"   {c['materia']}: {c['nota']}")
    print()


# --- Menú interactivo ---
def menu():
    cargar_estudiantes()  # Cargar estudiantes al iniciar

    while True:
        print("===== MENÚ PRINCIPAL =====")
        print("1. Agregar estudiante")
        print("2. Eliminar estudiante")
        print("3. Calcular promedio de un estudiante")
        print("4. Mostrar todos los estudiantes")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            eliminar_estudiante()
        elif opcion == "3":
            promedio_estudiante()
        elif opcion == "4":
            mostrar_estudiantes()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.\n")


# Ejecutar menú
menu()

