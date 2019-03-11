
gridSize = 20

def initializeMatrix(size):
    matrix = [[0] * (size+1) for i in range(size+1)]
    for i in range(len(matrix)-1):
        matrix[i][len(matrix)-1] = 1
        matrix[len(matrix)-1][i] = 1
    return matrix

def gridPaths(size):
    matrix = initializeMatrix(size)

    for i in range(len(matrix)-2, -1, -1):
        for j in range(len(matrix)-2, -1, -1):
            matrix[i][j] = matrix[i+1][j] + matrix[i][j+1]

    return matrix[0][0]

print(gridPaths(gridSize))
