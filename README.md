# SportMatch

Sistema de recomendaciones de equipos de futbol. Permite buscar, listar, filtrar y recomendar equipos de distintas ligas usando datos cargados desde archivos JSON.

## Integrantes

- Marcos Rivero
- Marcelo Albarenque
- Cristian Matias Torres

## Como ejecutar

1. Clonar el repositorio
2. Ejecutar: `python ui/terminal.py`

## Datos cargados

Los equipos se organizan en archivos JSON separados por pais y liga dentro de `datos/`.

Ligas incluidas:

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

El archivo `datos/generados/equipos_extra.json` contiene equipos ficticios de prueba para llegar a 1000 registros y poder comparar mejor la busqueda secuencial contra el arbol binario.

Se incluye arbol avl y arbol n-ario

Se modifica terminal.py 


## Estado

- TP0: Completado
- TP1: Completado
- TP3: Completado
- TP4: Completado
- TP5: Completado

## Documentación

- [Ver Propuesta del Proyecto y Diagramas](./docs/00-propuesta.md)
- [Diagrama de Flujo](./diagrama_flujo.png)
