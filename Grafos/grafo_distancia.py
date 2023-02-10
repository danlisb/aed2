# coding: utf-8

class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        # cria uma matriz preenchida com 0 com a quantidade de linhas e colunas igual a quantidade de vértices, na * fizemos para uma linha, no for generalizamos para todas colunas
        self.grafo = [[0] * self.vertices for i in range (self.vertices)] 

    def adiciona_aresta(self, u, v, peso): # u e v são vértices
        # pensando em grafos direcionados simples:
        self.grafo[u-1][v-1] = peso # o -1 é porque começamos a contagem da matriz no 0
        # self.grafo[v-1][u-1] = peso (caso o grafo não seja direcionado, para ser simétrico, 'ir e voltar')

    def mostra_matriz(self):
        print("Os dados do grafo são: ")
        for i in range(self.vertices):
            print(self.grafo[i])

v = int(input("Digite a quantidade de vértices (tamanho da matriz): "))
g = Grafo(v)
if(v > 20 or v < 0):
    print("Não pode ter mais que 20 arestas ou arestas negativas!")
    exit()
else:
    a = int(input("Digite a quantidade de arestas (quantidade de 'pontos' na matriz): "))
    for i in range(a):
        u = int(input("De qual vértice parte essa aresta (linha)? "))
        v = int(input("Para qual vértice essa aresta vai (coluna)? "))
        p = int(input("Qual é o peso dessa aresta (numero a ser inserido na matriz)? "))
        g.adiciona_aresta(u, v, p)
g.mostra_matriz()
