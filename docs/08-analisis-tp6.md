# Analisis TP6 - Heap (cola de prioridad)

## 1. Que resolvimos

Agregamos una consulta **Top N** (opcion 10 del menu) que muestra los N equipos con mayor prioridad. La estructura es una **heap binaria de maximos** implementada por el grupo en `estructuras/heap.py`, sin usar `heapq`.

## 2. Funcion de prioridad

```
prioridad = popularidad + titulos * 2
```

Esta definida en `Equipo.prioridad()`. Combina dos datos que ya tiene cada equipo: la popularidad (0 a 100) y los titulos, que pesan el doble para que un equipo muy ganador no quede por debajo de uno solo popular. Si dos equipos empatan, sale primero el de nombre menor alfabeticamente, asi el resultado siempre es el mismo.

## 3. Como funciona la heap

Es un arbol binario completo guardado en una lista. Para el elemento en el indice `i`, su padre esta en `(i - 1) // 2` y sus hijos en `2i + 1` y `2i + 2`. La regla es que cada padre tiene mas prioridad que sus hijos, por lo que el maximo siempre esta en la raiz.

| Operacion | Que hace | Costo |
|---|---|---|
| `insertar` | agrega al final y lo sube (`_subir`) | O(log n) |
| `ver_maximo` | lee la raiz | O(1) |
| `extraer_maximo` | saca la raiz, pone el ultimo en su lugar y lo baja (`_bajar`) | O(log n) |
| `desde_lista` | construye la heap bajando los nodos internos | O(n) |
| `top_n(n)` | copia la lista y extrae n veces | O(n + n log n) |

## 4. Por que heap y no ordenar todo

Para obtener los N mejores de un conjunto de `m` equipos:

- Ordenar todo con `sorted` cuesta O(m log m), aunque N sea chico.
- Con la heap ya construida, extraer N cuesta O(N log m) mas la copia O(m) para no destruir la heap.

Cuando N es mucho menor que m, la heap hace menos trabajo. Ademas, si llegan equipos nuevos, `insertar` cuesta O(log n) y no hace falta reordenar todo.

## 5. Mediciones

Medido sobre los 1000 equipos del proyecto, promedio de 200 repeticiones con `time.perf_counter()`:

| Consulta | Heap | `sorted` |
|---|---|---|
| Top 10 | 0.035 ms | 0.281 ms |
| Top 100 | 0.326 ms | 0.297 ms |

Construir la heap con `desde_lista` tardo 0.498 ms.

Con Top 10 la heap es unas 8 veces mas rapida. Con Top 100 ya es equivalente: cuando N crece, el costo de extraer N veces se acerca al de ordenar todo. Con pocos datos y N grande, `sorted` de Python puede ganar porque esta implementado en C.

## 6. Pruebas

`tests/test_heap.py` verifica: heap vacia, orden de extraccion, desempate por nombre, que `top_n` no modifica la heap, `top_n` mayor a la cantidad de elementos, que `desde_lista` coincide con `sorted` sobre 200 valores aleatorios, y la prioridad de un equipo.
