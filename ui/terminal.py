import json
import os
import sys
import time
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from modelos.equipo import Equipo
from estructuras.arbol_binario_busqueda import ArbolBinarioBusqueda
from estructuras.arbol_avl import ArbolAVL
from estructuras.arbol_general import ArbolGeneral
from estructuras.heap import HeapMaximos


def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def mostrar_presentacion():
    pelota = [
        "⚽         ",
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


def crear_arbol_avl(equipos):
    arbol = ArbolAVL()

    for equipo in equipos:
        arbol.insertar(equipo.nombre, equipo)

    return arbol


def crear_arbol_general_categorias(equipos):
    arbol = ArbolGeneral()
    raiz = arbol.insertar_raiz("Categorías de Fútbol / Ligas")

    # Agrupar equipos por país o liga para armar la jerarquía
    paises = {}
    for equipo in equipos:
        if equipo.pais not in paises:
            paises[equipo.pais] = arbol.agregar_hijo(raiz, equipo.pais)
        
        # Opcional: Agregar ligas o equipos como sub-hijos
        # Aquí agregamos el equipo como hijo del país correspondiente
        arbol.agregar_hijo(paises[equipo.pais], f"{equipo.nombre} ({equipo.liga})")

    return arbol


def crear_heap_prioridad(equipos):
    items = [(e.prioridad(), e.nombre.lower(), e) for e in equipos]

    return HeapMaximos.desde_lista(items)


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
    print("6. Buscar por nombre con arbol binario (BST)")
    print("7. Mostrar equipos ordenados por nombre (BST)")
    print("8. Buscar equipo con Árbol AVL")
    print("9. Explorar categorías (Árbol General)")
    print("10. Ver Top N equipos (Heap)")
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


def buscar_con_avl(arbol_avl):
    nombre = input("Nombre exacto del equipo a buscar con AVL: ")
    inicio = time.perf_counter()
    resultado, pasos = arbol_avl.buscar(nombre)
    tiempo_total = time.perf_counter() - inicio

    if resultado:
        print(f"\n¡Encontrado en {pasos} pasos (Altura AVL: {arbol_avl.obtener_altura()}):")
        print(resultado)
    else:
        print("\nEquipo no encontrado en el árbol AVL.")
    print(f"Tiempo de búsqueda AVL: {formatear_tiempo(tiempo_total)}")


def explorar_arbol_general(arbol_general):
    print("\n--- EXPLORANDO CATEGORÍAS (Árbol General - Amplitud) ---")
    elementos = arbol_general.amplitud()
    for i, elem in enumerate(elementos[:30], 1):  # Limitamos vista si es muy largo
        print(f"{i}. {elem}")
    if len(elementos) > 30:
        print(f"... y {len(elementos) - 30} nodos más en la jerarquía.")
    
    print(f"\nCantidad total de nodos en la jerarquía: {arbol_general.cantidad_nodos()}")


def ver_top_n(equipos, heap):
    texto = input("Cuantos equipos queres ver (Top N): ")

    if not texto.isdigit() or int(texto) == 0:
        print("Ingresa un numero entero mayor a 0.")
        return

    n = int(texto)

    inicio = time.perf_counter()
    top_heap = heap.top_n(n)
    tiempo_heap = time.perf_counter() - inicio

    inicio = time.perf_counter()
    top_sorted = sorted(equipos, key=lambda e: (-e.prioridad(), e.nombre.lower()))[:n]
    tiempo_sorted = time.perf_counter() - inicio

    print(f"\nTop {len(top_heap)} por prioridad (popularidad + titulos x 2):")
    for i, equipo in enumerate(top_heap, 1):
        print(f"{i}. {equipo} | prioridad: {equipo.prioridad()}")

    print()
    print("Comparacion de estrategias:")
    print(f"Heap (extraer {n} maximos): {formatear_tiempo(tiempo_heap)}")
    print(f"Ordenar todo con sorted: {formatear_tiempo(tiempo_sorted)}")

    if top_heap == top_sorted:
        print("Ambas estrategias devolvieron el mismo resultado.")


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
    
    # Inicializar estructuras (BST, AVL y Árbol General)
    arbol_por_nombre, tiempo_creacion_arbol = medir_creacion_arbol(equipos)
    arbol_avl = crear_arbol_avl(equipos)
    arbol_general = crear_arbol_general_categorias(equipos)
    heap_prioridad = crear_heap_prioridad(equipos)

    print(
        f"Arbol BST por nombre creado con {len(equipos)} equipos en "
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
        elif opcion == "8":
            buscar_con_avl(arbol_avl)
        elif opcion == "9":
            explorar_arbol_general(arbol_general)
        elif opcion == "10":
            ver_top_n(equipos, heap_prioridad)
        elif opcion == "0":
            print("Hasta luego!")
            break


if __name__ == "__main__":
    main()
