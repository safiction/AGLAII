def determinant(matrix, n):  # function to calculate a determinant of the matrix
    if n == 1:
        return matrix[0][0]
    elif n == 2:  # easy calculation
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:  # other cases
        result = 0
        for column in range(n):  # creating submatrix to skip first line and current column
            submatrix = [[0] * (n - 1) for _ in range(n - 1)]
            for i in range(1, n):
                subcolumn = 0
                for j in range(n):
                    if j == column:
                        continue
                    submatrix[i - 1][subcolumn] = matrix[i][j]
                    subcolumn += 1
            sign = 1 if column % 2 == 0 else -1
            result += sign * matrix[0][column] * determinant(submatrix, n - 1)
        return result

def partial_result(matrix, identity, n):
    for i in range(n):
        print(' '.join(list(map(str, matrix[i]))), '|', ' '.join(list(map(str, identity[i]))))
        print('\n')

def gauss_jordan_inverse(matrix, identity, n):
    for i in range(n):
        if matrix[i][i] == 0:
            for k in range(i + 1, n):
                if matrix[k][i] != 0:
                    matrix[i], matrix[k] = matrix[k], matrix[i]
                    identity[i], identity[k] = identity[k], identity[i]
                    break
            else:
                print("No inverse matrix can be calculated :(")
                return None
        
        diag_element = matrix[i][i]
        for j in range(n):
            matrix[i][j] /= diag_element
            identity[i][j] /= diag_element
        
        for k in range(n):
            if k != i:
                factor = matrix[k][i]
                for j in range(n):
                    matrix[k][j] -= factor * matrix[i][j]
                    identity[k][j] -= factor * identity[i][j]
    return identity

n = int(input('Enter dimension of your matrix: '))

matrix = [[0 for _ in range(n)] for _ in range(n)]
identity = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    print(f"Enter {i+1} row's elements separated by whitespace: ")
    line = input()
    row = list(map(float, line.split()))  # casting elements of each row to float
    matrix[i] = row  # inserting rows into our matrix
    for j in range(n):  # creating identity matrix for the appropriate dimension
        if i == j:
            identity[i][j] = 1.0

det = determinant(matrix, n)
if det == 0:
    print("No inverse matrix can be calculated :(")
else:
    inverse_matrix = gauss_jordan_inverse(matrix, identity, n)
    if inverse_matrix:
        print("Inverse matrix:")
        for row in inverse_matrix:
            print(' '.join(map(str, row)))
