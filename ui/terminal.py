import json
import os
import sys
import time
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from modelos.equipo import Equipo


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

    while time.time() - inicio < 5:
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
    with open("datos/equipos.json", "r", encoding="utf-8") as f:
        datos = json.load(f)

    equipos = []

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


def mostrar_menu():
    print("=" * 40)
    print(" SISTEMA DE RECOMENDACIONES")
    print("=" * 40)
    print("1. Buscar equipo")
    print("2. Listar equipos")
    print("3. Filtrar por pais")
    print("4. Filtrar por liga")
    print("5. Mostrar equipos relacionados")
    print("0. Salir")
    print("-" * 40)


def buscar(equipos):
    nombre = input("Equipo a buscar: ")

    for e in equipos:
        if nombre.lower() in e.nombre.lower():
            print(e)

    print("Fin de resultados.")


def listar(equipos):
    for i, e in enumerate(equipos, 1):
        print(f"{i}. {e}")


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
        elif opcion == "0":
            print("Hasta luego!")
            break


if __name__ == "__main__":
    main()
