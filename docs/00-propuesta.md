# Propuesta del Proyecto

## Nombre del proyecto

SportMatch

## Dominio elegido

Deportes
Hay mucha información sobre deportes para explotar la app.

## Problema que resuelve

Descubrir equipos de fútbol que puedan interesarle según gustos, rivalidades, ligas, país, historia o nivel competitivo, sin tener que investigar todo manualmente.

## Datos cargados

El sistema trabaja con archivos JSON separados por pais y liga. Actualmente incluye equipos de:

- Primera Division Argentina
- B Nacional Argentina
- La Liga Espana
- Premier League Inglaterra
- Brasileirao Serie A
- Serie A Italia
- Bundesliga Alemania
- Ligue 1 Francia
- Primeira Liga Portugal
- Eredivisie Paises Bajos
- Liga MX Mexico
- Primera Division Uruguay
- MLS Estados Unidos
- Ligas adicionales de prueba generadas

Ademas de los equipos representativos cargados manualmente, el archivo `datos/generados/equipos_extra.json` agrega equipos ficticios de prueba. Estos datos permiten llegar a 1000 registros y comparar mejor el comportamiento de la busqueda secuencial contra el arbol binario.

## Usuario objetivo

Persona que está empezando a interesarse por este deporte y quiere conocer equipos.
##5 Funcionalidades Iniciales\*\*

1. **Buscar equipo por nombre**  
   El usuario ingresa el nombre o parte del nombre de un equipo y el sistema muestra los equipos que coinciden.
2. **Listar todos los equipos cargados**  
   El sistema muestra todos los equipos disponibles en la base de datos inicial.
3. **Filtrar equipos por país**  
   El usuario ingresa un país, por ejemplo Argentina, Brasil o España, y el sistema muestra los equipos pertenecientes a ese país.
4. **Filtrar equipos por liga**  
   El usuario ingresa una liga, por ejemplo Primera División Argentina, Brasileirão o La Liga, y el sistema muestra los equipos de esa competencia.
5. **Mostrar equipos recomendados o relacionados**  
   El usuario elige un equipo y el sistema recomienda otros equipos similares o relacionados según criterios como misma liga, mismo país, estilo de juego, popularidad o títulos.
6. **Buscar por nombre con árbol binario de búsqueda**  
   El sistema arma un árbol binario usando como clave de ordenamiento el nombre del equipo. Esta estructura permite buscar un equipo por nombre exacto y comparar la cantidad de pasos y el tiempo de ejecución contra la búsqueda secuencial.
7. **Listar equipos ordenados por nombre**  
   El sistema usa el recorrido inorden del árbol para mostrar los equipos en orden alfabético y registra el tiempo que tarda en obtener ese orden.

## Ejemplo de interacción (boceto de consola)

(Poné un ejemplo de cómo se vería la pantalla cuando el usuario usa el
programa)

## Diagrama inicial de clases

Modelo simple para la primera version del proyecto:

```text
+-----------------------------+
|           Equipo            |
+-----------------------------+
| nombre                      |
| pais                        |
| liga                        |
| fundacion                   |
| popularidad                 |
| titulos                     |
| estilo                      |
+-----------------------------+
| coincide_con_nombre(texto)  |
| __str__()                   |
+-----------------------------+
```

La clase `Equipo` representa a cada equipo de futbol cargado desde el archivo JSON.

El programa principal trabaja con una lista de objetos `Equipo`:

```text
+-----------------------------+
|        terminal.py          |
+-----------------------------+
| cargar_datos()              |
| mostrar_menu()              |
| buscar(equipos)             |
| listar(equipos)             |
| filtrar_por_pais(equipos)   |
| filtrar_por_liga(equipos)   |
| recomendar(equipos)         |
| crear_arbol_por_nombre()    |
| buscar_con_arbol()          |
| listar_ordenados_por_nombre()|
| main()                      |
+-----------------------------+
```

Relacion:

```text
terminal.py usa muchos objetos Equipo
terminal.py crea un ArbolBinarioBusqueda con esos equipos
```

## Árbol binario de búsqueda

Para la segunda version se incorpora un árbol binario de búsqueda.

Clave de ordenamiento elegida:

```text
nombre del equipo
```

Esta clave se eligió porque la búsqueda por nombre es una funcionalidad real del sistema. Una persona que conoce el nombre de un club puede buscarlo directamente.

Operaciones implementadas:

- Inserción de equipos en el árbol.
- Búsqueda por nombre exacto.
- Recorrido inorden.
- Recorrido preorden.
- Recorrido postorden.

Uso dentro de la app:

- La opción 6 del menú busca un equipo usando el árbol binario.
- La misma opción compara la cantidad de pasos y el tiempo de búsqueda contra la búsqueda secuencial.
- La opción 7 muestra los equipos ordenados alfabéticamente usando recorrido inorden.
- La opción 7 registra el tiempo del recorrido inorden y lo compara contra `sorted`.
