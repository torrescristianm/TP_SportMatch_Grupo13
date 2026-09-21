# Analisis TP3 - Arbol Binario de Busqueda

## 1. Que resolvimos

En SportMatch incorporamos un **arbol binario de busqueda** para buscar equipos por nombre exacto.

Antes, las busquedas del proyecto se resolvian recorriendo la lista de equipos de forma secuencial. Eso funciona bien con pocos datos, pero al crecer la cantidad de equipos tambien crece la cantidad de comparaciones necesarias.

Con el ABB, cada equipo se inserta usando su nombre como clave. Despues, cuando el usuario busca un equipo por nombre exacto desde la opcion 6 del menu, el sistema compara dos estrategias:

- busqueda secuencial sobre la lista de equipos;
- busqueda en arbol binario usando la clave nombre.

El sistema muestra el equipo encontrado, la cantidad de pasos y el tiempo que tardo cada busqueda.

## 2. Clave de ordenamiento

La clave elegida fue el **nombre del equipo**.

Elegimos esa clave porque la funcionalidad principal del proyecto permite buscar equipos por nombre. Entonces tiene sentido ordenar el arbol por ese mismo dato: si el usuario ingresa `Boca Juniors`, `River Plate`, `Barcelona` o cualquier otro equipo, el ABB puede decidir en cada nodo si sigue por la izquierda o por la derecha segun el orden alfabetico.

La comparacion se hace pasando los nombres a minuscula para que la busqueda no dependa de mayusculas o minusculas. Por ejemplo, `river plate`, `River Plate` y `RIVER PLATE` apuntan a la misma clave logica.

## 3. Prueba del arbol

El arbol se implemento en `estructuras/arbol_binario_busqueda.py` y se prueba con `tests/test_arbol_binario_busqueda.py`.

Las pruebas verifican que:

- el ABB encuentra un equipo insertado;
- devuelve `None` cuando el equipo no existe;
- el recorrido inorden devuelve los equipos ordenados alfabeticamente.

## 4. Comparacion de tiempos

Los tiempos son reales, medidos sobre el proyecto actual con `time.perf_counter()`.

Para reducir variaciones muy chicas del sistema operativo, cada busqueda y cada ordenamiento se midio como promedio de 1000 repeticiones. Los datos actuales incluyen **1000 equipos**: equipos reales cargados por pais/liga y equipos ficticios de prueba en `datos/generados/equipos_extra.json`.

### Busqueda por nombre exacto

| N elementos | Equipo buscado | Secuencial (ms) | Pasos secuencial | ABB (ms) | Pasos ABB | Crear ABB (ms) |
|---:|---|---:|---:|---:|---:|---:|
| 100 | Independiente Norte 01 | 0.006246 | 100 | 0.000671 | 15 | 0.055700 |
| 1000 | Boston River | 0.059014 | 1000 | 0.000411 | 9 | 0.704100 |

### Ordenamiento por nombre

Tambien se agrego la opcion 7 del menu, que muestra los equipos ordenados alfabeticamente. Ahi se comparan:

- recorrido **inorden** del ABB;
- ordenamiento de la lista con `sorted`.

| N elementos | Inorden ABB (ms) | `sorted` secuencial (ms) |
|---:|---:|---:|
| 100 | 0.005030 | 0.006304 |
| 1000 | 0.053202 | 0.083343 |

Importante: el tiempo de inorden no incluye crear el arbol. El arbol ya se crea al iniciar la aplicacion. Si se quisiera ordenar una sola vez desde cero, habria que sumar tambien el costo de construccion del ABB.

## 5. Analisis de complejidad

- **Busqueda secuencial:** O(n). En el peor caso revisa todos los equipos hasta encontrar el buscado o confirmar que no existe.
- **Busqueda en ABB:** O(log n) promedio si el arbol queda razonablemente balanceado. En el peor caso puede ser O(n), por ejemplo si los datos se insertan ya ordenados y el arbol se degenera.
- **Insercion en ABB:** O(log n) promedio, O(n) peor caso.
- **Recorrido inorden, preorden y postorden:** O(n), porque visitan cada nodo una vez.
- **Ordenamiento con `sorted`:** O(n log n). Es eficiente, pero ordena la lista en ese momento.
- **Recorrido inorden para obtener datos ordenados:** O(n), siempre que el ABB ya este creado.

En este proyecto no implementamos busqueda binaria sobre lista ordenada. La comparacion principal del TP3 es entre la busqueda secuencial y la busqueda con arbol binario.

## 6. Conclusion

Para busquedas por nombre exacto, el ABB conviene cuando vamos a realizar muchas busquedas sobre la misma coleccion de equipos. La construccion del arbol tiene un costo inicial, pero se paga una sola vez al iniciar el programa.

Con 1000 equipos, la busqueda secuencial del ejemplo recorrio 1000 pasos, mientras que el ABB encontro el equipo en 9 pasos. Aunque los tiempos en milisegundos pueden variar mucho porque el dataset todavia es chico, la diferencia en pasos muestra mejor la ventaja teorica del arbol.

Para listar equipos ordenados, el recorrido inorden tambien resulta util porque aprovecha la estructura del ABB ya creada. Si no tuvieramos el arbol, `sorted` seria una buena opcion para ordenar la lista directamente.

## 7. Errores o dudas que tuvimos

Durante el trabajo aparecieron algunas dudas importantes:

- Al principio habia pocos equipos, entonces la busqueda secuencial podia parecer mas rapida que el ABB en algunos casos. Esto pasa porque con pocos datos las diferencias son minimas y el costo de llamar funciones tambien influye.
- Para comparar mejor, ampliamos la base a 1000 equipos. Aun asi, los tiempos en milisegundos siguen siendo muy chicos, por eso agregamos tambien la cantidad de pasos.
- Separar los equipos por pais y liga en varios JSON hizo que el proyecto quedara mas ordenado y facil de ampliar.
- Se agregaron logs de tiempo para busqueda, creacion del arbol y ordenamiento, usando `time.perf_counter()`.
