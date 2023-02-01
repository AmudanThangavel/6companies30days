def floyedWarshell(matrix):
    l = len(matrix)
    for k in range(l):
        for i in range(l):
            for j in range(l):
                if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
    return matrix


INF = float('inf')
matrix = [[0, 5, INF, 10],
          [INF, 0, 3, INF],
          [INF, INF, 0,   1],
          [INF, INF, INF, 0]]


print(floyedWarshell(matrix))
