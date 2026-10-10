import json
import os
import sys
import time
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from modelos.equipo import Equipo
from estructuras.arbol_binario_busqueda import ArbolBinarioBusqueda


def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def mostrar_presentacion():
    pelota = [
        "⚽          ",
        "  ⚽        ",
        "    ⚽      ",
        "      ⚽    ",
        "        ⚽  ",
        "          ⚽",
        "        ⚽  ",
        "      ⚽    ",
        "    ⚽      ",
        "  ⚽        ",
    ]

    inicio = time.time()
    posicion = 0

    while time.time() - inicio < 2:
        limpiar_pantalla()
        print("=" * 40)
        print("        SPORTMATCH")
        print("=" * 40)
        print()
        print("          CARGANDO")
        print()
        print("     " + pelota[posicion])
        print()
        print("Cargando sistema de recomendaciones...")

        posicion = posicion + 1

        if posicion == len(pelota):
            posicion = 0

        time.sleep(0.25)

    limpiar_pantalla()


def cargar_datos():
    equipos = []
    carpeta_datos = Path(__file__).resolve().parent.parent / "datos"

    for archivo_json in carpeta_datos.rglob("*.json"):
        with open(archivo_json, "r", encoding="utf-8") as f:
            datos = json.load(f)

        for d in datos:
            equipos.append(
                Equipo(
                    d["nombre"],
                    d["pais"],
                    d["liga"],
                    d["fundacion"],
                    d["popularidad"],
                    d["titulos"],
                    d["estilo"],
                )
            )

    return equipos


def crear_arbol_por_nombre(equipos):
    arbol = ArbolBinarioBusqueda()

    for equipo in equipos:
        arbol.insertar(equipo.nombre, equipo)

    return arbol


def medir_creacion_arbol(equipos):
    inicio = time.perf_counter()
    arbol = crear_arbol_por_nombre(equipos)
    tiempo_total = time.perf_counter() - inicio

    return arbol, tiempo_total


def mostrar_menu():
    print("=" * 40)
    print(" SISTEMA DE RECOMENDACIONES")
    print("=" * 40)
    print("1. Buscar equipo")
    print("2. Listar equipos")
    print("3. Filtrar por pais")
    print("4. Filtrar por liga")
    print("5. Mostrar equipos relacionados")
    print("6. Buscar por nombre con arbol binario")
    print("7. Mostrar equipos ordenados por nombre")
    print("0. Salir")
    print("-" * 40)


def formatear_tiempo(segundos):
    return f"{segundos * 1000:.6f} ms"


def buscar(equipos):
    nombre = input("Equipo a buscar: ")
    inicio = time.perf_counter()
    cantidad = 0

    for e in equipos:
        if nombre.lower() in e.nombre.lower():
            print(e)
            cantidad = cantidad + 1

    tiempo_total = time.perf_counter() - inicio

    print("Fin de resultados.")
    print(f"Coincidencias encontradas: {cantidad}")
    print(f"Tiempo de busqueda secuencial: {formatear_tiempo(tiempo_total)}")


def buscar_secuencial_exacta(equipos, nombre):
    pasos = 0

    for equipo in equipos:
        pasos = pasos + 1

        if equipo.nombre.lower() == nombre.lower():
            return equipo, pasos

    return None, pasos


def medir_busqueda_secuencial(equipos, nombre):
    inicio = time.perf_counter()
    equipo, pasos = buscar_secuencial_exacta(equipos, nombre)
    tiempo_total = time.perf_counter() - inicio

    return equipo, pasos, tiempo_total


def medir_busqueda_arbol(arbol, nombre):
    inicio = time.perf_counter()
    equipo, pasos = arbol.buscar(nombre)
    tiempo_total = time.perf_counter() - inicio

    return equipo, pasos, tiempo_total


def medir_ordenamiento_arbol(arbol):
    inicio = time.perf_counter()
    equipos_ordenados = arbol.inorden()
    tiempo_total = time.perf_counter() - inicio

    return equipos_ordenados, tiempo_total


def medir_ordenamiento_secuencial(equipos):
    inicio = time.perf_counter()
    equipos_ordenados = sorted(equipos, key=lambda equipo: equipo.nombre.lower())
    tiempo_total = time.perf_counter() - inicio

    return equipos_ordenados, tiempo_total


def buscar_con_arbol(equipos, arbol):
    nombre = input("Nombre exacto del equipo a buscar: ")

    equipo_arbol, pasos_arbol, tiempo_arbol = medir_busqueda_arbol(arbol, nombre)
    equipo_secuencial, pasos_secuencial, tiempo_secuencial = medir_busqueda_secuencial(
        equipos, nombre
    )

    if equipo_arbol is None:
        print("No se encontro el equipo.")
    else:
        print(equipo_arbol)

    print()
    print("Comparacion de estrategias:")
    print(
        f"Busqueda secuencial: {pasos_secuencial} pasos | "
        f"{formatear_tiempo(tiempo_secuencial)}"
    )
    print(
        f"Busqueda con arbol binario: {pasos_arbol} pasos | "
        f"{formatear_tiempo(tiempo_arbol)}"
    )

    if equipo_secuencial is None and equipo_arbol is None:
        print("Ambas estrategias recorrieron hasta no encontrar coincidencias.")
    else:
        print("Ambas estrategias encontraron el mismo equipo.")


def listar(equipos):
    for i, e in enumerate(equipos, 1):
        print(f"{i}. {e}")


def listar_ordenados_por_nombre(equipos, arbol):
    equipos_ordenados, tiempo_arbol = medir_ordenamiento_arbol(arbol)
    _, tiempo_secuencial = medir_ordenamiento_secuencial(equipos)

    for i, equipo in enumerate(equipos_ordenados, 1):
        print(f"{i}. {equipo}")

    print()
    print("Tiempo de ordenamiento:")
    print(f"Recorrido inorden del arbol: {formatear_tiempo(tiempo_arbol)}")
    print(f"Ordenamiento secuencial con sorted: {formatear_tiempo(tiempo_secuencial)}")


def mostrar_recorridos_arbol(arbol):
    print("Recorrido inorden:")
    for equipo in arbol.inorden():
        print(equipo.nombre)

    print()
    print("Recorrido preorden:")
    for equipo in arbol.preorden():
        print(equipo.nombre)

    print()
    print("Recorrido postorden:")
    for equipo in arbol.postorden():
        print(equipo.nombre)


def filtrar_por_pais(equipos):
    pais = input("Pais a filtrar: ")

    for e in equipos:
        if pais.lower() in e.pais.lower():
            print(e)


def filtrar_por_liga(equipos):
    liga = input("Liga a filtrar: ")

    for e in equipos:
        if liga.lower() in e.liga.lower():
            print(e)


def recomendar(equipos):
    nombre = input("Equipo base para recomendar: ")
    equipo_base = None

    for e in equipos:
        if nombre.lower() in e.nombre.lower():
            equipo_base = e
            break

    if equipo_base is None:
        print("No se encontro el equipo.")
        return

    print("Equipos recomendados:")

    cantidad = 0

    for e in equipos:
        if e.nombre != equipo_base.nombre:
            misma_liga = e.liga == equipo_base.liga
            mismo_estilo = e.estilo == equipo_base.estilo
            popularidad_parecida = abs(e.popularidad - equipo_base.popularidad) <= 10
            titulos_parecidos = abs(e.titulos - equipo_base.titulos) <= 5

            if misma_liga and (mismo_estilo or popularidad_parecida or titulos_parecidos):
                print(e)
                cantidad = cantidad + 1

    if cantidad == 0:
        print("No se encontraron recomendaciones.")


def main():
    mostrar_presentacion()
    equipos = cargar_datos()
    arbol_por_nombre, tiempo_creacion_arbol = medir_creacion_arbol(equipos)
    print(
        f"Arbol por nombre creado con {len(equipos)} equipos en "
        f"{formatear_tiempo(tiempo_creacion_arbol)}"
    )

    while True:
        mostrar_menu()
        opcion = input("Opcion: ")

        if opcion == "1":
            buscar(equipos)
        elif opcion == "2":
            listar(equipos)
        elif opcion == "3":
            filtrar_por_pais(equipos)
        elif opcion == "4":
            filtrar_por_liga(equipos)
        elif opcion == "5":
            recomendar(equipos)
        elif opcion == "6":
            buscar_con_arbol(equipos, arbol_por_nombre)
        elif opcion == "7":
            listar_ordenados_por_nombre(equipos, arbol_por_nombre)
        elif opcion == "0":
            print("Hasta luego!")
            break


if __name__ == "__main__":
    main()
