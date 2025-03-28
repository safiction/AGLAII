def get_rref(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    lead = 0
    
    for r in range(rows):
        if lead >= cols:
            return matrix
        i = r
        while matrix[i][lead] == 0:
            i += 1
            if i == rows:
                i = r
                lead += 1
                if lead == cols:
                    return matrix
        matrix[i], matrix[r] = matrix[r], matrix[i]

        lead_val = matrix[r][lead]
        matrix[r] = [x / lead_val for x in matrix[r]]
        
        for i in range(rows):
            if i != r:
                factor = matrix[i][lead]
                matrix[i] = [x - factor * y for x, y in zip(matrix[i], matrix[r])]
        
        lead += 1
    
    return matrix

def get_column_space(matrix):
    rref_matrix = get_rref([row[:] for row in matrix])  # Copy matrix
    columns = list(zip(*matrix))  # Transpose the matrix
    column_space = []
    
    for j in range(len(rref_matrix[0])):
        if any(row[j] != 0 for row in rref_matrix):  # Check if it's a pivot column
            column_space.append(columns[j])  # Take from original matrix
    
    return list(map(list, zip(*column_space))) if column_space else []

def get_row_space(matrix):
    rref_matrix = get_rref([row[:] for row in matrix])  # Copy matrix
    return [row for row in rref_matrix if any(row)]  # Take nonzero rows

def get_null_space(matrix):
    rref_matrix = get_rref([row[:] for row in matrix])  # Copy matrix
    rows = len(rref_matrix)
    cols = len(rref_matrix[0])
    
    free_vars = []
    pivot_columns = []
    
    for r in range(rows):
        for c in range(cols):
            if rref_matrix[r][c] == 1 and all(rref_matrix[x][c] == 0 for x in range(rows) if x != r):
                pivot_columns.append(c)
                break

    for c in range(cols):
        if c not in pivot_columns:
            free_vars.append(c)
    
    if not free_vars:
        return [[0] * cols]  # Only the zero vector if no free variables
    
    null_space = []
    for free_var in free_vars:
        solution = [0] * cols
        solution[free_var] = 1
        for r, pivot_col in enumerate(pivot_columns):
            solution[pivot_col] = -rref_matrix[r][free_var]
        null_space.append(solution)

    return null_space

n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

matrix = []

print("Enter the matrix by rows:")

for i in range(n):
    row = list(map(float, input().split()))
    matrix.append(row)

print("\nColumn Space:")
for row in get_column_space(matrix):
    print(row)

print("\nRow Space:")
for row in get_row_space(matrix):
    print(row)

print("\nColumn Null Space (Left Null Space):")
for row in get_null_space(list(zip(*matrix))):  # Transpose for left null space
    print(row)

print("\nRow Null Space (Null Space):")
for row in get_null_space(matrix):
    print(row)
