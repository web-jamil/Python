# matrix_operations_sympy.py
import sympy as sp

# 1. Define matrices
A = sp.Matrix([[1, 2], [3, 4]])
B = sp.Matrix([[5, 6], [7, 8]])
print("Matrix A:\n", A)
print("Matrix B:\n", B)

# 2. Matrix addition and subtraction
add = A + B
sub = A - B
print("A + B:\n", add)
print("A - B:\n", sub)

# 3. Matrix multiplication (dot product)
mult = A * B
print("A * B:\n", mult)

# 4. Matrix transpose
transpose = A.T
print("Transpose of A:\n", transpose)

# 5. Matrix determinant
det = A.det()
print("Determinant of A:", det)

# 6. Matrix inverse
inv = A.inv()
print("Inverse of A:\n", inv)

# 7. Matrix rank
rank = A.rank()
print("Rank of A:", rank)

# 8. Identity matrix
I = sp.eye(3)
print("3x3 Identity matrix:\n", I)

# 9. Zero matrix
Z = sp.zeros(2)
print("2x2 Zero matrix:\n", Z)

# 10. Diagonal matrix
D = sp.diag(1, 2, 3)
print("Diagonal matrix:\n", D)

# 11. Eigenvalues and eigenvectors
eigvals = A.eigenvals()
eigvecs = A.eigenvects()
print("Eigenvalues of A:", eigvals)
print("Eigenvectors of A:", eigvecs)

# 12. Solving linear system Ax = b
x, y = sp.symbols('x y')
M = sp.Matrix([[2, 1], [1, 3]])
v = sp.Matrix([8, 13])
sol = M.solve_least_squares(v)  # same as M.LUsolve(v) for exact solve
print("Solving Mx = v:", sol)

# 13. Row-reduction (RREF)
C = sp.Matrix([[1, 2, -1], [2, 4, -2], [3, 6, -3]])
rref, pivots = C.rref()
print("RREF of matrix C:\n", rref)
print("Pivot columns:", pivots)

# 14. Determinant simplification
X = sp.Matrix([[x, 1], [1, x]])
det_expr = X.det()
print("Determinant of symbolic matrix X:\n", det_expr)

# 15. Block matrix
block = sp.Matrix([[A, B], [B, A]])
print("Block matrix:\n", block)