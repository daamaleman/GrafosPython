import collections

class Grafo:
    def __init__(self, es_dirigido=False):
        self.grafo = {}
        self.es_dirigido = es_dirigido

    def agregar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = set()

    def agregar_arista(self, u, v, peso=1):
        self.agregar_vertice(u)
        self.agregar_vertice(v)
        self.grafo[u].add(v)
        if not self.es_dirigido:
            self.grafo[v].add(u)

    def obtener_vecinos(self, vertice):
        return list(self.grafo.get(vertice, []))

    def existe_arista(self, u, v):
        return u in self.grafo and v in self.grafo[u]

# --- Solicitar datos al usuario ---

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

print("\n--- Vecinos de cada vértice ---")
for vertice in g.grafo:
    print(f"Vecinos de '{vertice}':", g.obtener_vecinos(vertice))

u = input("\nConsulta de arista - vértice origen: ").strip()
v = input("Consulta de arista - vértice destino: ").strip()
print(f"¿Existe arista ('{u}', '{v}')?:", g.existe_arista(u, v))
