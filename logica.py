def isMutant(dna):
   if horizontal(dna) or vertical(dna) or diagonal(dna):
    return True
   return False


def horizontal(matrix):
    for elemento in matrix:
        letra_ant= ""
        contador = 0
        for caracter in elemento:
            if caracter != letra_ant:
                letra_ant= caracter
                contador=1
            else:
                contador+=1
                if contador == 4:
                    return True
    return False


def vertical(matrix):
    for i in range(len(matrix[0])):
        contador = 1
        letra_ant= ""
        for j in range(len(matrix)):
            letra = matrix[j][i]
            if letra == letra_ant:
                contador+=1
                if contador == 4:
                    return True
            else:
                letra_ant = letra
                contador = 1
    return False


def diagonal(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i <(len(matrix)-3) and j<(len(matrix[0])-3):
                valor = matrix[i][j]
                diagonal_desc = obtenerDiagonalDesc(matrix, valor, i, j)
                if diagonal_desc:
                    return True
            elif i > 2 and j<(len(matrix[0])-3):
                valor = matrix[i][j]
                diagonal_asc = obtenerDiagonalAsc(matrix, valor, i, j)
                if diagonal_asc:
                    return True
    return False


def obtenerDiagonalDesc(matrix, letra, i, j):
    if letra == matrix[i+1][j+1] and letra == matrix[i+2][j+2] and letra == matrix[i+3][j+3]:
        return True
    return False


def obtenerDiagonalAsc(matrix,letra,i,j):
    if letra == matrix[i-1][j+1] and letra == matrix[i-2][j+2] and letra == matrix[i-3][j+3]:
        return True
    return False

