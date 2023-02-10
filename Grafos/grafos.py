# coding: utf-8

class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        # cria uma matriz preenchida com 0 com a quantidade de linhas e colunas igual a quantidade de vértices, na * fizemos para uma linha, no for generalizamos para todas colunas
        self.grafo = [[0] * self.vertices for i in range (self.vertices)] 

    def adiciona_aresta(self, u, v): # u e v são arestas
        # pensando em grafos direcionados simples:
        self.grafo[u-1][v-1] = 1 # o -1 é porque começamos a contagem da matriz no 0, trocar = por += se for grafo múltiplo (para não ficar sempre em 1, para adicionar a contagem para 2, 3, ...)

        # self.grafo[v-1][u-1] = 1 (caso o grafo não seja direcionado, para ser simétrico, 'ir e voltar')

    def mostra_matriz(self):
        if(self.vertices >= 20):
            print("Não pode mais que 20 arestas!")
        else:
            print("Os dados da matriz de adjacencias são: ")
            for i in range(self.vertices):
                print(self.grafo[i])

g = Grafo(4)
g.adiciona_aresta(1, 2)
g.adiciona_aresta(3, 4)
g.adiciona_aresta(2, 3)
g.mostra_matriz()
