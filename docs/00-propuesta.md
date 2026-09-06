# Propuesta del Proyecto
## Nombre del proyecto
SportMatch
## Dominio elegido
Deportes
Hay mucha información sobre deportes para explotar la app.
## Problema que resuelve
Descubrir equipos de fútbol que puedan interesarle según gustos, rivalidades, ligas, país, historia o nivel competitivo, sin tener que investigar todo manualmente.
## Usuario objetivo
Persona que está empezando a interesarse por este deporte y quiere conocer equipos.
##5 Funcionalidades Iniciales**
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
| main()                      |
+-----------------------------+
```

Relacion:

```text
terminal.py usa muchos objetos Equipo
```
