# coding: utf-8

# Acha os vértices i e faz os conjuntos
def melhorCaminho(i):
    while grafo[i] != i:
        i = grafo[i]
    return i
 
# Une o i e o j. retorna false se i e j já estiverem no mesmo conjunto
def uneCaminho(i, j):
    a = melhorCaminho(i)
    b = melhorCaminho(j)
    grafo[a] = b
 
# Acha a AGM usando o algortimo de Kruskal
def kruskal(custo):
    custoMinimo = 0 
 
    # Inicializa os conjuntos disjuntos
    for i in range(v):
        grafo[i] = i
 
    # inclui peso mínimo para as arestas uma por uma
    aresta = 0
    while aresta < v - 1:
        menorCaminho = INF
        x = 0
        y = 0
        for i in range(v):
            for j in range(v):
                if melhorCaminho(i) != melhorCaminho(j) and custo[i][j] < menorCaminho:
                    menorCaminho = custo[i][j]
                    x = i
                    y = j
        uneCaminho(x, y)
        print('Aresta {}:({}, {}) custo: {}'.format(aresta, x, y, menorCaminho))
        aresta += 1
        custoMinimo += menorCaminho
    print("Custo mínimo = {}".format(custoMinimo))
 
v = 5 # Quantidade de vértices (0 a 4)
grafo = [i for i in range(v)]
INF = float('inf')

# Atribui os caminhos e pesos nas arestas
custo = [[INF, 3, INF, 2, INF],
        [1, INF, 2, 4, 3],
        [INF, 1, INF, INF, 3],
        [4, 3, INF, INF, 2],
        [INF, 3, 2, 1, INF]]

kruskal(custo)
 