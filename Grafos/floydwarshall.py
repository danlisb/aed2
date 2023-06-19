# coding: utf-8

# Percorrendo os vértices um a um
def floydWarshall(k, i, j, nV, matrix): 
    for k in range (nV):
        for i in range (nV):
            for j in range (nV):
                if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j] 
