# Analisis TP7 - Grafos

## 1. Que resolvimos

Modelamos los equipos como un **grafo** para poder relacionarlos entre si. La estructura esta en `estructuras/grafo.py` y el armado del grafo de equipos en `servicios/grafo_equipos.py`. Desde el menu, la opcion 11 muestra con que equipos esta conectado un equipo y que tan parecidos son.

## 2. Modelo

| Elemento | Que representa |
|---|---|
| Vertice | un equipo (clave: su nombre, valor: el objeto `Equipo`) |
| Arista | dos equipos parecidos |
| Peso | que tan distintos son: a menor peso, mas parecidos |
| Tipo | **no dirigido** (si A se parece a B, B se parece a A) y **pesado** |

### Calculo del peso

```
peso = |popularidad A - popularidad B| + |titulos A - titulos B|
       + 15 si son de ligas distintas
       + 10 si tienen estilo distinto
```

Son los mismos criterios que usa la opcion 5 de recomendaciones (liga, estilo, popularidad, titulos), pero ahora combinados en un solo numero. El peso nunca es negativo, lo cual importa para usar Dijkstra mas adelante.

### Que conexiones se crean

Conectar todos con todos daria casi 500.000 aristas. En cambio, cada equipo propone conectarse con sus **5 equipos mas parecidos**. Como la arista no tiene direccion, un equipo puede terminar con mas de 5 vecinos si otros lo eligen a el.

## 3. Representacion: lista de adyacencia

Cada vertice guarda la lista de sus vecinos como `(vecino, peso)`.

| | Lista de adyacencia | Matriz de adyacencia |
|---|---|---|
| Memoria | O(V + E) | O(V²) |
| Con nuestros datos | 1000 vertices + 2892 aristas | 1.000.000 de celdas, casi todas vacias |
| Recorrer vecinos de un vertice | O(grado) | O(V) |
| Preguntar si hay arista A-B | O(grado) | O(1) |

Elegimos la lista porque el grafo es **ralo**: cada equipo tiene entre 5 y 11 vecinos de 1000 posibles. BFS, DFS y Dijkstra recorren vecinos todo el tiempo, y ahi la lista es mas eficiente. La matriz solo ganaria si el grafo fuera denso o si preguntaramos por aristas puntuales todo el tiempo.

## 4. Datos medidos

Con los 1000 equipos del proyecto y 5 conexiones por equipo:

- Vertices: 1000. Aristas: 2892.
- Grado de cada equipo: minimo 5, maximo 11, promedio 5,78.
- El grafo es **conexo**: hay una sola componente, asi que existe camino entre cualquier par de equipos. Esto sirve para BFS (TP8) y camino minimo (TP9).
- Armarlo tarda unos 0,44 s, porque compara cada equipo contra todos los demas: O(n²) comparaciones mas ordenar los candidatos. Se hace una sola vez al iniciar el programa.

## 5. Pruebas

`tests/test_grafo.py` verifica: alta de vertices y aristas, que la arista vale en ambos sentidos, que no se repiten aristas ni se crean bucles, el error al conectar un vertice inexistente, el calculo de distancia entre equipos y que cada equipo se conecta con el mas parecido.
