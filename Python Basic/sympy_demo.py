# sympy_demo.py
import sympy as sp

# Define symbols
x, y, z = sp.symbols('x y z')

# 1. Basic algebra
expr = x**2 + 2*x + 1
factored = sp.factor(expr)
expanded = sp.expand(factored)
print("Expression:", expr)
print("Factored:", factored)
print("Expanded:", expanded)

# 2. Solving equations
solution = sp.solve(x**2 - 4, x)
print("Solutions to x^2 - 4 = 0:", solution)

# 3. Calculus: derivatives and integrals
derivative = sp.diff(sp.sin(x)*sp.exp(x), x)
integral = sp.integrate(sp.sin(x)*sp.exp(x), x)
print("Derivative of sin(x)e^x:", derivative)
print("Integral of sin(x)e^x:", integral)

# 4. Limits
limit_val = sp.limit((sp.sin(x)/x), x, 0)
print("Limit of sin(x)/x as x→0:", limit_val)

# 5. Series expansion
series_exp = sp.series(sp.sin(x), x, 0, 6)
print("Taylor series of sin(x) around 0:", series_exp)

# 6. Linear algebra: matrices
A = sp.Matrix([[1, 2], [3, 4]])
det_A = A.det()
inv_A = A.inv()
eigen = A.eigenvals()
print("Matrix A:\n", A)
print("Determinant:", det_A)
print("Inverse:\n", inv_A)
print("Eigenvalues:", eigen)

# 7. Solving system of equations
eq1 = sp.Eq(2*x + y, 1)
eq2 = sp.Eq(-x + 2*y, 3)
solution_sys = sp.solve((eq1, eq2), (x, y))
print("Solution to system of equations:", solution_sys)

# 8. Simplification
complex_expr = sp.sin(x)*2 + sp.cos(x)*2
simplified = sp.simplify(complex_expr)
print("Simplified expression (sin^2 + cos^2):", simplified)

# 9. Substitution
expr2 = x*2 + y*2
substituted = expr2.subs({x: 1, y: 2})
print("Substitution x=1, y=2 into x^2 + y^2:", substituted)

# 10. Boolean logic
A, B = sp.symbols('A B')
logic_expr = sp.And(A, sp.Or(B, ~A))
simplified_logic = sp.simplify_logic(logic_expr)
print("Simplified logic expression:", simplified_logic)