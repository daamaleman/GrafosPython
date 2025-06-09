# Implementación de Grafos en Python

![Estado del Proyecto](https://img.shields.io/badge/Estado-Activo-brightgreen) ![Python](https://img.shields.io/badge/Python-3.8+-blue) ![Licencia](https://img.shields.io/badge/Licencia-MIT-orange)

Bienvenido a la **Implementación de Grafos en Python**, un proyecto que ofrece una estructura de datos flexible para trabajar con grafos dirigidos y no dirigidos. Incluye funcionalidades para manipulación de grafos, recorridos (BFS y DFS), búsqueda de caminos y verificación de conectividad, todo diseñado para ser intuitivo y eficiente.

## 📋 Contenido
- [Características](#-características)
- [Instalación](#-instalación)
- [Uso](#-uso)
  - [Crear un Grafo](#crear-un-grafo)
  - [Agregar Vértices y Aristas](#agregar-vértices-y-aristas)
  - [Recorridos](#recorridos)
  - [Búsqueda de Caminos](#búsqueda-de-caminos)
  - [Verificación de Conectividad](#verificación-de-conectividad)
- [Ejemplos](#-ejemplos)
  - [Grafo No Dirigido](#grafo-no-dirigido)
  - [Grafo Dirigido](#grafo-dirigido)
  - [Grafo con Entrada de Usuario](#grafo-con-entrada-de-usuario)
- [Contribuir](#-contribuir)
- [Licencia](#-licencia)

## ✨ Características
- **Soporte para Grafos Dirigidos y No Dirigidos**: Usa un diccionario de conjuntos para representar grafos de manera eficiente.
- **Operaciones Principales**:
  - Agregar vértices (`agregar_vertice`)
  - Agregar aristas (`agregar_arista`)
  - Consultar vecinos (`obtener_vecinos`)
  - Verificar existencia de aristas (`existe_arista`)
- **Algoritmos de Recorrido**:
  - Búsqueda en Amplitud (BFS, `bfs`)
  - Búsqueda en Profundidad (DFS, `dfs`)
- **Búsqueda de Caminos**: Encuentra caminos entre vértices usando BFS (`encontrar_camino`).
- **Conectividad**: Verifica si un grafo no dirigido es conexo (`es_conexo`).
- **Visualización**: Imprime la estructura del grafo de forma clara (`imprimir_grafo`).
- **Entrada de Usuario**: Permite crear grafos dinámicamente desde la consola.

## 🛠 Instalación
1. Asegúrate de tener **Python 3.8+** instalado.
2. Descarga o clona el repositorio:
   ```bash
   git clone <url-del-repositorio>
   ```
3. No se requieren dependencias externas, ya que solo se usa el módulo estándar `collections`.

## 🚀 Uso

### Crear un Grafo
Crea un grafo dirigido o no dirigido:
```python
from grafo import Grafo

# Grafo no dirigido
grafo = Grafo(es_dirigido=False)

# Grafo dirigido
grafo_dir = Grafo(es_dirigido=True)
```

### Agregar Vértices y Aristas
Añade vértices y aristas al grafo:
```python
grafo.agregar_vertice('A')
grafo.agregar_arista('A', 'B')  # Añade arista A <-> B (no dirigido)
grafo_dir.agregar_arista('A', 'B')  # Añade arista A -> B (dirigido)
```

### Recorridos
Realiza recorridos BFS o DFS:
```python
print(grafo.bfs('A'))  # Búsqueda en Amplitud desde 'A'
print(grafo.dfs('A'))  # Búsqueda en Profundidad desde 'A'
```

### Búsqueda de Caminos
Encuentra un camino entre dos vértices:
```python
camino = grafo.encontrar_camino('A', 'C')
print(f"Camino de A a C: {camino}")
```

### Verificación de Conectividad
Verifica si un grafo no dirigido es conexo:
```python
print(f"¿Es conexo el grafo?: {grafo.es_conexo()}")
```

## 📚 Ejemplos

### Grafo No Dirigido
Crea un grafo no dirigido con ciudades de Nicaragua:
```python
mi_grafo = Grafo(es_dirigido=False)
mi_grafo.agregar_arista('Managua', 'Masaya')
mi_grafo.agregar_arista('Managua', 'Leon')
mi_grafo.agregar_arista('Masaya', 'Granada')
mi_grafo.agregar_arista('Granada', 'Rivas')
mi_grafo.agregar_arista('Managua', 'Granada')

mi_grafo.imprimir_grafo()
print(f"Recorrido BFS desde Managua: {mi_grafo.bfs('Managua')}")
print(f"Camino de Managua a Rivas: {mi_grafo.encontrar_camino('Managua', 'Rivas')}")
```

**Salida**:
```
--- Representacion del Grafo ---
Managua: Masaya, Leon, Granada
Masaya: Managua, Granada
Leon: Managua
Granada: Masaya, Rivas, Managua
Rivas: Granada
------------------------------
Recorrido BFS desde Managua: ['Managua', 'Masaya', 'Leon', 'Granada', 'Rivas']
Camino de Managua a Rivas: ['Managua', 'Granada', 'Rivas']
```

### Grafo Dirigido
Crea un grafo dirigido simple:
```python
grafo_dirigido = Grafo(es_dirigido=True)
grafo_dirigido.agregar_arista('Inicio', 'A')
grafo_dirigido.agregar_arista('A', 'B')
grafo_dirigido.agregar_arista('B', 'C')
grafo_dirigido.agregar_arista('C', 'Fin')
grafo_dirigido.agregar_arista('Inicio', 'D')
grafo_dirigido.agregar_arista('D', 'Fin')

grafo_dirigido.imprimir_grafo()
print(f"Recorrido BFS desde Inicio: {grafo_dirigido.bfs('Inicio')}")
print(f"Camino de Inicio a Fin: {grafo_dirigido.encontrar_camino('Inicio', 'Fin')}")
```

**Salida**:
```
--- Representacion del Grafo ---
Inicio: A, D
A: B
B: C
C: Fin
Fin: 
D: Fin
------------------------------
Recorrido BFS desde Inicio: ['Inicio', 'A', 'D', 'B', 'Fin', 'C']
Camino de Inicio a Fin: ['Inicio', 'D', 'Fin']
```

### Grafo con Entrada de Usuario
Crea un grafo interactivamente:
```python
tipo = input("¿El grafo es dirigido? (s/n): ").strip().lower()
es_dirigido = tipo == 's'
g = Grafo(es_dirigido=es_dirigido)

n = int(input("¿Cuántos vértices tiene el grafo?: "))
for _ in range(n):
    v = input("Nombre del vértice: ").strip()
    g.agregar_vertice(v)

m = int(input("¿Cuántas aristas tiene el grafo?: "))
for _ in range(m):
    u = input("Vértice origen: ").strip()
    v = input("Vértice destino: ").strip()
    g.agregar_arista(u, v)

for vertice in g.grafo:
    print(f"Vecinos de '{vertice}':", g.obtener_vecinos(vertice))
```

## 🤝 Contribuir
¡Tus contribuciones son bienvenidas! Sigue estos pasos:
1. Haz un fork del repositorio.
2. Crea una rama nueva (`git checkout -b mejora/funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -m 'Añade funcionalidad'`).
4. Sube los cambios (`git push origin mejora/funcionalidad`).
5. Abre un Pull Request.

## 📜 Licencia
Este proyecto está licenciado bajo la **Licencia MIT**. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

**Desarrollado con 🧠 por Diedereich Alemán**  
Para preguntas o sugerencias, abre un *issue* o contáctame. ¡Espero que disfrutes usando esta implementación de grafos!