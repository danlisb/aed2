# coding: utf-8

# 1. Permitir o armazenamento de até 20 vértices CHECK!
# 2. Fazer a leitura dos pesos das arestas de cada vértice CHECK!
# 3. Considerar sempre vértices positivos CHECK!
# 4. Mostrar o caminho mínimo entre dois vértices solicitados

import sys

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices # constructor da variável de vértices
        self.grafo = [[0] * self.vertices for i in range (self.vertices)] # cria uma matriz preenchida com 0 com a quantidade de linhas e colunas igual a quantidade de vértices, na * fizemos para uma linha, no for generalizamos para todas colunas

    def adiciona_aresta(self, u, v, peso): # u e v são vértices
        # pensando em grafos unidirecionais (caminho único em uma vértice). o -1 é porque começamos a contagem da matriz na posição 0
        self.grafo[u-1][v-1] = peso
        # self.grafo[v-1][u-1] = peso

    def mostra_matriz(self):
        print('A matriz de adjacências é:')
        for i in range(self.vertices):
            print(self.grafo[i])

    def mostra_solucao(self, dist):
        print("Distancia mínima entre a vértice e a origem: ")
        for i in range(self.vertices):
            print(i+1, dist[i])

    def dijkstra(self, start):
        dist = [sys.maxsize] * self.vertices # preenche todas vértices com o infinito
        dist[start] = 0
        menorCaminho = [False] * self.vertices # atribui false para todas vértices
        for cout in range(self.vertices): # for roda para cada vértice e acha o menor caminho
            u = self.distancia_minima(dist, menorCaminho)
            menorCaminho[u] = True
            for v in range(self.vertices):
                if self.grafo[u][v] > 0 and menorCaminho[v] == False and dist[v] > dist[u] + self.grafo[u][v]:
                    dist[v] = dist[u] + self.grafo[u][v]
        self.mostra_solucao(dist)

    def distancia_minima(self, dist, menorCaminho):
        min = sys.maxsize
        for v in range(self.vertices):
            if dist[v] < min and menorCaminho[v] == False:
                min = dist[v]
                min_index = v
        return min_index

v = int(input("Digite a quantidade de vértices (tamanho da matriz): ")) # cria a matriz
g = Grafo(v) # cria o grafo

if(v > 20 or v < 0): # excessões que retornam erro pedido no exercício
    print("Não pode ter mais que 20 vértices ou vértices negativas!")
    exit()
else: # laço que le a quantidade de arestas e faz um loop para o usuário preencher todas vértices e pesos
    a = int(input("Digite a quantidade de arestas (quantidade de 'pontos' na matriz): ")) 
    for i in range(a):
        u = int(input("De qual vértice parte essa aresta (linha)? "))
        v = int(input("Para qual vértice essa aresta vai (coluna)? "))
        p = int(input("Qual é o peso dessa aresta (numero a ser inserido na matriz)? "))
        g.adiciona_aresta(u, v, p)

g.mostra_matriz() # mostra a matriz definida pelo usuário
g.dijkstra(0) # define para 0 a origem do cálculo
