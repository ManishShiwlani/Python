def updateMatrix(matrix):
    if not matrix: return matrix
    rows, cols = len(matrix), len(matrix[0])
    queue, dist = [(r, c) for r, row in enumerate(matrix) for c, val in enumerate(row) if val != 0], 1
    while queue:
        tmp = []
        for r, c in queue:
            if ((r == 0 or matrix[r - 1][c] >= dist) and
                    (c == 0 or matrix[r][c - 1] >= dist) and
                    (r == rows - 1 or matrix[r + 1][c] >= dist) and
                    (c == cols - 1 or matrix[r][c + 1] >= dist)):
                matrix[r][c] = dist + 1
                tmp.append((r, c))
        dist += 1
        queue = tmp
    return matrix

matrix = [[0,0,0],
 [0,1,0],
 [0,0,0]]

print(updateMatrix(matrix))