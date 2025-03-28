import numpy as np

def get_rref(matrix): # Reduced REF calculation
    A = np.array(matrix, dtype=float)
    rows, cols = A.shape
    lead = 0
    
    for r in range(rows):
        if lead >= cols:
            return A
        i = r
        while A[i, lead] == 0:
            i += 1
            if i == rows:
                i = r
                lead += 1
                if cols == lead:
                    return A
        
        A[[i, r]] = A[[r, i]]  # swap rows
        A[r] = A[r] / A[r, lead]  # to normalize row
        for i in range(rows):
            if i != r:
                A[i] -= A[i, lead] * A[r]
        lead += 1
    return A

def get_column_space(matrix): # compute column space
    rref_matrix = get_rref(matrix)
    column_space = []
    
    pivot_columns = np.where(np.any(rref_matrix != 0, axis=0))[0]
    
    for col in pivot_columns:
        column_space.append(matrix[:, col])  # Take original columns
    
    return np.column_stack(column_space) if column_space else np.array([])

def get_row_space(matrix): # compute row space
    rref_matrix = get_rref(matrix)
    row_space = [row for row in rref_matrix if any(row != 0)]
    return np.array(row_space)

def get_null_space(matrix): # compute null space
    u, s, vh = np.linalg.svd(matrix)
    
    null_mask = (s < 1e-10)
    null_space = vh[null_mask].T
    
    if null_space.size == 0:
        return np.zeros((matrix.shape[1], 1))
    
    return null_space

n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

matrix = []

print("Enter the matrix row by row:")

for i in range(n):
    n = list(map(float, input().split()))
    matrix.append(n)

A = np.array(matrix)
    
print("\nColumn Space:")
print(get_column_space(A))

print("\nRow Space:")
print(get_row_space(A))

print("\nColumn Null Space (Left Null Space):")
print(get_null_space(A.T))

print("\nRow Null Space (Null Space):")
print(get_null_space(A))
