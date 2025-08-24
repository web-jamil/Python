# systems_of_equations_sympy.py
import sympy as sp

# Define symbols
x, y, z = sp.symbols('x y z')

# 1. Two linear equations, two variables
eq1 = sp.Eq(2*x + y, 8)
eq2 = sp.Eq(-x + 2*y, 3)
sol1 = sp.solve((eq1, eq2), (x, y))
print("System 1 (2 equations, 2 variables):")
print("Solution:", sol1)

# 2. Three linear equations, three variables
eq3 = sp.Eq(x + y + z, 6)
eq4 = sp.Eq(2*x - y + z, 3)
eq5 = sp.Eq(-x + 2*y + 2*z, 14)
sol2 = sp.solve((eq3, eq4, eq5), (x, y, z))
print("\nSystem 2 (3 equations, 3 variables):")
print("Solution:", sol2)

# 3. Linear system with matrix method
A = sp.Matrix([[2, 1], [-1, 2]])
b = sp.Matrix([8, 3])
sol3 = A.LUsolve(b)
print("\nMatrix solution (LUsolve):", sol3)

# 4. Underdetermined system (more variables than equations)
eq6 = sp.Eq(x + y + z, 4)
eq7 = sp.Eq(2*x - y + z, 5)
sol4 = sp.solve((eq6, eq7), (x, y, z), dict=True)
print("\nUnderdetermined system:")
print("Solutions (in terms of free variables):", sol4)

# 5. Overdetermined system (more equations than variables)
eq8 = sp.Eq(x + y, 2)
eq9 = sp.Eq(x - y, 0)
eq10 = sp.Eq(2*x + y, 4)
sol5 = sp.solve((eq8, eq9, eq10), (x, y), dict=True)
print("\nOverdetermined system:")
print("Solution (if consistent):", sol5)

# 6. Nonlinear system
eq11 = sp.Eq(x**2 + y, 5)
eq12 = sp.Eq(x + y**2, 7)
sol6 = sp.solve((eq11, eq12), (x, y), dict=True)
print("\nNonlinear system:")
print("Solutions:", sol6)

# 7. Parametric solution
a = sp.Symbol('a')
eq13 = sp.Eq(a*x + y, 1)
eq14 = sp.Eq(x - y, 2)
sol7 = sp.solve((eq13, eq14), (x, y))
print("\nSystem with parameter a:")
print("Solution:", sol7)

# 8. Using RREF to analyze solution
M = sp.Matrix([
    [1, 1, 1, 6],
    [2, -1, 1, 3],
    [-1, 2, 2, 14]
])
rref, pivots = M.rref()
print("\nRREF of augmented matrix:")
print(rref)
print("Pivot columns:", pivots)

# 9. Complex coefficients
eq15 = sp.Eq(x + 2*y, sp.I)
eq16 = sp.Eq(3*x - y, 2 + 3*sp.I)
sol9 = sp.solve((eq15, eq16), (x, y))
print("\nSystem with complex coefficients:")
print("Solution:", sol9)